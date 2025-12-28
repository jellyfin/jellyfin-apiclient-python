from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.group_repeat_mode import GroupRepeatMode
from ..models.group_shuffle_mode import GroupShuffleMode
from ..models.play_queue_update_reason import PlayQueueUpdateReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_play_queue_item import SyncPlayQueueItem


T = TypeVar("T", bound="PlayQueueUpdate")


@_attrs_define
class PlayQueueUpdate:
    """Class PlayQueueUpdate.

    Attributes:
        reason (PlayQueueUpdateReason | Unset): Enum PlayQueueUpdateReason.
        last_update (datetime.datetime | Unset): Gets the UTC time of the last change to the playing queue.
        playlist (list[SyncPlayQueueItem] | Unset): Gets the playlist.
        playing_item_index (int | Unset): Gets the playing item index in the playlist.
        start_position_ticks (int | Unset): Gets the start position ticks.
        is_playing (bool | Unset): Gets a value indicating whether the current item is playing.
        shuffle_mode (GroupShuffleMode | Unset): Enum GroupShuffleMode.
        repeat_mode (GroupRepeatMode | Unset): Enum GroupRepeatMode.
    """

    reason: PlayQueueUpdateReason | Unset = UNSET
    last_update: datetime.datetime | Unset = UNSET
    playlist: list[SyncPlayQueueItem] | Unset = UNSET
    playing_item_index: int | Unset = UNSET
    start_position_ticks: int | Unset = UNSET
    is_playing: bool | Unset = UNSET
    shuffle_mode: GroupShuffleMode | Unset = UNSET
    repeat_mode: GroupRepeatMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        last_update: str | Unset = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        playlist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.playlist, Unset):
            playlist = []
            for playlist_item_data in self.playlist:
                playlist_item = playlist_item_data.to_dict()
                playlist.append(playlist_item)

        playing_item_index = self.playing_item_index

        start_position_ticks = self.start_position_ticks

        is_playing = self.is_playing

        shuffle_mode: str | Unset = UNSET
        if not isinstance(self.shuffle_mode, Unset):
            shuffle_mode = self.shuffle_mode.value

        repeat_mode: str | Unset = UNSET
        if not isinstance(self.repeat_mode, Unset):
            repeat_mode = self.repeat_mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update
        if playlist is not UNSET:
            field_dict["Playlist"] = playlist
        if playing_item_index is not UNSET:
            field_dict["PlayingItemIndex"] = playing_item_index
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if is_playing is not UNSET:
            field_dict["IsPlaying"] = is_playing
        if shuffle_mode is not UNSET:
            field_dict["ShuffleMode"] = shuffle_mode
        if repeat_mode is not UNSET:
            field_dict["RepeatMode"] = repeat_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_play_queue_item import SyncPlayQueueItem

        d = dict(src_dict)
        _reason = d.pop("Reason", UNSET)
        reason: PlayQueueUpdateReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PlayQueueUpdateReason(_reason)

        _last_update = d.pop("LastUpdate", UNSET)
        last_update: datetime.datetime | Unset
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update)

        _playlist = d.pop("Playlist", UNSET)
        playlist: list[SyncPlayQueueItem] | Unset = UNSET
        if _playlist is not UNSET:
            playlist = []
            for playlist_item_data in _playlist:
                playlist_item = SyncPlayQueueItem.from_dict(playlist_item_data)

                playlist.append(playlist_item)

        playing_item_index = d.pop("PlayingItemIndex", UNSET)

        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        is_playing = d.pop("IsPlaying", UNSET)

        _shuffle_mode = d.pop("ShuffleMode", UNSET)
        shuffle_mode: GroupShuffleMode | Unset
        if isinstance(_shuffle_mode, Unset):
            shuffle_mode = UNSET
        else:
            shuffle_mode = GroupShuffleMode(_shuffle_mode)

        _repeat_mode = d.pop("RepeatMode", UNSET)
        repeat_mode: GroupRepeatMode | Unset
        if isinstance(_repeat_mode, Unset):
            repeat_mode = UNSET
        else:
            repeat_mode = GroupRepeatMode(_repeat_mode)

        play_queue_update = cls(
            reason=reason,
            last_update=last_update,
            playlist=playlist,
            playing_item_index=playing_item_index,
            start_position_ticks=start_position_ticks,
            is_playing=is_playing,
            shuffle_mode=shuffle_mode,
            repeat_mode=repeat_mode,
        )

        return play_queue_update
