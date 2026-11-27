from unittest import TestCase
from unittest.mock import patch

from jellyfin_apiclient_python.client import JellyfinClient


DEVICE_NAME = '家庭 🎬 "TV", 50%+'
ACCESS_TOKEN = "test/token+%="
APP_AUTHORIZATION = (
    'MediaBrowser Client="Test%20%2F%20Client", '
    'Device="%E5%AE%B6%E5%BA%AD%20%F0%9F%8E%AC%20%22TV%22%2C%2050%25%2B", '
    'DeviceId="device%2Fid%2C1", Version="1.0%2Bdev"'
)
TOKEN_FIELD = 'Token="test%2Ftoken%2B%25%3D"'


class TestAuthorization(TestCase):
    def setUp(self):
        self.client = JellyfinClient(allow_multiple_clients=True)
        self.client.config.app("Test / Client", "1.0+dev", DEVICE_NAME, "device/id,1")

    def test_login_header_encodes_app_values(self):
        headers = self.client.auth.API.get_default_headers()
        self.assertEqual(headers["Authorization"], APP_AUTHORIZATION)

    def test_websocket_header_encodes_app_values_and_token(self):
        self.client.config.auth("http://server", "test-user", ACCESS_TOKEN)
        self.client.wsc.stop = True
        with patch("jellyfin_apiclient_python.ws_client.websocket.WebSocketApp") as app:
            self.client.wsc.run()
        headers = app.call_args.kwargs["header"]
        self.assertEqual(headers["Authorization"], f"{APP_AUTHORIZATION}, {TOKEN_FIELD}")

    def test_token_validation_encodes_only_the_saved_token(self):
        self.client.config.auth("http://server", "test-user", "current-token")
        api = self.client.auth.API
        server = {"address": "http://server", "AccessToken": ACCESS_TOKEN}
        with patch.object(api, "send_request") as send:
            send.return_value.status_code = 200
            api.validate_authentication_token(server)
        headers = send.call_args.kwargs["headers"]
        self.assertEqual(headers["Authorization"], f"{APP_AUTHORIZATION}, {TOKEN_FIELD}")
        self.assertEqual(self.client.config.data["auth.token"], "current-token")
