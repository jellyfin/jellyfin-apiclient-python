# -*- coding: utf-8 -*-

#################################################################################################

import asyncio
import logging

from .async_api import AsyncAPI
from .async_http import AsyncHTTP
from .async_runner import AsyncRunner
from .configuration import Config
from .http import HTTP
from .ws_client import WSClient
from .connection_manager import ConnectionManager, CONNECTION_STATE
from .timesync_manager import TimeSyncManager

#################################################################################################

LOG = logging.getLogger('JELLYFIN.' + __name__)

#################################################################################################


def callback(message, data):

    ''' Callback function should received message, data
        message: string
        data: json dictionary
    '''
    pass


class JellyfinClient(object):

    logged_in = False

    def __init__(self, allow_multiple_clients=False):
        LOG.debug("JellyfinClient initializing...")

        self._runner = AsyncRunner()
        self.config = Config()
        self._async = AsyncJellyfinClient(
            allow_multiple_clients=allow_multiple_clients,
            config=self.config,
        )
        self.http = HTTP(self, async_http=self._async.http, runner=self._runner)
        self.wsc = WSClient(self, allow_multiple_clients)
        self.auth = ConnectionManager(self)
        self.jellyfin = _SyncAPIProxy(self._async.jellyfin, self._runner)
        self.callback_ws = callback
        self.callback = callback
        self._async.callback = self.callback
        self._async.callback_ws = self.callback_ws
        self.timesync = TimeSyncManager(self)

    def set_credentials(self, credentials=None):
        self.auth.credentials.set_credentials(credentials or {})

    def get_credentials(self):
        return self.auth.credentials.get_credentials()

    def authenticate(self, credentials=None, options=None, discover=True):

        self.set_credentials(credentials or {})
        state = self.auth.connect(options or {}, discover)

        if state['State'] == CONNECTION_STATE['SignedIn']:

            LOG.info("User is authenticated.")
            self.logged_in = True
            self.callback("ServerOnline", {'Id': self.auth.server_id})

        state['Credentials'] = self.get_credentials()

        return state

    def start(self, websocket=False, keep_alive=True):

        if not self.logged_in:
            raise ValueError("User is not authenticated.")

        self.http.start_session()

        if keep_alive:
            self.http.keep_alive = True

        if websocket:
            self.start_wsc()

    def start_wsc(self):
        self.wsc.start()

    def stop(self):
        self.close()

    def close(self):
        self.wsc.stop_client()
        self.timesync.stop_ping()
        try:
            self._runner.run(self._async.aclose())
        finally:
            self._runner.close()

    @property
    def aio(self):
        return self._async

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        self.close()


class AsyncJellyfinClient(object):

    logged_in = False

    def __init__(self, allow_multiple_clients=False, config=None):
        LOG.debug("AsyncJellyfinClient initializing...")

        self.config = config or Config()
        self.http = AsyncHTTP(self)
        self.jellyfin = AsyncAPI(self.http)
        self.callback_ws = callback
        self.callback = callback

    async def aclose(self):
        await self.http.stop_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, exc_tb):
        await self.aclose()


class _SyncAPIProxy:

    def __init__(self, async_api, runner):
        self._async_api = async_api
        self._runner = runner

    def __getattr__(self, name):
        attr = getattr(self._async_api, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                if asyncio.iscoroutine(result):
                    try:
                        return self._runner.run(result)
                    except RuntimeError:
                        result.close()
                        raise
                return result

            return wrapper
        return attr
