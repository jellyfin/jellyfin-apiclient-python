# -*- coding: utf-8 -*-

#################################################################################################

import json
import logging
import time
import urllib

import requests

from .exceptions import HTTPException

#################################################################################################

LOG = logging.getLogger('Jellyfin.' + __name__)

#################################################################################################


class HTTP(object):

    session = None
    keep_alive = False

    def __init__(self, client):

        self.client = client
        self.config = client.config

    def start_session(self):
        self.session = requests.Session()

        max_retries = self.config.data['http.max_retries']

        # Configure the session for tls client authentication
        if 'auth.tls_client_cert' in self.client.config.data and 'auth.tls_client_key' in self.client.config.data:
            self.session.cert = (self.client.config.data['auth.tls_client_cert'],
                                 self.client.config.data['auth.tls_client_key'])

            if self.client.config.data['auth.tls_server_ca']:
                self.session.verify = self.client.config.data['auth.tls_server_ca']

        self.session.mount("http://", requests.adapters.HTTPAdapter(max_retries=max_retries))
        self.session.mount("https://", requests.adapters.HTTPAdapter(max_retries=max_retries))

    def stop_session(self):

        if self.session is None:
            return

        try:
            LOG.info("--<[ session/%s ]", id(self.session))
            self.session.close()
        except Exception as error:
            LOG.warning("The requests session could not be terminated: %s", error)

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

    def request(self, data, session=None, dest_file=None):

        ''' Give a chance to retry the connection. Jellyfin sometimes can be slow to answer back
            data dictionary can contain:
            type: GET, POST, etc.
            url: (optional)
            handler: not considered when url is provided (optional)
            params: request parameters (optional)
            json: request body (optional)
            headers: (optional),
            verify: ssl certificate, True (verify using device built-in library) or False
        '''
        if not data:
            raise AttributeError("Request cannot be empty")

        data = self._request(data)
        LOG.debug("--->[ http ] %s", json.dumps(data, indent=4))
        retry = data.pop('retry', 5)
        stream = dest_file is not None

        while True:

            try:
                r = self._requests(session or self.session or requests, data.pop('type', "GET"), **data, stream=stream)
                if stream:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk: # filter out keep-alive new chunks
                            dest_file.write(chunk)
                else:
                    r.content  # release the connection

                if not self.keep_alive and self.session is not None:
                    self.stop_session()

                r.raise_for_status()

            except requests.exceptions.ConnectionError as error:
                if retry:

                    retry -= 1
                    time.sleep(1)

                    continue

                LOG.error(error)
                self.client.callback("ServerUnreachable", {'ServerId': self.config.data['auth.server-id']})

                raise HTTPException("ServerUnreachable", error)

            except requests.exceptions.ReadTimeout as error:
                if retry:

                    retry -= 1
                    time.sleep(1)

                    continue

                LOG.error(error)

                raise HTTPException("ReadTimeout", error)

            except requests.exceptions.HTTPError as error:
                LOG.error(error)

                if r.status_code == 401:

                    if 'X-Application-Error-Code' in r.headers:
                        self.client.callback("AccessRestricted", {'ServerId': self.config.data['auth.server-id']})

                        raise HTTPException("AccessRestricted", error)
                    else:
                        self.client.callback("Unauthorized", {'ServerId': self.config.data['auth.server-id']})
                        self.client.auth.revoke_token()

                        raise HTTPException("Unauthorized", error)

                elif r.status_code == 500:  # log and ignore.
                    LOG.error("--[ 500 response ] %s", error)

                    return

                elif r.status_code == 502:
                    if retry:

                        retry -= 1
                        time.sleep(1)

                        continue

                raise HTTPException(r.status_code, error)

            except requests.exceptions.MissingSchema as error:
                LOG.error("Request missing Schema. " + str(error))
                raise HTTPException("MissingSchema", {'Id': self.config.data.get('auth.server', "None")})

            except Exception:
                raise

            else:
                try:
                    if stream:
                        return
                    self.config.data['server-time'] = r.headers['Date']
                    elapsed = int(r.elapsed.total_seconds() * 1000)
                    response = r.json()
                    LOG.debug("---<[ http ][%s ms]", elapsed)
                    LOG.debug(json.dumps(response, indent=4))

                    return response
                except ValueError:
                    return

    def _request(self, data):

        if 'url' not in data:
            data['url'] = "%s/%s" % (self.config.data.get("auth.server", ""), data.pop('handler', ""))

        data['headers'] = self._get_default_headers()
        data['timeout'] = data.get('timeout') or self.config.data['http.timeout']
        data['verify'] = data.get('verify') or self.config.data.get('auth.ssl', False)
        data['url'] = self._replace_user_info(data['url'])
        self._process_params(data.get('params') or {})
        self._process_params(data.get('json') or {})

        return data

    def _process_params(self, params):

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

    def _requests(self, session, action, **kwargs):

        if action == "GET":
            return session.get(**kwargs)
        elif action == "POST":
            return session.post(**kwargs)
        elif action == "HEAD":
            return session.head(**kwargs)
        elif action == "DELETE":
            return session.delete(**kwargs)
