from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.media_type import MediaType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
    exclude_active_sessions: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    params["searchTerm"] = search_term

    json_parent_id: str | Unset = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parentId"] = json_parent_id

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_media_types: list[str] | Unset = UNSET
    if not isinstance(media_types, Unset):
        json_media_types = []
        for media_types_item_data in media_types:
            media_types_item = media_types_item_data.value
            json_media_types.append(media_types_item)

    params["mediaTypes"] = json_media_types

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    json_exclude_item_types: list[str] | Unset = UNSET
    if not isinstance(exclude_item_types, Unset):
        json_exclude_item_types = []
        for exclude_item_types_item_data in exclude_item_types:
            exclude_item_types_item = exclude_item_types_item_data.value
            json_exclude_item_types.append(exclude_item_types_item)

    params["excludeItemTypes"] = json_exclude_item_types

    json_include_item_types: list[str] | Unset = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    params["enableTotalRecordCount"] = enable_total_record_count

    params["enableImages"] = enable_images

    params["excludeActiveSessions"] = exclude_active_sessions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/UserItems/Resume",
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
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
    exclude_active_sessions: bool | Unset = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        media_types (list[MediaType] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.
        exclude_active_sessions (bool | Unset):  Default: False.

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
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        media_types=media_types,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
        exclude_active_sessions=exclude_active_sessions,
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
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
    exclude_active_sessions: bool | Unset = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        media_types (list[MediaType] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.
        exclude_active_sessions (bool | Unset):  Default: False.

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
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        media_types=media_types,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
        exclude_active_sessions=exclude_active_sessions,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
    exclude_active_sessions: bool | Unset = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        media_types (list[MediaType] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.
        exclude_active_sessions (bool | Unset):  Default: False.

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
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        media_types=media_types,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
        exclude_active_sessions=exclude_active_sessions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
    exclude_active_sessions: bool | Unset = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        media_types (list[MediaType] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.
        exclude_active_sessions (bool | Unset):  Default: False.

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
            search_term=search_term,
            parent_id=parent_id,
            fields=fields,
            media_types=media_types,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            exclude_item_types=exclude_item_types,
            include_item_types=include_item_types,
            enable_total_record_count=enable_total_record_count,
            enable_images=enable_images,
            exclude_active_sessions=exclude_active_sessions,
        )
    ).parsed
