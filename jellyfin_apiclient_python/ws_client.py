# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

#################################################################################################

import json
import logging
import threading

import websocket

from .keepalive import KeepAlive

##################################################################################################

LOG = logging.getLogger('JELLYFIN.' + __name__)

##################################################################################################


class WSClient(threading.Thread):
    multi_client = False
    global_wsc = None
    global_stop = False

    def __init__(self, client, allow_multiple_clients=False):

        LOG.debug("WSClient initializing...")

        self.client = client
        self.keepalive = None
        self.wsc = None
        self.stop = False
        self.message_ids = set()

        if self.multi_client or allow_multiple_clients:
            self.multi_client = True

        threading.Thread.__init__(self)

    def send(self, message, data=""):

        if self.wsc is None:
            raise ValueError("The websocket client is not started.")

        self.wsc.send(json.dumps({'MessageType': message, "Data": data}))

    def run(self):

        token = self.client.config.data['auth.token']
        device_id = self.client.config.data['app.device_id']
        server = self.client.config.data['auth.server']
        server = server.replace('https', "wss") if server.startswith('https') else server.replace('http', "ws")
        wsc_url = "%s/socket?api_key=%s&device_id=%s" % (server, token, device_id)

        LOG.info("Websocket url: %s", wsc_url)

        self.wsc = websocket.WebSocketApp(wsc_url,
                                          on_message=lambda ws, message: self.on_message(ws, message),
                                          on_error=lambda ws, error: self.on_error(ws, error))
        self.wsc.on_open = lambda ws: self.on_open(ws)
        
        if not self.multi_client:
            if self.global_wsc is not None:
                self.global_wsc.close()
            self.global_wsc = self.wsc

        while not self.stop and not self.global_stop:

            self.wsc.run_forever(ping_interval=10)

            if not self.stop:
                break

        LOG.info("---<[ websocket ]")
        self.client.callback('WebSocketDisconnect', None)

    def on_error(self, ws, error):
        LOG.error(error)
        self.client.callback('WebSocketError', error)

    def on_open(self, ws):
        LOG.info("--->[ websocket ]")
        self.client.callback('WebSocketConnect', None)

    def on_message(self, ws, message):

        message = json.loads(message)

        # If a message is received multiple times, ignore repeats.
        message_id = message.get("MessageId")
        if message_id is not None:
            if message_id in self.message_ids:
                return
            self.message_ids.add(message_id)

        data = message.get('Data', {})

        if message['MessageType'] == "ForceKeepAlive":
            self.send("KeepAlive")
            if self.keepalive is not None:
                self.keepalive.stop()
            self.keepalive = KeepAlive(data, self)
            self.keepalive.start()
            return
        elif message['MessageType'] == "KeepAlive":
            LOG.debug("KeepAlive received from server.")
            return

        if data is None:
            data = {}
        elif type(data) is not dict:
            data = {"value": data}

        if message['MessageType'] in ('RefreshProgress',):
            LOG.debug("Ignoring %s", message)
            return

        if not self.client.config.data['app.default']:
            data['ServerId'] = self.client.auth.server_id

        self.client.callback(message['MessageType'], data)

    def stop_client(self):

        self.stop = True

        if self.keepalive is not None:
            self.keepalive.stop()

        if self.wsc is not None:
            self.wsc.close()

        if not self.multi_client:
            self.global_stop = True
            self.global_wsc = None
