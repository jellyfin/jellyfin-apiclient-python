from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_playlist_item_request_dto import SetPlaylistItemRequestDto
from ...types import Response


def _get_kwargs(
    *,
    body: SetPlaylistItemRequestDto | SetPlaylistItemRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/SyncPlay/SetPlaylistItem",
    }

    if isinstance(body, SetPlaylistItemRequestDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SetPlaylistItemRequestDto):
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
    body: SetPlaylistItemRequestDto | SetPlaylistItemRequestDto,
) -> Response[Any]:
    """Request to change playlist item in SyncPlay group.

    Args:
        body (SetPlaylistItemRequestDto): Class SetPlaylistItemRequestDto.
        body (SetPlaylistItemRequestDto): Class SetPlaylistItemRequestDto.

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
    body: SetPlaylistItemRequestDto | SetPlaylistItemRequestDto,
) -> Response[Any]:
    """Request to change playlist item in SyncPlay group.

    Args:
        body (SetPlaylistItemRequestDto): Class SetPlaylistItemRequestDto.
        body (SetPlaylistItemRequestDto): Class SetPlaylistItemRequestDto.

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
