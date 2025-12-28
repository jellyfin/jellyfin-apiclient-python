from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.channel_type import ChannelType
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.item_sort_by import ItemSortBy
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: ChannelType | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_liked: bool | Unset = UNSET,
    is_disliked: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
    enable_favorite_sorting: bool | Unset = False,
    add_current_program: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["limit"] = limit

    params["isFavorite"] = is_favorite

    params["isLiked"] = is_liked

    params["isDisliked"] = is_disliked

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["enableUserData"] = enable_user_data

    json_sort_by: list[str] | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["enableFavoriteSorting"] = enable_favorite_sorting

    params["addCurrentProgram"] = add_current_program

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Channels",
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
    type_: ChannelType | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_liked: bool | Unset = UNSET,
    is_disliked: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
    enable_favorite_sorting: bool | Unset = False,
    add_current_program: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets available live tv channels.

    Args:
        type_ (ChannelType | Unset): Enum ChannelType.
        user_id (UUID | Unset):
        start_index (int | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        limit (int | Unset):
        is_favorite (bool | Unset):
        is_liked (bool | Unset):
        is_disliked (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.
        enable_favorite_sorting (bool | Unset):  Default: False.
        add_current_program (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        type_=type_,
        user_id=user_id,
        start_index=start_index,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        limit=limit,
        is_favorite=is_favorite,
        is_liked=is_liked,
        is_disliked=is_disliked,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_favorite_sorting=enable_favorite_sorting,
        add_current_program=add_current_program,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: ChannelType | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_liked: bool | Unset = UNSET,
    is_disliked: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
    enable_favorite_sorting: bool | Unset = False,
    add_current_program: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets available live tv channels.

    Args:
        type_ (ChannelType | Unset): Enum ChannelType.
        user_id (UUID | Unset):
        start_index (int | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        limit (int | Unset):
        is_favorite (bool | Unset):
        is_liked (bool | Unset):
        is_disliked (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.
        enable_favorite_sorting (bool | Unset):  Default: False.
        add_current_program (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        type_=type_,
        user_id=user_id,
        start_index=start_index,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        limit=limit,
        is_favorite=is_favorite,
        is_liked=is_liked,
        is_disliked=is_disliked,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_favorite_sorting=enable_favorite_sorting,
        add_current_program=add_current_program,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: ChannelType | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_liked: bool | Unset = UNSET,
    is_disliked: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
    enable_favorite_sorting: bool | Unset = False,
    add_current_program: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets available live tv channels.

    Args:
        type_ (ChannelType | Unset): Enum ChannelType.
        user_id (UUID | Unset):
        start_index (int | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        limit (int | Unset):
        is_favorite (bool | Unset):
        is_liked (bool | Unset):
        is_disliked (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.
        enable_favorite_sorting (bool | Unset):  Default: False.
        add_current_program (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        type_=type_,
        user_id=user_id,
        start_index=start_index,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        limit=limit,
        is_favorite=is_favorite,
        is_liked=is_liked,
        is_disliked=is_disliked,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_favorite_sorting=enable_favorite_sorting,
        add_current_program=add_current_program,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: ChannelType | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_liked: bool | Unset = UNSET,
    is_disliked: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
    enable_favorite_sorting: bool | Unset = False,
    add_current_program: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets available live tv channels.

    Args:
        type_ (ChannelType | Unset): Enum ChannelType.
        user_id (UUID | Unset):
        start_index (int | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        limit (int | Unset):
        is_favorite (bool | Unset):
        is_liked (bool | Unset):
        is_disliked (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.
        enable_favorite_sorting (bool | Unset):  Default: False.
        add_current_program (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            user_id=user_id,
            start_index=start_index,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            limit=limit,
            is_favorite=is_favorite,
            is_liked=is_liked,
            is_disliked=is_disliked,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            fields=fields,
            enable_user_data=enable_user_data,
            sort_by=sort_by,
            sort_order=sort_order,
            enable_favorite_sorting=enable_favorite_sorting,
            add_current_program=add_current_program,
        )
    ).parsed
