import io
from unittest import TestCase
from unittest.mock import Mock, patch

import requests

from jellyfin_apiclient_python.exceptions import HTTPException
from jellyfin_apiclient_python.http import HTTP

BODY = b"0123456789" * 10


class FakeResponse:
    def __init__(self, chunks, fail_after=False, status_code=200):
        self.chunks = chunks
        self.fail_after = fail_after
        self.status_code = status_code
        self.headers = {}

    def iter_content(self, chunk_size=1):
        yield from self.chunks
        if self.fail_after:
            # What requests raises when a read times out mid-body.
            raise requests.exceptions.ConnectionError("read timed out")

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(response=self)


class FakeSession:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.calls = 0

    def get(self, **kwargs):
        self.calls += 1
        return self.responses.pop(0)


class NonSeekable(io.BytesIO):
    def seekable(self):
        return False


class TestStreamRetry(TestCase):
    def setUp(self):
        client = Mock()
        client.config.data = {"http.timeout": 5, "http.user_agent": None}
        self.http = HTTP(client)
        patcher = patch("jellyfin_apiclient_python.http.time.sleep")
        self.addCleanup(patcher.stop)
        patcher.start()

    def stream(self, session, dest):
        self.http.request({"type": "GET", "url": "http://server/x"},
                          session=session, dest_file=dest)

    def test_retry_after_partial_body_keeps_one_copy(self):
        session = FakeSession(
            FakeResponse([BODY[:40]], fail_after=True),
            FakeResponse([BODY[:50], BODY[50:]]),
        )
        dest = io.BytesIO()
        self.stream(session, dest)
        self.assertEqual(session.calls, 2)
        self.assertEqual(dest.getvalue(), BODY)

    def test_retry_after_502_body_keeps_one_copy(self):
        session = FakeSession(
            FakeResponse([b"bad gateway"], status_code=502),
            FakeResponse([BODY]),
        )
        dest = io.BytesIO()
        self.stream(session, dest)
        self.assertEqual(dest.getvalue(), BODY)

    def test_non_seekable_dest_with_bytes_is_not_retried(self):
        session = FakeSession(
            FakeResponse([BODY[:40]], fail_after=True),
            FakeResponse([BODY]),
        )
        dest = NonSeekable()
        with self.assertRaises(HTTPException):
            self.stream(session, dest)
        self.assertEqual(session.calls, 1)

    def test_non_seekable_dest_without_bytes_is_retried(self):
        session = FakeSession(
            FakeResponse([], fail_after=True),
            FakeResponse([BODY]),
        )
        dest = NonSeekable()
        self.stream(session, dest)
        self.assertEqual(session.calls, 2)
        self.assertEqual(dest.getvalue(), BODY)
