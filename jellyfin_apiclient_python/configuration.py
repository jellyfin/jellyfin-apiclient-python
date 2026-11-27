# -*- coding: utf-8 -*-

''' This will hold all configs from the client.
    Configuration set here will be used for the HTTP client.
'''

#################################################################################################

import logging
from urllib.parse import quote

#################################################################################################

DEFAULT_HTTP_MAX_RETRIES = 3
DEFAULT_HTTP_TIMEOUT = 30
LOG = logging.getLogger('JELLYFIN.' + __name__)

#################################################################################################


def authorization_header(data):
    """Build the MediaBrowser authorization header for HTTP and WebSocket."""
    params = {}
    if "app.device_name" in data:
        params = {
            "Client": data["app.name"],
            "Device": data["app.device_name"],
            "DeviceId": data["app.device_id"],
            "Version": data["app.version"],
        }
    if "auth.token" in data:
        params["Token"] = data["auth.token"]
    # Jellyfin URL-decodes the values after splitting the header into fields.
    param_line = ", ".join(
        f'{key}="{quote(str(value), safe="")}"' for key, value in params.items()
    )
    return f"MediaBrowser {param_line}"


def tls_verify(data):
    """The ``verify`` value for requests and the websocket.

    Certificates are verified unless ``auth.ssl`` is explicitly ``False``,
    against ``auth.tls_server_ca`` when it is set.
    """
    if data.get('auth.ssl') is False:
        return False
    return data.get('auth.tls_server_ca') or True


class Config(object):

    def __init__(self):

        LOG.debug("Configuration initializing...")
        self.data = {}
        self.http()

    def app(self, name, version, device_name, device_id, capabilities=None, device_pixel_ratio=None):
        
        LOG.debug("Begin app constructor.")
        self.data['app.name'] = name
        self.data['app.version'] = version
        self.data['app.device_name'] = device_name
        self.data['app.device_id'] = device_id
        self.data['app.capabilities'] = capabilities
        self.data['app.device_pixel_ratio'] = device_pixel_ratio
        self.data['app.default'] = False

    def auth(self, server, user_id, token=None, ssl=None):
        
        LOG.debug("Begin auth constructor.")
        self.data['auth.server'] = server
        self.data['auth.user_id'] = user_id
        self.data['auth.token'] = token
        self.data['auth.ssl'] = ssl

    def http(self, user_agent=None, max_retries=DEFAULT_HTTP_MAX_RETRIES, timeout=DEFAULT_HTTP_TIMEOUT):
        
        LOG.debug("Begin http constructor.")
        self.data['http.max_retries'] = max_retries
        self.data['http.timeout'] = timeout
        self.data['http.user_agent'] = user_agent
