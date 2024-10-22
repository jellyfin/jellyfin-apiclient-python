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

```
client.config.data["app.name"] = 'your_brilliant_app'
client.config.data["app.version"] = '0.0.1'
client.authenticate({"Servers": [{"AccessToken": <API key here>, "address": <Server Address>}]}, discover=False)
```

### API

The API is accessed via the `jellyfin` attribute of the client. Return values
are a dictionary with 3 members, "Items", "TotalRecordCount" and "StartIndex"

The easiest way to fetch media objects is by calling `search_media_items`, like
so:

```
client.jellyfin.search_media_items(
    term="And Now for Something Completely Different", media="Videos")
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

## Contributing

When contributing, please maintain backward compatibility with existing calls in the API. Adding parameters is
fine, but please make sure that they have default options to prevent existing software from breaking. Please
also add your changes to the **Changes from Jellyfin Kodi** section.

If you would like to produce documentation for this API, I would also be interested in accepting pull requests
for documentation.
