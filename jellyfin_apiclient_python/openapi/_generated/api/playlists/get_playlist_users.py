from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.playlist_user_permissions import PlaylistUserPermissions
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    playlist_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Playlists/{playlist_id}/Users".format(
            playlist_id=playlist_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[PlaylistUserPermissions] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlaylistUserPermissions.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | list[PlaylistUserPermissions]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | list[PlaylistUserPermissions]]:
    """Get a playlist's users.

    Args:
        playlist_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[PlaylistUserPermissions]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | list[PlaylistUserPermissions] | None:
    """Get a playlist's users.

    Args:
        playlist_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[PlaylistUserPermissions]
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | list[PlaylistUserPermissions]]:
    """Get a playlist's users.

    Args:
        playlist_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[PlaylistUserPermissions]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | list[PlaylistUserPermissions] | None:
    """Get a playlist's users.

    Args:
        playlist_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[PlaylistUserPermissions]
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
        )
    ).parsed
