import json
import socket
import threading
import time
import unittest
from unittest.mock import patch

from jellyfin_apiclient_python import discovery
from jellyfin_apiclient_python.client import JellyfinClient
from jellyfin_apiclient_python.connection_manager import ConnectionManager


def _reply(**fields):
    return json.dumps(fields).encode()


class Responder:
    """A stand-in server on 127.0.0.1: answers the first query it receives
    with ``replies``, waiting ``gap`` seconds before each one."""

    def __init__(self, replies=(), gap=0.0):
        self.replies = list(replies)
        self.gap = gap
        self.queries = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.settimeout(5)
        self.address = self.sock.getsockname()
        self.thread = threading.Thread(target=self._serve, daemon=True)
        self.thread.start()

    def _serve(self):
        try:
            data, sender = self.sock.recvfrom(1024)
        except OSError:
            return
        self.queries.append(data)
        for reply in self.replies:
            time.sleep(self.gap)
            try:
                self.sock.sendto(reply, sender)
            except OSError:
                return

    def close(self):
        self.sock.close()
        self.thread.join(timeout=5)


class TestDiscoverServers(unittest.TestCase):
    def responder(self, *args, **kwargs):
        r = Responder(*args, **kwargs)
        self.addCleanup(r.close)
        return r

    def test_each_server_is_returned_once_and_junk_is_dropped(self):
        a = _reply(Id="a", Name="Den", Address="http://192.0.2.1:8096")
        b = _reply(Id="b", Name="Loft", Address="http://192.0.2.2:8096",
                   EndpointAddress="192.0.2.2")
        r = self.responder([a, a, b"not json", _reply(Name="no id"),
                            _reply(Id="c", Name="no address"), b])

        servers = discovery.discover_servers(timeout=0.5, address=r.address)

        self.assertEqual(r.queries, [discovery.DISCOVERY_MESSAGE])
        self.assertEqual([s["Id"] for s in servers], ["a", "b"])
        self.assertEqual(servers[1]["EndpointAddress"], "192.0.2.2")

    def test_nothing_answering_returns_empty_after_the_timeout(self):
        r = self.responder([])
        start = time.monotonic()
        servers = discovery.discover_servers(timeout=0.3, address=r.address)
        self.assertEqual(servers, [])
        self.assertLess(time.monotonic() - start, 2.0)

    def test_the_timeout_bounds_the_whole_wait_not_each_read(self):
        # A reply every 0.2s for 2s. A timeout that restarts with every
        # reply never expires here; one deadline for the whole wait does.
        replies = [_reply(Id=str(i), Address="http://192.0.2.9")
                   for i in range(10)]
        r = self.responder(replies, gap=0.2)
        start = time.monotonic()
        servers = discovery.discover_servers(timeout=0.5, address=r.address)
        elapsed = time.monotonic() - start
        self.assertLess(elapsed, 1.5, "kept listening past the timeout")
        self.assertLess(len(servers), len(replies))

    def test_a_send_that_fails_returns_empty_instead_of_raising(self):
        servers = discovery.discover_servers(
            timeout=0.2, address=("host.invalid", discovery.DISCOVERY_PORT))
        self.assertEqual(servers, [])

    def test_the_connection_manager_uses_it(self):
        manager = ConnectionManager(JellyfinClient())
        found = [{"Id": "a", "Address": "http://192.0.2.1:8096"}]
        with patch("jellyfin_apiclient_python.connection_manager"
                   ".discover_servers", return_value=found) as fn:
            self.assertEqual(manager._server_discovery(), found)
        fn.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
