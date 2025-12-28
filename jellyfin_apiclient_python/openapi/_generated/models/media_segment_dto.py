from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.media_segment_type import MediaSegmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaSegmentDto")


@_attrs_define
class MediaSegmentDto:
    """Api model for MediaSegment's.

    Attributes:
        id (UUID | Unset): Gets or sets the id of the media segment.
        item_id (UUID | Unset): Gets or sets the id of the associated item.
        type_ (MediaSegmentType | Unset): Defines the types of content an individual
            Jellyfin.Database.Implementations.Entities.MediaSegment represents. Default: MediaSegmentType.UNKNOWN.
        start_ticks (int | Unset): Gets or sets the start of the segment.
        end_ticks (int | Unset): Gets or sets the end of the segment.
    """

    id: UUID | Unset = UNSET
    item_id: UUID | Unset = UNSET
    type_: MediaSegmentType | Unset = MediaSegmentType.UNKNOWN
    start_ticks: int | Unset = UNSET
    end_ticks: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        item_id: str | Unset = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        start_ticks = self.start_ticks

        end_ticks = self.end_ticks

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if start_ticks is not UNSET:
            field_dict["StartTicks"] = start_ticks
        if end_ticks is not UNSET:
            field_dict["EndTicks"] = end_ticks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _item_id = d.pop("ItemId", UNSET)
        item_id: UUID | Unset
        if isinstance(_item_id, Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)

        _type_ = d.pop("Type", UNSET)
        type_: MediaSegmentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MediaSegmentType(_type_)

        start_ticks = d.pop("StartTicks", UNSET)

        end_ticks = d.pop("EndTicks", UNSET)

        media_segment_dto = cls(
            id=id,
            item_id=item_id,
            type_=type_,
            start_ticks=start_ticks,
            end_ticks=end_ticks,
        )

        return media_segment_dto
