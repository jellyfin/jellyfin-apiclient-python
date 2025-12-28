from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrickplayInfoDto")


@_attrs_define
class TrickplayInfoDto:
    """The trickplay api model.

    Attributes:
        width (int | Unset): Gets the width of an individual thumbnail.
        height (int | Unset): Gets the height of an individual thumbnail.
        tile_width (int | Unset): Gets the amount of thumbnails per row.
        tile_height (int | Unset): Gets the amount of thumbnails per column.
        thumbnail_count (int | Unset): Gets the total amount of non-black thumbnails.
        interval (int | Unset): Gets the interval in milliseconds between each trickplay thumbnail.
        bandwidth (int | Unset): Gets the peak bandwidth usage in bits per second.
    """

    width: int | Unset = UNSET
    height: int | Unset = UNSET
    tile_width: int | Unset = UNSET
    tile_height: int | Unset = UNSET
    thumbnail_count: int | Unset = UNSET
    interval: int | Unset = UNSET
    bandwidth: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        tile_width = self.tile_width

        tile_height = self.tile_height

        thumbnail_count = self.thumbnail_count

        interval = self.interval

        bandwidth = self.bandwidth

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if tile_width is not UNSET:
            field_dict["TileWidth"] = tile_width
        if tile_height is not UNSET:
            field_dict["TileHeight"] = tile_height
        if thumbnail_count is not UNSET:
            field_dict["ThumbnailCount"] = thumbnail_count
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if bandwidth is not UNSET:
            field_dict["Bandwidth"] = bandwidth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        tile_width = d.pop("TileWidth", UNSET)

        tile_height = d.pop("TileHeight", UNSET)

        thumbnail_count = d.pop("ThumbnailCount", UNSET)

        interval = d.pop("Interval", UNSET)

        bandwidth = d.pop("Bandwidth", UNSET)

        trickplay_info_dto = cls(
            width=width,
            height=height,
            tile_width=tile_width,
            tile_height=tile_height,
            thumbnail_count=thumbnail_count,
            interval=interval,
            bandwidth=bandwidth,
        )

        return trickplay_info_dto
