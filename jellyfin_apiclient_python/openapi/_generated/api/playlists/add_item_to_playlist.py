from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: UUID,
    *,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = []
        for ids_item_data in ids:
            ids_item = str(ids_item_data)
            json_ids.append(ids_item)

    params["ids"] = json_ids

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Playlists/{playlist_id}/Items".format(
            playlist_id=playlist_id,
        ),
        "params": params,
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
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Adds items to a playlist.

    Args:
        playlist_id (UUID):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        ids=ids,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Adds items to a playlist.

    Args:
        playlist_id (UUID):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        ids=ids,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Adds items to a playlist.

    Args:
        playlist_id (UUID):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        ids=ids,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Adds items to a playlist.

    Args:
        playlist_id (UUID):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            ids=ids,
            user_id=user_id,
        )
    ).parsed
