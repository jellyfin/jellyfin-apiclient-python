# -*- coding: utf-8 -*-

import asyncio
import importlib
import importlib.util
import json
from dataclasses import dataclass

import requests


def _load_httpx():
    spec = importlib.util.find_spec("httpx")
    if spec is None:
        return None
    return importlib.import_module("httpx")


_real_httpx = _load_httpx()


if _real_httpx is not None:
    httpx = _real_httpx
else:
    class ConnectError(Exception):
        pass

    class ReadTimeout(Exception):
        pass

    class InvalidURL(Exception):
        pass

    class HTTPStatusError(Exception):
        def __init__(self, message, response):
            super().__init__(message)
            self.response = response

    @dataclass
    class Request:
        method: str
        url: str
        headers: dict
        content: bytes

    jsonlib = json

    class Response:
        def __init__(self, status_code, json=None, headers=None, content=None, url=None, elapsed=None):
            self.status_code = status_code
            self.headers = headers or {}
            self._json = json
            if content is None and json is not None:
                content = jsonlib.dumps(json).encode("utf-8")
            self.content = content or b""
            self.url = url
            self.elapsed = elapsed or type("Elapsed", (), {"total_seconds": lambda self: 0})()

        def json(self):
            if self._json is not None:
                return self._json
            return jsonlib.loads(self.content.decode("utf-8"))

        def raise_for_status(self):
            if 400 <= self.status_code:
                raise HTTPStatusError(f"Status code {self.status_code}", self)

        async def aread(self):
            return self.content

        async def aiter_bytes(self, chunk_size=8192):
            for i in range(0, len(self.content), chunk_size):
                yield self.content[i:i + chunk_size]

        async def aclose(self):
            return

    class MockTransport:
        def __init__(self, handler):
            self._handler = handler

        async def handle_async_request(self, request):
            return self._handler(request)

    class AsyncClient:
        def __init__(self, transport=None, timeout=None, verify=None, cert=None):
            self._transport = transport
            self._timeout = timeout
            self._verify = verify
            self._cert = cert

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, exc_tb):
            await self.aclose()

        async def aclose(self):
            return

        async def request(self, method, url, **kwargs):
            if self._transport is not None:
                request = Request(
                    method=method.upper(),
                    url=url,
                    headers=kwargs.get("headers") or {},
                    content=kwargs.get("content") or b"",
                )
                response = await self._transport.handle_async_request(request)
                response.url = response.url or url
                return response
            return await asyncio.to_thread(self._sync_request, method, url, **kwargs)

        async def get(self, url, **kwargs):
            return await self.request("GET", url, **kwargs)

        async def post(self, url, **kwargs):
            return await self.request("POST", url, **kwargs)

        async def head(self, url, **kwargs):
            return await self.request("HEAD", url, **kwargs)

        async def delete(self, url, **kwargs):
            return await self.request("DELETE", url, **kwargs)

        def _sync_request(self, method, url, **kwargs):
            try:
                response = requests.request(method, url, **kwargs)
                elapsed = type("Elapsed", (), {"total_seconds": lambda self: response.elapsed.total_seconds()})()
                return Response(
                    response.status_code,
                    headers=dict(response.headers),
                    content=response.content,
                    url=response.url,
                    elapsed=elapsed,
                )
            except requests.exceptions.ConnectionError as error:
                raise ConnectError(error) from error
            except requests.exceptions.ReadTimeout as error:
                raise ReadTimeout(error) from error
            except requests.exceptions.MissingSchema as error:
                raise InvalidURL(error) from error

    httpx = type(
        "httpx",
        (),
        {
            "AsyncClient": AsyncClient,
            "MockTransport": MockTransport,
            "Response": Response,
            "ConnectError": ConnectError,
            "ReadTimeout": ReadTimeout,
            "HTTPStatusError": HTTPStatusError,
            "InvalidURL": InvalidURL,
        },
    )
