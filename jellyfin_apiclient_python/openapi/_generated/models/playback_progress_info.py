from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.play_method import PlayMethod
from ..models.playback_order import PlaybackOrder
from ..models.repeat_mode import RepeatMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto
    from ..models.queue_item import QueueItem


T = TypeVar("T", bound="PlaybackProgressInfo")


@_attrs_define
class PlaybackProgressInfo:
    """Class PlaybackProgressInfo.

    Attributes:
        can_seek (bool | Unset): Gets or sets a value indicating whether this instance can seek.
        item (BaseItemDto | None | Unset): Gets or sets the item.
        item_id (UUID | Unset): Gets or sets the item identifier.
        session_id (None | str | Unset): Gets or sets the session id.
        media_source_id (None | str | Unset): Gets or sets the media version identifier.
        audio_stream_index (int | None | Unset): Gets or sets the index of the audio stream.
        subtitle_stream_index (int | None | Unset): Gets or sets the index of the subtitle stream.
        is_paused (bool | Unset): Gets or sets a value indicating whether this instance is paused.
        is_muted (bool | Unset): Gets or sets a value indicating whether this instance is muted.
        position_ticks (int | None | Unset): Gets or sets the position ticks.
        playback_start_time_ticks (int | None | Unset):
        volume_level (int | None | Unset): Gets or sets the volume level.
        brightness (int | None | Unset):
        aspect_ratio (None | str | Unset):
        play_method (PlayMethod | Unset):
        live_stream_id (None | str | Unset): Gets or sets the live stream identifier.
        play_session_id (None | str | Unset): Gets or sets the play session identifier.
        repeat_mode (RepeatMode | Unset):
        playback_order (PlaybackOrder | Unset): Enum PlaybackOrder.
        now_playing_queue (list[QueueItem] | None | Unset):
        playlist_item_id (None | str | Unset):
    """

    can_seek: bool | Unset = UNSET
    item: BaseItemDto | None | Unset = UNSET
    item_id: UUID | Unset = UNSET
    session_id: None | str | Unset = UNSET
    media_source_id: None | str | Unset = UNSET
    audio_stream_index: int | None | Unset = UNSET
    subtitle_stream_index: int | None | Unset = UNSET
    is_paused: bool | Unset = UNSET
    is_muted: bool | Unset = UNSET
    position_ticks: int | None | Unset = UNSET
    playback_start_time_ticks: int | None | Unset = UNSET
    volume_level: int | None | Unset = UNSET
    brightness: int | None | Unset = UNSET
    aspect_ratio: None | str | Unset = UNSET
    play_method: PlayMethod | Unset = UNSET
    live_stream_id: None | str | Unset = UNSET
    play_session_id: None | str | Unset = UNSET
    repeat_mode: RepeatMode | Unset = UNSET
    playback_order: PlaybackOrder | Unset = UNSET
    now_playing_queue: list[QueueItem] | None | Unset = UNSET
    playlist_item_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_item_dto import BaseItemDto

        can_seek = self.can_seek

        item: dict[str, Any] | None | Unset
        if isinstance(self.item, Unset):
            item = UNSET
        elif isinstance(self.item, BaseItemDto):
            item = self.item.to_dict()
        else:
            item = self.item

        item_id: str | Unset = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        media_source_id: None | str | Unset
        if isinstance(self.media_source_id, Unset):
            media_source_id = UNSET
        else:
            media_source_id = self.media_source_id

        audio_stream_index: int | None | Unset
        if isinstance(self.audio_stream_index, Unset):
            audio_stream_index = UNSET
        else:
            audio_stream_index = self.audio_stream_index

        subtitle_stream_index: int | None | Unset
        if isinstance(self.subtitle_stream_index, Unset):
            subtitle_stream_index = UNSET
        else:
            subtitle_stream_index = self.subtitle_stream_index

        is_paused = self.is_paused

        is_muted = self.is_muted

        position_ticks: int | None | Unset
        if isinstance(self.position_ticks, Unset):
            position_ticks = UNSET
        else:
            position_ticks = self.position_ticks

        playback_start_time_ticks: int | None | Unset
        if isinstance(self.playback_start_time_ticks, Unset):
            playback_start_time_ticks = UNSET
        else:
            playback_start_time_ticks = self.playback_start_time_ticks

        volume_level: int | None | Unset
        if isinstance(self.volume_level, Unset):
            volume_level = UNSET
        else:
            volume_level = self.volume_level

        brightness: int | None | Unset
        if isinstance(self.brightness, Unset):
            brightness = UNSET
        else:
            brightness = self.brightness

        aspect_ratio: None | str | Unset
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        play_method: str | Unset = UNSET
        if not isinstance(self.play_method, Unset):
            play_method = self.play_method.value

        live_stream_id: None | str | Unset
        if isinstance(self.live_stream_id, Unset):
            live_stream_id = UNSET
        else:
            live_stream_id = self.live_stream_id

        play_session_id: None | str | Unset
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        repeat_mode: str | Unset = UNSET
        if not isinstance(self.repeat_mode, Unset):
            repeat_mode = self.repeat_mode.value

        playback_order: str | Unset = UNSET
        if not isinstance(self.playback_order, Unset):
            playback_order = self.playback_order.value

        now_playing_queue: list[dict[str, Any]] | None | Unset
        if isinstance(self.now_playing_queue, Unset):
            now_playing_queue = UNSET
        elif isinstance(self.now_playing_queue, list):
            now_playing_queue = []
            for now_playing_queue_type_0_item_data in self.now_playing_queue:
                now_playing_queue_type_0_item = (
                    now_playing_queue_type_0_item_data.to_dict()
                )
                now_playing_queue.append(now_playing_queue_type_0_item)

        else:
            now_playing_queue = self.now_playing_queue

        playlist_item_id: None | str | Unset
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_seek is not UNSET:
            field_dict["CanSeek"] = can_seek
        if item is not UNSET:
            field_dict["Item"] = item
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if session_id is not UNSET:
            field_dict["SessionId"] = session_id
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if is_paused is not UNSET:
            field_dict["IsPaused"] = is_paused
        if is_muted is not UNSET:
            field_dict["IsMuted"] = is_muted
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if playback_start_time_ticks is not UNSET:
            field_dict["PlaybackStartTimeTicks"] = playback_start_time_ticks
        if volume_level is not UNSET:
            field_dict["VolumeLevel"] = volume_level
        if brightness is not UNSET:
            field_dict["Brightness"] = brightness
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if play_method is not UNSET:
            field_dict["PlayMethod"] = play_method
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if repeat_mode is not UNSET:
            field_dict["RepeatMode"] = repeat_mode
        if playback_order is not UNSET:
            field_dict["PlaybackOrder"] = playback_order
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto
        from ..models.queue_item import QueueItem

        d = dict(src_dict)
        can_seek = d.pop("CanSeek", UNSET)

        def _parse_item(data: object) -> BaseItemDto | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_1 = BaseItemDto.from_dict(data)

                return item_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseItemDto | None | Unset, data)

        item = _parse_item(d.pop("Item", UNSET))

        _item_id = d.pop("ItemId", UNSET)
        item_id: UUID | Unset
        if isinstance(_item_id, Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("SessionId", UNSET))

        def _parse_media_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_source_id = _parse_media_source_id(d.pop("MediaSourceId", UNSET))

        def _parse_audio_stream_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_stream_index = _parse_audio_stream_index(d.pop("AudioStreamIndex", UNSET))

        def _parse_subtitle_stream_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subtitle_stream_index = _parse_subtitle_stream_index(
            d.pop("SubtitleStreamIndex", UNSET)
        )

        is_paused = d.pop("IsPaused", UNSET)

        is_muted = d.pop("IsMuted", UNSET)

        def _parse_position_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_ticks = _parse_position_ticks(d.pop("PositionTicks", UNSET))

        def _parse_playback_start_time_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        playback_start_time_ticks = _parse_playback_start_time_ticks(
            d.pop("PlaybackStartTimeTicks", UNSET)
        )

        def _parse_volume_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_level = _parse_volume_level(d.pop("VolumeLevel", UNSET))

        def _parse_brightness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        brightness = _parse_brightness(d.pop("Brightness", UNSET))

        def _parse_aspect_ratio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aspect_ratio = _parse_aspect_ratio(d.pop("AspectRatio", UNSET))

        _play_method = d.pop("PlayMethod", UNSET)
        play_method: PlayMethod | Unset
        if isinstance(_play_method, Unset):
            play_method = UNSET
        else:
            play_method = PlayMethod(_play_method)

        def _parse_live_stream_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        live_stream_id = _parse_live_stream_id(d.pop("LiveStreamId", UNSET))

        def _parse_play_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        _repeat_mode = d.pop("RepeatMode", UNSET)
        repeat_mode: RepeatMode | Unset
        if isinstance(_repeat_mode, Unset):
            repeat_mode = UNSET
        else:
            repeat_mode = RepeatMode(_repeat_mode)

        _playback_order = d.pop("PlaybackOrder", UNSET)
        playback_order: PlaybackOrder | Unset
        if isinstance(_playback_order, Unset):
            playback_order = UNSET
        else:
            playback_order = PlaybackOrder(_playback_order)

        def _parse_now_playing_queue(data: object) -> list[QueueItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                now_playing_queue_type_0 = []
                _now_playing_queue_type_0 = data
                for now_playing_queue_type_0_item_data in _now_playing_queue_type_0:
                    now_playing_queue_type_0_item = QueueItem.from_dict(
                        now_playing_queue_type_0_item_data
                    )

                    now_playing_queue_type_0.append(now_playing_queue_type_0_item)

                return now_playing_queue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[QueueItem] | None | Unset, data)

        now_playing_queue = _parse_now_playing_queue(d.pop("NowPlayingQueue", UNSET))

        def _parse_playlist_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

        playback_progress_info = cls(
            can_seek=can_seek,
            item=item,
            item_id=item_id,
            session_id=session_id,
            media_source_id=media_source_id,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            is_paused=is_paused,
            is_muted=is_muted,
            position_ticks=position_ticks,
            playback_start_time_ticks=playback_start_time_ticks,
            volume_level=volume_level,
            brightness=brightness,
            aspect_ratio=aspect_ratio,
            play_method=play_method,
            live_stream_id=live_stream_id,
            play_session_id=play_session_id,
            repeat_mode=repeat_mode,
            playback_order=playback_order,
            now_playing_queue=now_playing_queue,
            playlist_item_id=playlist_item_id,
        )

        return playback_progress_info
