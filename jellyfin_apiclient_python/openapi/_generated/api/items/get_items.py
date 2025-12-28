import datetime
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
from ...models.location_type import LocationType
from ...models.media_type import MediaType
from ...models.series_status import SeriesStatus
from ...models.sort_order import SortOrder
from ...models.video_type import VideoType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    max_official_rating: str | Unset = UNSET,
    has_theme_song: bool | Unset = UNSET,
    has_theme_video: bool | Unset = UNSET,
    has_subtitles: bool | Unset = UNSET,
    has_special_feature: bool | Unset = UNSET,
    has_trailer: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    index_number: int | Unset = UNSET,
    parent_index_number: int | Unset = UNSET,
    has_parental_rating: bool | Unset = UNSET,
    is_hd: bool | Unset = UNSET,
    is_4k: bool | Unset = UNSET,
    location_types: list[LocationType] | Unset = UNSET,
    exclude_location_types: list[LocationType] | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    is_unaired: bool | Unset = UNSET,
    min_community_rating: float | Unset = UNSET,
    min_critic_rating: float | Unset = UNSET,
    min_premiere_date: datetime.datetime | Unset = UNSET,
    min_date_last_saved: datetime.datetime | Unset = UNSET,
    min_date_last_saved_for_user: datetime.datetime | Unset = UNSET,
    max_premiere_date: datetime.datetime | Unset = UNSET,
    has_overview: bool | Unset = UNSET,
    has_imdb_id: bool | Unset = UNSET,
    has_tmdb_id: bool | Unset = UNSET,
    has_tvdb_id: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    exclude_item_ids: list[UUID] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    recursive: bool | Unset = UNSET,
    search_term: str | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    image_types: list[ImageType] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
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
    artists: list[str] | Unset = UNSET,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    artist_ids: list[UUID] | Unset = UNSET,
    album_artist_ids: list[UUID] | Unset = UNSET,
    contributing_artist_ids: list[UUID] | Unset = UNSET,
    albums: list[str] | Unset = UNSET,
    album_ids: list[UUID] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    video_types: list[VideoType] | Unset = UNSET,
    min_official_rating: str | Unset = UNSET,
    is_locked: bool | Unset = UNSET,
    is_place_holder: bool | Unset = UNSET,
    has_official_rating: bool | Unset = UNSET,
    collapse_box_set_items: bool | Unset = UNSET,
    min_width: int | Unset = UNSET,
    min_height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    is_3d: bool | Unset = UNSET,
    series_status: list[SeriesStatus] | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["maxOfficialRating"] = max_official_rating

    params["hasThemeSong"] = has_theme_song

    params["hasThemeVideo"] = has_theme_video

    params["hasSubtitles"] = has_subtitles

    params["hasSpecialFeature"] = has_special_feature

    params["hasTrailer"] = has_trailer

    json_adjacent_to: str | Unset = UNSET
    if not isinstance(adjacent_to, Unset):
        json_adjacent_to = str(adjacent_to)
    params["adjacentTo"] = json_adjacent_to

    params["indexNumber"] = index_number

    params["parentIndexNumber"] = parent_index_number

    params["hasParentalRating"] = has_parental_rating

    params["isHd"] = is_hd

    params["is4K"] = is_4k

    json_location_types: list[str] | Unset = UNSET
    if not isinstance(location_types, Unset):
        json_location_types = []
        for location_types_item_data in location_types:
            location_types_item = location_types_item_data.value
            json_location_types.append(location_types_item)

    params["locationTypes"] = json_location_types

    json_exclude_location_types: list[str] | Unset = UNSET
    if not isinstance(exclude_location_types, Unset):
        json_exclude_location_types = []
        for exclude_location_types_item_data in exclude_location_types:
            exclude_location_types_item = exclude_location_types_item_data.value
            json_exclude_location_types.append(exclude_location_types_item)

    params["excludeLocationTypes"] = json_exclude_location_types

    params["isMissing"] = is_missing

    params["isUnaired"] = is_unaired

    params["minCommunityRating"] = min_community_rating

    params["minCriticRating"] = min_critic_rating

    json_min_premiere_date: str | Unset = UNSET
    if not isinstance(min_premiere_date, Unset):
        json_min_premiere_date = min_premiere_date.isoformat()
    params["minPremiereDate"] = json_min_premiere_date

    json_min_date_last_saved: str | Unset = UNSET
    if not isinstance(min_date_last_saved, Unset):
        json_min_date_last_saved = min_date_last_saved.isoformat()
    params["minDateLastSaved"] = json_min_date_last_saved

    json_min_date_last_saved_for_user: str | Unset = UNSET
    if not isinstance(min_date_last_saved_for_user, Unset):
        json_min_date_last_saved_for_user = min_date_last_saved_for_user.isoformat()
    params["minDateLastSavedForUser"] = json_min_date_last_saved_for_user

    json_max_premiere_date: str | Unset = UNSET
    if not isinstance(max_premiere_date, Unset):
        json_max_premiere_date = max_premiere_date.isoformat()
    params["maxPremiereDate"] = json_max_premiere_date

    params["hasOverview"] = has_overview

    params["hasImdbId"] = has_imdb_id

    params["hasTmdbId"] = has_tmdb_id

    params["hasTvdbId"] = has_tvdb_id

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    json_exclude_item_ids: list[str] | Unset = UNSET
    if not isinstance(exclude_item_ids, Unset):
        json_exclude_item_ids = []
        for exclude_item_ids_item_data in exclude_item_ids:
            exclude_item_ids_item = str(exclude_item_ids_item_data)
            json_exclude_item_ids.append(exclude_item_ids_item)

    params["excludeItemIds"] = json_exclude_item_ids

    params["startIndex"] = start_index

    params["limit"] = limit

    params["recursive"] = recursive

    params["searchTerm"] = search_term

    json_sort_order: list[str] | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

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

    json_image_types: list[str] | Unset = UNSET
    if not isinstance(image_types, Unset):
        json_image_types = []
        for image_types_item_data in image_types:
            image_types_item = image_types_item_data.value
            json_image_types.append(image_types_item)

    params["imageTypes"] = json_image_types

    json_sort_by: list[str] | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    params["isPlayed"] = is_played

    json_genres: list[str] | Unset = UNSET
    if not isinstance(genres, Unset):
        json_genres = genres

    params["genres"] = json_genres

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

    json_artists: list[str] | Unset = UNSET
    if not isinstance(artists, Unset):
        json_artists = artists

    params["artists"] = json_artists

    json_exclude_artist_ids: list[str] | Unset = UNSET
    if not isinstance(exclude_artist_ids, Unset):
        json_exclude_artist_ids = []
        for exclude_artist_ids_item_data in exclude_artist_ids:
            exclude_artist_ids_item = str(exclude_artist_ids_item_data)
            json_exclude_artist_ids.append(exclude_artist_ids_item)

    params["excludeArtistIds"] = json_exclude_artist_ids

    json_artist_ids: list[str] | Unset = UNSET
    if not isinstance(artist_ids, Unset):
        json_artist_ids = []
        for artist_ids_item_data in artist_ids:
            artist_ids_item = str(artist_ids_item_data)
            json_artist_ids.append(artist_ids_item)

    params["artistIds"] = json_artist_ids

    json_album_artist_ids: list[str] | Unset = UNSET
    if not isinstance(album_artist_ids, Unset):
        json_album_artist_ids = []
        for album_artist_ids_item_data in album_artist_ids:
            album_artist_ids_item = str(album_artist_ids_item_data)
            json_album_artist_ids.append(album_artist_ids_item)

    params["albumArtistIds"] = json_album_artist_ids

    json_contributing_artist_ids: list[str] | Unset = UNSET
    if not isinstance(contributing_artist_ids, Unset):
        json_contributing_artist_ids = []
        for contributing_artist_ids_item_data in contributing_artist_ids:
            contributing_artist_ids_item = str(contributing_artist_ids_item_data)
            json_contributing_artist_ids.append(contributing_artist_ids_item)

    params["contributingArtistIds"] = json_contributing_artist_ids

    json_albums: list[str] | Unset = UNSET
    if not isinstance(albums, Unset):
        json_albums = albums

    params["albums"] = json_albums

    json_album_ids: list[str] | Unset = UNSET
    if not isinstance(album_ids, Unset):
        json_album_ids = []
        for album_ids_item_data in album_ids:
            album_ids_item = str(album_ids_item_data)
            json_album_ids.append(album_ids_item)

    params["albumIds"] = json_album_ids

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = []
        for ids_item_data in ids:
            ids_item = str(ids_item_data)
            json_ids.append(ids_item)

    params["ids"] = json_ids

    json_video_types: list[str] | Unset = UNSET
    if not isinstance(video_types, Unset):
        json_video_types = []
        for video_types_item_data in video_types:
            video_types_item = video_types_item_data.value
            json_video_types.append(video_types_item)

    params["videoTypes"] = json_video_types

    params["minOfficialRating"] = min_official_rating

    params["isLocked"] = is_locked

    params["isPlaceHolder"] = is_place_holder

    params["hasOfficialRating"] = has_official_rating

    params["collapseBoxSetItems"] = collapse_box_set_items

    params["minWidth"] = min_width

    params["minHeight"] = min_height

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["is3D"] = is_3d

    json_series_status: list[str] | Unset = UNSET
    if not isinstance(series_status, Unset):
        json_series_status = []
        for series_status_item_data in series_status:
            series_status_item = series_status_item_data.value
            json_series_status.append(series_status_item)

    params["seriesStatus"] = json_series_status

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

    json_studio_ids: list[str] | Unset = UNSET
    if not isinstance(studio_ids, Unset):
        json_studio_ids = []
        for studio_ids_item_data in studio_ids:
            studio_ids_item = str(studio_ids_item_data)
            json_studio_ids.append(studio_ids_item)

    params["studioIds"] = json_studio_ids

    json_genre_ids: list[str] | Unset = UNSET
    if not isinstance(genre_ids, Unset):
        json_genre_ids = []
        for genre_ids_item_data in genre_ids:
            genre_ids_item = str(genre_ids_item_data)
            json_genre_ids.append(genre_ids_item)

    params["genreIds"] = json_genre_ids

    params["enableTotalRecordCount"] = enable_total_record_count

    params["enableImages"] = enable_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items",
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
    max_official_rating: str | Unset = UNSET,
    has_theme_song: bool | Unset = UNSET,
    has_theme_video: bool | Unset = UNSET,
    has_subtitles: bool | Unset = UNSET,
    has_special_feature: bool | Unset = UNSET,
    has_trailer: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    index_number: int | Unset = UNSET,
    parent_index_number: int | Unset = UNSET,
    has_parental_rating: bool | Unset = UNSET,
    is_hd: bool | Unset = UNSET,
    is_4k: bool | Unset = UNSET,
    location_types: list[LocationType] | Unset = UNSET,
    exclude_location_types: list[LocationType] | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    is_unaired: bool | Unset = UNSET,
    min_community_rating: float | Unset = UNSET,
    min_critic_rating: float | Unset = UNSET,
    min_premiere_date: datetime.datetime | Unset = UNSET,
    min_date_last_saved: datetime.datetime | Unset = UNSET,
    min_date_last_saved_for_user: datetime.datetime | Unset = UNSET,
    max_premiere_date: datetime.datetime | Unset = UNSET,
    has_overview: bool | Unset = UNSET,
    has_imdb_id: bool | Unset = UNSET,
    has_tmdb_id: bool | Unset = UNSET,
    has_tvdb_id: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    exclude_item_ids: list[UUID] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    recursive: bool | Unset = UNSET,
    search_term: str | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    image_types: list[ImageType] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
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
    artists: list[str] | Unset = UNSET,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    artist_ids: list[UUID] | Unset = UNSET,
    album_artist_ids: list[UUID] | Unset = UNSET,
    contributing_artist_ids: list[UUID] | Unset = UNSET,
    albums: list[str] | Unset = UNSET,
    album_ids: list[UUID] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    video_types: list[VideoType] | Unset = UNSET,
    min_official_rating: str | Unset = UNSET,
    is_locked: bool | Unset = UNSET,
    is_place_holder: bool | Unset = UNSET,
    has_official_rating: bool | Unset = UNSET,
    collapse_box_set_items: bool | Unset = UNSET,
    min_width: int | Unset = UNSET,
    min_height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    is_3d: bool | Unset = UNSET,
    series_status: list[SeriesStatus] | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        max_official_rating (str | Unset):
        has_theme_song (bool | Unset):
        has_theme_video (bool | Unset):
        has_subtitles (bool | Unset):
        has_special_feature (bool | Unset):
        has_trailer (bool | Unset):
        adjacent_to (UUID | Unset):
        index_number (int | Unset):
        parent_index_number (int | Unset):
        has_parental_rating (bool | Unset):
        is_hd (bool | Unset):
        is_4k (bool | Unset):
        location_types (list[LocationType] | Unset):
        exclude_location_types (list[LocationType] | Unset):
        is_missing (bool | Unset):
        is_unaired (bool | Unset):
        min_community_rating (float | Unset):
        min_critic_rating (float | Unset):
        min_premiere_date (datetime.datetime | Unset):
        min_date_last_saved (datetime.datetime | Unset):
        min_date_last_saved_for_user (datetime.datetime | Unset):
        max_premiere_date (datetime.datetime | Unset):
        has_overview (bool | Unset):
        has_imdb_id (bool | Unset):
        has_tmdb_id (bool | Unset):
        has_tvdb_id (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        exclude_item_ids (list[UUID] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        recursive (bool | Unset):
        search_term (str | Unset):
        sort_order (list[SortOrder] | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        image_types (list[ImageType] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        is_played (bool | Unset):
        genres (list[str] | Unset):
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
        artists (list[str] | Unset):
        exclude_artist_ids (list[UUID] | Unset):
        artist_ids (list[UUID] | Unset):
        album_artist_ids (list[UUID] | Unset):
        contributing_artist_ids (list[UUID] | Unset):
        albums (list[str] | Unset):
        album_ids (list[UUID] | Unset):
        ids (list[UUID] | Unset):
        video_types (list[VideoType] | Unset):
        min_official_rating (str | Unset):
        is_locked (bool | Unset):
        is_place_holder (bool | Unset):
        has_official_rating (bool | Unset):
        collapse_box_set_items (bool | Unset):
        min_width (int | Unset):
        min_height (int | Unset):
        max_width (int | Unset):
        max_height (int | Unset):
        is_3d (bool | Unset):
        series_status (list[SeriesStatus] | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        studio_ids (list[UUID] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        index_number=index_number,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
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
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    max_official_rating: str | Unset = UNSET,
    has_theme_song: bool | Unset = UNSET,
    has_theme_video: bool | Unset = UNSET,
    has_subtitles: bool | Unset = UNSET,
    has_special_feature: bool | Unset = UNSET,
    has_trailer: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    index_number: int | Unset = UNSET,
    parent_index_number: int | Unset = UNSET,
    has_parental_rating: bool | Unset = UNSET,
    is_hd: bool | Unset = UNSET,
    is_4k: bool | Unset = UNSET,
    location_types: list[LocationType] | Unset = UNSET,
    exclude_location_types: list[LocationType] | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    is_unaired: bool | Unset = UNSET,
    min_community_rating: float | Unset = UNSET,
    min_critic_rating: float | Unset = UNSET,
    min_premiere_date: datetime.datetime | Unset = UNSET,
    min_date_last_saved: datetime.datetime | Unset = UNSET,
    min_date_last_saved_for_user: datetime.datetime | Unset = UNSET,
    max_premiere_date: datetime.datetime | Unset = UNSET,
    has_overview: bool | Unset = UNSET,
    has_imdb_id: bool | Unset = UNSET,
    has_tmdb_id: bool | Unset = UNSET,
    has_tvdb_id: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    exclude_item_ids: list[UUID] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    recursive: bool | Unset = UNSET,
    search_term: str | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    image_types: list[ImageType] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
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
    artists: list[str] | Unset = UNSET,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    artist_ids: list[UUID] | Unset = UNSET,
    album_artist_ids: list[UUID] | Unset = UNSET,
    contributing_artist_ids: list[UUID] | Unset = UNSET,
    albums: list[str] | Unset = UNSET,
    album_ids: list[UUID] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    video_types: list[VideoType] | Unset = UNSET,
    min_official_rating: str | Unset = UNSET,
    is_locked: bool | Unset = UNSET,
    is_place_holder: bool | Unset = UNSET,
    has_official_rating: bool | Unset = UNSET,
    collapse_box_set_items: bool | Unset = UNSET,
    min_width: int | Unset = UNSET,
    min_height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    is_3d: bool | Unset = UNSET,
    series_status: list[SeriesStatus] | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        max_official_rating (str | Unset):
        has_theme_song (bool | Unset):
        has_theme_video (bool | Unset):
        has_subtitles (bool | Unset):
        has_special_feature (bool | Unset):
        has_trailer (bool | Unset):
        adjacent_to (UUID | Unset):
        index_number (int | Unset):
        parent_index_number (int | Unset):
        has_parental_rating (bool | Unset):
        is_hd (bool | Unset):
        is_4k (bool | Unset):
        location_types (list[LocationType] | Unset):
        exclude_location_types (list[LocationType] | Unset):
        is_missing (bool | Unset):
        is_unaired (bool | Unset):
        min_community_rating (float | Unset):
        min_critic_rating (float | Unset):
        min_premiere_date (datetime.datetime | Unset):
        min_date_last_saved (datetime.datetime | Unset):
        min_date_last_saved_for_user (datetime.datetime | Unset):
        max_premiere_date (datetime.datetime | Unset):
        has_overview (bool | Unset):
        has_imdb_id (bool | Unset):
        has_tmdb_id (bool | Unset):
        has_tvdb_id (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        exclude_item_ids (list[UUID] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        recursive (bool | Unset):
        search_term (str | Unset):
        sort_order (list[SortOrder] | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        image_types (list[ImageType] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        is_played (bool | Unset):
        genres (list[str] | Unset):
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
        artists (list[str] | Unset):
        exclude_artist_ids (list[UUID] | Unset):
        artist_ids (list[UUID] | Unset):
        album_artist_ids (list[UUID] | Unset):
        contributing_artist_ids (list[UUID] | Unset):
        albums (list[str] | Unset):
        album_ids (list[UUID] | Unset):
        ids (list[UUID] | Unset):
        video_types (list[VideoType] | Unset):
        min_official_rating (str | Unset):
        is_locked (bool | Unset):
        is_place_holder (bool | Unset):
        has_official_rating (bool | Unset):
        collapse_box_set_items (bool | Unset):
        min_width (int | Unset):
        min_height (int | Unset):
        max_width (int | Unset):
        max_height (int | Unset):
        is_3d (bool | Unset):
        series_status (list[SeriesStatus] | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        studio_ids (list[UUID] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        index_number=index_number,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
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
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    max_official_rating: str | Unset = UNSET,
    has_theme_song: bool | Unset = UNSET,
    has_theme_video: bool | Unset = UNSET,
    has_subtitles: bool | Unset = UNSET,
    has_special_feature: bool | Unset = UNSET,
    has_trailer: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    index_number: int | Unset = UNSET,
    parent_index_number: int | Unset = UNSET,
    has_parental_rating: bool | Unset = UNSET,
    is_hd: bool | Unset = UNSET,
    is_4k: bool | Unset = UNSET,
    location_types: list[LocationType] | Unset = UNSET,
    exclude_location_types: list[LocationType] | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    is_unaired: bool | Unset = UNSET,
    min_community_rating: float | Unset = UNSET,
    min_critic_rating: float | Unset = UNSET,
    min_premiere_date: datetime.datetime | Unset = UNSET,
    min_date_last_saved: datetime.datetime | Unset = UNSET,
    min_date_last_saved_for_user: datetime.datetime | Unset = UNSET,
    max_premiere_date: datetime.datetime | Unset = UNSET,
    has_overview: bool | Unset = UNSET,
    has_imdb_id: bool | Unset = UNSET,
    has_tmdb_id: bool | Unset = UNSET,
    has_tvdb_id: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    exclude_item_ids: list[UUID] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    recursive: bool | Unset = UNSET,
    search_term: str | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    image_types: list[ImageType] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
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
    artists: list[str] | Unset = UNSET,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    artist_ids: list[UUID] | Unset = UNSET,
    album_artist_ids: list[UUID] | Unset = UNSET,
    contributing_artist_ids: list[UUID] | Unset = UNSET,
    albums: list[str] | Unset = UNSET,
    album_ids: list[UUID] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    video_types: list[VideoType] | Unset = UNSET,
    min_official_rating: str | Unset = UNSET,
    is_locked: bool | Unset = UNSET,
    is_place_holder: bool | Unset = UNSET,
    has_official_rating: bool | Unset = UNSET,
    collapse_box_set_items: bool | Unset = UNSET,
    min_width: int | Unset = UNSET,
    min_height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    is_3d: bool | Unset = UNSET,
    series_status: list[SeriesStatus] | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        max_official_rating (str | Unset):
        has_theme_song (bool | Unset):
        has_theme_video (bool | Unset):
        has_subtitles (bool | Unset):
        has_special_feature (bool | Unset):
        has_trailer (bool | Unset):
        adjacent_to (UUID | Unset):
        index_number (int | Unset):
        parent_index_number (int | Unset):
        has_parental_rating (bool | Unset):
        is_hd (bool | Unset):
        is_4k (bool | Unset):
        location_types (list[LocationType] | Unset):
        exclude_location_types (list[LocationType] | Unset):
        is_missing (bool | Unset):
        is_unaired (bool | Unset):
        min_community_rating (float | Unset):
        min_critic_rating (float | Unset):
        min_premiere_date (datetime.datetime | Unset):
        min_date_last_saved (datetime.datetime | Unset):
        min_date_last_saved_for_user (datetime.datetime | Unset):
        max_premiere_date (datetime.datetime | Unset):
        has_overview (bool | Unset):
        has_imdb_id (bool | Unset):
        has_tmdb_id (bool | Unset):
        has_tvdb_id (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        exclude_item_ids (list[UUID] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        recursive (bool | Unset):
        search_term (str | Unset):
        sort_order (list[SortOrder] | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        image_types (list[ImageType] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        is_played (bool | Unset):
        genres (list[str] | Unset):
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
        artists (list[str] | Unset):
        exclude_artist_ids (list[UUID] | Unset):
        artist_ids (list[UUID] | Unset):
        album_artist_ids (list[UUID] | Unset):
        contributing_artist_ids (list[UUID] | Unset):
        albums (list[str] | Unset):
        album_ids (list[UUID] | Unset):
        ids (list[UUID] | Unset):
        video_types (list[VideoType] | Unset):
        min_official_rating (str | Unset):
        is_locked (bool | Unset):
        is_place_holder (bool | Unset):
        has_official_rating (bool | Unset):
        collapse_box_set_items (bool | Unset):
        min_width (int | Unset):
        min_height (int | Unset):
        max_width (int | Unset):
        max_height (int | Unset):
        is_3d (bool | Unset):
        series_status (list[SeriesStatus] | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        studio_ids (list[UUID] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        index_number=index_number,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
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
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    max_official_rating: str | Unset = UNSET,
    has_theme_song: bool | Unset = UNSET,
    has_theme_video: bool | Unset = UNSET,
    has_subtitles: bool | Unset = UNSET,
    has_special_feature: bool | Unset = UNSET,
    has_trailer: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    index_number: int | Unset = UNSET,
    parent_index_number: int | Unset = UNSET,
    has_parental_rating: bool | Unset = UNSET,
    is_hd: bool | Unset = UNSET,
    is_4k: bool | Unset = UNSET,
    location_types: list[LocationType] | Unset = UNSET,
    exclude_location_types: list[LocationType] | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    is_unaired: bool | Unset = UNSET,
    min_community_rating: float | Unset = UNSET,
    min_critic_rating: float | Unset = UNSET,
    min_premiere_date: datetime.datetime | Unset = UNSET,
    min_date_last_saved: datetime.datetime | Unset = UNSET,
    min_date_last_saved_for_user: datetime.datetime | Unset = UNSET,
    max_premiere_date: datetime.datetime | Unset = UNSET,
    has_overview: bool | Unset = UNSET,
    has_imdb_id: bool | Unset = UNSET,
    has_tmdb_id: bool | Unset = UNSET,
    has_tvdb_id: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    exclude_item_ids: list[UUID] | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    recursive: bool | Unset = UNSET,
    search_term: str | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    image_types: list[ImageType] | Unset = UNSET,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    genres: list[str] | Unset = UNSET,
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
    artists: list[str] | Unset = UNSET,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    artist_ids: list[UUID] | Unset = UNSET,
    album_artist_ids: list[UUID] | Unset = UNSET,
    contributing_artist_ids: list[UUID] | Unset = UNSET,
    albums: list[str] | Unset = UNSET,
    album_ids: list[UUID] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    video_types: list[VideoType] | Unset = UNSET,
    min_official_rating: str | Unset = UNSET,
    is_locked: bool | Unset = UNSET,
    is_place_holder: bool | Unset = UNSET,
    has_official_rating: bool | Unset = UNSET,
    collapse_box_set_items: bool | Unset = UNSET,
    min_width: int | Unset = UNSET,
    min_height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    is_3d: bool | Unset = UNSET,
    series_status: list[SeriesStatus] | Unset = UNSET,
    name_starts_with_or_greater: str | Unset = UNSET,
    name_starts_with: str | Unset = UNSET,
    name_less_than: str | Unset = UNSET,
    studio_ids: list[UUID] | Unset = UNSET,
    genre_ids: list[UUID] | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    enable_images: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets items based on a query.

    Args:
        user_id (UUID | Unset):
        max_official_rating (str | Unset):
        has_theme_song (bool | Unset):
        has_theme_video (bool | Unset):
        has_subtitles (bool | Unset):
        has_special_feature (bool | Unset):
        has_trailer (bool | Unset):
        adjacent_to (UUID | Unset):
        index_number (int | Unset):
        parent_index_number (int | Unset):
        has_parental_rating (bool | Unset):
        is_hd (bool | Unset):
        is_4k (bool | Unset):
        location_types (list[LocationType] | Unset):
        exclude_location_types (list[LocationType] | Unset):
        is_missing (bool | Unset):
        is_unaired (bool | Unset):
        min_community_rating (float | Unset):
        min_critic_rating (float | Unset):
        min_premiere_date (datetime.datetime | Unset):
        min_date_last_saved (datetime.datetime | Unset):
        min_date_last_saved_for_user (datetime.datetime | Unset):
        max_premiere_date (datetime.datetime | Unset):
        has_overview (bool | Unset):
        has_imdb_id (bool | Unset):
        has_tmdb_id (bool | Unset):
        has_tvdb_id (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        exclude_item_ids (list[UUID] | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        recursive (bool | Unset):
        search_term (str | Unset):
        sort_order (list[SortOrder] | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        media_types (list[MediaType] | Unset):
        image_types (list[ImageType] | Unset):
        sort_by (list[ItemSortBy] | Unset):
        is_played (bool | Unset):
        genres (list[str] | Unset):
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
        artists (list[str] | Unset):
        exclude_artist_ids (list[UUID] | Unset):
        artist_ids (list[UUID] | Unset):
        album_artist_ids (list[UUID] | Unset):
        contributing_artist_ids (list[UUID] | Unset):
        albums (list[str] | Unset):
        album_ids (list[UUID] | Unset):
        ids (list[UUID] | Unset):
        video_types (list[VideoType] | Unset):
        min_official_rating (str | Unset):
        is_locked (bool | Unset):
        is_place_holder (bool | Unset):
        has_official_rating (bool | Unset):
        collapse_box_set_items (bool | Unset):
        min_width (int | Unset):
        min_height (int | Unset):
        max_width (int | Unset):
        max_height (int | Unset):
        is_3d (bool | Unset):
        series_status (list[SeriesStatus] | Unset):
        name_starts_with_or_greater (str | Unset):
        name_starts_with (str | Unset):
        name_less_than (str | Unset):
        studio_ids (list[UUID] | Unset):
        genre_ids (list[UUID] | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        enable_images (bool | Unset):  Default: True.

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
            max_official_rating=max_official_rating,
            has_theme_song=has_theme_song,
            has_theme_video=has_theme_video,
            has_subtitles=has_subtitles,
            has_special_feature=has_special_feature,
            has_trailer=has_trailer,
            adjacent_to=adjacent_to,
            index_number=index_number,
            parent_index_number=parent_index_number,
            has_parental_rating=has_parental_rating,
            is_hd=is_hd,
            is_4k=is_4k,
            location_types=location_types,
            exclude_location_types=exclude_location_types,
            is_missing=is_missing,
            is_unaired=is_unaired,
            min_community_rating=min_community_rating,
            min_critic_rating=min_critic_rating,
            min_premiere_date=min_premiere_date,
            min_date_last_saved=min_date_last_saved,
            min_date_last_saved_for_user=min_date_last_saved_for_user,
            max_premiere_date=max_premiere_date,
            has_overview=has_overview,
            has_imdb_id=has_imdb_id,
            has_tmdb_id=has_tmdb_id,
            has_tvdb_id=has_tvdb_id,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            exclude_item_ids=exclude_item_ids,
            start_index=start_index,
            limit=limit,
            recursive=recursive,
            search_term=search_term,
            sort_order=sort_order,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            include_item_types=include_item_types,
            filters=filters,
            is_favorite=is_favorite,
            media_types=media_types,
            image_types=image_types,
            sort_by=sort_by,
            is_played=is_played,
            genres=genres,
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
            artists=artists,
            exclude_artist_ids=exclude_artist_ids,
            artist_ids=artist_ids,
            album_artist_ids=album_artist_ids,
            contributing_artist_ids=contributing_artist_ids,
            albums=albums,
            album_ids=album_ids,
            ids=ids,
            video_types=video_types,
            min_official_rating=min_official_rating,
            is_locked=is_locked,
            is_place_holder=is_place_holder,
            has_official_rating=has_official_rating,
            collapse_box_set_items=collapse_box_set_items,
            min_width=min_width,
            min_height=min_height,
            max_width=max_width,
            max_height=max_height,
            is_3d=is_3d,
            series_status=series_status,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            studio_ids=studio_ids,
            genre_ids=genre_ids,
            enable_total_record_count=enable_total_record_count,
            enable_images=enable_images,
        )
    ).parsed
