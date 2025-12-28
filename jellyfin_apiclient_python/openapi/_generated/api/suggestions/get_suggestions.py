from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...models.media_type import MediaType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    media_type: list[MediaType] | Unset = UNSET,
    type_: list[BaseItemKind] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    enable_total_record_count: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_media_type: list[str] | Unset = UNSET
    if not isinstance(media_type, Unset):
        json_media_type = []
        for media_type_item_data in media_type:
            media_type_item = media_type_item_data.value
            json_media_type.append(media_type_item)

    params["mediaType"] = json_media_type

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["startIndex"] = start_index

    params["limit"] = limit

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/Suggestions",
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
    media_type: list[MediaType] | Unset = UNSET,
    type_: list[BaseItemKind] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    enable_total_record_count: bool | Unset = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets suggestions.

    Args:
        user_id (UUID | Unset):
        media_type (list[MediaType] | Unset):
        type_ (list[BaseItemKind] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        enable_total_record_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type_=type_,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    media_type: list[MediaType] | Unset = UNSET,
    type_: list[BaseItemKind] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    enable_total_record_count: bool | Unset = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets suggestions.

    Args:
        user_id (UUID | Unset):
        media_type (list[MediaType] | Unset):
        type_ (list[BaseItemKind] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        enable_total_record_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        media_type=media_type,
        type_=type_,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    media_type: list[MediaType] | Unset = UNSET,
    type_: list[BaseItemKind] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    enable_total_record_count: bool | Unset = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets suggestions.

    Args:
        user_id (UUID | Unset):
        media_type (list[MediaType] | Unset):
        type_ (list[BaseItemKind] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        enable_total_record_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type_=type_,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    media_type: list[MediaType] | Unset = UNSET,
    type_: list[BaseItemKind] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    enable_total_record_count: bool | Unset = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets suggestions.

    Args:
        user_id (UUID | Unset):
        media_type (list[MediaType] | Unset):
        type_ (list[BaseItemKind] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        enable_total_record_count (bool | Unset):  Default: False.

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
            media_type=media_type,
            type_=type_,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
