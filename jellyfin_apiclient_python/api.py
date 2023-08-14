# -*- coding: utf-8 -*-
from typing import List
from datetime import datetime
import requests
import json
import logging

LOG = logging.getLogger('JELLYFIN.' + __name__)


def jellyfin_url(client, handler):
    return "%s/%s" % (client.config.data['auth.server'], handler)


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


class API(object):

    ''' All the api calls to the server.
    '''
    def __init__(self, client, *args, **kwargs):
        self.client = client
        self.config = client.config
        self.default_timeout = 5

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

    #################################################################################################

    # Bigger section of the Jellyfin api

    #################################################################################################

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
    
    def media_folders(self, handler="", params=None, json=None):
        return self._get("Library/MediaFolders/", params)

    def virtual_folders(self, handler="", action="GET", params=None, json=None):
        if action == "POST":
            return self._post("Library/VirtualFolders", json, params)
        elif action == "DELETE":
            return self._delete("Library/VirtualFolders", params)
        else:
            return self._get("Library/VirtualFolders", params)

    def physical_paths(self, handler="", params=None, json=None):
        return self._get("Library/PhysicalPaths/", params)

    def folder_contents(self, abspath="/", params={}, json=None):
        params['path'] = abspath
        params['includeFiles'] = params['includeFiles'] if 'includeFiles' in params else True
        params['includeDirectories'] = params['includeDirectories'] if 'includeDirectories' in params else True
        return self._get("Environment/DirectoryContents", params)

    def scan_library(self):
        return self._post("Library/Refresh")


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

    def artwork(self, item_id, art, max_width, ext="jpg", index=None):
        params = {"MaxWidth": max_width, "format": ext}
        handler = ("Items/%s/Images/%s" % (item_id, art) if index is None
            else "Items/%s/Images/%s/%s" % (item_id, art, index)
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

    #################################################################################################

    # More granular api

    #################################################################################################

    def get_users(self):
        return self._get("Users")

    def get_public_users(self):
        return self._get("Users/Public")

    def get_user(self, user_id=None):
        return self.users() if user_id is None else self._get("Users/%s" % user_id)

    def create_user(self, name, password):
        return self._post("Users/New", {"Name": name, "Password": password})

    def delete_user_by_name(self, name):
        deleted_users = []
        for user_info in self.get_users():
            if user_info['Name'] == name:
                self._delete("Users/%s" % user_info['Id'])
                deleted_users.append(user_info)
        return deleted_users

    def get_user_settings(self, client="emby"):
        return self._get("DisplayPreferences/usersettings", params={
            "userId": "{UserId}",
            "client": client
        })

    # TODO: The path validation API is not working
    def validate_path(self, path):
        json = {
            "ValidateWritable": False,
            "Path": path,
            "IsFile": True
        }
        return self._post('Environment/ValidatePath', json=json, params={})

    def get_virtual_folders(self):
        return self.virtual_folders()

    def create_virtual_folder(self, name, paths=[], collection_type='Movies', json=None, refresh_library=False):
        params = {
            'name': name,
            'collectionType': collection_type,
            'paths': paths,
            'refreshLibrary': refresh_library
        }
        
        # Just don't fetch metadata from internet by default
        if json is None:
            json = {
                'LibraryOptions': {
                    'EnablePhotos': True, 
                    'EnableRealtimeMonitor': True, 
                    'EnableChapterImageExtraction': True, 
                    'ExtractChapterImagesDuringLibraryScan': True, 
                    'SaveLocalMetadata': False, 
                    'EnableInternetProviders': False, 
                    'EnableAutomaticSeriesGrouping': False, 
                    'EnableEmbeddedTitles': False, 
                    'EnableEmbeddedEpisodeInfos': False, 
                    'AutomaticRefreshIntervalDays': 0, 
                    'PreferredMetadataLanguage': '', 
                    'MetadataCountryCode': '', 
                    'SeasonZeroDisplayName': 'Specials', 
                    'MetadataSavers': [], 
                    'DisabledLocalMetadataReaders': [], 
                    'LocalMetadataReaderOrder': ['Nfo'], 
                    'DisabledSubtitleFetchers': [], 
                    'SubtitleFetcherOrder': [], 
                    'SkipSubtitlesIfEmbeddedSubtitlesPresent': False, 
                    'SkipSubtitlesIfAudioTrackMatches': False, 
                    'SubtitleDownloadLanguages': [], 
                    'RequirePerfectSubtitleMatch': True, 
                    'SaveSubtitlesWithMedia': True, 
                    'TypeOptions': [
                        {
                            'Type': 'Movie', 
                            'MetadataFetchers': ['TheMovieDb', 'The Open Movie Database'], 
                            'MetadataFetcherOrder': ['TheMovieDb', 'The Open Movie Database'], 
                            'ImageFetchers': ['Screen Grabber'], 
                            'ImageFetcherOrder': ['Screen Grabber'], 
                            'ImageOptions': []
                        }
                    ]
                }
            }
        return self.virtual_folders(handler="", action="POST", params=params, json=json)
    
    def rename_virtual_folder(self, name, new_name, refresh_library=False):
        params = {
            'name': name,
            'newName': new_name,
            'refreshLibrary': refresh_library
        }
        return self.virtual_folders(handler="", action="POST", params=params, json={})

    def delete_virtual_folder(self, name):
        return self.virtual_folders(handler="", action="DELETE", params={'name': name})

    def get_views(self):
        return self.users("/Views")

    def get_media_folders(self):
        return self.users("/Items")

    def get_item(self, item_id):
        return self.users("/Items/%s" % item_id)

    def get_items(self, item_ids):
        return self.users("/Items", params={
            'Ids': ','.join(str(x) for x in item_ids),
            'Fields': info()
        })

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

    def search_media_items(self, term=None, media=None, limit=20):
        return self.user_items(params={
            'searchTerm': term,
            'Recursive': True,
            'IncludeItemTypes': media,
            'Limit': limit
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

    def refresh_item(self, item_id):
        return self.items("/%s/Refresh" % item_id, "POST", json={
            'Recursive': True,
            'ImageRefreshMode': "FullRefresh",
            'MetadataRefreshMode': "FullRefresh",
            'ReplaceAllImages': False,
            'ReplaceAllMetadata': True
        })

    def favorite(self, item_id, option=True):
        return self.users("/FavoriteItems/%s" % item_id, "POST" if option else "DELETE")

    def get_system_info(self):
        return self._get("System/Configuration")

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
        """Set the volume on the sessions.
        
            @id: The session id to control
            @ticks: The position (in ticks) to seek to"""
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
        
            @id: The session id to control
            @item_ids: A list of items to play
            @command: When to play. (*PlayNow*, PlayNext, PlayLast, PlayInstantMix, PlayShuffle)
        """
        return self.remote(
            id,
            None,
            json=json,
            params={"playCommand": command, "itemIds": item_ids, **params},
        )

    def remote_set_volume(self, id: str, volume: int, json={}):
        """Set the volume on the sessions.
        
            @id: The session id to control
            @volume: The volume normalized from 0 to 100"""
        return self.command(id, "SetVolume", json={"Volume": volume, **json})

    def remote_mute(self, id):
        return self.command(id, "Mute")

    def remote_unmute(self, id):
        return self.command(id, "Unmute")

    def item_played(self, item_id, watched):
        return self.users("/PlayedItems/%s" % item_id, "POST" if watched else "DELETE")

    def get_sync_queue(self, date, filters=None):
        return self._get("Jellyfin.Plugin.KodiSyncQueue/{UserId}/GetItems", params={
            'LastUpdateDT': date,
            'filter': filters or None
        })

    def get_server_time(self):
        return self._get("Jellyfin.Plugin.KodiSyncQueue/GetServerDateTime")

    def get_play_info(self, item_id, profile, aid=None, sid=None, start_time_ticks=None, is_playback=True):
        args = {
            'UserId': "{UserId}",
            'DeviceProfile': profile,
            'AutoOpenLiveStream': is_playback,
            'IsPlayback': is_playback
        }
        if sid:
            args['SubtitleStreamIndex'] = sid
        if aid:
            args['AudioStreamIndex'] = aid
        if start_time_ticks:
            args['StartTimeTicks'] = start_time_ticks
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
        auth = "MediaBrowser "
        auth += "Client=%s, " % self.config.data['app.name']
        auth += "Device=%s, " % self.config.data['app.device_name']
        auth += "DeviceId=%s, " % self.config.data['app.device_id']
        auth += "Version=%s" % self.config.data['app.version']

        return {
            "Accept": "application/json",
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Application": "%s/%s" % (self.config.data['app.name'], self.config.data['app.version']),
            "Accept-Charset": "UTF-8,*",
            "Accept-encoding": "gzip",
            "User-Agent": self.config.data['http.user_agent'] or "%s/%s" % (self.config.data['app.name'], self.config.data['app.version']),
            "x-emby-authorization": auth
        }

    def send_request(self, url, path, method="get", timeout=None, headers=None, data=None, session=None):
        request_method = getattr(session or requests, method.lower())
        url = "%s/%s" % (url, path)
        request_settings = {
            "timeout": timeout or self.default_timeout,
            "headers": headers or self.get_default_headers(),
            "data": data
        }

        # Changed to use non-Kodi specific setting.
        if self.config.data.get('auth.ssl') == False:
            request_settings["verify"] = False

        LOG.info("Sending %s request to %s" % (method, path))
        LOG.debug(request_settings['timeout'])
        LOG.debug(request_settings['headers'])

        return request_method(url, **request_settings)

    # TODO: Quick connect is not responding to the requests.
    def quick_connect_with_token(self, server_url, token):
        path="Users/AuthenticateWithQuickConnect"
        authData = {'Token': token}

        headers = self.get_default_headers()
        headers.update({'Content-type': "application/json"})

        response = self.send_request(server_url, path, method="post", headers=headers,
                                    data=json.dumps(authData), timeout=(5, 30))

        if response.status_code == 200:
            return response.json()
        else:
            LOG.error("Failed to login to server with status code: " + str(response.status_code))
            LOG.error("Server Response:\n" + str(response.content))
            LOG.debug(headers)
            print(headers)
            return {}

    def login(self, server_url, username, password=""):
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
                                         data=json.dumps(authData), timeout=(5, 30))

            if response.status_code == 200:
                return response.json()
            else:
                LOG.error("Failed to login to server with status code: " + str(response.status_code))
                LOG.error("Server Response:\n" + str(response.content))
                LOG.debug(headers)

                return {}
        except Exception as e: # Find exceptions for likely cases i.e, server timeout, etc
            LOG.error(e)

        return {}

    def validate_authentication_token(self, server):
        authTokenHeader = {
                    'X-MediaBrowser-Token': server['AccessToken']
                }
        headers = self.get_default_headers()
        headers.update(authTokenHeader)

        response = self.send_request(server['address'], "system/info", headers=headers)
        return response.json() if response.status_code == 200 else {}

    def get_public_info(self, server_address):
        response = self.send_request(server_address, "system/info/public")
        return response.json() if response.status_code == 200 else {}

    def check_redirect(self, server_address):
        ''' Checks if the server is redirecting traffic to a new URL and
        returns the URL the server prefers to use
        '''
        response = self.send_request(server_address, "system/info/public")
        url = response.url.replace('/system/info/public', '')
        return url

    #################################################################################################

    # Syncplay

    #################################################################################################

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
