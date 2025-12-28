from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueItem")


@_attrs_define
class QueueItem:
    """
    Attributes:
        id (UUID | Unset):
        playlist_item_id (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    playlist_item_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        playlist_item_id: None | str | Unset
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

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

        def _parse_playlist_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

        queue_item = cls(
            id=id,
            playlist_item_id=playlist_item_id,
        )

        return queue_item
