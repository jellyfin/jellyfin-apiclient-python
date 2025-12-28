from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NextItemRequestDto")


@_attrs_define
class NextItemRequestDto:
    """Class NextItemRequestDto.

    Attributes:
        playlist_item_id (UUID | Unset): Gets or sets the playing item identifier.
    """

    playlist_item_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        playlist_item_id: str | Unset = UNSET
        if not isinstance(self.playlist_item_id, Unset):
            playlist_item_id = str(self.playlist_item_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _playlist_item_id = d.pop("PlaylistItemId", UNSET)
        playlist_item_id: UUID | Unset
        if isinstance(_playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = UUID(_playlist_item_id)

        next_item_request_dto = cls(
            playlist_item_id=playlist_item_id,
        )

        return next_item_request_dto
