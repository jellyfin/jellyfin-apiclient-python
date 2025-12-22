# -*- coding: utf-8 -*-

import asyncio
import json
import logging

from .httpx_compat import httpx

from .api import API

LOG = logging.getLogger('JELLYFIN.' + __name__)


class AsyncAPI:
    """
    Async wrapper around the existing API mixins.

    Methods are exposed as async callables and route to AsyncHTTP.request,
    while a small subset of request helpers are reimplemented to avoid
    blocking on synchronous requests.

    Future work should investigate making this async version the primary
    implementation and have the sync API be the wrapper.
    """

    def __init__(self, http):
        self._api = API(http)
        self.client = self._api.client
        self.config = self._api.config
        self.default_timeout = self._api.default_timeout

    def _client_kwargs(self):
        cert = None
        verify = self.config.data.get('auth.ssl', False)
        if 'auth.tls_client_cert' in self.config.data and 'auth.tls_client_key' in self.config.data:
            cert = (
                self.config.data['auth.tls_client_cert'],
                self.config.data['auth.tls_client_key'],
            )
            if self.config.data['auth.tls_server_ca']:
                verify = self.config.data['auth.tls_server_ca']
        return {
            "verify": verify,
            "cert": cert,
        }

    async def send_request(self, server_url, path, method="get", headers=None,
                           data=None, timeout=None, session=None):
        headers = headers or self.get_default_headers()
        request_settings = {
            'headers': headers,
            'timeout': timeout or self.default_timeout,
        }
        if data is not None:
            request_settings['data'] = data

        url = "%s/%s" % (server_url.rstrip('/'), path.lstrip('/'))

        if self.config.data.get('auth.ssl') is False:
            request_settings["verify"] = False

        LOG.info("Sending %s request to %s", method, path)
        LOG.debug(request_settings['timeout'])
        LOG.debug(request_settings['headers'])

        if session is not None:
            request_method = getattr(session, method.lower())
            return await request_method(url, **request_settings)

        async with httpx.AsyncClient(**self._client_kwargs()) as client:
            request_method = getattr(client, method.lower())
            return await request_method(url, **request_settings)

    async def login(self, server_url, username, password="", session=None):
        path = "Users/AuthenticateByName"
        auth_data = {
            "username": username,
            "Pw": password
        }

        headers = self.get_default_headers()
        headers.update({'Content-type': "application/json"})

        try:
            LOG.info("Trying to login to %s/%s as %s", server_url, path, username)
            response = await self.send_request(
                server_url,
                path,
                method="post",
                headers=headers,
                data=json.dumps(auth_data),
                timeout=(5, 30),
                session=session,
            )

            if response.status_code == 200:
                return response.json()
            LOG.error("Failed to login to server with status code: %s", response.status_code)
            LOG.error("Server Response:\n%s", response.content)
            LOG.debug(headers)

            return {}
        except Exception as error:
            LOG.error(error)

        return {}

    async def validate_authentication_token(self, server, session=None):
        headers = self.get_default_headers()
        comma = "," if "app.device_name" in self.config.data else ""
        headers["Authorization"] += f"{comma} Token=\"{server['AccessToken']}\""

        response = await self.send_request(
            server['address'],
            "system/info",
            headers=headers,
            session=session,
        )
        return response.json() if response.status_code == 200 else {}

    async def get_public_info(self, server_address, session=None):
        response = await self.send_request(server_address, "system/info/public", session=session)
        return response.json() if response.status_code == 200 else {}

    async def check_redirect(self, server_address, session=None):
        response = await self.send_request(server_address, "system/info/public", session=session)
        url = response.url.replace('/system/info/public', '')
        return url

    def get_default_headers(self):
        return self._api.get_default_headers()

    def __getattr__(self, name):
        """
        Forward the requests to the sync API
        """
        attr = getattr(self._api, name)
        if callable(attr):
            async def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                if asyncio.iscoroutine(result):
                    return await result
                return result

            return wrapper
        return attr
