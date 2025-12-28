import datetime
from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.item_sort_by import ItemSortBy
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    min_start_date: datetime.datetime | Unset = UNSET,
    has_aired: bool | Unset = UNSET,
    is_airing: bool | Unset = UNSET,
    max_start_date: datetime.datetime | Unset = UNSET,
    min_end_date: datetime.datetime | Unset = UNSET,
    max_end_date: datetime.datetime | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    library_series_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_channel_ids: list[str] | Unset = UNSET
    if not isinstance(channel_ids, Unset):
        json_channel_ids = []
        for channel_ids_item_data in channel_ids:
            channel_ids_item = str(channel_ids_item_data)
            json_channel_ids.append(channel_ids_item)

    params["channelIds"] = json_channel_ids

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_min_start_date: str | Unset = UNSET
    if not isinstance(min_start_date, Unset):
        json_min_start_date = min_start_date.isoformat()
    params["minStartDate"] = json_min_start_date

    params["hasAired"] = has_aired

    params["isAiring"] = is_airing

    json_max_start_date: str | Unset = UNSET
    if not isinstance(max_start_date, Unset):
        json_max_start_date = max_start_date.isoformat()
    params["maxStartDate"] = json_max_start_date

    json_min_end_date: str | Unset = UNSET
    if not isinstance(min_end_date, Unset):
        json_min_end_date = min_end_date.isoformat()
    params["minEndDate"] = json_min_end_date

    json_max_end_date: str | Unset = UNSET
    if not isinstance(max_end_date, Unset):
        json_max_end_date = max_end_date.isoformat()
    params["maxEndDate"] = json_max_end_date

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["startIndex"] = start_index

    params["limit"] = limit

    json_sort_by: list[str] | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    json_sort_order: list[str] | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    json_genres: list[str] | Unset = UNSET
    if not isinstance(genres, Unset):
        json_genres = genres

    params["genres"] = json_genres

    json_genre_ids: list[str] | Unset = UNSET
    if not isinstance(genre_ids, Unset):
        json_genre_ids = []
        for genre_ids_item_data in genre_ids:
            genre_ids_item = str(genre_ids_item_data)
            json_genre_ids.append(genre_ids_item)

    params["genreIds"] = json_genre_ids

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["enableUserData"] = enable_user_data

    params["seriesTimerId"] = series_timer_id

    json_library_series_id: str | Unset = UNSET
    if not isinstance(library_series_id, Unset):
        json_library_series_id = str(library_series_id)
    params["librarySeriesId"] = json_library_series_id

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Programs",
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
    channel_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    min_start_date: datetime.datetime | Unset = UNSET,
    has_aired: bool | Unset = UNSET,
    is_airing: bool | Unset = UNSET,
    max_start_date: datetime.datetime | Unset = UNSET,
    min_end_date: datetime.datetime | Unset = UNSET,
    max_end_date: datetime.datetime | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    library_series_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets available live tv epgs.

    Args:
        channel_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        min_start_date (datetime.datetime | Unset):
        has_aired (bool | Unset):
        is_airing (bool | Unset):
        max_start_date (datetime.datetime | Unset):
        min_end_date (datetime.datetime | Unset):
        max_end_date (datetime.datetime | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        series_timer_id (str | Unset):
        library_series_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_ids=channel_ids,
        user_id=user_id,
        min_start_date=min_start_date,
        has_aired=has_aired,
        is_airing=is_airing,
        max_start_date=max_start_date,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        start_index=start_index,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        genres=genres,
        genre_ids=genre_ids,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        series_timer_id=series_timer_id,
        library_series_id=library_series_id,
        fields=fields,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    min_start_date: datetime.datetime | Unset = UNSET,
    has_aired: bool | Unset = UNSET,
    is_airing: bool | Unset = UNSET,
    max_start_date: datetime.datetime | Unset = UNSET,
    min_end_date: datetime.datetime | Unset = UNSET,
    max_end_date: datetime.datetime | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    library_series_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets available live tv epgs.

    Args:
        channel_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        min_start_date (datetime.datetime | Unset):
        has_aired (bool | Unset):
        is_airing (bool | Unset):
        max_start_date (datetime.datetime | Unset):
        min_end_date (datetime.datetime | Unset):
        max_end_date (datetime.datetime | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        series_timer_id (str | Unset):
        library_series_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        channel_ids=channel_ids,
        user_id=user_id,
        min_start_date=min_start_date,
        has_aired=has_aired,
        is_airing=is_airing,
        max_start_date=max_start_date,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        start_index=start_index,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        genres=genres,
        genre_ids=genre_ids,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        series_timer_id=series_timer_id,
        library_series_id=library_series_id,
        fields=fields,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    min_start_date: datetime.datetime | Unset = UNSET,
    has_aired: bool | Unset = UNSET,
    is_airing: bool | Unset = UNSET,
    max_start_date: datetime.datetime | Unset = UNSET,
    min_end_date: datetime.datetime | Unset = UNSET,
    max_end_date: datetime.datetime | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    library_series_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets available live tv epgs.

    Args:
        channel_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        min_start_date (datetime.datetime | Unset):
        has_aired (bool | Unset):
        is_airing (bool | Unset):
        max_start_date (datetime.datetime | Unset):
        min_end_date (datetime.datetime | Unset):
        max_end_date (datetime.datetime | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        series_timer_id (str | Unset):
        library_series_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_ids=channel_ids,
        user_id=user_id,
        min_start_date=min_start_date,
        has_aired=has_aired,
        is_airing=is_airing,
        max_start_date=max_start_date,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        start_index=start_index,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        genres=genres,
        genre_ids=genre_ids,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        series_timer_id=series_timer_id,
        library_series_id=library_series_id,
        fields=fields,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    min_start_date: datetime.datetime | Unset = UNSET,
    has_aired: bool | Unset = UNSET,
    is_airing: bool | Unset = UNSET,
    max_start_date: datetime.datetime | Unset = UNSET,
    min_end_date: datetime.datetime | Unset = UNSET,
    max_end_date: datetime.datetime | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    library_series_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets available live tv epgs.

    Args:
        channel_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        min_start_date (datetime.datetime | Unset):
        has_aired (bool | Unset):
        is_airing (bool | Unset):
        max_start_date (datetime.datetime | Unset):
        min_end_date (datetime.datetime | Unset):
        max_end_date (datetime.datetime | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        series_timer_id (str | Unset):
        library_series_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_ids=channel_ids,
            user_id=user_id,
            min_start_date=min_start_date,
            has_aired=has_aired,
            is_airing=is_airing,
            max_start_date=max_start_date,
            min_end_date=min_end_date,
            max_end_date=max_end_date,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            start_index=start_index,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            genres=genres,
            genre_ids=genre_ids,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            series_timer_id=series_timer_id,
            library_series_id=library_series_id,
            fields=fields,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
