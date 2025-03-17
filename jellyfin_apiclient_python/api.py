# -*- coding: utf-8 -*-
"""
For API info see:
    https://api.jellyfin.org/
"""
from typing import List
from datetime import datetime
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

    def _http_url(self, action, url, request={}):
        request.update({"type": action, "handler": url})

        return self.client.request_url(request)

    def _http_stream(self, action, url, dest_file, request={}):
        request.update({'type': action, 'handler': url})

        self.client.request(request, dest_file=dest_file)

    def _get(self, handler, params=None):
        return self._http("GET", handler, {'params': params})

    def _get_url(self, handler, params=None):
        return self._http_url("GET", handler, {"params": params})

    def _post(self, handler, json=None, params=None):
        return self._http("POST", handler, {'params': params, 'json': json})

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

    def sessions(self, handler="", action="GET", params=None, json=None):
        if action == "POST":
            return self._post("Sessions%s" % handler, json, params)
        elif action == "DELETE":
            return self._delete("Sessions%s" % handler, params)
        else:
            return self._get("Sessions%s" % handler, params)

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

    def items(self, handler="", action="GET", params=None, json=None):
        if action == "POST":
            return self._post("Items%s" % handler, json, params)
        elif action == "DELETE":
            return self._delete("Items%s" % handler, params)
        else:
            return self._get("Items%s" % handler, params)

    def user_items(self, handler="", params=None):
        return self.users("/Items%s" % handler, params=params)

    def shows(self, handler, params):
        return self._get("Shows%s" % handler, params)

    def videos(self, handler):
        return self._get("Videos%s" % handler)

    def media_segments(self, handler, params=None):
        return self._get("MediaSegments%s" % handler, params)

    def artwork(self, item_id, art, max_width, ext="jpg", index=None):
        params = {"MaxWidth": max_width, "format": ext}
        handler = ("Items/%s/Images/%s" % (item_id, art) if index is None
                   else "items/%s/images/%s/%s" % (item_id, art, index)
                   )

        return self._get_url(handler, params)

    def audio_url(self, item_id, container=None, audio_codec=None, max_streaming_bitrate=140000000):
        params = {
            "UserId": "{UserId}",
            "DeviceId": "{DeviceId}",
            "MaxStreamingBitrate": max_streaming_bitrate,
        }

        if container:
            params["Container"] = container

        if audio_codec:
            params["AudioCodec"] = audio_codec

        return self._get_url("Audio/%s/universal" % item_id, params)

    def video_url(self, item_id, media_source_id=None):
        params = {
            "static": "true",
            "DeviceId": "{DeviceId}"
        }
        if media_source_id is not None:
            params["MediaSourceId"] = media_source_id

        return self._get_url("Videos/%s/stream" % item_id, params)

    def download_url(self, item_id):
        params = {}
        return self._get_url("Items/%s/Download" % item_id, params)


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

    def get_item(self, item_id):
        """
        Lookup metadata for an item.

        Args:
            item_id (str): item uuid to lookup metadata for

        Returns:
            Dict[str, Any]: metadata keys and values for the queried item.
        """
        return self.users("/Items/%s" % item_id, params={
            'Fields': info()
        })

    def get_items(self, item_ids):
        """
        Lookup metadata for multiple items.

        Args:
            item_ids (List[str]): item uuids to lookup metadata for

        Returns:
            Dict[str, Any]: A result dictionary where the info from each
                item is stored in the "Items" list.
        """
        return self.users("/Items", params={
            'Ids': ','.join(str(x) for x in item_ids),
            'Fields': info()
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

    def get_recently_added(self, media=None, parent_id=None, limit=20):
        return self.user_items("/Latest", {
            'Limit': limit,
            'UserId': "{UserId}",
            'IncludeItemTypes': media,
            'ParentId': parent_id,
            'Fields': info()
        })

    def get_next(self, index=None, limit=1):
        return self.shows("/NextUp", {
            'Limit': limit,
            'UserId': "{UserId}",
            'StartIndex': None if index is None else int(index)
        })

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

    def get_genres(self, parent_id=None):
        return self._get("Genres", {
            'ParentId': parent_id,
            'UserId': "{UserId}",
            'Fields': info()
        })

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

    def get_channels(self):
        return self._get("LiveTv/Channels", {
            'UserId': "{UserId}",
            'EnableImages': True,
            'EnableUserData': True
        })

    def get_intros(self, item_id):
        return self.user_items("/%s/Intros" % item_id)

    def get_additional_parts(self, item_id):
        return self.videos("/%s/AdditionalParts" % item_id)

    def get_media_segments(self, item_id):
        return self.media_segments("/%s" % item_id)

    def delete_item(self, item_id):
        return self.items("/%s" % item_id, "DELETE")

    def get_local_trailers(self, item_id):
        return self.user_items("/%s/LocalTrailers" % item_id)

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
        return self._post("LiveStreams/Close", json={
            'LiveStreamId': live_id
        })

    def close_transcode(self, device_id):
        return self._delete("Videos/ActiveEncodings", params={
            'DeviceId': device_id
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

    def identify(client, item_id, provider_ids):
        """
        Remote search for item metadata given one or more provider id.

        This method requires an authenticated user with elevated permissions
        [RemoveProviderSearch]_.

        Args:
            item_id (str): item uuid to identify and update metadata for.

            provider_ids (Dict):
                maps providers to the content id. (E.g. {"Imdb": "tt1254207"})
                Valid keys will depend on available providers. Common ones are:
                    "Tvdb" and "Imdb".

        References:
            .. [RemoveProviderSearch] https://api.jellyfin.org/#tag/ItemLookup/operation/ApplySearchCriteria
        """
        body = {'ProviderIds': provider_ids}
        return client.jellyfin.items('/RemoteSearch/Apply/' + item_id, action='POST', params=None, json=body)

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


class CollectionAPIMixin:
    """
    Methods for creating and modifying collections.

    Note: there does not seem to be an API endpoint for removing a collection.
    """

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
        json = {}
        params['ids'] = ','.join(item_ids)
        return self._delete(f"Collections/{collection_id}/Items", json, params)


class API(InternalAPIMixin, BiggerAPIMixin, GranularAPIMixin,
          SyncPlayAPIMixin, ExperimentalAPIMixin, CollectionAPIMixin):
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
