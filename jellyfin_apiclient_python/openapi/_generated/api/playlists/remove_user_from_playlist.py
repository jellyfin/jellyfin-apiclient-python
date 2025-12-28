from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    playlist_id: UUID,
    user_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/Playlists/{playlist_id}/Users/{user_id}".format(
            playlist_id=playlist_id,
            user_id=user_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails]:
    """Remove a user from a playlist's users.

    Args:
        playlist_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | None:
    """Remove a user from a playlist's users.

    Args:
        playlist_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        playlist_id=playlist_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails]:
    """Remove a user from a playlist's users.

    Args:
        playlist_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | None:
    """Remove a user from a playlist's users.

    Args:
        playlist_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
