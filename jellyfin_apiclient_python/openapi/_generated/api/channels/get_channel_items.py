from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...models.item_sort_by import ItemSortBy
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: UUID,
    *,
    folder_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_folder_id: str | Unset = UNSET
    if not isinstance(folder_id, Unset):
        json_folder_id = str(folder_id)
    params["folderId"] = json_folder_id

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_sort_order: list[str] | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    json_filters: list[str] | Unset = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    json_sort_by: list[str] | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Channels/{channel_id}/Items".format(
            channel_id=channel_id,
        ),
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
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (UUID | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_order (list[SortOrder] | Unset):
        filters (list[ItemFilter] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (UUID | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_order (list[SortOrder] | Unset):
        filters (list[ItemFilter] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (UUID | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_order (list[SortOrder] | Unset):
        filters (list[ItemFilter] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (UUID | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_order (list[SortOrder] | Unset):
        filters (list[ItemFilter] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            folder_id=folder_id,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            sort_order=sort_order,
            filters=filters,
            sort_by=sort_by,
            fields=fields,
        )
    ).parsed
