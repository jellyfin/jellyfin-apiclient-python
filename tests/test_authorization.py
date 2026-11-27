from unittest import TestCase
from unittest.mock import patch

from jellyfin_apiclient_python.client import JellyfinClient


DEVICE_NAME = '家庭 🎬 "TV", 50%+'
APP_AUTHORIZATION = (
    'MediaBrowser Client="Test", '
    'Device="%E5%AE%B6%E5%BA%AD%20%F0%9F%8E%AC%20%22TV%22%2C%2050%25%2B", '
    'DeviceId="test-device", Version="1.0"'
)


class TestAuthorization(TestCase):
    def setUp(self):
        self.client = JellyfinClient(allow_multiple_clients=True)
        self.client.config.app("Test", "1.0", DEVICE_NAME, "test-device")

    def test_login_header_encodes_device_name(self):
        headers = self.client.auth.API.get_default_headers()
        self.assertEqual(headers["Authorization"], APP_AUTHORIZATION)

    def test_websocket_header_encodes_device_name(self):
        self.client.config.auth("http://server", "test-user", "test-token")
        self.client.wsc.stop = True
        with patch("jellyfin_apiclient_python.ws_client.websocket.WebSocketApp") as app:
            self.client.wsc.run()
        headers = app.call_args.kwargs["header"]
        self.assertEqual(
            headers["Authorization"], APP_AUTHORIZATION + ', Token="test-token"'
        )
