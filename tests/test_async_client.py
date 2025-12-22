import asyncio
import io

from jellyfin_apiclient_python.httpx_compat import httpx
import pytest

from jellyfin_apiclient_python.client import AsyncJellyfinClient, JellyfinClient


def _mock_transport():
    def handler(request):
        return httpx.Response(
            200,
            json={"Name": "Jellyfin"},
            headers={"Date": "Mon, 01 Jan 2024 00:00:00 GMT"},
        )

    return httpx.MockTransport(handler)


def _configure_client(client):
    client.config.data["auth.server"] = "https://example.com"
    client.config.data["auth.token"] = "token"


def test_async_api_returns_payload():
    async_client = AsyncJellyfinClient()
    _configure_client(async_client)
    async_client.http.keep_alive = True
    async_client.http.session = httpx.AsyncClient(transport=_mock_transport())

    async def run():
        response = await async_client.jellyfin.get_system_info()
        assert response == {"Name": "Jellyfin"}
        await async_client.aclose()

    asyncio.run(run())


def test_sync_api_reuses_runner_thread():
    client = JellyfinClient()
    _configure_client(client)
    client.aio.http.keep_alive = True
    client.aio.http.session = httpx.AsyncClient(transport=_mock_transport())
    thread_id = client._runner.thread_id

    first = client.jellyfin.get_system_info()
    second = client.jellyfin.get_system_info()

    assert first == {"Name": "Jellyfin"}
    assert second == {"Name": "Jellyfin"}
    assert client._runner.thread_id == thread_id
    client.close()


def test_sync_api_called_from_event_loop_raises():
    client = JellyfinClient()
    _configure_client(client)
    client.aio.http.keep_alive = True
    client.aio.http.session = httpx.AsyncClient(transport=_mock_transport())

    async def run():
        with pytest.raises(RuntimeError, match="async API"):
            client.jellyfin.get_system_info()

    asyncio.run(run())
    client.close()


def test_async_stream_writes_bytes_and_closes_session():
    # This covers the streaming path to ensure we do not attempt JSON parsing,
    # and that keep-alive disabled sessions are still closed after a request.
    async_client = AsyncJellyfinClient()
    _configure_client(async_client)
    async_client.http.keep_alive = False
    async_client.http.session = httpx.AsyncClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                200,
                content=b"jellyfin-stream",
                headers={"Date": "Mon, 01 Jan 2024 00:00:00 GMT"},
            )
        )
    )
    buffer = io.BytesIO()

    async def run():
        await async_client.http.request(
            {"type": "GET", "url": "https://example.com/stream"},
            dest_file=buffer,
        )

    asyncio.run(run())

    assert buffer.getvalue() == b"jellyfin-stream"
    assert async_client.http.session is None


def test_async_keep_alive_retains_session_for_multiple_requests():
    # This ensures keep-alive preserves the shared async session across calls.
    async_client = AsyncJellyfinClient()
    _configure_client(async_client)
    async_client.http.keep_alive = True
    async_client.http.session = httpx.AsyncClient(transport=_mock_transport())
    session_id = id(async_client.http.session)

    async def run():
        first = await async_client.jellyfin.get_system_info()
        second = await async_client.jellyfin.get_system_info()
        return first, second

    first, second = asyncio.run(run())

    assert first == {"Name": "Jellyfin"}
    assert second == {"Name": "Jellyfin"}
    assert async_client.http.session is not None
    assert id(async_client.http.session) == session_id
    asyncio.run(async_client.aclose())
