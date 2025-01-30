import typing
import rich
import ubelt as ub
import networkx as nx
import progiter


class MediaGraph:
    """
    Wraps a Jellyfin API client with an interface to walk media folders.

    Builds a graph of all media items in a jellyfin database. A current working
    directory pointer is maintained to allow filesystem like navigation of the
    database.

    Maintains an in-memory graph of the jellyfin database state. This allows
    for efficient client-side queries and exploration, but does take some time
    to construct, and is not kept in sync with the server in the case of
    server-side changes.

    Example:
        >>> from jellyfin_apiclient_python.media_graph import MediaGraph
        >>> import ubelt as ub
        >>> # Given an API client
        >>> MediaGraph.ensure_demo_server(reset=0)
        >>> client = MediaGraph.demo_client()
        >>> # Create the media graph by passing it the client
        >>> self = MediaGraph(client)
        >>> self.walk_config['initial_depth'] = None
        >>> self.setup()
        ...
        >>> # Print the graph at the top level
        >>> self.tree()
        ╟──  f137a2dd21bbc1b99aa5c0f6bf02a805 : 📂 CollectionFolder - Movies
        ╎   ├─╼  826931c9344d013db9db13341db65cce : 🎥 Movie - The great train robbery
        ╎   ├─╼  6144770939e7eeef8d9bd4eb519bf770 : 🎥 Movie - Popeye the Sailor meets Sinbad the Sailor
        ╎   ├─╼  0a8c358081cc4bf1eb74a660ca8616f4 : 🎥 Movie - File:Zur%C3%BCck_in_die_Zukunft_(Film)_01
        ╎   └─╼  32a52b6711776ffeb09b0e737aab5558 : 🎥 Movie - Popeye the Sailor meets Sinbad the Sailor
        ╟──  7e64e319657a9516ec78490da03edccb : 📂 CollectionFolder - Music
        ╎   ├─╼  8288fbf650ae583fc36d715b2c82dff5 : ♬ Audio - Zurück in die Zukunft
        ╎   ├─╼  76ed290f795e4a24a9cceba4aa8bfb33 : ♬ Audio - Heart_Monitor_Beep--freesound.org
        ╎   └─╼  7a7f9d14d80062884dbefd156818b339 : ♬ Audio - Clair De Lune
        ╙──  1071671e7bffa0532e930debee501d2e : 📂 ManualPlaylistsFolder - Playlists
        >>> # Search for items based on name
        >>> found = list(self.find('the'))
        >>> print(f'found = {ub.urepr(found, nl=1)}')
        found = [
            '6144770939e7eeef8d9bd4eb519bf770',
            '32a52b6711776ffeb09b0e737aab5558',
        ]
        >>> # List the folder nodes at the top level
        >>> top_level = self.ls()
        >>> print(f'top_level = {ub.urepr(top_level, nl=1)}')
        top_level = [
            'f137a2dd21bbc1b99aa5c0f6bf02a805',
            '7e64e319657a9516ec78490da03edccb',
            '1071671e7bffa0532e930debee501d2e',
        ]
        >>> # Change the CWD to the music folder
        >>> self.cd('7e64e319657a9516ec78490da03edccb')
        >>> # Print the graph at the CWD
        >>> self.tree()
        ╙──  7e64e319657a9516ec78490da03edccb : 📂 CollectionFolder - Music
            ├─╼  8288fbf650ae583fc36d715b2c82dff5 : ♬ Audio - Zurück in die Zukunft
            ├─╼  76ed290f795e4a24a9cceba4aa8bfb33 : ♬ Audio - Heart_Monitor_Beep--freesound.org
            └─╼  7a7f9d14d80062884dbefd156818b339 : ♬ Audio - Clair De Lune
        >>> # Searching is in the context of the cwd
        >>> found = list(self.find('the'))
        >>> print(f'found = {ub.urepr(found, nl=1)}')
        []
        >>> found = list(self.find('Clair'))
        >>> print(f'found = {ub.urepr(found, nl=1)}')
        found = [
            '7a7f9d14d80062884dbefd156818b339',
        ]
        >>> # Print details about a specific item
        >>> self.print_item('7a7f9d14d80062884dbefd156818b339')
        node=7a7f9d14d80062884dbefd156818b339
        properties = {
            'expanded': False,
        }
        item = {
            'Name': 'Clair De Lune',
            ...
            'Id': '7a7f9d14d80062884dbefd156818b339',
            ...
            'Path': '/media/music/Clair_de_Lune_-_Wright_Brass_-_United_States_Air_Force_Band_of_Flight.mp3',
            ...
            'MediaType': 'Audio',
        }
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
        """
        Create a client for demos

        Returns:
            jellyfin_apiclient_python.JellyfinClient
        """
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
        """
        Print the graph at the current working directory.
        """
        if self._cwd is None:
            self.print_graph(max_depth=max_depth)
        else:
            self.print_graph(sources=[self._cwd], max_depth=max_depth)

    def ls(self):
        """
        List the children of the current working directory (node) in the graph.
        """
        if self._cwd is None:
            return self._media_root_nodes
        else:
            return self._cwd_children

    def cd(self, node):
        """
        Change the cwd to a specific node, and add its children to the graph if
        they have not already been.
        """
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
        """
        Perform an initial walk to build the graph using the user-specified
        configuration.
        """
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
        """
        Add some or all of a node's children to the graph.
        """
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

            perquery_limit = 200
            offset = 0
            need_more = True
            while need_more:
                # Query API for children (todo: we want to async this)
                children = client.jellyfin.user_items(params={
                    'ParentId': parent_id,
                    'Recursive': False,
                    'fields': fields,
                    'limit': perquery_limit,
                    'startIndex': offset,
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

                offset += len(children['Items'])
                need_more = offset < children['TotalRecordCount']

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
        """
        Alias for :func:`MediaGraph.print_graph`.
        """
        self.print_graph()

    def print_graph(self, sources=None, max_depth=None):
        """
        Prints the current state of the media graph to stdout at a particular
        starting point with a specified depth.
        """
        nx.write_network_text(self.graph, path=rich.print, end='', sources=sources, max_depth=max_depth)

    def print_item(self, node):
        node_data = self.graph.nodes[node]
        item = node_data.get('item', None)
        properties = node_data.get('properties', None)
        rprint(f'node={node}')
        rprint(f'properties = {ub.urepr(properties, nl=1)}')
        rprint(f'item = {ub.urepr(item, nl=1)}')

    def find(self, pattern, data=False, root=None):
        """
        Search for a pattern within the current directory.

        Args:
            pattern (str): text to find in the media name.
            data (bool): if True, also return the data dict
            root (str | None): if specified search from this location,
                if unspecified the cwd is used.

        Yields:
            str | Tuple[str, dict]:
                the id of the found item, or the id and its data if
                data=True
        """
        import networkx as nx
        if root is None:
            root = self._cwd
        graph = self.graph
        if root is None:
            nodes = graph.nodes
        else:
            nodes = nx.descendants(graph, root)
        for node in nodes:
            node_data = graph.nodes[node]
            item = node_data['item']
            # TODO: allow multiple types of patterns (i.e. similar to
            # kwutil.Pattern) to abstract regex, glob, and raw string matching.
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
