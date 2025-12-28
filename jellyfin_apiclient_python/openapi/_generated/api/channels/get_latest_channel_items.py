from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    channel_ids: list[UUID] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_filters: list[str] | Unset = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_channel_ids: list[str] | Unset = UNSET
    if not isinstance(channel_ids, Unset):
        json_channel_ids = []
        for channel_ids_item_data in channel_ids:
            channel_ids_item = str(channel_ids_item_data)
            json_channel_ids.append(channel_ids_item)

    params["channelIds"] = json_channel_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Channels/Items/Latest",
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
    filters: list[ItemFilter] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    channel_ids: list[UUID] | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets latest channel items.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        filters (list[ItemFilter] | Unset):
        fields (list[ItemFields] | Unset):
        channel_ids (list[UUID] | Unset):

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
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
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
    filters: list[ItemFilter] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    channel_ids: list[UUID] | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets latest channel items.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        filters (list[ItemFilter] | Unset):
        fields (list[ItemFields] | Unset):
        channel_ids (list[UUID] | Unset):

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
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    channel_ids: list[UUID] | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets latest channel items.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        filters (list[ItemFilter] | Unset):
        fields (list[ItemFields] | Unset):
        channel_ids (list[UUID] | Unset):

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
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    channel_ids: list[UUID] | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets latest channel items.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        filters (list[ItemFilter] | Unset):
        fields (list[ItemFields] | Unset):
        channel_ids (list[UUID] | Unset):

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
            filters=filters,
            fields=fields,
            channel_ids=channel_ids,
        )
    ).parsed
