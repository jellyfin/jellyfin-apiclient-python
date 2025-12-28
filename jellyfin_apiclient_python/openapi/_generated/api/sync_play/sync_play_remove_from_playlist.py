from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto
from ...types import Response


def _get_kwargs(
    *,
    body: RemoveFromPlaylistRequestDto | RemoveFromPlaylistRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/SyncPlay/RemoveFromPlaylist",
    }

    if isinstance(body, RemoveFromPlaylistRequestDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RemoveFromPlaylistRequestDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 503:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RemoveFromPlaylistRequestDto | RemoveFromPlaylistRequestDto,
) -> Response[Any]:
    """Request to remove items from the playlist in SyncPlay group.

    Args:
        body (RemoveFromPlaylistRequestDto): Class RemoveFromPlaylistRequestDto.
        body (RemoveFromPlaylistRequestDto): Class RemoveFromPlaylistRequestDto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RemoveFromPlaylistRequestDto | RemoveFromPlaylistRequestDto,
) -> Response[Any]:
    """Request to remove items from the playlist in SyncPlay group.

    Args:
        body (RemoveFromPlaylistRequestDto): Class RemoveFromPlaylistRequestDto.
        body (RemoveFromPlaylistRequestDto): Class RemoveFromPlaylistRequestDto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
