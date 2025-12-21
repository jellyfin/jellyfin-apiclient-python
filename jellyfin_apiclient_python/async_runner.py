# -*- coding: utf-8 -*-

import asyncio
import threading


class AsyncRunner:
    """
    Run asyncio coroutines in a dedicated background event loop thread.

    This keeps sync API calls from blocking the caller's thread while reusing
    a single event loop and async HTTP session for connection pooling.
    """

    def __init__(self):
        self._loop = None
        self._thread = None
        self._ready = threading.Event()
        self._closed = False
        self._thread_id = None
        self._start_loop_thread()

    @property
    def thread_id(self):
        return self._thread_id

    def _start_loop_thread(self):
        def _run_loop():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop = loop
            self._thread_id = threading.get_ident()
            self._ready.set()
            loop.run_forever()
            pending = asyncio.all_tasks(loop)
            if pending:
                for task in pending:
                    task.cancel()
                loop.run_until_complete(
                    asyncio.gather(*pending, return_exceptions=True)
                )
            loop.close()

        self._thread = threading.Thread(
            target=_run_loop,
            daemon=True,
            name="JellyfinAsyncRunner",
        )
        self._thread.start()
        self._ready.wait()

    def _raise_if_running_loop(self):
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return
        raise RuntimeError(
            "Sync JellyfinClient methods cannot be called from a running event loop. "
            "Use the async API via client.aio instead."
        )

    def run(self, coro):
        self._raise_if_running_loop()
        if self._closed:
            raise RuntimeError("AsyncRunner is closed.")
        future = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return future.result()

    def close(self):
        if self._closed:
            return
        self._closed = True
        if self._loop is None:
            return
        self._loop.call_soon_threadsafe(self._loop.stop)
        self._thread.join()
