import unittest

from jellyfin_apiclient_python.api import API
from jellyfin_apiclient_python.client import JellyfinClient, Config
from jellyfin_apiclient_python.connection_manager import ConnectionManager
from jellyfin_apiclient_python.credentials import Credentials


class TestConnectionManager(unittest.TestCase):
    def setUp(self):
        client = JellyfinClient()
        self.manager = ConnectionManager(client)

    def test_attributes(self):
        self.assertIsInstance(self.manager.client, JellyfinClient)
        self.assertIsInstance(self.manager.config, Config)
        self.assertIsInstance(self.manager.credentials, Credentials)
        self.assertIsInstance(self.manager.API, API)

    def test_clear_data(self):
        self.manager.clear_data()
        self.assertIsNone(self.manager.user)
        self.assertEqual({'Servers': []}, self.manager.credentials.get())

    def test_revoke_token(self):
        creds = {'Servers': [{'AccessToken': 2}, {'AccessToken': 1}]}
        self.manager.credentials.set(creds)
        self.manager.revoke_token()
        for server in creds['Servers']:
            server['AccessToken'] = None
        self.assertEqual(creds, self.manager.credentials.get())
        self.assertIsNone(self.manager.config.data["auth.token"])

    def test_process_found_servers(self):
        servers = [
            {'Id': 2, 'EndpointAddress': 'foo.bar', 'Address': 'x:81', 'Name': 'foo'},
            {'Id': 4, 'EndpointAddress': 'baz.quux', 'Address': 'y:83', 'Name': 'baz'}
            ]
        new_servers = self.manager.process_found_servers(servers)
        returned_servers = [
            {'Id': 2, 'address': 'http://foo.bar:81', 'Name': 'foo'},
            {'Id': 4, 'address': 'http://baz.quux:83', 'Name': 'baz'}
            ]
        self.assertEqual(new_servers, returned_servers)

    def test_get_server_info_empty(self):
        self.assertEqual(self.manager.get_server_info(None), {})

    def test_get_server_info_not_found(self):
        self.assertIsNone(self.manager.get_server_info(4))

    def test_get_server_info(self):
        server = {'Id': 2}
        self.manager.credentials.set({"Servers": [server]})
        self.assertEqual(self.manager.get_server_info(2), server)

    def test_jellyfin_user_id(self):
        # self.server_id is set by _after_connect_validated()
        server = {'Id': 2, 'UserId': 4}
        self.manager.credentials.set({"Servers": [server]})
        self.manager.server_id = 2
        self.assertEqual(self.manager.jellyfin_user_id(), 4)

    def test_jellyfin_token(self):
        # self.server_id is set by _after_connect_validated()
        server = {'Id': 4, 'AccessToken': 68}
        self.manager.credentials.set({"Servers": [server]})
        self.manager.server_id = 4
        self.assertEqual(self.manager.jellyfin_token(), 68)

