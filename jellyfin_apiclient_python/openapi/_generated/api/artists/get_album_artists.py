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
from ...models.item_filter import ItemFilter
from ...models.item_sort_by import ItemSortBy
from ...models.media_type import MediaType
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    min_community_rating: float | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    official_ratings: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    years: list[int] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    person: str | Unset = UNSET,
    person_ids: list[UUID] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    studios: list[str] | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    enable_images: bool | Unset = True,
    enable_total_record_count: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["minCommunityRating"] = min_community_rating

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

    json_filters: list[str] | Unset = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    params["isFavorite"] = is_favorite

    json_media_types: list[str] | Unset = UNSET
    if not isinstance(media_types, Unset):
        json_media_types = []
        for media_types_item_data in media_types:
            media_types_item = media_types_item_data.value
            json_media_types.append(media_types_item)

    params["mediaTypes"] = json_media_types

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

    json_official_ratings: list[str] | Unset = UNSET
    if not isinstance(official_ratings, Unset):
        json_official_ratings = official_ratings

    params["officialRatings"] = json_official_ratings

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_years: list[int] | Unset = UNSET
    if not isinstance(years, Unset):
        json_years = years

    params["years"] = json_years

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["person"] = person

    json_person_ids: list[str] | Unset = UNSET
    if not isinstance(person_ids, Unset):
        json_person_ids = []
        for person_ids_item_data in person_ids:
            person_ids_item = str(person_ids_item_data)
            json_person_ids.append(person_ids_item)

    params["personIds"] = json_person_ids

    json_person_types: list[str] | Unset = UNSET
    if not isinstance(person_types, Unset):
        json_person_types = person_types

    params["personTypes"] = json_person_types

    json_studios: list[str] | Unset = UNSET
    if not isinstance(studios, Unset):
        json_studios = studios

    params["studios"] = json_studios

    json_studio_ids: list[str] | Unset = UNSET
    if not isinstance(studio_ids, Unset):
        json_studio_ids = []
        for studio_ids_item_data in studio_ids:
            studio_ids_item = str(studio_ids_item_data)
            json_studio_ids.append(studio_ids_item)

    params["studioIds"] = json_studio_ids

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

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

    params["enableImages"] = enable_images

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Artists/AlbumArtists",
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
    min_community_rating: float | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    official_ratings: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    years: list[int] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    person: str | Unset = UNSET,
    person_ids: list[UUID] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    studios: list[str] | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    enable_images: bool | Unset = True,
    enable_total_record_count: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets all album artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (float | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        official_ratings (list[str] | Unset):
        tags (list[str] | Unset):
        years (list[int] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        person (str | Unset):
        person_ids (list[UUID] | Unset):
        person_types (list[str] | Unset):
        studios (list[str] | Unset):
        studio_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        enable_images (bool | Unset):  Default: True.
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        min_community_rating=min_community_rating,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        genres=genres,
        genre_ids=genre_ids,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        studio_ids=studio_ids,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    min_community_rating: float | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    official_ratings: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    years: list[int] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    person: str | Unset = UNSET,
    person_ids: list[UUID] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    studios: list[str] | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    enable_images: bool | Unset = True,
    enable_total_record_count: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets all album artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (float | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        official_ratings (list[str] | Unset):
        tags (list[str] | Unset):
        years (list[int] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        person (str | Unset):
        person_ids (list[UUID] | Unset):
        person_types (list[str] | Unset):
        studios (list[str] | Unset):
        studio_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        enable_images (bool | Unset):  Default: True.
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        min_community_rating=min_community_rating,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        genres=genres,
        genre_ids=genre_ids,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        studio_ids=studio_ids,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    min_community_rating: float | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    official_ratings: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    years: list[int] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    person: str | Unset = UNSET,
    person_ids: list[UUID] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    studios: list[str] | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    enable_images: bool | Unset = True,
    enable_total_record_count: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets all album artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (float | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        official_ratings (list[str] | Unset):
        tags (list[str] | Unset):
        years (list[int] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        person (str | Unset):
        person_ids (list[UUID] | Unset):
        person_types (list[str] | Unset):
        studios (list[str] | Unset):
        studio_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        enable_images (bool | Unset):  Default: True.
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        min_community_rating=min_community_rating,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        genres=genres,
        genre_ids=genre_ids,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        studio_ids=studio_ids,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    min_community_rating: float | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    official_ratings: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    years: list[int] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    person: str | Unset = UNSET,
    person_ids: list[UUID] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    studios: list[str] | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    enable_images: bool | Unset = True,
    enable_total_record_count: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets all album artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (float | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        search_term (str | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        genres (list[str] | Unset):
        genre_ids (list[UUID] | Unset):
        official_ratings (list[str] | Unset):
        tags (list[str] | Unset):
        years (list[int] | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        person (str | Unset):
        person_ids (list[UUID] | Unset):
        person_types (list[str] | Unset):
        studios (list[str] | Unset):
        studio_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):
        enable_images (bool | Unset):  Default: True.
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
            min_community_rating=min_community_rating,
            start_index=start_index,
            limit=limit,
            search_term=search_term,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            include_item_types=include_item_types,
            filters=filters,
            is_favorite=is_favorite,
            media_types=media_types,
            genres=genres,
            genre_ids=genre_ids,
            official_ratings=official_ratings,
            tags=tags,
            years=years,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            person=person,
            person_ids=person_ids,
            person_types=person_types,
            studios=studios,
            studio_ids=studio_ids,
            user_id=user_id,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            sort_by=sort_by,
            sort_order=sort_order,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
