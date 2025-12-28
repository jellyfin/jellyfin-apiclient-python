from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_kind import BaseItemKind
from ...models.media_type import MediaType
from ...models.query_filters_legacy import QueryFiltersLegacy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_parent_id: str | Unset = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parentId"] = json_parent_id

    json_include_item_types: list[str] | Unset = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    json_media_types: list[str] | Unset = UNSET
    if not isinstance(media_types, Unset):
        json_media_types = []
        for media_types_item_data in media_types:
            media_types_item = media_types_item_data.value
            json_media_types.append(media_types_item)

    params["mediaTypes"] = json_media_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/Filters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | QueryFiltersLegacy | None:
    if response.status_code == 200:
        response_200 = QueryFiltersLegacy.from_dict(response.json())

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
) -> Response[Any | QueryFiltersLegacy]:
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
    parent_id: UUID | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
) -> Response[Any | QueryFiltersLegacy]:
    """Gets legacy query filters.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | QueryFiltersLegacy]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        media_types=media_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
) -> Any | QueryFiltersLegacy | None:
    """Gets legacy query filters.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | QueryFiltersLegacy
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        media_types=media_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
) -> Response[Any | QueryFiltersLegacy]:
    """Gets legacy query filters.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | QueryFiltersLegacy]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        media_types=media_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
) -> Any | QueryFiltersLegacy | None:
    """Gets legacy query filters.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | QueryFiltersLegacy
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            include_item_types=include_item_types,
            media_types=media_types,
        )
    ).parsed
