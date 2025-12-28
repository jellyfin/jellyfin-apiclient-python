from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto import BaseItemDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    genre_name: str,
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
        "url": "/Genres/{genre_name}".format(
            genre_name=genre_name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BaseItemDto | None:
    if response.status_code == 200:
        response_200 = BaseItemDto.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BaseItemDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    genre_name: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | BaseItemDto]:
    """Gets a genre, by name.

    Args:
        genre_name (str):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDto]
    """

    kwargs = _get_kwargs(
        genre_name=genre_name,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    genre_name: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Any | BaseItemDto | None:
    """Gets a genre, by name.

    Args:
        genre_name (str):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDto
    """

    return sync_detailed(
        genre_name=genre_name,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    genre_name: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | BaseItemDto]:
    """Gets a genre, by name.

    Args:
        genre_name (str):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDto]
    """

    kwargs = _get_kwargs(
        genre_name=genre_name,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    genre_name: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
) -> Any | BaseItemDto | None:
    """Gets a genre, by name.

    Args:
        genre_name (str):
        user_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDto
    """

    return (
        await asyncio_detailed(
            genre_name=genre_name,
            client=client,
            user_id=user_id,
        )
    ).parsed
