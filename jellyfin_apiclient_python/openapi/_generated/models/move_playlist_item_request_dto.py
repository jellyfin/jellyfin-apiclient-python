from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MovePlaylistItemRequestDto")


@_attrs_define
class MovePlaylistItemRequestDto:
    """Class MovePlaylistItemRequestDto.

    Attributes:
        playlist_item_id (UUID | Unset): Gets or sets the playlist identifier of the item.
        new_index (int | Unset): Gets or sets the new position.
    """

    playlist_item_id: UUID | Unset = UNSET
    new_index: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        playlist_item_id: str | Unset = UNSET
        if not isinstance(self.playlist_item_id, Unset):
            playlist_item_id = str(self.playlist_item_id)

        new_index = self.new_index

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if new_index is not UNSET:
            field_dict["NewIndex"] = new_index

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

        new_index = d.pop("NewIndex", UNSET)

        move_playlist_item_request_dto = cls(
            playlist_item_id=playlist_item_id,
            new_index=new_index,
        )

        return move_playlist_item_request_dto
