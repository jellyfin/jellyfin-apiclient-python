from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    supports_latest_items: bool | Unset = UNSET,
    supports_media_deletion: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    params["supportsLatestItems"] = supports_latest_items

    params["supportsMediaDeletion"] = supports_media_deletion

    params["isFavorite"] = is_favorite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Channels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BaseItemDtoQueryResult | None:
    if response.status_code == 200:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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
) -> Response[Any | BaseItemDtoQueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    supports_latest_items: bool | Unset = UNSET,
    supports_media_deletion: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets available channels.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        supports_latest_items (bool | Unset):
        supports_media_deletion (bool | Unset):
        is_favorite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        supports_latest_items=supports_latest_items,
        supports_media_deletion=supports_media_deletion,
        is_favorite=is_favorite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    supports_latest_items: bool | Unset = UNSET,
    supports_media_deletion: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets available channels.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        supports_latest_items (bool | Unset):
        supports_media_deletion (bool | Unset):
        is_favorite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        supports_latest_items=supports_latest_items,
        supports_media_deletion=supports_media_deletion,
        is_favorite=is_favorite,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    supports_latest_items: bool | Unset = UNSET,
    supports_media_deletion: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets available channels.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        supports_latest_items (bool | Unset):
        supports_media_deletion (bool | Unset):
        is_favorite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        supports_latest_items=supports_latest_items,
        supports_media_deletion=supports_media_deletion,
        is_favorite=is_favorite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    supports_latest_items: bool | Unset = UNSET,
    supports_media_deletion: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets available channels.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        supports_latest_items (bool | Unset):
        supports_media_deletion (bool | Unset):
        is_favorite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            supports_latest_items=supports_latest_items,
            supports_media_deletion=supports_media_deletion,
            is_favorite=is_favorite,
        )
    ).parsed
