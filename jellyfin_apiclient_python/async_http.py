# -*- coding: utf-8 -*-

#################################################################################################

import asyncio
import json
import logging
import urllib

from .httpx_compat import httpx

from .exceptions import HTTPException

#################################################################################################

LOG = logging.getLogger('Jellyfin.' + __name__)

#################################################################################################


class AsyncHTTP:

    session = None
    keep_alive = False

    def __init__(self, client):
        self.client = client
        self.config = client.config

    async def start_session(self):
        self.session = self._create_client()

    async def stop_session(self):
        if self.session is None:
            return
        try:
            LOG.info("--<[ session/%s ]", id(self.session))
            await self.session.aclose()
        except Exception as error:
            LOG.warning("The async HTTP session could not be terminated: %s", error)
        finally:
            self.session = None

    def _client_kwargs(self):
        cert = None
        verify = self.config.data.get('auth.ssl', False)
        if 'auth.tls_client_cert' in self.client.config.data and 'auth.tls_client_key' in self.client.config.data:
            cert = (
                self.client.config.data['auth.tls_client_cert'],
                self.client.config.data['auth.tls_client_key'],
            )
            if self.client.config.data['auth.tls_server_ca']:
                verify = self.client.config.data['auth.tls_server_ca']
        return {
            "timeout": self.config.data['http.timeout'],
            "verify": verify,
            "cert": cert,
        }

    def _create_client(self):
        return httpx.AsyncClient(**self._client_kwargs())

    def _replace_user_info(self, string):
        if '{server}' in string:
            if self.config.data.get('auth.server', None):
                string = string.replace("{server}", self.config.data['auth.server'])
            else:
                LOG.debug("Server address not set")

        if '{UserId}'in string:
            if self.config.data.get('auth.user_id', None):
                string = string.replace("{UserId}", self.config.data['auth.user_id'])
            else:
                LOG.debug("UserId is not set.")

        if '{DeviceId}'in string:
            if self.config.data.get('app.device_id', None):
                string = string.replace("{DeviceId}", self.config.data['app.device_id'])
            else:
                LOG.debug("DeviceId is not set.")

        return string

    def request_url(self, data):
        if not data:
            raise AttributeError("Request cannot be empty")

        data = self._request(data)

        params = data["params"]
        if "api_key" not in params:
            params["api_key"] = self.config.data.get('auth.token')

        encoded_params = urllib.parse.urlencode(data["params"])
        return "%s?%s" % (data["url"], encoded_params)

    async def request(self, data, session=None, dest_file=None):
        if not data:
            raise AttributeError("Request cannot be empty")

        data = self._request(data)
        LOG.debug("--->[ http ] %s", json.dumps(data, indent=4))
        retry = data.pop('retry', 5)
        stream = dest_file is not None

        server_id = None
        if 'auth.server-id' in self.config.data:
            server_id = self.config.data['auth.server-id']

        while True:
            try:
                method = data.pop('type', "GET")
                response = await self._request_with_session(session, method, stream=stream, **data)
                try:
                    if stream:
                        async for chunk in response.aiter_bytes(chunk_size=8192):
                            if chunk:
                                dest_file.write(chunk)
                    else:
                        await response.aread()

                    if not self.keep_alive and self.session is not None:
                        await self.stop_session()

                    response.raise_for_status()
                finally:
                    await response.aclose()

            except httpx.ConnectError as error:
                if retry:
                    retry -= 1
                    await asyncio.sleep(1)
                    continue

                LOG.error(error)
                if server_id is not None:
                    self.client.callback("ServerUnreachable", {'ServerId': server_id})

                raise HTTPException("ServerUnreachable", error)

            except httpx.ReadTimeout as error:
                if retry:
                    retry -= 1
                    await asyncio.sleep(1)
                    continue

                LOG.error(error)
                raise HTTPException("ReadTimeout", error)

            except httpx.HTTPStatusError as error:
                LOG.error(error)
                status_code = error.response.status_code

                if status_code == 401:
                    if 'X-Application-Error-Code' in error.response.headers:
                        if server_id is not None:
                            self.client.callback("AccessRestricted", {'ServerId': server_id})
                        raise HTTPException("AccessRestricted", error)

                    if server_id is not None:
                        self.client.callback("Unauthorized", {'ServerId': server_id})
                    if hasattr(self.client, "auth"):
                        self.client.auth.revoke_token()
                    raise HTTPException("Unauthorized", error)

                if status_code == 500:
                    LOG.error("--[ 500 response ] %s", error)
                    return

                if status_code == 502:
                    if retry:
                        retry -= 1
                        await asyncio.sleep(1)
                        continue

                raise HTTPException(status_code, error)

            except httpx.InvalidURL as error:
                LOG.error("Request missing Schema. %s", error)
                raise HTTPException("MissingSchema", {'Id': self.config.data.get('auth.server', "None")})

            except Exception:
                raise

            else:
                try:
                    if stream:
                        return
                    self.config.data['server-time'] = response.headers['Date']
                    elapsed_ms = None
                    if hasattr(response, "_elapsed"):
                        elapsed_ms = int(response.elapsed.total_seconds() * 1000)
                    response_json = response.json()
                    if elapsed_ms is not None:
                        LOG.debug("---<[ http ][%s ms]", elapsed_ms)
                    else:
                        LOG.debug("---<[ http ]")
                    LOG.debug(json.dumps(response_json, indent=4))

                    return response_json
                except ValueError:
                    return

    async def _request_with_session(self, session, action, stream=False, **kwargs):
        active_session = session or self.session
        if active_session is None:
            async with self._create_client() as client:
                return await self._requests(client, action, stream=stream, **kwargs)
        return await self._requests(active_session, action, stream=stream, **kwargs)

    async def _requests(self, session, action, stream=False, **kwargs):
        kwargs.pop("verify", None)
        if stream:
            try:
                return await session.request(action, **kwargs, stream=True)
            except TypeError:
                return await session.request(action, **kwargs)
        if action == "GET":
            return await session.get(**kwargs)
        if action == "POST":
            return await session.post(**kwargs)
        if action == "HEAD":
            return await session.head(**kwargs)
        if action == "DELETE":
            return await session.delete(**kwargs)

    def _request(self, data):
        if 'url' not in data:
            data['url'] = "%s/%s" % (self.config.data.get("auth.server", ""), data.pop('handler', ""))

        headers = self._get_default_headers()
        user_specified_headers = (data.get('headers', None) or {})
        headers.update(user_specified_headers)

        data['headers'] = headers
        data['timeout'] = data.get('timeout') or self.config.data['http.timeout']
        data['verify'] = data.get('verify') or self.config.data.get('auth.ssl', False)
        data['url'] = self._replace_user_info(data['url'])
        self._process_params(data.get('params') or {})
        self._process_params(data.get('json') or {})

        return data

    def _process_params(self, params):
        if isinstance(params, str):
            return

        for key in params:
            value = params[key]

            if isinstance(value, dict):
                self._process_params(value)

            if isinstance(value, str):
                params[key] = self._replace_user_info(value)

    def _get_authenication_header(self):
        params = {}
        if "app.device_name" in self.config.data:
            params.update({
                "Client": self.config.data['app.name'],
                "Device": self.config.data['app.device_name'],
                "DeviceId": self.config.data['app.device_id'],
                "Version": self.config.data['app.version']
                })
        if "auth.token" in self.config.data:
            params["Token"] = self.config.data['auth.token']
        param_line = ", ".join(f'{k}="{v}"' for k, v in params.items())
        return f"MediaBrowser {param_line}"

    def _get_default_headers(self, content_type="application/json"):
        app_name = f"{self.config.data.get('app.name', 'Jellyfin for Kodi')}/{self.config.data.get('app.version', '0.0.0')}"
        return {
            "Accept": "application/json",
            "Content-type": content_type,
            "X-Application": app_name,
            "Accept-Charset": "UTF-8,*",
            "Accept-encoding": "gzip",
            "User-Agent": self.config.data['http.user_agent'] or app_name,
            "Authorization": self._get_authenication_header()
        }
