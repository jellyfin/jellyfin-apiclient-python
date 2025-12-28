from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.playback_info_response import PlaybackInfoResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    user_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/{item_id}/PlaybackInfo".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PlaybackInfoResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PlaybackInfoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
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
) -> Response[Any | PlaybackInfoResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | PlaybackInfoResponse | ProblemDetails]:
    """Gets live playback media info for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaybackInfoResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Any | PlaybackInfoResponse | ProblemDetails | None:
    """Gets live playback media info for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaybackInfoResponse | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | PlaybackInfoResponse | ProblemDetails]:
    """Gets live playback media info for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaybackInfoResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Any | PlaybackInfoResponse | ProblemDetails | None:
    """Gets live playback media info for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaybackInfoResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
