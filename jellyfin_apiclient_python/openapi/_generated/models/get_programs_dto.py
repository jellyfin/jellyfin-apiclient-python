from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.image_type import ImageType
from ..models.item_fields import ItemFields
from ..models.item_sort_by import ItemSortBy
from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProgramsDto")


@_attrs_define
class GetProgramsDto:
    """Get programs dto.

    Attributes:
        channel_ids (list[UUID] | None | Unset): Gets or sets the channels to return guide information for.
        user_id (None | Unset | UUID): Gets or sets optional. Filter by user id.
        min_start_date (datetime.datetime | None | Unset): Gets or sets the minimum premiere start date.
        has_aired (bool | None | Unset): Gets or sets filter by programs that have completed airing, or not.
        is_airing (bool | None | Unset): Gets or sets filter by programs that are currently airing, or not.
        max_start_date (datetime.datetime | None | Unset): Gets or sets the maximum premiere start date.
        min_end_date (datetime.datetime | None | Unset): Gets or sets the minimum premiere end date.
        max_end_date (datetime.datetime | None | Unset): Gets or sets the maximum premiere end date.
        is_movie (bool | None | Unset): Gets or sets filter for movies.
        is_series (bool | None | Unset): Gets or sets filter for series.
        is_news (bool | None | Unset): Gets or sets filter for news.
        is_kids (bool | None | Unset): Gets or sets filter for kids.
        is_sports (bool | None | Unset): Gets or sets filter for sports.
        start_index (int | None | Unset): Gets or sets the record index to start at. All items with a lower index will
            be dropped from the results.
        limit (int | None | Unset): Gets or sets the maximum number of records to return.
        sort_by (list[ItemSortBy] | None | Unset): Gets or sets specify one or more sort orders, comma delimited.
            Options: Name, StartDate.
        sort_order (list[SortOrder] | None | Unset): Gets or sets sort order.
        genres (list[str] | None | Unset): Gets or sets the genres to return guide information for.
        genre_ids (list[UUID] | None | Unset): Gets or sets the genre ids to return guide information for.
        enable_images (bool | None | Unset): Gets or sets include image information in output.
        enable_total_record_count (bool | Unset): Gets or sets a value indicating whether retrieve total record count.
            Default: True.
        image_type_limit (int | None | Unset): Gets or sets the max number of images to return, per image type.
        enable_image_types (list[ImageType] | None | Unset): Gets or sets the image types to include in the output.
        enable_user_data (bool | None | Unset): Gets or sets include user data.
        series_timer_id (None | str | Unset): Gets or sets filter by series timer id.
        library_series_id (None | Unset | UUID): Gets or sets filter by library series id.
        fields (list[ItemFields] | None | Unset): Gets or sets specify additional fields of information to return in the
            output.
    """

    channel_ids: list[UUID] | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    min_start_date: datetime.datetime | None | Unset = UNSET
    has_aired: bool | None | Unset = UNSET
    is_airing: bool | None | Unset = UNSET
    max_start_date: datetime.datetime | None | Unset = UNSET
    min_end_date: datetime.datetime | None | Unset = UNSET
    max_end_date: datetime.datetime | None | Unset = UNSET
    is_movie: bool | None | Unset = UNSET
    is_series: bool | None | Unset = UNSET
    is_news: bool | None | Unset = UNSET
    is_kids: bool | None | Unset = UNSET
    is_sports: bool | None | Unset = UNSET
    start_index: int | None | Unset = UNSET
    limit: int | None | Unset = UNSET
    sort_by: list[ItemSortBy] | None | Unset = UNSET
    sort_order: list[SortOrder] | None | Unset = UNSET
    genres: list[str] | None | Unset = UNSET
    genre_ids: list[UUID] | None | Unset = UNSET
    enable_images: bool | None | Unset = UNSET
    enable_total_record_count: bool | Unset = True
    image_type_limit: int | None | Unset = UNSET
    enable_image_types: list[ImageType] | None | Unset = UNSET
    enable_user_data: bool | None | Unset = UNSET
    series_timer_id: None | str | Unset = UNSET
    library_series_id: None | Unset | UUID = UNSET
    fields: list[ItemFields] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel_ids: list[str] | None | Unset
        if isinstance(self.channel_ids, Unset):
            channel_ids = UNSET
        elif isinstance(self.channel_ids, list):
            channel_ids = []
            for channel_ids_type_0_item_data in self.channel_ids:
                channel_ids_type_0_item = str(channel_ids_type_0_item_data)
                channel_ids.append(channel_ids_type_0_item)

        else:
            channel_ids = self.channel_ids

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        min_start_date: None | str | Unset
        if isinstance(self.min_start_date, Unset):
            min_start_date = UNSET
        elif isinstance(self.min_start_date, datetime.datetime):
            min_start_date = self.min_start_date.isoformat()
        else:
            min_start_date = self.min_start_date

        has_aired: bool | None | Unset
        if isinstance(self.has_aired, Unset):
            has_aired = UNSET
        else:
            has_aired = self.has_aired

        is_airing: bool | None | Unset
        if isinstance(self.is_airing, Unset):
            is_airing = UNSET
        else:
            is_airing = self.is_airing

        max_start_date: None | str | Unset
        if isinstance(self.max_start_date, Unset):
            max_start_date = UNSET
        elif isinstance(self.max_start_date, datetime.datetime):
            max_start_date = self.max_start_date.isoformat()
        else:
            max_start_date = self.max_start_date

        min_end_date: None | str | Unset
        if isinstance(self.min_end_date, Unset):
            min_end_date = UNSET
        elif isinstance(self.min_end_date, datetime.datetime):
            min_end_date = self.min_end_date.isoformat()
        else:
            min_end_date = self.min_end_date

        max_end_date: None | str | Unset
        if isinstance(self.max_end_date, Unset):
            max_end_date = UNSET
        elif isinstance(self.max_end_date, datetime.datetime):
            max_end_date = self.max_end_date.isoformat()
        else:
            max_end_date = self.max_end_date

        is_movie: bool | None | Unset
        if isinstance(self.is_movie, Unset):
            is_movie = UNSET
        else:
            is_movie = self.is_movie

        is_series: bool | None | Unset
        if isinstance(self.is_series, Unset):
            is_series = UNSET
        else:
            is_series = self.is_series

        is_news: bool | None | Unset
        if isinstance(self.is_news, Unset):
            is_news = UNSET
        else:
            is_news = self.is_news

        is_kids: bool | None | Unset
        if isinstance(self.is_kids, Unset):
            is_kids = UNSET
        else:
            is_kids = self.is_kids

        is_sports: bool | None | Unset
        if isinstance(self.is_sports, Unset):
            is_sports = UNSET
        else:
            is_sports = self.is_sports

        start_index: int | None | Unset
        if isinstance(self.start_index, Unset):
            start_index = UNSET
        else:
            start_index = self.start_index

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        sort_by: list[str] | None | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, list):
            sort_by = []
            for sort_by_type_0_item_data in self.sort_by:
                sort_by_type_0_item = sort_by_type_0_item_data.value
                sort_by.append(sort_by_type_0_item)

        else:
            sort_by = self.sort_by

        sort_order: list[str] | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        elif isinstance(self.sort_order, list):
            sort_order = []
            for sort_order_type_0_item_data in self.sort_order:
                sort_order_type_0_item = sort_order_type_0_item_data.value
                sort_order.append(sort_order_type_0_item)

        else:
            sort_order = self.sort_order

        genres: list[str] | None | Unset
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        genre_ids: list[str] | None | Unset
        if isinstance(self.genre_ids, Unset):
            genre_ids = UNSET
        elif isinstance(self.genre_ids, list):
            genre_ids = []
            for genre_ids_type_0_item_data in self.genre_ids:
                genre_ids_type_0_item = str(genre_ids_type_0_item_data)
                genre_ids.append(genre_ids_type_0_item)

        else:
            genre_ids = self.genre_ids

        enable_images: bool | None | Unset
        if isinstance(self.enable_images, Unset):
            enable_images = UNSET
        else:
            enable_images = self.enable_images

        enable_total_record_count = self.enable_total_record_count

        image_type_limit: int | None | Unset
        if isinstance(self.image_type_limit, Unset):
            image_type_limit = UNSET
        else:
            image_type_limit = self.image_type_limit

        enable_image_types: list[str] | None | Unset
        if isinstance(self.enable_image_types, Unset):
            enable_image_types = UNSET
        elif isinstance(self.enable_image_types, list):
            enable_image_types = []
            for enable_image_types_type_0_item_data in self.enable_image_types:
                enable_image_types_type_0_item = (
                    enable_image_types_type_0_item_data.value
                )
                enable_image_types.append(enable_image_types_type_0_item)

        else:
            enable_image_types = self.enable_image_types

        enable_user_data: bool | None | Unset
        if isinstance(self.enable_user_data, Unset):
            enable_user_data = UNSET
        else:
            enable_user_data = self.enable_user_data

        series_timer_id: None | str | Unset
        if isinstance(self.series_timer_id, Unset):
            series_timer_id = UNSET
        else:
            series_timer_id = self.series_timer_id

        library_series_id: None | str | Unset
        if isinstance(self.library_series_id, Unset):
            library_series_id = UNSET
        elif isinstance(self.library_series_id, UUID):
            library_series_id = str(self.library_series_id)
        else:
            library_series_id = self.library_series_id

        fields: list[str] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.value
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if channel_ids is not UNSET:
            field_dict["ChannelIds"] = channel_ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if min_start_date is not UNSET:
            field_dict["MinStartDate"] = min_start_date
        if has_aired is not UNSET:
            field_dict["HasAired"] = has_aired
        if is_airing is not UNSET:
            field_dict["IsAiring"] = is_airing
        if max_start_date is not UNSET:
            field_dict["MaxStartDate"] = max_start_date
        if min_end_date is not UNSET:
            field_dict["MinEndDate"] = min_end_date
        if max_end_date is not UNSET:
            field_dict["MaxEndDate"] = max_end_date
        if is_movie is not UNSET:
            field_dict["IsMovie"] = is_movie
        if is_series is not UNSET:
            field_dict["IsSeries"] = is_series
        if is_news is not UNSET:
            field_dict["IsNews"] = is_news
        if is_kids is not UNSET:
            field_dict["IsKids"] = is_kids
        if is_sports is not UNSET:
            field_dict["IsSports"] = is_sports
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if sort_by is not UNSET:
            field_dict["SortBy"] = sort_by
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if genre_ids is not UNSET:
            field_dict["GenreIds"] = genre_ids
        if enable_images is not UNSET:
            field_dict["EnableImages"] = enable_images
        if enable_total_record_count is not UNSET:
            field_dict["EnableTotalRecordCount"] = enable_total_record_count
        if image_type_limit is not UNSET:
            field_dict["ImageTypeLimit"] = image_type_limit
        if enable_image_types is not UNSET:
            field_dict["EnableImageTypes"] = enable_image_types
        if enable_user_data is not UNSET:
            field_dict["EnableUserData"] = enable_user_data
        if series_timer_id is not UNSET:
            field_dict["SeriesTimerId"] = series_timer_id
        if library_series_id is not UNSET:
            field_dict["LibrarySeriesId"] = library_series_id
        if fields is not UNSET:
            field_dict["Fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_channel_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channel_ids_type_0 = []
                _channel_ids_type_0 = data
                for channel_ids_type_0_item_data in _channel_ids_type_0:
                    channel_ids_type_0_item = UUID(channel_ids_type_0_item_data)

                    channel_ids_type_0.append(channel_ids_type_0_item)

                return channel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        channel_ids = _parse_channel_ids(d.pop("ChannelIds", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        def _parse_min_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                min_start_date_type_0 = isoparse(data)

                return min_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        min_start_date = _parse_min_start_date(d.pop("MinStartDate", UNSET))

        def _parse_has_aired(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_aired = _parse_has_aired(d.pop("HasAired", UNSET))

        def _parse_is_airing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_airing = _parse_is_airing(d.pop("IsAiring", UNSET))

        def _parse_max_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_start_date_type_0 = isoparse(data)

                return max_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        max_start_date = _parse_max_start_date(d.pop("MaxStartDate", UNSET))

        def _parse_min_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                min_end_date_type_0 = isoparse(data)

                return min_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        min_end_date = _parse_min_end_date(d.pop("MinEndDate", UNSET))

        def _parse_max_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_end_date_type_0 = isoparse(data)

                return max_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        max_end_date = _parse_max_end_date(d.pop("MaxEndDate", UNSET))

        def _parse_is_movie(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_movie = _parse_is_movie(d.pop("IsMovie", UNSET))

        def _parse_is_series(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_series = _parse_is_series(d.pop("IsSeries", UNSET))

        def _parse_is_news(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_news = _parse_is_news(d.pop("IsNews", UNSET))

        def _parse_is_kids(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_kids = _parse_is_kids(d.pop("IsKids", UNSET))

        def _parse_is_sports(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_sports = _parse_is_sports(d.pop("IsSports", UNSET))

        def _parse_start_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_index = _parse_start_index(d.pop("StartIndex", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("Limit", UNSET))

        def _parse_sort_by(data: object) -> list[ItemSortBy] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_by_type_0 = []
                _sort_by_type_0 = data
                for sort_by_type_0_item_data in _sort_by_type_0:
                    sort_by_type_0_item = ItemSortBy(sort_by_type_0_item_data)

                    sort_by_type_0.append(sort_by_type_0_item)

                return sort_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ItemSortBy] | None | Unset, data)

        sort_by = _parse_sort_by(d.pop("SortBy", UNSET))

        def _parse_sort_order(data: object) -> list[SortOrder] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_order_type_0 = []
                _sort_order_type_0 = data
                for sort_order_type_0_item_data in _sort_order_type_0:
                    sort_order_type_0_item = SortOrder(sort_order_type_0_item_data)

                    sort_order_type_0.append(sort_order_type_0_item)

                return sort_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SortOrder] | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("SortOrder", UNSET))

        def _parse_genres(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(list[str], data)

                return genres_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        genres = _parse_genres(d.pop("Genres", UNSET))

        def _parse_genre_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genre_ids_type_0 = []
                _genre_ids_type_0 = data
                for genre_ids_type_0_item_data in _genre_ids_type_0:
                    genre_ids_type_0_item = UUID(genre_ids_type_0_item_data)

                    genre_ids_type_0.append(genre_ids_type_0_item)

                return genre_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        genre_ids = _parse_genre_ids(d.pop("GenreIds", UNSET))

        def _parse_enable_images(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_images = _parse_enable_images(d.pop("EnableImages", UNSET))

        enable_total_record_count = d.pop("EnableTotalRecordCount", UNSET)

        def _parse_image_type_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_type_limit = _parse_image_type_limit(d.pop("ImageTypeLimit", UNSET))

        def _parse_enable_image_types(data: object) -> list[ImageType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enable_image_types_type_0 = []
                _enable_image_types_type_0 = data
                for enable_image_types_type_0_item_data in _enable_image_types_type_0:
                    enable_image_types_type_0_item = ImageType(
                        enable_image_types_type_0_item_data
                    )

                    enable_image_types_type_0.append(enable_image_types_type_0_item)

                return enable_image_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageType] | None | Unset, data)

        enable_image_types = _parse_enable_image_types(d.pop("EnableImageTypes", UNSET))

        def _parse_enable_user_data(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_user_data = _parse_enable_user_data(d.pop("EnableUserData", UNSET))

        def _parse_series_timer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series_timer_id = _parse_series_timer_id(d.pop("SeriesTimerId", UNSET))

        def _parse_library_series_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                library_series_id_type_0 = UUID(data)

                return library_series_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        library_series_id = _parse_library_series_id(d.pop("LibrarySeriesId", UNSET))

        def _parse_fields(data: object) -> list[ItemFields] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = ItemFields(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ItemFields] | None | Unset, data)

        fields = _parse_fields(d.pop("Fields", UNSET))

        get_programs_dto = cls(
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
            enable_total_record_count=enable_total_record_count,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            series_timer_id=series_timer_id,
            library_series_id=library_series_id,
            fields=fields,
        )

        return get_programs_dto
