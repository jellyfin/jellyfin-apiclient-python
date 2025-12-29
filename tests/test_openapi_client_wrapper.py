import inspect
import uuid

import httpx
import pytest
import respx

from jellyfin_apiclient_python.openapi.client import EndpointProxy, Jellyfin


@respx.mock
def test_login_with_ephemeral_password_and_authenticated_request() -> None:
    base_url = "http://example.com"
    user_id = str(uuid.uuid4())

    auth_route = respx.post(f"{base_url}/Users/AuthenticateByName").mock(
        return_value=httpx.Response(
            status_code=200,
            json={
                "AccessToken": "token-123",
                "User": {"Id": user_id, "Name": "alice"},
            },
        )
    )
    system_route = respx.get(f"{base_url}/System/Info").mock(
        return_value=httpx.Response(
            status_code=200,
            json={
                "ServerName": "jf",
                "Version": "10.9.0",
            },
        )
    )

    jf = Jellyfin(base_url=base_url, username="alice")
    jf.login(password="super-secret")

    assert auth_route.called, "Login should call the auth endpoint"
    assert jf._password is None  # ephemeral password is not persisted
    assert str(jf.user_id) == user_id
    assert jf.username == "alice"

    resp = jf.api.system.get_system_info()

    assert resp.status_code == 200
    assert system_route.called
    request = system_route.calls.last.request
    assert request.headers["X-Emby-Token"] == "token-123"
    assert resp.parsed.server_name == "jf"


def test_login_with_token_configures_headers_and_proxy_signature() -> None:
    jf = Jellyfin(base_url="http://example.com")
    jf.login_with_token("token-abc")

    # The generated client should be configured with the Jellyfin token header (no bearer prefix).
    httpx_client = jf.client.get_httpx_client()
    assert httpx_client.headers["X-Emby-Token"] == "token-abc"
    assert "Authorization" not in httpx_client.headers

    proxy = jf.api.system.get_system_info
    assert isinstance(proxy, EndpointProxy)
    sig = inspect.signature(proxy)
    assert "client" not in sig.parameters


def test_api_mounting_can_be_disabled() -> None:
    jf = Jellyfin(base_url="http://example.com", mount_api=False)

    with pytest.raises(AttributeError):
        _ = jf.api.system

    jf._mount_generated_api()
    assert isinstance(jf.api.system.get_system_info, EndpointProxy)


@pytest.mark.asyncio
@respx.mock
async def test_async_endpoint_proxy_uses_client_and_parses_response() -> None:
    base_url = "http://example.com"
    system_route = respx.get(f"{base_url}/System/Info").mock(
        return_value=httpx.Response(
            status_code=200,
            json={
                "ServerName": "jf-async",
                "Version": "10.9.1",
            },
        )
    )

    jf = Jellyfin(base_url=base_url)
    jf.login_with_token("async-token")

    resp = await jf.api.system.get_system_info.asyncio_detailed()

    assert resp.status_code == 200
    assert system_route.called
    request = system_route.calls.last.request
    assert request.headers["X-Emby-Token"] == "async-token"
    assert resp.parsed.server_name == "jf-async"


@respx.mock
def test_list_media_folders_includes_token_and_parses_items() -> None:
    base_url = "http://example.com"
    folders_route = respx.get(f"{base_url}/Library/MediaFolders").mock(
        return_value=httpx.Response(
            status_code=200,
            json={
                "Items": [
                    {"Id": str(uuid.uuid4()), "Name": "Movies"},
                    {"Id": str(uuid.uuid4()), "Name": "Shows"},
                ],
                "TotalRecordCount": 2,
                "StartIndex": 0,
            },
        )
    )

    jf = Jellyfin(base_url=base_url)
    jf.login_with_token("media-token")

    resp = jf.api.library.get_media_folders(is_hidden=True)

    assert resp.status_code == 200
    assert folders_route.called
    request = folders_route.calls.last.request
    assert request.headers["X-Emby-Token"] == "media-token"
    # Query parameter was passed through (capitalization handled by httpx).
    assert request.url.params["isHidden"] == "true"

    items = resp.parsed.items
    assert [item.name for item in items] == ["Movies", "Shows"]
