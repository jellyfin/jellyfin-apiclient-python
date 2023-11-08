import unittest

from jellyfin_apiclient_python.credentials import Credentials


class TestCredientials(unittest.TestCase):
    def setUp(self):
        self.credentials = Credentials()

    def assertEmptyCredentials(self, credentials):
        empty_creds = {"Servers": []}
        self.assertEqual(credentials, empty_creds)

    def test_set_credentials_and_get_credentials(self):
        credentials = {"Server": "Foo"}
        self.credentials.set_credentials(credentials)
        self.assertEqual(self.credentials.get_credentials(), credentials)

    def test_get_credentials(self):
        empty = self.credentials.get_credentials()
        self.assertEmptyCredentials(empty)

    def test_set_credentials_evals_to_false(self):
        self.credentials.set_credentials(False)
        # get() then swallows the ValueError, and returns empty credentials,
        # but only if self.credentials evaluates to False
        self.assertEmptyCredentials(self.credentials.get())

    def test_get(self):
        empty = self.credentials.get()
        self.assertEmptyCredentials(empty)

    def test_set(self):
        data = {"User": "foobar"}
        self.credentials.set(data)
        self.assertEqual(self.credentials.get(), data)
        # Passing anything that evaluates to false will clear it
        self.credentials.set(False)
        self.assertEmptyCredentials(self.credentials.get())

    def test_add_update_user(self):
        server = {}
        user_data = {"Id": 42}
        self.credentials.add_update_user(server, user_data)
        self.assertEqual(server, {"Users": [user_data]})
        # If we re-add the same user, it is unchanged.
        self.credentials.add_update_user(server, user_data)
        self.assertEqual(server, {"Users": [user_data]})

    def test_add_update_server_no_id(self):
        with self.assertRaises(KeyError):
            self.credentials.add_update_server({}, {"Foo": "Bar"})

    def test_add_update_server_adds_datelastaccessed(self):
        servers = []
        server = {"Id": 42}
        new_server = self.credentials.add_update_server(servers, server)
        server["DateLastAccessed"] = "2001-01-01T00:00:00Z"
        self.assertEqual(new_server, server)

    def test_add_update_server_merges_data(self):
        # DateLastAccessed must be older for merges to happen
        servers = [{"Id": 42, "DateLastAccessed": "1999-12-31T23:58:59Z"}]
        server = {
            "Id": 42, "AccessToken": "xx", "UserId": 1, "UserLinkType": "Foo",
            "ExchangeToken": "Bar", "ManualAddress": 2, "LocalAddress": 3,
            "Name": "Test", "LastConnectionMode": "Unknown",
            "ConnectServerId": 44
            }
        new_server = self.credentials.add_update_server(servers, server)
        self.assertEqual(new_server, server)

    def test_add_update_server_does_not_merge_if_newer(self):
        servers = [{"Id": 42, "DateLastAccessed": "2023-10-01T01:02:03Z"}]
        server = {"Id": 42}
        new_server = self.credentials.add_update_server(servers, server)
        self.assertEqual(new_server, servers[0])

    def test_add_update_server_does_not_merge_unknown_fields(self):
        servers = [{"Id": 42, "DateLastAccessed": "1999-12-31T23:58:59Z"}]
        server = {"Id": 42, "Foo": "Bar"}
        new_server = self.credentials.add_update_server(servers, server)
        merged_server = {"Id": 42, "DateLastAccessed": "2001-01-01T00:00:00Z"}
        self.assertEqual(new_server, merged_server)
