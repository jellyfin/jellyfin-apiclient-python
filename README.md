# Jellyfin ApiClient Python

This is the API client from Jellyfin Kodi extracted as a python package so that other users may use the API without maintaining a fork of the API client. Please note that this API client is not complete. You may have to add API calls to perform certain tasks. Please see **Contributing** below.

## Usage

This client can be installed with `pip3 install jellyfin-apiclient-python` and imported with `import jellyfin_apiclient_python`.

### Creating a client

```
from jellyfin_apiclient_python import JellyfinClient
client = JellyfinClient()
```

You need to set some configuration values before you can connect a server:

```
client.config.app('your_brilliant_app', '0.0.1', 'machine_name', 'unique_id')
client.config.data["auth.ssl"] = True
```

### Finding servers on the local network

```python
from jellyfin_apiclient_python.discovery import discover_servers
servers = discover_servers(timeout=1.0)  # [{'Id': ..., 'Name': ..., 'Address': ...}, ...]
```

This blocks for the whole timeout, so call it off your UI thread. The replies
are not authenticated: anything on the network can answer with any name and
address, and a real server usually advertises plain `http://`. Show the address
and let the user choose it rather than signing in to one automatically.

### Authenticating to a server

If you do not have a token, you will need to connect via username and password:

```
client.auth.connect_to_address('server_url')
client.auth.login('server_url', 'username', 'password')
```

You can then generate a token:

```
credentials = client.auth.credentials.get_credentials()
server = credentials["Servers"][0]
server["username"] = 'username'
json.dumps(server)
```

And if you wish then use that token to authenticate in future:

```
json.loads(credentials)
client.authenticate({"Servers": [credentials]}, discover=False)
```

You can also authenticate using an API key, which is generated on the server.
This is different to a device AccessToken, and is set by not configuring a
device name, or a device id:

```python
client.config.data["app.name"] = 'your_brilliant_app'
client.config.data["app.version"] = '0.0.1'
client.authenticate({"Servers": [{"AccessToken": '<API key here>', "address": '<Server Address>'}]}, discover=False)

# Some endpoint require a user context event using API Key.

client.config.data["auth.user_id"] = '<UserID here>'
client.authenticate({"Servers": [{"AccessToken": '<API key here>', "address": '<Server Address>'}]}, discover=False)
```

### API

The API is accessed via the `jellyfin` attribute of the client. Return values
are a dictionary with 3 members, "Items", "TotalRecordCount" and "StartIndex"

The easiest way to fetch media objects is by calling `search_media_items`, like
so:

```python
client.jellyfin.search_media_items(term="And Now for Something Completely Different", media="Videos")
```

For details on what the individual API calls do or how to do a certain task, you will probably find the [Jellyfin MPV Shim](https://github.com/iwalton3/jellyfin-mpv-shim) and [Jellyfin Kodi](https://github.com/jellyfin/jellyfin-kodi) repositories useful.

## Running the tests

The test suite is run via `tox`, and you can install it from PyPi.

 - To run the linter: `tox -elint`
 - To run the test suite, for Python 3.9: `tox -epy39`
 - You can run multiple environments, if you wish: `tox -elint,py311`

## Changes from Jellyfin Kodi

 - Removal of `websocket.py` (now a dependency to `websocket_client`).
 - Removal of dependencies on `helper` (from Jellyfin Kodi) and `kodi_six`.
 - Add `has_attribute` directly to `__init__.py`.
 - Add API calls:
   - `get_season` for fetching season metadata.
   - `get_audio_stream` to read an audio stream into a file
   - `search_media_items` to search for media items
   - `audio_url` to return the URL to an audio file
 - Add parameters `aid=None, sid=None, start_time_ticks=None, is_playback=True` to API call `get_play_info`.
 - Add timesync manager and SyncPlay API methods.
 - Remove usage of `six` module.
 - Add group of `remote_` API calls to remote control another session
 - Configurable item refreshes allowing custom refresh logic (can also iterate through a list of items)
 - Add support for authenticating via an API key
 - Add support for the optional 'date played' parameter in the `item_played` API method
 - Add API calls `get_userdata_for_item` and `update_userdata_for_item`
 - Add API call `get_playlist_items` for fetching a playlist's contents in order
 - Add support for the backup API introduced in Jellyfin 10.11.0
 - Extend the (currently) experimental `identify` API call to include all parameters supported by Jellyfin
 - Fix `close_live_stream` sending the stream id as a JSON body; the server binds
   it from the query string, so the call always failed and leaked the tuner
 - Add API call `get_user_items`, a named-argument form of the general item query
   (`GET Users/{UserId}/Items`) that browse UIs otherwise had to build by hand
 - Add browse API calls `get_resume_items`, `get_random_items`,
   `get_items_by_person`, `get_album_tracks`, `get_artist_albums`,
   `get_artist_songs`, `get_genre_songs` and `get_playlists`
 - Add Live TV API calls `get_programs` and `get_recommended_programs`, and add
   paging/field/`add_current_program` parameters to `get_channels`, which was
   previously unbounded (note that `LiveTv/Channels` has no way to skip the
   total record count, unlike the item endpoints)
 - Add API calls `get_endpoint_info` (`System/Endpoint`) and
   `update_user_settings`, the write side of `get_user_settings`
 - Add API calls `get_chapter_image` and `get_trickplay_tile` for downloading
   chapter thumbnails and scrubbing-preview tiles
 - Add parameters `fields`, `enable_image_types`, `image_type_limit` and
   `enable_total_record_count` to `get_recently_added`, `fields` to `get_items`,
   and paging/sorting parameters to `get_collections`, `get_artists` and
   `get_album_artists`
 - Add parameters `timeout` and `retry` to `sessions`, so a health check can
   fail fast instead of waiting out the client-wide defaults
 - Add parameter `include_segment_types` to `get_media_segments`
 - Add `discovery.discover_servers`, public server discovery with one deadline
   for the whole wait and one entry per server; `ConnectionManager` now uses it,
   and it closes its socket
 - Add API call `get_live_tv_info` (`LiveTv/Info`), whose `EnabledUsers` is the
   only way to tell whether Live TV is actually available to a user before
   showing a guide or recordings view

## Contributing

When contributing, please maintain backward compatibility with existing calls in the API. Adding parameters is
fine, but please make sure that they have default options to prevent existing software from breaking. Please
also add your changes to the **Changes from Jellyfin Kodi** section.

If you would like to produce documentation for this API, I would also be interested in accepting pull requests
for documentation.
