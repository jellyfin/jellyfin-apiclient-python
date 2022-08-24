# -*- coding: utf-8 -*-

#################################################################################################

import logging

from . import api
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

        self.config = Config()
        self.http = HTTP(self)
        self.wsc = WSClient(self, allow_multiple_clients)
        self.auth = ConnectionManager(self)
        self.jellyfin = api.API(self.http)
        self.callback_ws = callback
        self.callback = callback
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
        self.wsc.stop_client()
        self.http.stop_session()
        self.timesync.stop_ping()
