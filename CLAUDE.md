# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Python client for the Jellyfin media server API. Originally extracted from Jellyfin Kodi so other projects (e.g. Jellyfin MPV Shim) can consume the API without forking. Distributed on PyPI as `jellyfin-apiclient-python`. The API surface is intentionally incomplete — features get added when consumers need them.

## Common commands

Tests and linting are driven by `tox`:

- `tox -elint` — ruff lint over `jellyfin_apiclient_python` and `tests`.
- `tox -epy39` (or any of `py38,py39,py310,py311,py312`) — run the pytest suite under that interpreter.
- `tox -elint,py311` — chain envs.
- `pytest tests/test_api.py::test_jellyfin_url_handles_trailing_slash` — run a single test (inside an env or with pytest installed directly). Anything after `--` in `tox -epy311 -- ...` is forwarded to pytest.

CI (`.github/workflows/ci.yml`) runs the same `tox` matrix on push to `master` and on PRs.

## Architecture

### Entry points and lifecycle

Two ways to instantiate:

- `JellyfinClient()` directly (`jellyfin_apiclient_python/client.py`) — straightforward composition root. Constructs `Config`, `HTTP`, `WSClient`, `ConnectionManager` (as `auth`), `API` (as `jellyfin`), and `TimeSyncManager`. Lifecycle is `authenticate()` → `start(websocket=…, keep_alive=…)` → `stop()`.
- `Jellyfin('server_id')` facade in `__init__.py` — **Borg pattern**: all instances share `_shared_state` and a class-level `client` dict keyed by `server_id`. `__getattr__`/`__setattr__` proxy through to the underlying `JellyfinClient`, lazily constructing one via `@ensure_client()`. This is how multi-server callers manage parallel clients without juggling references. Treat it as a registry, not a normal object.

### `JellyfinClient` composition

`config` (`Config`) is a thin `dict` wrapper. Code throughout the package reads/writes string keys directly on `config.data` (`auth.server`, `auth.token`, `auth.user_id`, `app.device_id`, `auth.tls_client_cert`, `auth.ssl`, `http.timeout`, …). There is no schema — keys are a de facto contract spread across `http.py`, `connection_manager.py`, and `ws_client.py`. When adding a config key, grep for siblings to keep naming consistent.

`http` (`HTTP`) wraps `requests.Session` with retry/backoff and Jellyfin-specific behavior:

- Builds the `Authorization: MediaBrowser …` header from `app.*` and `auth.token` config in `_get_authenication_header`.
- Substitutes `{server}`, `{UserId}`, `{DeviceId}` placeholders in URLs and params via `_replace_user_info` — this is why API mixin handlers can be written as literal strings like `"Users/{UserId}/Items"`.
- On 401, distinguishes `AccessRestricted` (header `X-Application-Error-Code` present) from `Unauthorized` (which also calls `auth.revoke_token()`); both fire `client.callback(...)`. 500s are logged and swallowed (return `None`). Connection/read errors retry with a 1s sleep.
- Optional mTLS via `auth.tls_client_cert`/`auth.tls_client_key`/`auth.tls_server_ca` — also honored by `WSClient` and `ConnectionManager`.

`auth` (`ConnectionManager`) owns server discovery, login, and credential storage:

- `_server_discovery()` does UDP broadcast on port 7359 with `b"who is JellyfinServer?"`.
- `connect()` / `connect_to_address()` / `connect_to_server()` return a state dict whose `'State'` is a `CONNECTION_STATE` enum (`Unavailable`, `ServerSelection`, `ServerSignIn`, `SignedIn`).
- `Credentials` (`credentials.py`) holds a `{'Servers': [...]}` dict. Server entries carry `Id`, `address`, `AccessToken`, `UserId`, `DateLastAccessed`, etc. `add_update_server` merges by `Id` and is the single place to mutate the server list.
- Authentication supports username/password, persisted access tokens, and server-side API keys (omit `app.device_name`/`app.device_id` to use API-key mode — see README).

`jellyfin` (`api.API`) is **composed by multiple inheritance** from mixins in `api.py`:

- `InternalAPIMixin` — `_get`/`_post`/`_delete`/`_get_url`/`_get_stream` helpers that route through `client.request(...)`.
- `BiggerAPIMixin` — broad endpoints (`sessions`, `users`, `items`, `shows`, `videos`, `artwork`, `audio_url`, library management).
- `GranularAPIMixin` — user-scoped helpers like `get_item`, `search_media_items`, `get_userdata_for_item`.
- `SyncPlayAPIMixin` — SyncPlay endpoints; coordinates with `TimeSyncManager`.
- `ExperimentalAPIMixin` — newer/unstable endpoints.
- `CollectionAPIMixin` — collection management.

When adding endpoints, place them in the mixin that matches their domain. The MRO is fixed by the `class API(InternalAPIMixin, BiggerAPIMixin, GranularAPIMixin, SyncPlayAPIMixin, ExperimentalAPIMixin, CollectionAPIMixin)` declaration at the bottom of `api.py`.

`wsc` (`WSClient`, `ws_client.py`) is a `threading.Thread` that maintains the realtime websocket. Two modes:

- Default (`multi_client=False`) — class-level `global_wsc`/`global_stop` ensure one socket process-wide; instantiating a new client closes the previous.
- `allow_multiple_clients=True` — per-instance socket; required when using the `Jellyfin` Borg facade with multiple `server_id`s.

Incoming `MessageId`s are deduped in `self.message_ids`. `ForceKeepAlive` messages start a `KeepAlive` (`keepalive.py`) thread that periodically pings. All messages dispatch via `client.callback(message_type, data)`; consumers reassign `client.callback` to receive events. When the Borg facade is in use, `data['ServerId']` is injected so a single callback can demultiplex.

`timesync` (`TimeSyncManager`) is a port of jellyfin-web's SyncPlay time sync. Polls `utc_time()`, retains the 8 lowest-delay measurements, exposes `get_time_offset()` / `get_ping()` and a subscriber callback API. Polls greedily (1s) for the first few measurements then drops to 60s.

### Cross-cutting conventions

- **Backward compatibility is a hard rule** for `api.py` — see README's "Contributing" section. Add new parameters with defaults; don't rename or remove existing ones. Document additions in README's "Changes from Jellyfin Kodi" list.
- **Logging** uses two logger names inconsistently: `'Jellyfin'` (root, in `__init__.py`/`http.py`/`credentials.py`) and `'JELLYFIN.<module>'` (everywhere else). Follow the surrounding file rather than unifying.
- **Callbacks** are the primary out-of-band signal. `client.callback(event, data)` is invoked for `ServerOnline`, `ServerUnreachable`, `AccessRestricted`, `Unauthorized`, `WebSocketConnect`/`Disconnect`/`Error`, and every websocket message type. Default is a no-op; consumers override.
- **Python 3.6+** per `pyproject.toml`, but the tox/CI matrix is 3.8–3.12. f-strings and `from __future__` are fine; avoid 3.10-only syntax (match statements, `X | Y` unions in runtime contexts).
