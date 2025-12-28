from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveFromPlaylistRequestDto")


@_attrs_define
class RemoveFromPlaylistRequestDto:
    """Class RemoveFromPlaylistRequestDto.

    Attributes:
        playlist_item_ids (list[UUID] | Unset): Gets or sets the playlist identifiers of the items. Ignored when
            clearing the playlist.
        clear_playlist (bool | Unset): Gets or sets a value indicating whether the entire playlist should be cleared.
        clear_playing_item (bool | Unset): Gets or sets a value indicating whether the playing item should be removed as
            well. Used only when clearing the playlist.
    """

    playlist_item_ids: list[UUID] | Unset = UNSET
    clear_playlist: bool | Unset = UNSET
    clear_playing_item: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        playlist_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.playlist_item_ids, Unset):
            playlist_item_ids = []
            for playlist_item_ids_item_data in self.playlist_item_ids:
                playlist_item_ids_item = str(playlist_item_ids_item_data)
                playlist_item_ids.append(playlist_item_ids_item)

        clear_playlist = self.clear_playlist

        clear_playing_item = self.clear_playing_item

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playlist_item_ids is not UNSET:
            field_dict["PlaylistItemIds"] = playlist_item_ids
        if clear_playlist is not UNSET:
            field_dict["ClearPlaylist"] = clear_playlist
        if clear_playing_item is not UNSET:
            field_dict["ClearPlayingItem"] = clear_playing_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _playlist_item_ids = d.pop("PlaylistItemIds", UNSET)
        playlist_item_ids: list[UUID] | Unset = UNSET
        if _playlist_item_ids is not UNSET:
            playlist_item_ids = []
            for playlist_item_ids_item_data in _playlist_item_ids:
                playlist_item_ids_item = UUID(playlist_item_ids_item_data)

                playlist_item_ids.append(playlist_item_ids_item)

        clear_playlist = d.pop("ClearPlaylist", UNSET)

        clear_playing_item = d.pop("ClearPlayingItem", UNSET)

        remove_from_playlist_request_dto = cls(
            playlist_item_ids=playlist_item_ids,
            clear_playlist=clear_playlist,
            clear_playing_item=clear_playing_item,
        )

        return remove_from_playlist_request_dto
