import unittest
from unittest.mock import patch

import requests

from jellyfin_apiclient_python.api import API
from jellyfin_apiclient_python.client import JellyfinClient, Config
from jellyfin_apiclient_python.connection_manager import (
    CONNECTION_STATE,
    ConnectionManager,
)
from jellyfin_apiclient_python.credentials import Credentials
from jellyfin_apiclient_python.exceptions import HTTPException


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

    def test_login_with_quick_connect_persists_credentials(self):
        self.manager.credentials.set({"Servers": [{"Id": "srv"}]})
        auth_result = {
            "AccessToken": "tok",
            "ServerId": "srv",
            "User": {"Id": "user-1"},
        }
        with patch.object(API, "login_with_quick_connect", return_value=auth_result):
            result = self.manager.login_with_quick_connect("https://s", "secret")

        self.assertEqual(result, auth_result)
        server = self.manager.credentials.get()["Servers"][0]
        self.assertEqual(server["AccessToken"], "tok")
        self.assertEqual(server["UserId"], "user-1")
        self.assertEqual(self.manager.config.data["auth.token"], "tok")
        self.assertEqual(self.manager.config.data["auth.user_id"], "user-1")

    def test_login_with_quick_connect_failure_returns_empty(self):
        with patch.object(API, "login_with_quick_connect", return_value={}):
            self.assertEqual(
                self.manager.login_with_quick_connect("https://s", "secret"), {}
            )

    def test_connect_to_address_unreachable_is_not_an_error(self):
        for error in (
            requests.exceptions.ConnectionError("refused"),
            requests.exceptions.ConnectTimeout("timed out"),
        ):
            with self.subTest(error=error):
                with patch.object(API, "check_redirect", side_effect=error):
                    with self.assertLogs("JELLYFIN", level="INFO") as logs:
                        result = self.manager.connect_to_address("http://s:8096")

                self.assertEqual(
                    result, {"State": CONNECTION_STATE["Unavailable"]}
                )
                self.assertEqual(
                    [record.levelname for record in logs.records], ["INFO"]
                )

    def test_connect_to_address_unexpected_error_is_logged(self):
        with patch.object(API, "check_redirect", side_effect=ValueError("boom")):
            with self.assertLogs("JELLYFIN", level="ERROR"):
                result = self.manager.connect_to_address("http://s:8096")

        self.assertEqual(result, {"State": CONNECTION_STATE["Unavailable"]})

    def test_login_with_quick_connect_requires_secret(self):
        with self.assertRaises(AttributeError):
            self.manager.login_with_quick_connect("https://s", "")


    def test_api_key_without_ssl_setting_signs_in(self):
        # README API-key example: no config.app() and no auth.ssl.
        client = JellyfinClient()
        client.config.data["app.name"] = "app"
        client.config.data["app.version"] = "0.0.1"
        system_info = {"Id": "server-id", "ServerName": "s", "Version": "10.11.8"}

        with patch.object(API, "get_public_info", return_value=system_info), \
                patch.object(API, "validate_authentication_token", return_value=system_info):
            state = client.authenticate(
                {"Servers": [{"AccessToken": "api-key", "address": "http://s:8096"}]},
                discover=False,
            )

        self.assertEqual(state["State"], CONNECTION_STATE["SignedIn"])
        self.assertIsNone(client.config.data["auth.ssl"])

    def test_http_error_callbacks_get_the_server_id_after_connect(self):
        client = JellyfinClient()
        client.config.data["app.name"] = "app"
        client.config.data["app.version"] = "0.0.1"
        client.config.data["auth.ssl"] = True
        system_info = {"Id": "server-id", "ServerName": "s", "Version": "12.3.0"}

        with patch.object(API, "get_public_info", return_value=system_info), \
                patch.object(API, "validate_authentication_token", return_value=system_info):
            client.authenticate(
                {"Servers": [{"AccessToken": "api-key", "address": "http://s:8096"}]},
                discover=False,
            )

        events = []
        client.callback = lambda event, data: events.append((event, data))
        with patch.object(client.http, "_requests",
                          side_effect=requests.exceptions.ConnectionError("refused")):
            with self.assertRaises(HTTPException):
                client.http.request({"type": "GET", "handler": "Sessions", "retry": 0})

        self.assertEqual(events, [("ServerUnreachable", {"ServerId": "server-id"})])
