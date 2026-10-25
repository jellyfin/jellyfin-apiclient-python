import ssl
from unittest import TestCase
from unittest.mock import Mock, patch

import certifi

from jellyfin_apiclient_python.api import API
from jellyfin_apiclient_python.configuration import tls_verify
from jellyfin_apiclient_python.http import HTTP
from jellyfin_apiclient_python.ws_client import WSClient

CA = "/etc/ssl/private-ca.pem"

NO_VERIFY = {"cert_reqs": ssl.CERT_NONE}
SYSTEM_CAS = {"context": None, "ca_certs": certifi.where()}
PRIVATE_CA = {"context": None, "ca_certs": CA}

# (config, expected verify value, expected websocket sslopt)
CASES = (
    ({"auth.ssl": True}, True, SYSTEM_CAS),
    ({"auth.ssl": None}, True, SYSTEM_CAS),
    ({}, True, SYSTEM_CAS),
    ({"auth.ssl": False}, False, NO_VERIFY),
    ({"auth.ssl": True, "auth.tls_server_ca": CA}, CA, PRIVATE_CA),
    ({"auth.ssl": None, "auth.tls_server_ca": CA}, CA, PRIVATE_CA),
    ({"auth.tls_server_ca": CA}, CA, PRIVATE_CA),
    ({"auth.ssl": False, "auth.tls_server_ca": CA}, False, NO_VERIFY),
)


def make_client(data):
    client = Mock()
    client.config.data = {"http.timeout": 5, "http.user_agent": None, **data}
    return client


class TestTlsVerify(TestCase):
    def test_tls_verify(self):
        for data, expected, _ in CASES:
            with self.subTest(data=data):
                self.assertEqual(tls_verify(data), expected)

    def test_http_request_uses_it(self):
        for data, expected, _ in CASES:
            with self.subTest(data=data):
                http = HTTP(make_client(data))
                request = http._request({"type": "GET", "url": "https://server/x"})
                self.assertEqual(request["verify"], expected)

    def test_send_request_uses_it(self):
        for data, expected, _ in CASES:
            with self.subTest(data=data):
                api = API(Mock())
                api.config = make_client(data).config
                with patch("jellyfin_apiclient_python.api.requests.get") as get, \
                        patch.object(API, "get_default_headers", return_value={}):
                    api.send_request("https://server", "System/Info/Public")
                self.assertEqual(get.call_args.kwargs["verify"], expected)

    def test_websocket_uses_it(self):
        for data, _, expected_sslopt in CASES:
            with self.subTest(data=data):
                client = make_client({"auth.server": "https://server", **data})
                wsc = WSClient(client, allow_multiple_clients=True)
                with patch("jellyfin_apiclient_python.ws_client.websocket.WebSocketApp") as app:
                    app.return_value.run_forever.side_effect = lambda **kw: setattr(wsc, "stop", True)
                    wsc.run()
                self.assertEqual(app.return_value.run_forever.call_args.kwargs["sslopt"], expected_sslopt)
