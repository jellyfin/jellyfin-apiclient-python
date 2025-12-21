# -*- coding: utf-8 -*-

#################################################################################################

from .async_http import AsyncHTTP
from .async_runner import AsyncRunner

#################################################################################################

class HTTP:
    """
    Synchronous HTTP adapter that delegates to AsyncHTTP via AsyncRunner.
    """

    def __init__(self, client, async_http=None, runner=None):
        self.client = client
        self.config = client.config
        self._async_http = async_http or AsyncHTTP(client)
        self._runner = runner or getattr(client, "_runner", None) or AsyncRunner()

    @property
    def session(self):
        return self._async_http.session

    @session.setter
    def session(self, value):
        self._async_http.session = value

    @property
    def keep_alive(self):
        return self._async_http.keep_alive

    @keep_alive.setter
    def keep_alive(self, value):
        self._async_http.keep_alive = value

    def start_session(self):
        return self._runner.run(self._async_http.start_session())

    def stop_session(self):
        return self._runner.run(self._async_http.stop_session())

    def request_url(self, data):
        return self._async_http.request_url(data)

    def request(self, data, session=None, dest_file=None):
        return self._runner.run(
            self._async_http.request(data, session=session, dest_file=dest_file)
        )
