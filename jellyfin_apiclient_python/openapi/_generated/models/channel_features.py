from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.channel_item_sort_field import ChannelItemSortField
from ..models.channel_media_content_type import ChannelMediaContentType
from ..models.channel_media_type import ChannelMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelFeatures")


@_attrs_define
class ChannelFeatures:
    """
    Attributes:
        name (str | Unset): Gets or sets the name.
        id (UUID | Unset): Gets or sets the identifier.
        can_search (bool | Unset): Gets or sets a value indicating whether this instance can search.
        media_types (list[ChannelMediaType] | Unset): Gets or sets the media types.
        content_types (list[ChannelMediaContentType] | Unset): Gets or sets the content types.
        max_page_size (int | None | Unset): Gets or sets the maximum number of records the channel allows retrieving at
            a time.
        auto_refresh_levels (int | None | Unset): Gets or sets the automatic refresh levels.
        default_sort_fields (list[ChannelItemSortField] | Unset): Gets or sets the default sort orders.
        supports_sort_order_toggle (bool | Unset): Gets or sets a value indicating whether a sort ascending/descending
            toggle is supported.
        supports_latest_media (bool | Unset): Gets or sets a value indicating whether [supports latest media].
        can_filter (bool | Unset): Gets or sets a value indicating whether this instance can filter.
        supports_content_downloading (bool | Unset): Gets or sets a value indicating whether [supports content
            downloading].
    """

    name: str | Unset = UNSET
    id: UUID | Unset = UNSET
    can_search: bool | Unset = UNSET
    media_types: list[ChannelMediaType] | Unset = UNSET
    content_types: list[ChannelMediaContentType] | Unset = UNSET
    max_page_size: int | None | Unset = UNSET
    auto_refresh_levels: int | None | Unset = UNSET
    default_sort_fields: list[ChannelItemSortField] | Unset = UNSET
    supports_sort_order_toggle: bool | Unset = UNSET
    supports_latest_media: bool | Unset = UNSET
    can_filter: bool | Unset = UNSET
    supports_content_downloading: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        can_search = self.can_search

        media_types: list[str] | Unset = UNSET
        if not isinstance(self.media_types, Unset):
            media_types = []
            for media_types_item_data in self.media_types:
                media_types_item = media_types_item_data.value
                media_types.append(media_types_item)

        content_types: list[str] | Unset = UNSET
        if not isinstance(self.content_types, Unset):
            content_types = []
            for content_types_item_data in self.content_types:
                content_types_item = content_types_item_data.value
                content_types.append(content_types_item)

        max_page_size: int | None | Unset
        if isinstance(self.max_page_size, Unset):
            max_page_size = UNSET
        else:
            max_page_size = self.max_page_size

        auto_refresh_levels: int | None | Unset
        if isinstance(self.auto_refresh_levels, Unset):
            auto_refresh_levels = UNSET
        else:
            auto_refresh_levels = self.auto_refresh_levels

        default_sort_fields: list[str] | Unset = UNSET
        if not isinstance(self.default_sort_fields, Unset):
            default_sort_fields = []
            for default_sort_fields_item_data in self.default_sort_fields:
                default_sort_fields_item = default_sort_fields_item_data.value
                default_sort_fields.append(default_sort_fields_item)

        supports_sort_order_toggle = self.supports_sort_order_toggle

        supports_latest_media = self.supports_latest_media

        can_filter = self.can_filter

        supports_content_downloading = self.supports_content_downloading

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if can_search is not UNSET:
            field_dict["CanSearch"] = can_search
        if media_types is not UNSET:
            field_dict["MediaTypes"] = media_types
        if content_types is not UNSET:
            field_dict["ContentTypes"] = content_types
        if max_page_size is not UNSET:
            field_dict["MaxPageSize"] = max_page_size
        if auto_refresh_levels is not UNSET:
            field_dict["AutoRefreshLevels"] = auto_refresh_levels
        if default_sort_fields is not UNSET:
            field_dict["DefaultSortFields"] = default_sort_fields
        if supports_sort_order_toggle is not UNSET:
            field_dict["SupportsSortOrderToggle"] = supports_sort_order_toggle
        if supports_latest_media is not UNSET:
            field_dict["SupportsLatestMedia"] = supports_latest_media
        if can_filter is not UNSET:
            field_dict["CanFilter"] = can_filter
        if supports_content_downloading is not UNSET:
            field_dict["SupportsContentDownloading"] = supports_content_downloading

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        can_search = d.pop("CanSearch", UNSET)

        _media_types = d.pop("MediaTypes", UNSET)
        media_types: list[ChannelMediaType] | Unset = UNSET
        if _media_types is not UNSET:
            media_types = []
            for media_types_item_data in _media_types:
                media_types_item = ChannelMediaType(media_types_item_data)

                media_types.append(media_types_item)

        _content_types = d.pop("ContentTypes", UNSET)
        content_types: list[ChannelMediaContentType] | Unset = UNSET
        if _content_types is not UNSET:
            content_types = []
            for content_types_item_data in _content_types:
                content_types_item = ChannelMediaContentType(content_types_item_data)

                content_types.append(content_types_item)

        def _parse_max_page_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_page_size = _parse_max_page_size(d.pop("MaxPageSize", UNSET))

        def _parse_auto_refresh_levels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_refresh_levels = _parse_auto_refresh_levels(
            d.pop("AutoRefreshLevels", UNSET)
        )

        _default_sort_fields = d.pop("DefaultSortFields", UNSET)
        default_sort_fields: list[ChannelItemSortField] | Unset = UNSET
        if _default_sort_fields is not UNSET:
            default_sort_fields = []
            for default_sort_fields_item_data in _default_sort_fields:
                default_sort_fields_item = ChannelItemSortField(
                    default_sort_fields_item_data
                )

                default_sort_fields.append(default_sort_fields_item)

        supports_sort_order_toggle = d.pop("SupportsSortOrderToggle", UNSET)

        supports_latest_media = d.pop("SupportsLatestMedia", UNSET)

        can_filter = d.pop("CanFilter", UNSET)

        supports_content_downloading = d.pop("SupportsContentDownloading", UNSET)

        channel_features = cls(
            name=name,
            id=id,
            can_search=can_search,
            media_types=media_types,
            content_types=content_types,
            max_page_size=max_page_size,
            auto_refresh_levels=auto_refresh_levels,
            default_sort_fields=default_sort_fields,
            supports_sort_order_toggle=supports_sort_order_toggle,
            supports_latest_media=supports_latest_media,
            can_filter=can_filter,
            supports_content_downloading=supports_content_downloading,
        )

        return channel_features
