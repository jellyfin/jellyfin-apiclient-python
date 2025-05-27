"""holds all integration tests. Spins up a docker-based jellyfin instance."""

import unittest

from jellyfin_apiclient_python import JellyfinClient
from tests_integration.create_instance import create_instance, cleanup_instance

TEST_URL = 'http://127.0.0.1:11111'
TEST_USER = 'root'
TEST_PASSWORD = 'password'
TEST_USER_UUID = '3b7cd9fdee774b80828e38168a8cd3d6' # manually retrieved from API

class IntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_instance()

    def setUp(self):
        self.api = JellyfinClient()
        self.api.config.app(
            name = 'python_api_integration_test',
            version = '0.0.1',
            device_name = 'python_api_integration_test',
            device_id = '42')
        self.api.config.data["auth.ssl"] = False
        self.api.auth.connect_to_address(TEST_URL)


        assert self.api.auth.login(
            server_url = TEST_URL,
            username = TEST_USER,
            password = TEST_PASSWORD
        )

    @classmethod
    def tearDownClass(cls):
        cleanup_instance()

    def test_get_public_information(self):
        assert self.api.jellyfin.get_public_info(TEST_URL)

    def test_try_server(self):
        assert self.api.jellyfin.try_server()

    ################################################################################################
    #  User data                                                                                   #
    ################################################################################################

    def test_get_users(self):
        users = self.api.jellyfin.get_users()
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)
        user = users[0]
        self.assertEqual(user.get('Id'), TEST_USER_UUID)
        self.assertEqual(user.get('Name'), TEST_USER)
        self.assertTrue(user.get('HasPassword'))

    def test_get_public_users(self):
        users = self.api.jellyfin.get_public_users()
        self.assertEqual(users, [])

    def test_get_user(self):
        user = self.api.jellyfin.get_user(TEST_USER_UUID)
        self.assertEqual(user.get('Id'), TEST_USER_UUID)
        self.assertEqual(user.get('Name'), TEST_USER)
        self.assertTrue(user.get('HasPassword'))

    def test_get_user_with_name(self):
        """Run a get user with a username but expects an uuid, will throw error"""
        with self.assertRaises(RuntimeError):
            self.api.jellyfin.get_user(TEST_USER)

    def test_get_user_without_id(self):
        self.assertEqual(self.api.jellyfin.get_user(), self.api.jellyfin.get_users()[0])

    def test_get_user_settings(self):
        settings = self.api.jellyfin.get_user_settings()
        self.assertIsNotNone(settings)
        self.assertIsInstance(settings, dict)

    def test_create_and_delete_new_user(self):
        new_user = self.api.jellyfin.new_user("New User", "very_safe_password")
        self.assertIsNotNone(new_user)
        self.assertIsInstance(new_user, dict)
        self.assertIsNotNone(new_user.get('Id'))
        new_user_id = new_user.get('Id')
        self.assertIsNotNone(new_user_id)

        res = self.api.jellyfin.delete_user(new_user_id)
        self.assertIsNone(res)

    def test_get_views(self):
        views = self.api.jellyfin.get_views()
        self.assertIsNotNone(views)
        self.assertIsInstance(views, dict)

    def test_get_media_folders(self):
        folders = self.api.jellyfin.get_media_folders()
        self.assertIsNotNone(folders)
        print(folders)
