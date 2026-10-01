# -*- coding: utf-8 -*-
"""
For API info see:
    https://api.jellyfin.org/
"""
from typing import List
from datetime import datetime
from urllib.parse import quote
import requests
import json
import logging

LOG = logging.getLogger('JELLYFIN.' + __name__)


def jellyfin_url(client, handler):
    base_url = client.config.data['auth.server'].rstrip('/')
    return f"{base_url}/{handler.lstrip('/')}"


def basic_info():
    return "Etag"


def info():
    return (
        "Path,Genres,SortName,Studios,Writer,Taglines,LocalTrailerCount,"
        "OfficialRating,CumulativeRunTimeTicks,ItemCounts,"
        "Metascore,AirTime,DateCreated,People,Overview,"
        "CriticRating,CriticRatingSummary,Etag,ShortOverview,ProductionLocations,"
        "Tags,ProviderIds,ParentId,RemoteTrailers,SpecialEpisodeNumbers,"
        "MediaSources,VoteCount,RecursiveItemCount,PrimaryImageAspectRatio"
    )


def music_info():
    return (
        "Etag,Genres,SortName,Studios,Writer,"
        "OfficialRating,CumulativeRunTimeTicks,Metascore,"
        "AirTime,DateCreated,MediaStreams,People,ProviderIds,Overview,ItemCounts"
    )


class InternalAPIMixin:
    """
    A mixin class containing a common set of internal calls the other mixin
    classes will use.
    """

    def _http(self, action, url, request={}):
        request.update({'type': action, 'handler': url})

        return self.client.request(request)

    def _http_url(self, action, url, request={}, include_apikey=True):
        request.update({"type": action, "handler": url})

        return self.client.request_url(request, include_apikey=include_apikey)

    def _http_stream(self, action, url, dest_file, request={}):
        request.update({'type': action, 'handler': url})

        self.client.request(request, dest_file=dest_file)

    def _get(self, handler, params=None):
        return self._http("GET", handler, {'params': params})

    def _get_url(self, handler, params=None, include_apikey=True):
        return self._http_url("GET", handler, {"params": params},
                              include_apikey=include_apikey)

    def _post(self, handler, json=None, params=None, data=None, headers=None):
        return self._http("POST", handler, {'params': params, 'json': json,
                                            'data': data, 'headers': headers})

    def _delete(self, handler, params=None):
        return self._http("DELETE", handler, {'params': params})

    def _get_stream(self, handler, dest_file, params=None):
        self._http_stream("GET", handler, dest_file, {'params': params})


class BiggerAPIMixin:
    """
    Bigger section of the Jellyfin api
    """

    def try_server(self):
        return self._get("System/Info/Public")

    def command(self, id, command, params=None, json=None):
        return self._post(
            "Sessions/%s/Command" % id,
            json={"Name": command, "Arguments": json},
            params=params,
        )

    def remote(self, id, command, params=None, json=None):
        handler = (
            "Sessions/%s/Playing/%s" % (id, command)
            if command
            else "Sessions/%s/Playing" % id
        )
        return self._post(
            handler,
            json=json,
            params=params,
        )

    def sessions(self, handler="", action="GET", params=None, json=None,
                 timeout=None, retry=None):
        """Session endpoints.

        ``timeout`` and ``retry`` bound this one call instead of using the
        client-wide defaults (30s, 5 retries). A caller polling for liveness —
        a health check — wants a request that fails fast, since the defaults
        can wedge its thread for minutes against an unresponsive server.
        """
        request = {'params': params}
        if timeout is not None:
            request['timeout'] = timeout
        if retry is not None:
            request['retry'] = retry
        if action == "POST":
            request['json'] = json
            return self._http("POST", "Sessions%s" % handler, request)
        elif action == "DELETE":
            return self._http("DELETE", "Sessions%s" % handler, request)
        else:
            return self._http("GET", "Sessions%s" % handler, request)

    def users(self, handler="", action="GET", params=None, json=None):
        if action == "POST":
            return self._post("Users/{UserId}%s" % handler, json, params)
        elif action == "DELETE":
            return self._delete("Users/{UserId}%s" % handler, params)
        else:
            return self._get("Users/{UserId}%s" % handler, params)

    def media_folders(self, params=None):
        return self._get("Library/MediaFolders/", params)

    def virtual_folders(self, action="GET", params=None, json=None):
        if action == "POST":
            return self._post("Library/VirtualFolders", json, params)
        elif action == "DELETE":
            return self._delete("Library/VirtualFolders", params)
        else:
            return self._get("Library/VirtualFolders", params)

    def physical_paths(self, params=None):
        return self._get("Library/PhysicalPaths/", params)

    def folder_contents(self, abspath="/", params=None, json=None):
        params = {} if params is None else params.copy()
        params['path'] = abspath
        params['includeFiles'] = params.get('includeFiles', True)
        params['includeDirectories'] = params.get('includeDirectories', True)
        return self._get("Environment/DirectoryContents", params)

    def refresh_library(self):
        """
        Starts a library scan.
        """
        return self._post("Library/Refresh")

    def add_media_library(self, name, collectionType, paths, refreshLibrary=True):
        """
        Create a new media library.

        Args:
            name (str): name of the new library

            collectionType (str): one of "movies" "tvshows" "music" "musicvideos"
                "homevideos" "boxsets" "books" "mixed"

            paths (List[str]):
                paths on the server to use in the media library

        References:
            .. [AddVirtualFolder] https://api.jellyfin.org/#tag/LibraryStructure/operation/AddVirtualFolder
        """
        params = {
            'name': name,
            'collectionType': collectionType,
            'paths': paths,
            'refreshLibrary': refreshLibrary,

        }
        return self.virtual_folders('POST', params=params)

    def items(self, handler="", action="GET", params=None, json=None, data=None, headers=None):
        if action == "POST":
            return self._post("Items%s" % handler, json, params, data, headers)
        elif action == "DELETE":
            return self._delete("Items%s" % handler, params)
        else:
            return self._get("Items%s" % handler, params)

    def user_items(self, handler="", params=None):
        return self.users("/Items%s" % handler, params=params)

    def get_playlist_items(self, playlist_id, fields=None, start_index=None,
                           limit=None):
        """Items of a playlist in playlist order (GET Playlists/{id}/Items).

        Unlike a ``ParentId`` query, this preserves the user's playlist ordering
        and returns each entry's ``PlaylistItemId``. ``UserId`` is filled from
        the session so per-user data (played/resume) comes back.
        """
        params = {"UserId": "{UserId}"}
        if fields is not None:
            params["Fields"] = fields
        if start_index is not None:
            params["StartIndex"] = start_index
        if limit is not None:
            params["Limit"] = limit
        return self._get("Playlists/%s/Items" % playlist_id, params)

    def shows(self, handler, params):
        return self._get("Shows%s" % handler, params)

    def videos(self, handler):
        return self._get("Videos%s" % handler)

    def media_segments(self, handler, params=None):
        return self._get("MediaSegments%s" % handler, params)

    def artwork(self, item_id, art, max_width, ext="jpg", index=None,
                include_apikey=True):
        params = {"MaxWidth": max_width, "format": ext}
        handler = ("Items/%s/Images/%s" % (item_id, art) if index is None
                   else "items/%s/images/%s/%s" % (item_id, art, index)
                   )

        return self._get_url(handler, params,
                             include_apikey=include_apikey)

    def audio_url(self, item_id, container=None, audio_codec=None,
                  max_streaming_bitrate=140000000, include_apikey=True):
        params = {
            "UserId": "{UserId}",
            "DeviceId": "{DeviceId}",
            "MaxStreamingBitrate": max_streaming_bitrate,
        }

        if container:
            params["Container"] = container

        if audio_codec:
            params["AudioCodec"] = audio_codec

        return self._get_url("Audio/%s/universal" % item_id, params,
                             include_apikey=include_apikey)

    def video_url(self, item_id, media_source_id=None, include_apikey=True):
        params = {
            "static": "true",
            "DeviceId": "{DeviceId}"
        }
        if media_source_id is not None:
            params["MediaSourceId"] = media_source_id

        return self._get_url("Videos/%s/stream" % item_id, params,
                             include_apikey=include_apikey)

    def download_url(self, item_id, include_apikey=True):
        params = {}
        return self._get_url("Items/%s/Download" % item_id, params,
                             include_apikey=include_apikey)

    def image_url(self, item_id, image_type="Primary", index=None, tag=None,
                  max_width=None, fill_width=None, fill_height=None,
                  quality=90, include_apikey=True):
        """Build an image URL for an item.

        Pass ``fill_width``/``fill_height`` to crop to an exact box, or
        ``max_width`` to scale within a width. ``index`` selects a numbered
        image (e.g. ``Backdrop`` index ``0``).
        """
        handler = "Items/%s/Images/%s" % (item_id, image_type)
        if index is not None:
            handler = "%s/%s" % (handler, index)
        params = {}
        if quality is not None:
            params["quality"] = quality
        if fill_width is not None and fill_height is not None:
            params["fillWidth"] = int(fill_width)
            params["fillHeight"] = int(fill_height)
        elif max_width is not None:
            params["maxWidth"] = int(max_width)
        if tag is not None:
            params["tag"] = tag
        return self._get_url(handler, params,
                             include_apikey=include_apikey)

    def subtitle_url(self, item_id, media_source_id, index, fmt, fmt_index=0,
                     include_apikey=True):
        """Build the external-subtitle sidecar stream URL for one stream."""
        return self._get_url(
            "Videos/%s/%s/Subtitles/%s/%s/Stream.%s"
            % (item_id, media_source_id, index, fmt_index, fmt), {},
            include_apikey=include_apikey)

    def trickplay_tile_url(self, item_id, width, index, media_source_id=None,
                           include_apikey=True):
        """Build the URL for a single trickplay (scrubbing preview) tile."""
        params = {}
        if media_source_id is not None:
            params["MediaSourceId"] = media_source_id
        return self._get_url(
            "Videos/%s/Trickplay/%s/%s.jpg" % (item_id, width, index), params,
            include_apikey=include_apikey)


class GranularAPIMixin:
    """
    Mixin class containing Jellyfin API granular user-level calls
    """

    def get_users(self):
        return self._get("Users")

    def get_public_users(self):
        return self._get("Users/Public")

    def get_user(self, user_id=None):
        return self.users() if user_id is None else self._get("Users/%s" % user_id)

    def get_user_settings(self, client="emby"):
        return self._get("DisplayPreferences/usersettings", params={
            "userId": "{UserId}",
            "client": client
        })

    def new_user(self, name, pw):
        return self._post("Users/New", {
            "name": name,
            "Password": pw
        })

    def delete_user(self, userID):
        return self._delete(f"Users/{userID}")

    def get_views(self):
        return self.users("/Views")

    def get_media_folders(self, fields=None):
        params = None
        if fields is not None:
            params = {'fields': fields}
        return self.users("/Items", params=params)

    def get_item(self, item_id, fields=None):
        """
        Lookup metadata for an item.

        Args:
            item_id (str): item uuid to lookup metadata for
            fields (str): comma-separated Fields to request; defaults to the
                standard ``info()`` field set.

        Returns:
            Dict[str, Any]: metadata keys and values for the queried item.
        """
        return self.users("/Items/%s" % item_id, params={
            'Fields': fields if fields is not None else info()
        })

    def get_items(self, item_ids, fields=None):
        """
        Lookup metadata for multiple items.

        The server does not preserve the requested order, and it drops ids it
        cannot resolve, so callers that care about order should re-index the
        result by ``Id``. Very long id lists are best sent in batches — they
        travel in the query string, which servers and proxies cap (HTTP 414).

        Args:
            item_ids (List[str]): item uuids to lookup metadata for

            fields (str): comma-separated Fields to request; defaults to the
                standard ``info()`` field set.

        Returns:
            Dict[str, Any]: A result dictionary where the info from each
                item is stored in the "Items" list.
        """
        return self.users("/Items", params={
            'Ids': ','.join(str(x) for x in item_ids),
            'Fields': info() if fields is None else fields
        })

    def update_item(self, item_id, data):
        """
        Updates the metadata for an item.

        Requires a user with elevated permissions [UpdateItem]_.

        Args:
            item_id (str): item uuid to update metadata for

            data (Dict): the new information to add to this item.
                Note: any specified items are completely overwritten.

        References:
            .. [UpdateItem] https://api.jellyfin.org/#tag/ItemUpdate/operation/UpdateItem
        """
        # Force us to get the entire original item, we need to pass
        # all information, otherwise all info is overwritten
        body = self.get_item(item_id)
        body.update(data)
        assert body['Id'] == item_id
        return self.items('/' + item_id, action='POST', params=None, json=body)

    def get_sessions(self):
        return self.sessions(params={'ControllableByUserId': "{UserId}"})

    def get_device(self, device_id):
        return self.sessions(params={'DeviceId': device_id})

    def post_session(self, session_id, url, params=None, data=None):
        return self.sessions("/%s/%s" % (session_id, url), "POST", params, data)

    def get_images(self, item_id):
        return self.items("/%s/Images" % item_id)

    def get_suggestion(self, media="Movie,Episode", limit=1):
        return self.users("/Suggestions", params={
            'Type': media,
            'Limit': limit
        })

    def get_recently_added(self, media=None, parent_id=None, limit=20,
                           fields=None, enable_image_types=None,
                           image_type_limit=None,
                           enable_total_record_count=None):
        """Recently added items (GET Users/{UserId}/Items/Latest).

        Answers a bare list of items, not the usual ``{"Items": [...]}``
        envelope.

        ``fields`` defaults to the broad ``info()`` set for backward
        compatibility; pass a lean list when building a home-screen row, since
        the default pulls MediaSources, People and Studios for every item.
        ``enable_total_record_count=False`` skips the server's separate
        ``COUNT(*)``, which a fixed-size row never reads.
        """
        params = {
            'Limit': limit,
            'UserId': "{UserId}",
            'IncludeItemTypes': media,
            'ParentId': parent_id,
            'Fields': info() if fields is None else fields,
        }
        if enable_image_types is not None:
            params['EnableImageTypes'] = enable_image_types
        if image_type_limit is not None:
            params['ImageTypeLimit'] = image_type_limit
        if enable_total_record_count is not None:
            params['EnableTotalRecordCount'] = enable_total_record_count
        return self.user_items("/Latest", params)

    def get_next(self, index=None, limit=1, series_id=None, fields=None,
                 enable_image_types=None, image_type_limit=None):
        """Next Up (GET /Shows/NextUp).

        ``image_type_limit`` caps how many tags of each type come back per
        item. Without it a series with twenty backdrops sends twenty tags
        for a card that will use one; jellyfin-web sends 1 here.
        """
        params = {
            'Limit': limit,
            'UserId': "{UserId}",
            'StartIndex': None if index is None else int(index)
        }
        if series_id is not None:
            params['SeriesId'] = series_id
        if fields is not None:
            params['Fields'] = fields
        if enable_image_types is not None:
            params['EnableImageTypes'] = enable_image_types
        if image_type_limit is not None:
            params['ImageTypeLimit'] = image_type_limit
        return self.shows("/NextUp", params)

    def get_adjacent_episodes(self, show_id, item_id):
        return self.shows("/%s/Episodes" % show_id, {
            'UserId': "{UserId}",
            'AdjacentTo': item_id,
            'Fields': "Overview"
        })

    def get_season(self, show_id, season_id):
        return self.shows("/%s/Episodes" % show_id, {
            'UserId': "{UserId}",
            'SeasonId': season_id
        })

    def get_episodes(self, series_id, season_id=None, start_item_id=None,
                     fields=None, limit=None):
        """Episodes for a series, optionally scoped to one season or starting
        at a given episode (``start_item_id`` crosses season boundaries)."""
        params = {'UserId': "{UserId}"}
        if season_id is not None:
            params['SeasonId'] = season_id
        if start_item_id is not None:
            params['StartItemId'] = start_item_id
        if fields is not None:
            params['Fields'] = fields
        if limit is not None:
            params['Limit'] = limit
        return self.shows("/%s/Episodes" % series_id, params)

    def get_studios(self, parent_id=None, include_item_types=None,
                    sort_by="SortName", sort_order="Ascending",
                    fields=None, start_index=None, limit=None):
        """Studios / networks under a library (GET /Studios).

        The by-name counterpart to ``get_genres``: it answers with Studio
        items carrying their own ids and artwork, which is what a studios
        screen draws and what ``StudioIds`` on an item query then filters by.
        """
        params = {
            "ParentId": parent_id,
            "UserId": "{UserId}",
            "SortBy": sort_by,
            "SortOrder": sort_order,
            "Recursive": True,
            "Fields": fields if fields is not None else "PrimaryImageAspectRatio",
        }
        if include_item_types is not None:
            params["IncludeItemTypes"] = include_item_types
        if start_index is not None:
            params["StartIndex"] = start_index
        if limit is not None:
            params["Limit"] = limit
        return self._get("Studios", params)

    def get_genres(self, parent_id=None, include_item_types=None):
        params = {
            'ParentId': parent_id,
            'UserId': "{UserId}",
            'Fields': info(),
        }
        if include_item_types is not None:
            # e.g. "MusicAlbum" for a music library's genre list.
            params['IncludeItemTypes'] = include_item_types
        return self._get("Genres", params)

    def _artist_query(self, handler, params, parent_id, sort_by, sort_order,
                      start_index, limit, fields, image_type_limit,
                      enable_image_types, search_term):
        p = {
            "UserId": "{UserId}",
            "ParentId": parent_id,
            "SortBy": sort_by,
            "SortOrder": sort_order,
            "StartIndex": start_index,
            "Limit": limit,
            "Fields": fields,
            "ImageTypeLimit": image_type_limit,
            "EnableImageTypes": enable_image_types,
            "SearchTerm": search_term,
        }
        p = {k: v for k, v in p.items() if v is not None}
        if params:
            p.update(params)
        return self._get(handler, p)

    def get_artists(self, params=None, parent_id=None, sort_by=None,
                    sort_order=None, start_index=None, limit=None, fields=None,
                    image_type_limit=None, enable_image_types=None,
                    search_term=None):
        """Artists (GET /Artists) — includes track-level / featured artists.
        Pass ``parent_id`` to scope to a library, plus the usual paging and
        sort arguments. ``params`` is merged in last for anything this
        signature does not name. UserId is added so per-user data comes back."""
        return self._artist_query(
            "Artists", params, parent_id, sort_by, sort_order, start_index,
            limit, fields, image_type_limit, enable_image_types, search_term)

    def get_album_artists(self, params=None, parent_id=None, sort_by=None,
                          sort_order=None, start_index=None, limit=None,
                          fields=None, image_type_limit=None,
                          enable_image_types=None, search_term=None):
        """Album artists (GET /Artists/AlbumArtists) — artists credited on an
        album, the more useful artist list. Same arguments as get_artists."""
        return self._artist_query(
            "Artists/AlbumArtists", params, parent_id, sort_by, sort_order,
            start_index, limit, fields, image_type_limit, enable_image_types,
            search_term)

    def get_instant_mix(self, item_id, limit=200, fields=None):
        """A radio-style auto queue seeded from an item (GET
        /Items/{id}/InstantMix); works for a song, album, artist, or genre.

        ``fields`` defaults to the ``music_info()`` set for backwards
        compatibility, but that set is expensive here in a way it is not on a
        single item: ``MediaStreams``, ``People`` and ``ItemCounts`` are all
        per-item lookups, and this endpoint returns up to ``limit`` (200)
        items, so the server does hundreds of extra queries before it answers.
        jellyfin-web asks for no fields at all here. Pass ``fields=""`` to do
        the same, or a lean set of your own.
        """
        params = {
            "UserId": "{UserId}",
            "Limit": limit,
        }
        fields = music_info() if fields is None else fields
        if fields:
            params["Fields"] = fields
        return self._get("Items/%s/InstantMix" % item_id, params)

    def get_recommendation(self, parent_id=None, limit=20):
        return self._get("Movies/Recommendations", {
            'ParentId': parent_id,
            'UserId': "{UserId}",
            'Fields': info(),
            'Limit': limit
        })

    def get_items_by_letter(self, parent_id=None, media=None, letter=None):
        return self.user_items(params={
            'ParentId': parent_id,
            'NameStartsWith': letter,
            'Fields': info(),
            'Recursive': True,
            'IncludeItemTypes': media
        })

    def search_media_items(self, term=None, year=None, media=None, limit=20, parent_id=None):
        """
        Description:
            Search for media using terms, production year(s) and media type

        Args:
            term (str):
            year (int):
            media (str):
            limit (int):
            parent_id (str):

        Returns:
            dict

        Example:
            >>> result = client.jellyfin.search_media_items(term='The Lion King', year=1994, media='Movie', limit=1)
            >>> result['Items']
            [
                {
                    'Name': 'The Lion King',
                    ...
                    'ProductionYear': 1994
                    ...
                    'Type': 'Movie'
                }
            ]
        """
        return self.user_items(params={
            'searchTerm': term,
            'years': year,
            'Recursive': True,
            'IncludeItemTypes': media,
            'Limit': limit,
            'parentId': parent_id,
        })

    def get_user_items(self, parent_id=None, include_item_types=None,
                       media_types=None, recursive=None, sort_by=None,
                       sort_order=None, start_index=None, limit=None,
                       fields=None, filters=None, ids=None, genres=None,
                       genre_ids=None, years=None, person_ids=None,
                       artist_ids=None, album_artist_ids=None,
                       search_term=None, is_favorite=None,
                       name_starts_with=None, name_less_than=None,
                       image_type_limit=None, enable_image_types=None,
                       enable_images=None, enable_user_data=None,
                       enable_total_record_count=None, params=None):
        """The general item query (GET Users/{UserId}/Items).

        This is the endpoint behind every library grid: pass ``parent_id`` to
        scope to a folder or library, ``recursive=True`` to search below it,
        and the usual sort/page/filter arguments. Arguments left at ``None``
        are not sent, so the server's own defaults apply.

        ``filters`` takes Jellyfin's ``Filters`` enum as a comma-separated
        string (``"IsUnplayed"``, ``"IsResumable"``, ``"IsFavorite"``, …).
        ``params`` is merged in last, for query parameters this signature does
        not name.

        Prefer the narrower helpers where one exists (``get_resume_items``,
        ``get_album_tracks``, ``get_artist_albums``, ``get_playlists``,
        ``get_random_items``, ``search_media_items``) — they document intent
        and pick the right sort.

        References:
            .. [GetItems] https://api.jellyfin.org/#tag/Items/operation/GetItems
        """
        query = {
            'ParentId': parent_id,
            'IncludeItemTypes': include_item_types,
            'MediaTypes': media_types,
            'Recursive': recursive,
            'SortBy': sort_by,
            'SortOrder': sort_order,
            'StartIndex': start_index,
            'Limit': limit,
            'Fields': fields,
            'Filters': filters,
            'Ids': ','.join(str(x) for x in ids) if ids is not None else None,
            'Genres': genres,
            'GenreIds': genre_ids,
            'Years': years,
            'PersonIds': person_ids,
            'ArtistIds': artist_ids,
            'AlbumArtistIds': album_artist_ids,
            'SearchTerm': search_term,
            'IsFavorite': is_favorite,
            'NameStartsWith': name_starts_with,
            'NameLessThan': name_less_than,
            'ImageTypeLimit': image_type_limit,
            'EnableImageTypes': enable_image_types,
            'EnableImages': enable_images,
            'EnableUserData': enable_user_data,
            'EnableTotalRecordCount': enable_total_record_count,
        }
        query = {k: v for k, v in query.items() if v is not None}
        if params:
            query.update(params)
        return self.user_items(params=query)

    def get_resume_items(self, limit=20, parent_id=None,
                         include_item_types=None, media_types=None,
                         fields=None, image_type_limit=None,
                         enable_image_types=None,
                         enable_total_record_count=None):
        """Items the user can resume, most recently played first — the
        "Continue Watching" row.

        Pass ``media_types="Audio"`` for the audio equivalent ("Continue
        Listening"); it catches Audio and AudioBook without enumerating types.

        Leaving ``parent_id`` unset is meaningful: the server applies the
        user's "Display in home screen sections" library exclusions only to
        queries that carry no ``ParentId``.
        """
        return self.get_user_items(
            parent_id=parent_id, include_item_types=include_item_types,
            media_types=media_types, recursive=True, filters="IsResumable",
            sort_by="DatePlayed", sort_order="Descending", limit=limit,
            fields=fields, image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_total_record_count=enable_total_record_count)

    def get_random_items(self, parent_id=None, include_item_types=None,
                         limit=100, fields=None, image_types=None,
                         max_official_rating=None, enable_images=None,
                         enable_total_record_count=None, media_types=None):
        """A random sample of items, shuffled by the server (``SortBy=Random``)
        so it spans the whole library rather than one loaded page.

        ``image_types`` restricts the result to items that *have* that image
        (e.g. ``"Backdrop"`` when picking artwork), which is not the same as
        ``enable_image_types``.

        ``media_types`` (``"Video,Audio"``) filters on what an item *is to a
        player*, which for "give me something to queue" is usually a better
        axis than ``include_item_types``: that one matches the concrete
        entity the library scanner chose, so the answer depends on which
        resolver ran (a clip in a Home Videos library is a ``Video``, the
        same file in a movies library a ``Movie``).
        """
        return self.get_user_items(
            parent_id=parent_id, include_item_types=include_item_types,
            media_types=media_types,
            recursive=True, sort_by="Random", limit=limit, fields=fields,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
            params={k: v for k, v in (
                ('ImageTypes', image_types),
                ('MaxOfficialRating', max_official_rating),
            ) if v is not None})

    def get_items_by_person(self, person_id, include_item_types="Movie,Series",
                            sort_by="SortName", sort_order="Ascending",
                            start_index=None, limit=None, fields=None,
                            image_type_limit=None, enable_image_types=None):
        """A person's filmography — everything they are credited on."""
        return self.get_user_items(
            person_ids=person_id, include_item_types=include_item_types,
            recursive=True, sort_by=sort_by, sort_order=sort_order,
            start_index=start_index, limit=limit, fields=fields,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types)

    def get_album_tracks(self, album_id, fields=None):
        """An album's tracks in disc/track order.

        Sorted by ``ParentIndexNumber`` (disc) before ``IndexNumber`` (track),
        which is what keeps a multi-disc album in album order rather than
        interleaving the discs.
        """
        return self.get_user_items(
            parent_id=album_id, fields=fields, sort_order="Ascending",
            sort_by="ParentIndexNumber,IndexNumber,SortName")

    def get_artist_albums(self, artist_id, fields=None, limit=None,
                          image_type_limit=None, enable_image_types=None):
        """Albums credited to an album artist, newest first.

        Uses ``AlbumArtistIds``, not ``ArtistIds``: the latter also matches
        albums the artist merely guests on a track of.
        """
        return self.get_user_items(
            album_artist_ids=artist_id, include_item_types="MusicAlbum",
            recursive=True, sort_by="PremiereDate,ProductionYear,SortName",
            sort_order="Descending", limit=limit, fields=fields,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types)

    def get_artist_songs(self, artist_id, limit=None, fields=None):
        """Every track an artist appears on, in album order.

        Uses ``ArtistIds`` (not ``AlbumArtistIds``) so featured appearances
        are included — this backs "play everything by X".
        """
        return self.get_user_items(
            artist_ids=artist_id, include_item_types="Audio", recursive=True,
            sort_by="AlbumArtist,Album,ParentIndexNumber,IndexNumber,SortName",
            limit=limit, fields=fields)

    def get_genre_songs(self, genre_id, parent_id=None, limit=None,
                        fields=None):
        """Every track in a genre, optionally scoped to one music library."""
        return self.get_user_items(
            genre_ids=genre_id, parent_id=parent_id,
            include_item_types="Audio", recursive=True,
            sort_by="AlbumArtist,Album,ParentIndexNumber,IndexNumber,SortName",
            limit=limit, fields=fields)

    def get_endpoint_info(self):
        """Where the server thinks this connection came from (GET
        System/Endpoint) — ``{"IsLocal": bool, "IsInNetwork": bool}``.

        ``IsInNetwork`` is judged against the admin-configured LAN subnets, so
        it is the server's own answer to "is this client remote?", which a
        client cannot always work out for itself (notably over IPv6, where
        home networks use globally-routable addresses).

        References:
            .. [GetEndpointInfo] https://api.jellyfin.org/#tag/System/operation/GetEndpointInfo
        """
        return self._get("System/Endpoint")

    def update_user_settings(self, data, client="emby"):
        """Write back the display preferences read by ``get_user_settings``
        (POST DisplayPreferences/usersettings).

        There is no partial-update path on this API: the server replaces the
        whole document, so pass a DTO you read with ``get_user_settings`` and
        mutated, or you will drop settings other clients wrote.

        ``client`` must match the namespace the settings were read from — the
        official web client uses ``"emby"``, and any other string addresses a
        different, empty preference set.

        References:
            .. [UpdateDisplayPreferences] https://api.jellyfin.org/#tag/DisplayPreferences/operation/UpdateDisplayPreferences
        """
        return self._post("DisplayPreferences/usersettings", json=data,
                          params={"userId": "{UserId}", "client": client})

    def get_live_tv_info(self):
        """Live TV availability, per user (GET LiveTv/Info).

        ``IsEnabled`` is true on every server, because the built-in DVR
        counts as a Live TV service even with nothing behind it; ``Services``
        is just that service's name. The field to read is ``EnabledUsers``:
        the ids (32 hex digits, no dashes) of the users who hold the Live TV
        permission on a server that has at least one tuner or listings
        provider configured. Check the signed-in user against it before
        showing a guide or a recordings view -- the channel, program and
        timer calls answer with empty lists on a server without a tuner, so
        they cannot tell "nothing on" from "no Live TV".

        The call itself sits behind the Live TV permission: a user without
        it gets a 403, which ``HTTP.request`` raises as ``HTTPException``
        rather than returning.

        References:
            .. [GetLiveTvInfo] https://api.jellyfin.org/#tag/LiveTv/operation/GetLiveTvInfo
        """
        return self._get("LiveTv/Info")

    def get_channels(self, limit=None, start_index=None, fields=None,
                     enable_images=True, enable_user_data=True,
                     image_type_limit=None, enable_image_types=None,
                     add_current_program=None, is_favorite=None,
                     sort_by=None, sort_order=None,
                     enable_favorite_sorting=None, is_movie=None,
                     is_series=None, is_news=None, is_kids=None,
                     is_sports=None):
        """Live TV channels (GET LiveTv/Channels).

        The no-argument call is unbounded, which is only safe for small tuner
        line-ups: an M3U/IPTV source with thousands of channels answers with
        all of them, with images and user data. Pass ``limit``/``start_index``
        to page. Unlike the item endpoints there is no way to skip the total
        record count — this controller always computes and returns it.

        ``add_current_program`` (server default: true) attaches each channel's
        currently-airing program, which is what lets a channel list show "what
        is on now" without a second request to ``get_programs``.

        ``enable_favorite_sorting`` floats favourited channels to the top;
        ``sort_by="DatePlayed"`` orders by when the user last watched each
        one. Both are what the official guide's channel-order setting drives.

        The ``is_*`` category flags do NOT combine the way they look like
        they should. ``is_sports``/``is_news``/``is_kids`` become a tag
        filter and OR among themselves, but ``is_movie`` is a separate
        column predicate and ANDs with them — so ``is_movie=True,
        is_news=True`` asks for a movie that is also tagged News and matches
        nothing. Passing none of them means "every channel", which is the
        only way to express it: passing all four is an intersection, not a
        union. The same is true of ``get_programs``.

        References:
            .. [GetLiveTvChannels] https://api.jellyfin.org/#tag/LiveTv/operation/GetLiveTvChannels
        """
        params = {
            'UserId': "{UserId}",
            'EnableImages': enable_images,
            'EnableUserData': enable_user_data,
            'Limit': limit,
            'StartIndex': start_index,
            'Fields': fields,
            'ImageTypeLimit': image_type_limit,
            'EnableImageTypes': enable_image_types,
            'AddCurrentProgram': add_current_program,
            'IsFavorite': is_favorite,
            'SortBy': sort_by,
            'SortOrder': sort_order,
            'EnableFavoriteSorting': enable_favorite_sorting,
            'IsMovie': is_movie,
            'IsSeries': is_series,
            'IsNews': is_news,
            'IsKids': is_kids,
            'IsSports': is_sports,
        }
        return self._get("LiveTv/Channels",
                         {k: v for k, v in params.items() if v is not None})

    def get_programs(self, channel_ids=None, library_series_id=None,
                     min_start_date=None, max_start_date=None,
                     min_end_date=None, max_end_date=None, is_airing=None,
                     is_movie=None, is_series=None, is_news=None,
                     is_kids=None, is_sports=None, genres=None,
                     sort_by=None, sort_order=None, start_index=None,
                     limit=None, fields=None, image_type_limit=None,
                     enable_image_types=None, enable_user_data=None,
                     enable_total_record_count=None,
                     has_aired=None):
        """Guide entries (GET LiveTv/Programs).

        ``channel_ids`` accepts a list or a comma-separated string, matching
        the server's comma-delimited binder. ``genres`` does NOT: that one
        binds pipe-delimited (``value.Split('|')``), so join it with ``|`` or
        the whole string arrives as a single bogus genre.

        ``has_aired=False`` is what an "upcoming" list asks for; ``is_airing``
        is the narrower "on right now". They are separate filters, not two
        spellings of one — the official clients' Programs screen pairs
        ``has_aired=False`` with the category flags for its upcoming rows.

        The date bounds are how a guide grid asks for one time window. They
        must be ISO 8601 carrying ``Z`` or an explicit offset — the server
        binds them with ``AdjustToUniversal``, and an offset-less string
        (including what ``str(datetime)`` produces) is accepted without being
        shifted, silently querying the wrong window.

        This is the GET form, so the whole query travels in the request line;
        past roughly 150-200 channel ids that exceeds the default request-line
        limit in Kestrel and common reverse proxies (414/431). Page the
        channel set, as the official guide does. The server also offers a POST
        form for large line-ups, which is not implemented here.

        Request ``fields="ChannelInfo"`` to get ``ChannelName`` and
        ``ChannelNumber`` on each program. The channel's **logo** is a
        separate field: ``AddInfoToProgramDto`` sets
        ``ChannelPrimaryImageTag`` only under ``ChannelImage``, so ask for
        ``fields="ChannelInfo,ChannelImage"`` — as the official clients do.
        That matters more than it sounds, because guide data often carries
        no artwork of its own and the channel logo is then the only image
        available at all.

        References:
            .. [GetLiveTvPrograms] https://api.jellyfin.org/#tag/LiveTv/operation/GetLiveTvPrograms
        """
        if channel_ids is not None and not isinstance(channel_ids, str):
            channel_ids = ','.join(str(x) for x in channel_ids)
        params = {
            'UserId': "{UserId}",
            'ChannelIds': channel_ids,
            'LibrarySeriesId': library_series_id,
            'MinStartDate': min_start_date,
            'MaxStartDate': max_start_date,
            'MinEndDate': min_end_date,
            'MaxEndDate': max_end_date,
            'IsAiring': is_airing,
            'HasAired': has_aired,
            'IsMovie': is_movie,
            'IsSeries': is_series,
            'IsNews': is_news,
            'IsKids': is_kids,
            'IsSports': is_sports,
            'Genres': genres,
            'SortBy': sort_by,
            'SortOrder': sort_order,
            'StartIndex': start_index,
            'Limit': limit,
            'Fields': fields,
            'ImageTypeLimit': image_type_limit,
            'EnableImageTypes': enable_image_types,
            'EnableUserData': enable_user_data,
            'EnableTotalRecordCount': enable_total_record_count,
        }
        return self._get("LiveTv/Programs",
                         {k: v for k, v in params.items() if v is not None})

    def get_recommended_programs(self, is_airing=None, has_aired=None,
                                 is_series=None, is_movie=None, is_news=None,
                                 is_kids=None, is_sports=None, genre_ids=None,
                                 limit=None, fields=None,
                                 image_type_limit=None,
                                 enable_image_types=None,
                                 enable_user_data=None,
                                 enable_total_record_count=None):
        """The server's recommended guide entries (GET
        LiveTv/Programs/Recommended).

        ``is_airing=True`` is the "On Now" strip the official clients show on
        the home screen. As with ``get_programs``, pass
        ``fields="…,ChannelInfo,ChannelImage"`` or most entries will have no
        artwork — the logo needs the second of those, see there.

        References:
            .. [GetRecommendedPrograms] https://api.jellyfin.org/#tag/LiveTv/operation/GetRecommendedPrograms
        """
        params = {
            'UserId': "{UserId}",
            'IsAiring': is_airing,
            'HasAired': has_aired,
            'IsSeries': is_series,
            'IsMovie': is_movie,
            'IsNews': is_news,
            'IsKids': is_kids,
            'IsSports': is_sports,
            'GenreIds': genre_ids,
            'Limit': limit,
            'Fields': fields,
            'ImageTypeLimit': image_type_limit,
            'EnableImageTypes': enable_image_types,
            'EnableUserData': enable_user_data,
            'EnableTotalRecordCount': enable_total_record_count,
        }
        return self._get("LiveTv/Programs/Recommended",
                         {k: v for k, v in params.items() if v is not None})

    def get_live_tv_program(self, program_id):
        """One guide entry, with its recording state (GET
        LiveTv/Programs/{id}).

        The ``TimerId``/``SeriesTimerId``/``Status`` fields this carries are
        what a program page needs to decide whether its Record button reads
        "Record" or "Cancel Recording" — the list endpoints omit them unless
        user data is enabled, and even then are a snapshot from before the
        user pressed anything.

        References:
            .. [GetProgram] https://api.jellyfin.org/#tag/LiveTv/operation/GetProgram
        """
        return self._get("LiveTv/Programs/%s" % program_id,
                         {'UserId': "{UserId}"})

    def get_live_tv_guide_info(self):
        """The guide's available date range (GET LiveTv/GuideInfo).

        ``StartDate``/``EndDate`` bound how far the date picker may go; a
        guide that offers days the provider has no data for just shows empty
        rows.

        References:
            .. [GetGuideInfo] https://api.jellyfin.org/#tag/LiveTv/operation/GetGuideInfo
        """
        return self._get("LiveTv/GuideInfo")

    def get_live_tv_recordings(self, series_timer_id=None, is_in_progress=None,
                               status=None, start_index=None, limit=None,
                               fields=None, enable_images=None,
                               image_type_limit=None, enable_image_types=None,
                               enable_user_data=None,
                               enable_total_record_count=None):
        """Completed and in-progress recordings (GET LiveTv/Recordings).

        ``is_in_progress=True`` is the "recording right now" list; the
        unfiltered call is the recordings library. Recordings are ordinary
        items once written, so they play through the normal item path.

        References:
            .. [GetRecordings] https://api.jellyfin.org/#tag/LiveTv/operation/GetRecordings
        """
        params = {
            'UserId': "{UserId}",
            'SeriesTimerId': series_timer_id,
            'IsInProgress': is_in_progress,
            'Status': status,
            'StartIndex': start_index,
            'Limit': limit,
            'Fields': fields,
            'EnableImages': enable_images,
            'ImageTypeLimit': image_type_limit,
            'EnableImageTypes': enable_image_types,
            'EnableUserData': enable_user_data,
            'EnableTotalRecordCount': enable_total_record_count,
        }
        return self._get("LiveTv/Recordings",
                         {k: v for k, v in params.items() if v is not None})

    def get_recording_folders(self):
        """The virtual folders recordings are filed under (GET
        LiveTv/Recordings/Folders) — one per recording group the server
        keeps, which is what the Recordings screen browses into.

        References:
            .. [GetRecordingFolders] https://api.jellyfin.org/#tag/LiveTv/operation/GetRecordingFolders
        """
        return self._get("LiveTv/Recordings/Folders",
                         {'UserId': "{UserId}"})

    def get_live_tv_timers(self, channel_id=None, series_timer_id=None,
                           is_active=None, is_scheduled=None):
        """Scheduled single recordings (GET LiveTv/Timers).

        ``is_active=False, is_scheduled=True`` is the "Upcoming Recordings"
        list; ``is_active=True`` is what is recording now. The DTOs are
        ``Timer`` objects, not items — they carry ``ProgramId``, the channel
        and the start/end times, and are addressed by their own ``Id``.

        References:
            .. [GetTimers] https://api.jellyfin.org/#tag/LiveTv/operation/GetTimers
        """
        params = {
            'ChannelId': channel_id,
            'SeriesTimerId': series_timer_id,
            'IsActive': is_active,
            'IsScheduled': is_scheduled,
        }
        return self._get("LiveTv/Timers",
                         {k: v for k, v in params.items() if v is not None})

    def get_live_tv_timer(self, timer_id):
        """One timer, for the recording editor (GET LiveTv/Timers/{id})."""
        return self._get("LiveTv/Timers/%s" % timer_id)

    def get_new_timer_defaults(self, program_id=None):
        """A pre-filled timer for ``program_id`` (GET LiveTv/Timers/Defaults).

        This is how a recording is created: ask the server for the defaults
        (padding, keep-until, and the program's own channel and times), then
        POST the result back — creating one from a hand-built DTO skips the
        server's own configuration.

        Called without ``program_id`` it returns the bare defaults, which is
        what the series-timer editor shows for a new series rule.

        References:
            .. [GetDefaultTimer] https://api.jellyfin.org/#tag/LiveTv/operation/GetDefaultTimer
        """
        params = {'programId': program_id} if program_id else None
        return self._get("LiveTv/Timers/Defaults", params)

    def create_live_tv_timer(self, timer):
        """Schedule a single recording from a ``get_new_timer_defaults``
        payload (POST LiveTv/Timers)."""
        return self._post("LiveTv/Timers", json=timer)

    def update_live_tv_timer(self, timer_id, timer):
        """Rewrite a timer (POST LiveTv/Timers/{id}). The whole DTO is
        replaced, so send one you read back from ``get_live_tv_timer``."""
        return self._post("LiveTv/Timers/%s" % timer_id, json=timer)

    def cancel_live_tv_timer(self, timer_id):
        """Cancel a scheduled recording, or stop one in progress (DELETE
        LiveTv/Timers/{id})."""
        return self._delete("LiveTv/Timers/%s" % timer_id)

    def get_live_tv_series_timers(self, sort_by=None, sort_order=None):
        """Series recording rules (GET LiveTv/SeriesTimers).

        References:
            .. [GetSeriesTimers] https://api.jellyfin.org/#tag/LiveTv/operation/GetSeriesTimers
        """
        params = {'SortBy': sort_by, 'SortOrder': sort_order}
        return self._get("LiveTv/SeriesTimers",
                         {k: v for k, v in params.items() if v is not None})

    def get_live_tv_series_timer(self, timer_id):
        """One series rule, for the series editor (GET
        LiveTv/SeriesTimers/{id})."""
        return self._get("LiveTv/SeriesTimers/%s" % timer_id)

    def create_live_tv_series_timer(self, timer):
        """Record every showing of a program (POST LiveTv/SeriesTimers).

        Takes the same ``get_new_timer_defaults`` payload the single-recording
        path uses; the server derives the series rule from the program it was
        seeded with.
        """
        return self._post("LiveTv/SeriesTimers", json=timer)

    def update_live_tv_series_timer(self, timer_id, timer):
        """Rewrite a series rule (POST LiveTv/SeriesTimers/{id})."""
        return self._post("LiveTv/SeriesTimers/%s" % timer_id, json=timer)

    def cancel_live_tv_series_timer(self, timer_id):
        """Stop recording a series (DELETE LiveTv/SeriesTimers/{id})."""
        return self._delete("LiveTv/SeriesTimers/%s" % timer_id)

    def get_intros(self, item_id):
        return self.user_items("/%s/Intros" % item_id)

    def get_additional_parts(self, item_id):
        return self.videos("/%s/AdditionalParts" % item_id)

    def get_media_segments(self, item_id, include_segment_types=None):
        """Media segments (intros, outros, previews, …) for an item.

        ``include_segment_types`` takes a list of segment type names; the
        server repeats the parameter per type. Segments come from a plugin, so
        an item can legitimately have none.
        """
        params = None
        if include_segment_types is not None:
            if isinstance(include_segment_types, str):
                include_segment_types = [include_segment_types]
            params = {'includeSegmentTypes': list(include_segment_types)}
        return self.media_segments("/%s" % item_id, params)

    def delete_item(self, item_id):
        return self.items("/%s" % item_id, "DELETE")

    def get_local_trailers(self, item_id):
        return self.user_items("/%s/LocalTrailers" % item_id)

    def get_similar(self, item_id, limit=12, fields=None):
        """Items similar to the given one (GET Items/{id}/Similar) — the
        "More Like This" row in the official clients.

        References:
            .. [GetSimilarItems] https://api.jellyfin.org/#tag/Library/operation/GetSimilarItems
        """
        params = {"UserId": "{UserId}", "Limit": limit}
        if fields is not None:
            params["Fields"] = fields
        return self.items("/%s/Similar" % item_id, params=params)

    def get_filters(self, parent_id=None, include_item_types=None):
        """Distinct filter values (genres, tags, official ratings, years)
        available under a folder (GET Items/Filters) — used to build filter
        pickers without scanning the whole library client-side.

        References:
            .. [GetQueryFiltersLegacy] https://api.jellyfin.org/#tag/Filter/operation/GetQueryFiltersLegacy
        """
        params = {"UserId": "{UserId}"}
        if parent_id is not None:
            params["ParentId"] = parent_id
        if include_item_types is not None:
            params["IncludeItemTypes"] = include_item_types
        return self.items("/Filters", params=params)

    def get_persons(self, search_term=None, limit=20, fields=None):
        """Search people (GET Persons) — actors/directors for people search.

        References:
            .. [GetPersons] https://api.jellyfin.org/#tag/Persons/operation/GetPersons
        """
        params = {"UserId": "{UserId}", "Limit": limit}
        if search_term is not None:
            params["SearchTerm"] = search_term
        if fields is not None:
            params["Fields"] = fields
        return self._get("Persons", params)

    def get_transcode_settings(self):
        return self._get('System/Configuration/encoding')

    def get_ancestors(self, item_id):
        return self.items("/%s/Ancestors" % item_id, params={
            'UserId': "{UserId}"
        })

    def get_items_theme_video(self, parent_id):
        return self.users("/Items", params={
            'HasThemeVideo': True,
            'ParentId': parent_id
        })

    def get_themes(self, item_id):
        return self.items("/%s/ThemeMedia" % item_id, params={
            'UserId': "{UserId}",
            'InheritFromParent': True
        })

    def get_items_theme_song(self, parent_id):
        return self.users("/Items", params={
            'HasThemeSong': True,
            'ParentId': parent_id
        })

    def get_plugins(self):
        return self._get("Plugins")

    def check_companion_installed(self):
        try:
            self._get("/Jellyfin.Plugin.KodiSyncQueue/GetServerDateTime")
            return True
        except Exception:
            return False

    def get_seasons(self, show_id):
        return self.shows("/%s/Seasons" % show_id, params={
            'UserId': "{UserId}",
            'EnableImages': True,
            'Fields': info()
        })

    def get_date_modified(self, date, parent_id, media=None):
        return self.users("/Items", params={
            'ParentId': parent_id,
            'Recursive': False,
            'IsMissing': False,
            'IsVirtualUnaired': False,
            'IncludeItemTypes': media or None,
            'MinDateLastSaved': date,
            'Fields': info()
        })

    def get_userdata_date_modified(self, date, parent_id, media=None):
        return self.users("/Items", params={
            'ParentId': parent_id,
            'Recursive': True,
            'IsMissing': False,
            'IsVirtualUnaired': False,
            'IncludeItemTypes': media or None,
            'MinDateLastSavedForUser': date,
            'Fields': info()
        })

    def get_userdata_for_item(self, item_id):
        return self._get(
            f"UserItems/{item_id}/UserData", params={"UserId": "{UserId}"}
        )

    def update_userdata_for_item(self, item_id, data):
        """
        Updates the userdata for an item.

        Args:
            item_id (str): item uuid to update userdata for

            data (dict): the information to add to the current user's
                userdata for the item. Any fields in data overwrite the
                equivalent fields in UserData, other UserData fields are
                left untouched.

        References:
            .. [UpdateItemUserData] https://api.jellyfin.org/#tag/Items/operation/UpdateItemUserData
        """
        return self._post(f"UserItems/{item_id}/UserData", params={"UserId": "{UserId}"}, json=data)


    def refresh_item(self, item_id, recursive=True, image_refresh='FullRefresh', metadata_refresh='FullRefresh', replace_images=False, replace_metadata=True, preset=None):
        """
        Description:

            - Refreshes media items on server. Pass a single item or pass multiple as a list.
            - Use of presets lets you run a refresh similar to Jellyfin's Web UI.
            - preset='missing' searches for missing metadata, while preset='replace' replaces all metadata.
            - You may also configure the refresh manually by passing a value for each parameter.

        Args:
            item_id (str | List[str]): one or more items to refresh
            recursive (bool):
            image_refresh (str):  'Default' or 'ValidationOnly' or 'FullRefresh'
            image_refresh (str): 'Default' or 'ValidationOnly' or 'FullRefresh'
            replace_images (bool):
            replace_metadata (bool)
            preset (str): 'missing' or 'replace'

        Examples:
            >>> client.jellyfin.refresh_item('123456abcd', preset='missing')
            -
            >>> client.jellyfin.refresh_item(['123456abcd', 'abcd123456'])
        """

        # Presets modeled after Jellyfin's Web UI
        if preset:
            if preset.lower() == 'missing':
                recursive = True
                image_refresh = 'FullRefresh'
                metadata_refresh = 'FullRefresh'
                replace_images = False
                replace_metadata = False
            elif preset.lower() == 'replace':
                recursive = True
                image_refresh = 'FullRefresh'
                metadata_refresh = 'FullRefresh'
                replace_images = True
                replace_metadata = True

        params = {
            'Recursive': recursive,
            'ImageRefreshMode': image_refresh,
            'MetadataRefreshMode': metadata_refresh,
            'ReplaceAllImages': replace_images,
            'ReplaceAllMetadata': replace_metadata
        }

        # If item_id is a list, loop through each item and refresh it
        if isinstance(item_id, list):
            results = []
            for i in item_id:
                result = self.items("/%s/Refresh" % i, "POST", params=params)
                results.append(result)
            return results
        else:
            # If item_id is a single string, just refresh that item
            return self.items("/%s/Refresh" % item_id, "POST", params=params)

    def favorite(self, item_id, option=True):
        return self.users("/FavoriteItems/%s" % item_id, "POST" if option else "DELETE")

    def get_system_info(self):
        """Returns configuration for legacy reasons, not System/Info, use get_system_info_new for that"""
        return self._get("System/Configuration")

    def get_system_info_new(self):
        """Actual System/Info API call"""
        return self._get("System/Info")

    def get_system_configuration(self):
        return self._get("System/Configuration")

    def get_server_logs(self):
        """
        Returns:
            List[Dict] - list of information about available log files

        References:
            .. [GetServerLogs] https://api.jellyfin.org/#tag/System/operation/GetServerLogs
        """
        return self._get("System/Logs")

    def get_log_entries(self, startIndex=None, limit=None, minDate=None, hasUserId=None):
        """
        Returns a list of recent log entries

        Returns:
            Dict: with main key "Items"
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if startIndex is not None:
            params['startIndex'] = startIndex
        if minDate is not None:
            params['minDate'] = minDate
        if hasUserId is not None:
            params['hasUserId'] = hasUserId
        return self._get("System/ActivityLog/Entries", params=params)

    def post_capabilities(self, data):
        return self.sessions("/Capabilities/Full", "POST", json=data)

    def session_add_user(self, session_id, user_id, option=True):
        return self.sessions("/%s/Users/%s" % (session_id, user_id), "POST" if option else "DELETE")

    def session_playing(self, data):
        return self.sessions("/Playing", "POST", json=data)

    def session_progress(self, data):
        return self.sessions("/Playing/Progress", "POST", json=data)

    def session_stop(self, data):
        return self.sessions("/Playing/Stopped", "POST", json=data)

    def remote_pause(self, id):
        return self.remote(id, "Pause")

    def remote_playpause(self, id):
        return self.remote(id, "PlayPause")

    def remote_seek(self, id, ticks, params={}, json={}):
        """
        Seek to a specific position in the specified session.

        Args:
            id (int): The session id to control
            ticks (int): The position (in ticks) to seek to
        """
        return self.remote(
            id, "Seek", params={"seekPositionTicks": ticks, **params}, json=json
        )

    def remote_stop(self, id):
        return self.remote(id, "Stop")

    def remote_unpause(self, id):
        return self.remote(id, "Unpause")

    def remote_play_media(
        self, id: str, item_ids: List[str], command: str = "PlayNow", params={}, json={}
    ):
        """Instruct the session to play some media

        Args:
            id (str): The session id to control
            item_ids (List[str]): A list of items to play
            command (str): When to play. (*PlayNow*, PlayNext, PlayLast, PlayInstantMix, PlayShuffle)
        """
        return self.remote(
            id,
            None,
            json=json,
            params={"playCommand": command, "itemIds": item_ids, **params},
        )

    def remote_set_volume(self, id: str, volume: int, json={}):
        """
        Set the volume on the sessions.

        Args:
            id (int): The session id to control
            volume (int): The volume normalized from 0 to 100
        """
        return self.command(id, "SetVolume", json={"Volume": volume, **json})

    def remote_mute(self, id):
        return self.command(id, "Mute")

    def remote_unmute(self, id):
        return self.command(id, "Unmute")

    def item_played(self, item_id, watched, date=None):
        params = {}
        if watched and date is not None:
            params["datePlayed"] = date
        return self.users("/PlayedItems/%s" % item_id, "POST" if watched else "DELETE", params=params)

    def get_sync_queue(self, date, filters=None):
        return self._get("Jellyfin.Plugin.KodiSyncQueue/{UserId}/GetItems", params={
            'LastUpdateDT': date,
            'filter': filters or None
        })

    def get_server_time(self):
        return self._get("Jellyfin.Plugin.KodiSyncQueue/GetServerDateTime")

    def get_play_info(self, item_id, profile=None, aid=None, sid=None, start_time_ticks=None, is_playback=True, media_source_id=None):
        args = {
            'UserId': "{UserId}",
            'AutoOpenLiveStream': is_playback,
            'IsPlayback': is_playback
        }
        if profile is not None:
            args['DeviceProfile'] = profile
        if sid:
            args['SubtitleStreamIndex'] = sid
        if aid:
            args['AudioStreamIndex'] = aid
        if start_time_ticks:
            args['StartTimeTicks'] = start_time_ticks
        if media_source_id:
            args['MediaSourceId'] = media_source_id

        return self.items("/%s/PlaybackInfo" % item_id, "POST", json=args)

    def get_live_stream(self, item_id, play_id, token, profile):
        return self._post("LiveStreams/Open", json={
            'UserId': "{UserId}",
            'DeviceProfile': profile,
            'OpenToken': token,
            'PlaySessionId': play_id,
            'ItemId': item_id
        })

    def close_live_stream(self, live_id):
        """Release a live stream and the tuner behind it.

        The id goes in the query string because that is where the server binds
        it (``CloseLiveStream([FromQuery, Required] string liveStreamId)``);
        sent as a JSON body it fails model validation with a 400 and the
        stream is never closed. Nothing reaps a leaked stream — it is freed
        only by this call, a stop report carrying the ``LiveStreamId``, a
        session disconnect, or a server restart — so on a single-tuner box a
        leak means no more live TV until the server comes back.
        """
        return self._post("LiveStreams/Close",
                          params={'liveStreamId': live_id})

    def close_transcode(self, device_id, play_session_id):
        return self._delete("Videos/ActiveEncodings", params={
            'DeviceId': device_id,
            'PlaySessionId': play_session_id,
        })

    def get_audio_stream(self, dest_file, item_id, play_id, container, max_streaming_bitrate=140000000, audio_codec=None):
        self._get_stream("Audio/%s/universal" % item_id, dest_file, params={
            'UserId': "{UserId}",
            'DeviceId': "{DeviceId}",
            'PlaySessionId': play_id,
            'Container': container,
            'AudioCodec': audio_codec,
            "MaxStreamingBitrate": max_streaming_bitrate,
        })

    def get_chapter_image(self, dest_file, item_id, index, tag=None,
                          max_width=None, quality=None):
        """Download one chapter thumbnail into ``dest_file``.

        ``index`` is the chapter's position in the item's ``Chapters`` list;
        ``tag`` is that chapter's ``ImageTag`` and is what makes the URL
        cacheable. Chapters without an ``ImageTag`` have no image — asking for
        one is a 404.

        Use ``image_url(item_id, "Chapter", index=…, tag=…)`` instead when a
        URL is wanted rather than the bytes.
        """
        params = {'tag': tag, 'maxWidth': max_width, 'quality': quality}
        self._get_stream(
            "Items/%s/Images/Chapter/%s" % (item_id, index), dest_file,
            {k: v for k, v in params.items() if v is not None})

    def get_trickplay_tile(self, dest_file, item_id, width, index,
                           media_source_id=None):
        """Download one trickplay (scrubbing preview) tile sheet into
        ``dest_file``.

        ``width`` selects which generated resolution to read and must be one
        the server actually produced — the item's ``Trickplay`` manifest lists
        them (request the ``Trickplay`` field to get it).

        See ``trickplay_tile_url`` for the URL-building equivalent.
        """
        params = {}
        if media_source_id is not None:
            params['MediaSourceId'] = media_source_id
        self._get_stream(
            "Videos/%s/Trickplay/%s/%s.jpg" % (item_id, width, index),
            dest_file, params)

    def get_default_headers(self):
        return self.client._get_default_headers(content_type="application/x-www-form-urlencoded; charset=UTF-8")

    def send_request(self, url, path, method="get", timeout=None, headers=None, data=None, session=None):
        request_method = getattr(session or requests, method.lower())
        url = "%s/%s" % (url, path)
        request_settings = {
            "timeout": timeout or self.default_timeout,
            "headers": headers or self.get_default_headers(),
            "data": data
        }

        # Changed to use non-Kodi specific setting.
        if self.config.data.get('auth.ssl') is False:
            request_settings["verify"] = False

        LOG.info("Sending %s request to %s" % (method, path))
        LOG.debug(request_settings['timeout'])
        LOG.debug(request_settings['headers'])

        return request_method(url, **request_settings)

    def login(self, server_url, username, password="", session=None):
        path = "Users/AuthenticateByName"
        authData = {
                    "username": username,
                    "Pw": password
                }

        headers = self.get_default_headers()
        headers.update({'Content-type': "application/json"})

        try:
            LOG.info("Trying to login to %s/%s as %s" % (server_url, path, username))
            response = self.send_request(server_url, path, method="post", headers=headers,
                                         data=json.dumps(authData), timeout=(5, 30), session=session)

            if response.status_code == 200:
                return response.json()
            else:
                LOG.error("Failed to login to server with status code: " + str(response.status_code))
                LOG.error("Server Response:\n" + str(response.content))
                LOG.debug(headers)

                return {}
        except Exception as e:  # Find exceptions for likely cases i.e, server timeout, etc
            LOG.error(e)

        return {}

    def quick_connect_enabled(self, server_url, session=None):
        """Return whether Quick Connect is enabled on the server."""
        try:
            response = self.send_request(
                server_url, "QuickConnect/Enabled", session=session
            )
            if response.status_code == 200:
                return bool(response.json())
            LOG.error(
                "Failed to query Quick Connect status: " + str(response.status_code)
            )
        except Exception as e:
            LOG.error(e)

        return False

    def quick_connect_initiate(self, server_url, session=None):
        """Start a Quick Connect request, returning a dict with Secret and Code."""
        headers = self.get_default_headers()

        try:
            response = self.send_request(
                server_url, "QuickConnect/Initiate", method="post",
                headers=headers, timeout=(5, 30), session=session
            )
            if response.status_code == 200:
                return response.json()
            LOG.error(
                "Failed to initiate Quick Connect: " + str(response.status_code)
            )
        except Exception as e:
            LOG.error(e)

        return {}

    def quick_connect_state(self, server_url, secret, session=None):
        """Return the current state of a Quick Connect request as a dict.

        The returned dict's ``Authenticated`` field indicates whether the user
        has approved the request yet.
        """
        path = "QuickConnect/Connect?secret=" + quote(secret, safe="")

        try:
            response = self.send_request(server_url, path, session=session)
            if response.status_code == 200:
                return response.json()
            LOG.error(
                "Failed to query Quick Connect state: " + str(response.status_code)
            )
        except Exception as e:
            LOG.error(e)

        return {}

    def login_with_quick_connect(self, server_url, secret, session=None):
        """Exchange an authorized Quick Connect secret for an AuthenticationResult.

        Returns the same payload shape as ``login()`` (AccessToken, User, ...)
        on success, or an empty dict on failure.
        """
        path = "Users/AuthenticateWithQuickConnect"
        authData = {"Secret": secret}

        headers = self.get_default_headers()
        headers.update({'Content-type': "application/json"})

        try:
            response = self.send_request(
                server_url, path, method="post", headers=headers,
                data=json.dumps(authData), timeout=(5, 30), session=session
            )
            if response.status_code == 200:
                return response.json()
            LOG.error(
                "Failed to authenticate with Quick Connect, status code: "
                + str(response.status_code)
            )
            LOG.error("Server Response:\n" + str(response.content))
        except Exception as e:
            LOG.error(e)

        return {}

    def validate_authentication_token(self, server, session=None):
        headers = self.get_default_headers()
        comma = "," if "app.device_name" in self.config.data else ""
        headers["Authorization"] += f"{comma} Token=\"{server['AccessToken']}\""

        response = self.send_request(server['address'], "system/info", headers=headers, session=session)
        return response.json() if response.status_code == 200 else {}

    def get_public_info(self, server_address, session=None):
        response = self.send_request(server_address, "system/info/public", session=session)
        return response.json() if response.status_code == 200 else {}

    def check_redirect(self, server_address, session=None):
        ''' Checks if the server is redirecting traffic to a new URL and
        returns the URL the server prefers to use
        '''
        response = self.send_request(server_address, "system/info/public", session=session)
        url = response.url.replace('/system/info/public', '')
        return url


class SyncPlayAPIMixin:
    """
    Mixin class containing Jellyfin API calls related to Syncplay
    """

    def _parse_precise_time(self, time):
        # We have to remove the Z and the least significant digit.
        return datetime.strptime(time[:-2], "%Y-%m-%dT%H:%M:%S.%f")

    def utc_time(self):
        # Measure time as close to the call as is possible.
        server_address = self.config.data.get("auth.server")
        session = self.client.session

        response = self.send_request(server_address, "GetUTCTime", session=session)
        response_received = datetime.utcnow()
        request_sent = response_received - response.elapsed

        response_obj = response.json()
        request_received = self._parse_precise_time(response_obj["RequestReceptionTime"])
        response_sent = self._parse_precise_time(response_obj["ResponseTransmissionTime"])

        return {
            "request_sent": request_sent,
            "request_received": request_received,
            "response_sent": response_sent,
            "response_received": response_received
        }

    def get_sync_play(self, item_id=None):
        params = {}
        if item_id is not None:
            params["FilterItemId"] = item_id
        return self._get("SyncPlay/List", params)

    def join_sync_play(self, group_id):
        return self._post("SyncPlay/Join", {
            "GroupId": group_id
        })

    def leave_sync_play(self):
        return self._post("SyncPlay/Leave")

    def play_sync_play(self):
        """deprecated (<= 10.7.0)"""
        return self._post("SyncPlay/Play")

    def pause_sync_play(self):
        return self._post("SyncPlay/Pause")

    def unpause_sync_play(self):
        """10.7.0+ only"""
        return self._post("SyncPlay/Unpause")

    def seek_sync_play(self, position_ticks):
        return self._post("SyncPlay/Seek", {
            "PositionTicks": position_ticks
        })

    def buffering_sync_play(self, when, position_ticks, is_playing, item_id):
        return self._post("SyncPlay/Buffering", {
            "When": when.isoformat() + "Z",
            "PositionTicks": position_ticks,
            "IsPlaying": is_playing,
            "PlaylistItemId": item_id
        })

    def ready_sync_play(self, when, position_ticks, is_playing, item_id):
        """10.7.0+ only"""
        return self._post("SyncPlay/Ready", {
            "When": when.isoformat() + "Z",
            "PositionTicks": position_ticks,
            "IsPlaying": is_playing,
            "PlaylistItemId": item_id
        })

    def reset_queue_sync_play(self, queue_item_ids, position=0, position_ticks=0):
        """10.7.0+ only"""
        return self._post("SyncPlay/SetNewQueue", {
            "PlayingQueue": queue_item_ids,
            "PlayingItemPosition": position,
            "StartPositionTicks": position_ticks
        })

    def ignore_sync_play(self, should_ignore):
        """10.7.0+ only"""
        return self._post("SyncPlay/SetIgnoreWait", {
            "IgnoreWait": should_ignore
        })

    def next_sync_play(self, item_id):
        """10.7.0+ only"""
        return self._post("SyncPlay/NextItem", {
            "PlaylistItemId": item_id
        })

    def prev_sync_play(self, item_id):
        """10.7.0+ only"""
        return self._post("SyncPlay/PreviousItem", {
            "PlaylistItemId": item_id
        })

    def set_item_sync_play(self, item_id):
        """10.7.0+ only"""
        return self._post("SyncPlay/SetPlaylistItem", {
            "PlaylistItemId": item_id
        })

    def ping_sync_play(self, ping):
        return self._post("SyncPlay/Ping", {
            "Ping": ping
        })

    def new_sync_play(self):
        """deprecated (< 10.7.0)"""
        return self._post("SyncPlay/New")

    def new_sync_play_v2(self, group_name):
        """10.7.0+ only"""
        return self._post("SyncPlay/New", {
            "GroupName": group_name
        })


class ExperimentalAPIMixin:
    """
    This is a location for testing proposed additions to the API Client.
    """

    def identify(self, item_id, name=None, provider_ids=None, year=None, replaceAllImages=True):
        """
        Applies search criteria to an item and refreshes metadata.

        This method requires an authenticated user with elevated permissions
        [RequiresElevation]_.

        Args:
            item_id (str): item uuid to identify and update metadata for.

            name (str):
                name for the identified item
            provider_ids (dict):
                maps providers to the content id. (E.g. {"Imdb": "tt1254207"})
                Valid keys will depend on available providers. Common ones are:
                    "Tvdb" and "Imdb".
            year (int):
                production year for the identified idem
            replaceAllImages(bool):
                whether all images should be replaced by default

        References:
            .. [ApplySearchCriteria] https://api.jellyfin.org/#tag/ItemLookup/operation/ApplySearchCriteria
        """

        data = {
            'Name': name, 
            'ProviderIds': provider_ids, 
            'ProductionYear': year
        }
        params = {
            'replaceAllImages': replaceAllImages
        }

        return self._post(
            f'Items/RemoteSearch/Apply/{item_id}', params=params, json=data
        )


    def get_now_playing(self, session_id):
        """
        Simplified API to get now playing information for a session including the
        play state.

        References:
            https://github.com/jellyfin/jellyfin/issues/9665
        """
        resp = self.sessions(params={
            'Id': session_id,
            'fields': ['PlayState']
        })
        found = None
        for item in resp:
            if item['Id'] == session_id:
                found = item
        if not found:
            raise KeyError(f'No session_id={session_id}')
        play_state = found['PlayState']
        now_playing = found.get('NowPlayingItem', None)
        if now_playing is None:
            # handle case if nothing is playing
            now_playing = {'Name': None}
        now_playing['PlayState'] = play_state
        return now_playing

    @staticmethod
    def _coerce_image_bytes(image_data) -> bytes:
        """
        Transform data into a common b64 representation with associated mime
        type
        """
        import os
        import base64
        import mimetypes

        image_bytes = None

        # It doesn't seem to matter which image mimetype we choose
        mimetype = 'image/jpeg'

        if isinstance(image_data, (str, os.PathLike)):
            file_path = image_data

            mimetype, encoding = mimetypes.guess_type(file_path)

            with open(file_path, 'rb') as f:
                raw_data = f.read()
                img_bytes1 = base64.b64encode(raw_data)

            image_bytes = img_bytes1
        elif isinstance(image_data, bytes):
            image_bytes = image_data

        if image_bytes is None:
            raise Exception("unable to construct image bytes")

        return image_bytes, mimetype

    def set_item_image(self, item_id, image_data, image_type='Primary',
                       mimetype='auto'):
        """
        Args:
            item_id (str): item to set the image of

            image_data (str | PathLike | bytes):
                A path to an image on disk or raw bytes of an image.

            image_type (str): A valid image type. I.e. one of
                'Primary', 'Art', 'Backdrop', 'Banner', 'Logo', 'Thumb',
                'Disc', 'Box', 'Screenshot', 'Menu', 'Chapter', 'BoxRear',
                'Profile'.

            mimetype (str): if "auto", attempt to infer the mimetype.
                falls back to image/jpeg if unable. Otherwise this is used.

        References:
            .. [SetItemImageByIndex] https://api.jellyfin.org/#tag/Image/operation/SetItemImageByIndex
        """
        from jellyfin_apiclient_python.constants import ImageType

        image_bytes, auto_mimetype = self._coerce_image_bytes(image_data)

        if mimetype == 'auto':
            mimetype = auto_mimetype

        if image_type not in ImageType:
            raise KeyError(f'image_type must be one of: {ImageType}')

        data = image_bytes.decode()

        # Overriding headers are important for this call
        headers = {
            'Accept': '*/*',
            'Content-type': mimetype,
        }
        resp = self.items(f'/{item_id}/Images/{image_type}', action='POST',
                          data=data, headers=headers)
        return resp

    def set_user_image(self, user_id, image_data, mimetype='auto'):
        """
        Args:
            item_id (str): user id to set the image for

            image_data (str | PathLike | bytes):
                A path to an image on disk or raw bytes of an image.

            mimetype (str): if "auto", attempt to infer the mimetype.
                falls back to image/jpeg if unable. Otherwise this is used.

        References:
            .. [PostUserImage] https://api.jellyfin.org/#tag/Image/operation/PostUserImage
        """
        image_bytes, auto_mimetype = self._coerce_image_bytes(image_data)

        if mimetype == 'auto':
            mimetype = auto_mimetype

        data = image_bytes.decode()
        # Overriding headers are important for this call
        headers = {
            'Accept': '*/*',
            'Content-type': mimetype,
        }
        resp = self._post("/UserImage", params={'user_id': user_id}, data=data,
                          headers=headers)
        return resp


class PlaylistAPIMixin:
    """
    Methods for creating and editing playlists.

    Note: removal and reordering address playlist ENTRIES by their
    ``PlaylistItemId`` (as returned by ``get_playlist_items``), not by the
    underlying item id — the same item can appear in a playlist twice.
    """

    def get_playlists(self, limit=None, fields=None, start_index=None,
                      sort_by="SortName", sort_order="Ascending"):
        """The user's playlists, as ordinary items.

        Jellyfin lets a playlist's declared ``MediaType`` diverge from what it
        actually holds, so this deliberately does not filter by media type —
        inspect the contents (``get_playlist_items``) to classify one.
        """
        return self.get_user_items(
            include_item_types="Playlist", recursive=True, sort_by=sort_by,
            sort_order=sort_order, start_index=start_index, limit=limit,
            fields=fields)

    def new_playlist(self, name, item_ids=None, media_type="Video",
                     is_public=None):
        """
        Create a new playlist.

        Args:
            name (str):
                Name of the playlist to create.

            item_ids (List[str] | None):
                Item ids to seed the playlist with.

            media_type (str | None):
                The playlist media type ("Video" or "Audio").

            is_public (bool | None):
                Whether the playlist is visible to all users. When None the
                server default is used (currently public); pass ``False`` for a
                playlist private to its owner.

        Returns:
            Dict:
                with one entry: "Id", the id of the new playlist.

        References:
            .. [CreatePlaylist] https://api.jellyfin.org/#tag/Playlists/operation/CreatePlaylist
        """
        json = {
            "Name": name,
            "UserId": "{UserId}",
        }
        if media_type is not None:
            json["MediaType"] = media_type
        if item_ids is not None:
            json["Ids"] = list(item_ids)
        if is_public is not None:
            json["IsPublic"] = bool(is_public)
        return self._post("Playlists", json)

    def get_playlist(self, playlist_id):
        """
        Fetch a playlist's metadata (visibility and shares).

        Args:
            playlist_id (str):
                Id of the playlist.

        Returns:
            Dict:
                A ``PlaylistDto`` — notably ``OpenAccess`` (bool; True means
                visible to all users) and ``Shares``.

        References:
            .. [GetPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/GetPlaylist
        """
        return self._get("Playlists/%s" % playlist_id)

    def update_playlist(self, playlist_id, name=None, item_ids=None,
                        users=None, is_public=None):
        """
        Update a playlist's name, item order, shares, or visibility. Only the
        arguments you pass are changed; the server leaves omitted fields alone,
        so this is safe for a rename-only or visibility-only edit.

        Args:
            playlist_id (str):
                Id of the playlist to update.

            name (str | None):
                New name, or None to leave unchanged.

            item_ids (List[str] | None):
                Full ordered item id list to replace the contents, or None to
                leave the contents unchanged.

            users (List[Dict] | None):
                ``PlaylistUserPermissions`` entries to replace the share list,
                or None to leave shares unchanged.

            is_public (bool | None):
                New visibility (True = all users, False = owner only), or None
                to leave unchanged.

        References:
            .. [UpdatePlaylist] https://api.jellyfin.org/#tag/Playlists/operation/UpdatePlaylist
        """
        json = {}
        if name is not None:
            json["Name"] = name
        if item_ids is not None:
            json["Ids"] = list(item_ids)
        if users is not None:
            json["Users"] = list(users)
        if is_public is not None:
            json["IsPublic"] = bool(is_public)
        return self._post("Playlists/%s" % playlist_id, json)

    def add_playlist_items(self, playlist_id, item_ids):
        """
        Append items to a playlist. Folder-ish ids (a series, a season) are
        expanded to their children by the server.

        Args:
            playlist_id (str):
                Id of the playlist to add items to.

            item_ids (List[str]):
                Item ids to append.

        References:
            .. [AddItemToPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/AddItemToPlaylist
        """
        params = {
            "Ids": ",".join(item_ids),
            "UserId": "{UserId}",
        }
        return self._post("Playlists/%s/Items" % playlist_id, None, params)

    def remove_playlist_items(self, playlist_id, entry_ids):
        """
        Remove entries from a playlist.

        Args:
            playlist_id (str):
                Id of the playlist to remove entries from.

            entry_ids (List[str]):
                ``PlaylistItemId`` values of the entries to remove (NOT the
                item ids; see ``get_playlist_items``).

        References:
            .. [RemoveItemFromPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/RemoveItemFromPlaylist
        """
        params = {"EntryIds": ",".join(entry_ids)}
        return self._delete("Playlists/%s/Items" % playlist_id, params)

    def move_playlist_item(self, playlist_id, entry_id, new_index):
        """
        Move one playlist entry to a new position.

        Args:
            playlist_id (str):
                Id of the playlist being reordered.

            entry_id (str):
                ``PlaylistItemId`` of the entry to move.

            new_index (int):
                Target position within the playlist.

        References:
            .. [MoveItem] https://api.jellyfin.org/#tag/Playlists/operation/MoveItem
        """
        return self._post("Playlists/%s/Items/%s/Move/%s"
                          % (playlist_id, entry_id, int(new_index)))


class CollectionAPIMixin:
    """
    Methods for creating and modifying collections.

    Note: there does not seem to be an API endpoint for removing a collection.
    """

    def get_collection_folders(self, term=None):
        """
        Queries for top-level default collections

        I.e. Movies, Music, Shows, Collections, Playlists, etc...

        Returns:
            Dict: pagenated result with key "Items"
        """
        from jellyfin_apiclient_python.constants import ItemType
        # For whatever reason, including search term in the query does nothing.
        # Furthermore, recursive has to base False, and the basic Music,
        # Collections, Movies, Playlists folders are always returned.
        result = self.user_items(params={
            'recursive': False,
            # 'searchTerm': term,
            'includeItemTypes': [ItemType.COLLECTION_FOLDER],
        })
        items = result['Items']
        if term is not None:
            # manual filter
            name_lower = term.lower()
            items = [item for item in items if name_lower in item['Name'].lower()]
        result['Items'] = items
        return result

    def get_collections(self, term=None, limit=None, start_index=None,
                        sort_by=None, sort_order=None, fields=None,
                        image_type_limit=None, enable_image_types=None):
        """
        Queries for user-created collections

        Args:
            term (str): query string to match

            limit (int): maximum collections to return; without it the server
                answers with every collection the user can see.

            start_index (int): paging offset, used with ``limit``.

            sort_by (str): e.g. ``"SortName"``. Left unset, the order is
                whatever the server returns.

            sort_order (str): ``"Ascending"`` or ``"Descending"``.

            fields (str): comma-separated Fields to request.

        Returns:
            Dict: pagenated result with key "Items"
        """
        from jellyfin_apiclient_python.constants import ItemType
        params = {
            'recursive': True,
            'searchTerm': term,
            'includeItemTypes': [ItemType.BOX_SET],
            'Limit': limit,
            'StartIndex': start_index,
            'SortBy': sort_by,
            'SortOrder': sort_order,
            'Fields': fields,
            'ImageTypeLimit': image_type_limit,
            'EnableImageTypes': enable_image_types,
        }
        result = self.user_items(
            params={k: v for k, v in params.items() if v is not None})
        return result

    def delete_collection(self, item_id=None, name=None):
        """
        Delete a collection by name or ID.

        This is mostly a wraper around delete_item, but with additional safety
        checks that ensure the item you are deleting is a collection.
        """
        if bool(name) ^ bool(item_id):
            raise ValueError('Exactly one of item_id or name must be given')

        results = self.user_items(params={'searchTerm': name, 'recursive': True})
        items = results['Items']

        if name is not None:
            # Filter to a case insensitive exact name match
            lower_name = name.lower()
            items = [item for item in items if item['Name'].lower() == lower_name]

        if len(items) == 0:
            raise Exception('No items matched the given input')
        assert len(items) == 1, 'filtered to length 0 or 1'
        item = items[0]

        # It looks like what the UI calls collections are called box sets in
        # the backend.  there is a collection type, but these seem to be for
        # special groups like Music / Movies that should likely not be deleted.
        collection_types = {'BoxSet'}

        if item['Type'] not in collection_types:
            raise ValueError('Given item={item} is not a collection')

        return self.delete_item(item['Id'])

    def new_collection(self, name, item_ids=None, parent_id=None, is_locked=False):
        """
        Create a new collection, or search for a collection with a given name.

        Args:
            name (str):
                Name of the collection to create or lookup

            item_ids (List[str] | None):
                List of item ids to initialize the collection with.

            parent_id (str | None):
                Create the collection within a specific folder.

            is_locked (str | None):
                Whether or not to lock the new collection.

        Returns:
            Dict:
                with one entry: "Id", which contains the id of the new or found
                collection.

        References:
            .. [CreateCollection] https://api.jellyfin.org/#tag/Collection/operation/CreateCollection
        """
        params = {}
        params['name'] = name
        params['isLocked'] = is_locked
        json = {}
        if parent_id is not None:
            params['parentId'] = parent_id
        if item_ids is not None:
            params['ids'] = item_ids
        return self._post("Collections", json, params)

    def add_collection_items(self, collection_id, item_ids):
        """
        Adds items to a collection.

        Args:
            collection_id (str):
                Id of the collection to add items to.

            item_ids (List[str]):
                List of item ids to add to the collection.

        References:
            .. [AddToCollection] https://api.jellyfin.org/#tag/Collection/operation/AddToCollection
        """
        params = {}
        json = {}
        params['ids'] = ','.join(item_ids)
        return self._post(f"Collections/{collection_id}/Items", json, params)

    def remove_collection_items(self, collection_id, item_ids=None):
        """
        Removes items from a collection.

        Args:
            collection_id (str):
                Id of the collection to remove items from.

            item_ids (List[str]):
                List of item ids to remove from the collection.

        References:
            .. [RemoveFromCollection] https://api.jellyfin.org/#tag/Collection/operation/RemoveFromCollection
        """
        params = {}
        params['ids'] = ','.join(item_ids)
        # _delete takes (handler, params); a stray positional json argument
        # here used to make every call raise TypeError.
        return self._delete(f"Collections/{collection_id}/Items", params)


class BackupAPIMixin:
    """
    Methods for creating, restoring and listing system backups

    10.11.0+ only

    Note: backup manifests are dictionary objects with the following structure:

        {
            "ServerVersion": "string",
            "BackupEngineVersion": "string",
            "DateCreated": "2019-08-24T14:15:22Z",
            "Path": "string",
            "Options": {
                "Metadata": true,
                "Trickplay": true,
                "Subtitles": true,
                "Database": true
            }
        }

    """

    def create_backup(
        self,
        include_metadata: bool = False,
        include_subtitles: bool = False,
        include_trickplay: bool = False,
    ):
        """
        Creates a new backup including the database and any of the optional
        elements requested. If metadata is included, this can be a time-consuming
        operation.

        Args:
            include_metadata (bool)
                Whether or not to include metadata in the backup

            include_subtitles (bool)
                Whether or not to include subtitles in the backup

            include_trickplay (bool)
                Whether or not to include trickplay information in the backup

        Returns:
            The manifest of the backup if it was created, an empty directory
            otherwise.

        """
        params = {
            "database": True,
            "metadata": include_metadata,
            "subtitles": include_subtitles,
            "trickplay": include_trickplay,
        }
        return self._post("Backup/Create", params)

    def get_backup_manifest(self, path: str):
        """
        Gets the manifest of a backup at the path passed

        Args:
            path (str):
                Location of the backup

        Returns:
            The backup's manifest, if the backup exists, an empty dictionary
            otherwise.

        References:
            .. [BackupManifest] https://api.jellyfin.org/#tag/Backup/operation/GetBackup
        """
        params = {"path": path}
        return self._get("Backup/Manifest", params)

    def get_backups(self):
        """
        Gets a list of all currently present backups in the backup directory.

        Args:
            None

        Returns:
            List of manifests for the backup that exist, one per backup.

        References:
            .. [Backup] https://api.jellyfin.org/#tag/Backup/operation/ListBackups
        """
        return self._get("Backup")

    def restore_backup(self, backup_name: str):
        """
        Starts the process of restoring a backup with the name passed.

        Args:
            backup_name (str)
                The name of the backup archive, which must exist in the
                backups directory for the restore process to start

        Returns:
            True if the restore process started, False otherwise

        """
        params = {"ArchiveFileName": backup_name}
        try:
            # This post call returns a 204 to indicate that the restore has
            # been requested, but the client ingests the non-error code
            # and the _post() call returns nothing.
            self._post("Backup/Restore", params)
            return True

        except Exception as e:
            LOG.error(e)

        return False


class API(
    InternalAPIMixin,
    BiggerAPIMixin,
    GranularAPIMixin,
    SyncPlayAPIMixin,
    ExperimentalAPIMixin,
    PlaylistAPIMixin,
    CollectionAPIMixin,
    BackupAPIMixin,
):
    """
    The Jellyfin Python API client containing all api calls to the server.

    This class implements a subset of the [JellyfinWebAPI]_.

    References:
        .. [JellyfinWebAPI] https://api.jellyfin.org/

    Example:
        >>> from jellyfin_apiclient_python import JellyfinClient
        >>> client = JellyfinClient()
        >>> #
        >>> client.config.app(
        >>>     name='your_brilliant_app',
        >>>     version='0.0.1',
        >>>     device_name='machine_name',
        >>>     device_id='unique_id')
        >>> client.config.data["auth.ssl"] = True
        >>> #
        >>> your_jellyfin_url = 'http://127.0.0.1:8096'  # Use your jellyfin IP / port
        >>> your_jellyfin_username = 'jellyfin'          # Use your jellyfin userid
        >>> your_jellyfin_password = ''                  # Use your user's password
        >>> #
        >>> client.auth.connect_to_address(your_jellyfin_url)
        >>> client.auth.login(
        >>>     server_url=your_jellyfin_url,
        >>>     username=your_jellyfin_username,
        >>>     password=your_jellyfin_password
        >>> )
        >>> #
        >>> # Test basic calls
        >>> system_info = client.jellyfin.get_system_info()
        >>> print(system_info)
        >>> media_folders = client.jellyfin.get_media_folders()
        >>> print(media_folders)
    """

    def __init__(self, client, *args, **kwargs):
        """
        Args:
            client (jellyfin_apiclient_python.client.JellyfinClient): the client object
            *args: unused
            **kwargs: unused
        """
        self.client = client
        self.config = client.config
        self.default_timeout = 5
