# Jellyfin ApiClient Python

This is the API client from Jellyfin Kodi extracted as a python package so that other users may use the API without maintaining a fork of the API client. Please note that this API client is not complete. You may have to add API calls to perform certain tasks. Please see **Contributing** below.

## Usage

This client can be installed with `pip3 install jellyfin-apiclient-python` and imported with `import jellyfin_apiclient_python`.

### Example client initialization
```python
#!/usr/bin/env python
from jellyfin_apiclient_python.client import JellyfinClient
from socket import gethostname


client = JellyfinClient()
app_name = 'Python API Client Example'
version = 1
device_name = gethostname()
device_id = gethostname()
client.config.app(app_name, version, device_name, device_id)

server_url = 'http://hostname:port'
username = 'USERNAME'
password = 'PASSWORD'

client.auth.login(server_url, username, password)
```


For details on what the individual API calls do or how to do a certain task, you will probably find the [Jellyfin MPV Shim](https://github.com/iwalton3/jellyfin-mpv-shim) and [Jellyfin Kodi](https://github.com/jellyfin/jellyfin-kodi) repositories useful.

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

## Contributing

When contributing, please maintain backward compatibility with existing calls in the API. Adding parameters is
fine, but please make sure that they have default options to prevent existing software from breaking. Please
also add your changes to the **Changes from Jellyfin Kodi** section.

If you would like to produce documentation for this API, I would also be interested in accepting pull requests
for documentation.
