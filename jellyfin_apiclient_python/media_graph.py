import typing
import rich
import ubelt as ub
import networkx as nx
import progiter


class MediaGraph:
    """
    Builds a graph of all media items in a jellyfin database.

    Maintains an in-memory graph of the jellyfin database state. This allows
    for efficient client-side queries and exploration, but does take some time
    to construct, and is not kept in sync with the server in the case of
    server-side changes.

    Example:
        >>> from jellyfin_apiclient_python.media_graph import MediaGraph
        >>> MediaGraph.ensure_demo_server(reset=0)
        >>> client = MediaGraph.demo_client()
        >>> self = MediaGraph(client)
        >>> self.walk_config['initial_depth'] = None
        >>> self.setup()
        >>> self.tree()

    Ignore:
        self = MediaGraph(client).setup()
        self.tree()

        node = self.ls()[0]
        self.cd(node)
        self.tree()
        self.print_item(node)

        self.cd(self.ls()[3])
        self.tree()
        self.cd(self.ls()[0])
        self.tree()
        self.print_item(self.ls()[0])

        self.cd(None)
        self.ls()
        self.print_graph()
    """
    def __init__(self, client):
        self.client = client
        self.graph = None
        self.walk_config = {
            'initial_depth': 0,
            'include_collection_types': None,
            'exclude_collection_types': None,
        }
        self.display_config = {
            'show_path': False,
        }
        self._cwd = None
        self._cwd_children = None
        self._media_root_nodes = None

    @classmethod
    def ensure_demo_server(cls, reset=False):
        """
        We want to ensure we have a demo server to play with.  We can do this
        with a docker image.

        Requires docker.

        References:
            https://jellyfin.org/docs/general/installation/container#docker
            https://commons.wikimedia.org/wiki/Category:Audio_files
        """
        from jellyfin_apiclient_python.demo.demo_jellyfin_server import DemoJellyfinServerManager
        demoman = DemoJellyfinServerManager()
        demoman.ensure_server(reset=False)

    @classmethod
    def demo_client(cls):
        # TODO: Ensure test environment can spin up a dummy jellyfin server.
        from jellyfin_apiclient_python import JellyfinClient
        client = JellyfinClient()
        client.config.app(
            name='DemoApp',
            version='0.0.1',
            device_name='machine_name',
            device_id='unique_id')
        client.config.data["auth.ssl"] = True
        url = 'http://127.0.0.1:8097'
        username = 'jellyfin'
        password = 'jellyfin'
        client.auth.connect_to_address(url)
        client.auth.login(url, username, password)
        return client

    def tree(self, max_depth=None):
        if self._cwd is None:
            self.print_graph(max_depth=max_depth)
        else:
            self.print_graph(sources=[self._cwd], max_depth=max_depth)

    def ls(self):
        if self._cwd is None:
            return self._media_root_nodes
        else:
            return self._cwd_children

    def cd(self, node):
        self._cwd = node
        if node is None:
            self._cwd_children = self._media_root_nodes
        else:
            if not self.graph.nodes[node]['item']['IsFolder']:
                raise Exception('can only cd into a folder')
            self.open_node(node, verbose=0)
            self._cwd_children = list(self.graph.succ[node])

    def __truediv__(self, node):
        self.open_node(node, verbose=1)

    def setup(self):
        try:
            self._init_media_folders()
        finally:
            self._update_graph_labels()
        return self

    def _init_media_folders(self):
        # Initialize Graph
        client = self.client
        graph = nx.DiGraph()
        self.graph = graph

        include_collection_types = self.walk_config.get('include_collection_types', None)
        exclude_collection_types = self.walk_config.get('exclude_collection_types', None)
        initial_depth = self.walk_config['initial_depth']

        self._media_root_nodes = []

        stats = {
            'node_types': ub.ddict(int),
            'edge_types': ub.ddict(int),
            'nondag_edge_types': ub.ddict(int),
            'total': 0,
            'latest_name': None,
        }

        pman = progiter.ProgressManager()
        with pman:

            media_folders = client.jellyfin.get_media_folders(fields=['Path'])
            items = []
            for folder in pman.progiter(media_folders['Items'], desc='Media Folders'):
                collection_type = folder.get('CollectionType', None)
                if include_collection_types is not None:
                    if collection_type not in include_collection_types:
                        continue
                if exclude_collection_types is not None:
                    if collection_type not in exclude_collection_types:
                        continue

                if 1:
                    item = folder
                else:
                    # Weirdness is not needed if we have access to fields
                    # in get-media-folders
                    # Query API for children (todo: we want to async this)
                    item_id = folder['Id']
                    # This returns all root items, I'm not sure why
                    # hack around it for now.
                    _weird_result = client.jellyfin.user_items(params={
                        'Id': item_id,
                        'Recursive': False,
                        'fields': ['Path'],
                    })
                    item = None
                    for cand in _weird_result['Items']:
                        if cand['Id'] == item_id:
                            item = cand
                            break
                    assert item is not None

                self._media_root_nodes.append(item['Id'])
                items.append(item)
                graph.add_node(item['Id'], item=item, properties=dict(expanded=False))

            for item in pman.progiter(items, desc='Walk Media Folders'):
                self._walk_node(item, pman, stats, max_depth=initial_depth)

    def open_node(self, node, verbose=0, max_depth=1):
        if verbose:
            print(f'open node={node}')
        node_data = self.graph.nodes[node]
        item = node_data['item']
        pman = progiter.ProgressManager(verbose=verbose)
        stats = {
            'node_types': ub.ddict(int),
            'edge_types': ub.ddict(int),
            'nondag_edge_types': ub.ddict(int),
            'total': 0,
            'latest_name': None,
        }
        with pman:
            self._walk_node(item, pman, stats, max_depth=max_depth)
        self._update_graph_labels(sources=[node])

        if verbose:
            self.print_graph([node])
            self.print_item(node)

    def _walk_node(self, item, pman, stats, max_depth=None):
        """
        Iterates through an items children and adds them to the graph until a
        limit is reached.
        """
        client = self.client
        if pman is not None:
            folder_prog = pman.progiter(desc=f'Walking {item["Name"]}')
            folder_prog.start()

        type_add_blocklist = {
            'UserView',
            'CollectionFolder',
        }
        type_recurse_blocklist = {
            'Audio',
            'Episode',
        }

        timer = ub.Timer()
        graph = self.graph

        class StackFrame(typing.NamedTuple):
            item: dict
            depth: int

        from jellyfin_apiclient_python.api import info
        fields = info()

        stack = [StackFrame(item, 0)]
        while stack:
            if pman is not None:
                folder_prog.step()
            frame = stack.pop()

            if max_depth is not None and frame.depth >= max_depth:
                continue

            parent = frame.item
            node_data = graph.nodes[parent['Id']]
            node_data['properties']['expanded'] = True

            stats['latest_name'] = parent['Name']
            stats['latest_path'] = parent.get('Path', None)

            parent_id = parent['Id']

            HANDLE_SPECIAL_FEATURES = 1
            if HANDLE_SPECIAL_FEATURES:
                if parent['Type'] in {'Series', 'Season'}:
                    # Not sure why special features are not included as children
                    special_features = client.jellyfin.user_items(f'/{parent_id}/SpecialFeatures')
                    if special_features:
                        # Hack in a dummy special features item into the graph
                        special_features_id = parent_id + '/SpecialFeatures'
                        special_features_item = {
                            'Name': 'Special Features',
                            'Id': special_features_id,
                            'Type': 'SpecialFeatures',
                        }
                        special_parent = special_features_item
                        graph.add_node(special_parent['Id'], item=special_parent, properties=dict(expanded=True))
                        graph.add_edge(parent['Id'], special_parent['Id'])
                        stats['edge_types'][(parent['Type'], special_parent['Type'])] += 1
                        for special in special_features:
                            stats['edge_types']['SpecialFeatures', special['Type']] += 1
                            if special['Id'] in graph.nodes:
                                stats['nondag_edge_types'][(parent['Type'], special['Type'])] += 1
                                assert False
                            else:
                                # Add child to graph
                                graph.add_node(special['Id'], item=special, properties=dict(expanded=False))
                                graph.add_edge(special_parent['Id'], special['Id'])
                                assert not special['IsFolder']

            # Query API for children (todo: we want to async this)
            children = client.jellyfin.user_items(params={
                'ParentId': parent_id,
                'Recursive': False,
                'fields': fields,
            })
            if children and 'Items' in children:
                stats['total'] += len(children['Items'])
                for child in children['Items']:
                    if child['Id'] in graph.nodes:
                        stats['nondag_edge_types'][(parent['Type'], child['Type'])] += 1
                    else:
                        if child['Type'] not in type_add_blocklist:
                            stats['edge_types'][(parent['Type'], child['Type'])] += 1
                            stats['node_types'][child['Type']] += 1

                            # Add child to graph
                            graph.add_node(child['Id'], item=child, properties=dict(expanded=False))
                            graph.add_edge(parent['Id'], child['Id'])

                            if child['IsFolder'] and child['Type'] not in type_recurse_blocklist:
                                child_frame = StackFrame(child, frame.depth + 1)
                                stack.append(child_frame)

            if timer.toc() > 1.9:
                pman.update_info(ub.urepr(stats))
                timer.tic()
        folder_prog.stop()

    def _update_graph_labels(self, sources=None):
        """
        Update the rich text representation of select items in the graph.
        """

        glyphs = {
            'FILE_FOLDER': '📁',
            'OPEN_FILE_FOLDER': '📂',
            'FOLD': '🗀',
            'OPEN_FOLDER': '🗁',
            'BEAMED_SIXTEENTH_NOTES': '♬',
            'MOVIE_CAMERA': '🎥',
            'TELEVISION': '📺',
            'FILM_FRAMES': '🎞',
        }

        url = self.client.http.config.data['auth.server']

        nx.dfs_successors
        graph = self.graph

        reachable_nodes = reachable(graph, sources)

        # Relabel Graph
        for node in reachable_nodes:
            node_data = graph.nodes[node]
            item = node_data['item']
            properties = node_data['properties']
            expanded = properties.get('expanded', False)
            glyph_key = 'OPEN_FILE_FOLDER' if expanded else 'FILE_FOLDER'
            type_glyph = glyphs[glyph_key]

            if item['Type'] == 'Folder':
                color = 'blue'
            if item['Type'] == 'CollectionFolder':
                color = 'blue'
            elif item['Type'] == 'Series':
                color = 'cyan'
            elif item['Type'] == 'Season':
                color = 'yellow'
            elif item['Type'] == 'MusicAlbum':
                color = 'cyan'
            elif item['Type'] == 'MusicArtist':
                color = 'cyan'
            elif item['Type'] == 'Episode':
                color = None
                type_glyph = glyphs['TELEVISION']
            elif item['Type'] == 'Video':
                color = None
                type_glyph = glyphs['FILM_FRAMES']
            elif item['Type'] == 'Movie':
                color = None
                type_glyph = glyphs['MOVIE_CAMERA']
            elif item['Type'] == 'Audio':
                color = None
                type_glyph = glyphs['BEAMED_SIXTEENTH_NOTES']
            else:
                color = None

            if color is not None:
                color_part1 = f'[{color}]'
                color_part2 = f'[/{color}]'
            else:
                color_part1 = ''
                color_part2 = ''

            namerep = item['Name']
            path = item.get('Path', None)
            if self.display_config['show_path']:
                if path is not None:
                    namerep = item['Name'] + ' - ' + path
                    # namerep = path

            item_id_link = f'{url}/web/index.html#!/details?id={item["Id"]}'
            item_id_rep = item["Id"]
            item_id_rep = f'[link={item_id_link}]{item_id_rep}[/link]'

            label = f'{color_part1} {item_id_rep} : {type_glyph} {item["Type"]} - {namerep} {color_part2}'
            node_data['label'] = label

    def print(self):
        self.print_graph()

    def print_graph(self, sources=None, max_depth=None):
        nx.write_network_text(self.graph, path=rich.print, end='', sources=sources, max_depth=max_depth)

    def print_item(self, node):
        node_data = self.graph.nodes[node]
        item = node_data.get('item', None)
        properties = node_data.get('properties', None)
        rprint(f'node={node}')
        rprint(f'properties = {ub.urepr(properties, nl=1)}')
        rprint(f'item = {ub.urepr(item, nl=1)}')

    def find(self, pattern, data=False):
        graph = self.graph
        for node in graph.nodes:
            node_data = graph.nodes[node]
            item = node_data['item']
            if pattern in item['Name']:
                if data:
                    yield node, node_data
                else:
                    yield node


def reachable(graph, sources=None):
    if sources is None:
        yield from graph.nodes
    else:
        seen = set()
        for source in sources:
            if source in seen:
                continue
            for node in nx.dfs_preorder_nodes(graph, source):
                seen.add(node)
                yield node


def _find_sources(graph):
    """
    Determine a minimal set of nodes such that the entire graph is reachable
    """
    import networkx as nx
    # For each connected part of the graph, choose at least
    # one node as a starting point, preferably without a parent
    if graph.is_directed():
        # Choose one node from each SCC with minimum in_degree
        sccs = list(nx.strongly_connected_components(graph))
        # condensing the SCCs forms a dag, the nodes in this graph with
        # 0 in-degree correspond to the SCCs from which the minimum set
        # of nodes from which all other nodes can be reached.
        scc_graph = nx.condensation(graph, sccs)
        supernode_to_nodes = {sn: [] for sn in scc_graph.nodes()}
        # Note: the order of mapping differs between pypy and cpython
        # so we have to loop over graph nodes for consistency
        mapping = scc_graph.graph["mapping"]
        for n in graph.nodes:
            sn = mapping[n]
            supernode_to_nodes[sn].append(n)
        sources = []
        for sn in scc_graph.nodes():
            if scc_graph.in_degree[sn] == 0:
                scc = supernode_to_nodes[sn]
                node = min(scc, key=lambda n: graph.in_degree[n])
                sources.append(node)
    else:
        # For undirected graph, the entire graph will be reachable as
        # long as we consider one node from every connected component
        sources = [
            min(cc, key=lambda n: graph.degree[n])
            for cc in nx.connected_components(graph)
        ]
        sources = sorted(sources, key=lambda n: graph.degree[n])
    return sources


def rprint(*args):
    try:
        import rich
        rich.print(*args)
    except ImportError:
        print(*args)
