from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto
    from ..models.queue_item import QueueItem


T = TypeVar("T", bound="PlaybackStopInfo")


@_attrs_define
class PlaybackStopInfo:
    """Class PlaybackStopInfo.

    Attributes:
        item (BaseItemDto | None | Unset): Gets or sets the item.
        item_id (UUID | Unset): Gets or sets the item identifier.
        session_id (None | str | Unset): Gets or sets the session id.
        media_source_id (None | str | Unset): Gets or sets the media version identifier.
        position_ticks (int | None | Unset): Gets or sets the position ticks.
        live_stream_id (None | str | Unset): Gets or sets the live stream identifier.
        play_session_id (None | str | Unset): Gets or sets the play session identifier.
        failed (bool | Unset): Gets or sets a value indicating whether this MediaBrowser.Model.Session.PlaybackStopInfo
            is failed.
        next_media_type (None | str | Unset):
        playlist_item_id (None | str | Unset):
        now_playing_queue (list[QueueItem] | None | Unset):
    """

    item: BaseItemDto | None | Unset = UNSET
    item_id: UUID | Unset = UNSET
    session_id: None | str | Unset = UNSET
    media_source_id: None | str | Unset = UNSET
    position_ticks: int | None | Unset = UNSET
    live_stream_id: None | str | Unset = UNSET
    play_session_id: None | str | Unset = UNSET
    failed: bool | Unset = UNSET
    next_media_type: None | str | Unset = UNSET
    playlist_item_id: None | str | Unset = UNSET
    now_playing_queue: list[QueueItem] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_item_dto import BaseItemDto

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

        position_ticks: int | None | Unset
        if isinstance(self.position_ticks, Unset):
            position_ticks = UNSET
        else:
            position_ticks = self.position_ticks

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

        failed = self.failed

        next_media_type: None | str | Unset
        if isinstance(self.next_media_type, Unset):
            next_media_type = UNSET
        else:
            next_media_type = self.next_media_type

        playlist_item_id: None | str | Unset
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item is not UNSET:
            field_dict["Item"] = item
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if session_id is not UNSET:
            field_dict["SessionId"] = session_id
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if failed is not UNSET:
            field_dict["Failed"] = failed
        if next_media_type is not UNSET:
            field_dict["NextMediaType"] = next_media_type
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto
        from ..models.queue_item import QueueItem

        d = dict(src_dict)

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

        def _parse_position_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_ticks = _parse_position_ticks(d.pop("PositionTicks", UNSET))

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

        failed = d.pop("Failed", UNSET)

        def _parse_next_media_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_media_type = _parse_next_media_type(d.pop("NextMediaType", UNSET))

        def _parse_playlist_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

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

        playback_stop_info = cls(
            item=item,
            item_id=item_id,
            session_id=session_id,
            media_source_id=media_source_id,
            position_ticks=position_ticks,
            live_stream_id=live_stream_id,
            play_session_id=play_session_id,
            failed=failed,
            next_media_type=next_media_type,
            playlist_item_id=playlist_item_id,
            now_playing_queue=now_playing_queue,
        )

        return playback_stop_info
