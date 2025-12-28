from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.play_command import PlayCommand
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayRequest")


@_attrs_define
class PlayRequest:
    """Class PlayRequest.

    Attributes:
        item_ids (list[UUID] | None | Unset): Gets or sets the item ids.
        start_position_ticks (int | None | Unset): Gets or sets the start position ticks that the first item should be
            played at.
        play_command (PlayCommand | Unset): Enum PlayCommand.
        controlling_user_id (UUID | Unset): Gets or sets the controlling user identifier.
        subtitle_stream_index (int | None | Unset):
        audio_stream_index (int | None | Unset):
        media_source_id (None | str | Unset):
        start_index (int | None | Unset):
    """

    item_ids: list[UUID] | None | Unset = UNSET
    start_position_ticks: int | None | Unset = UNSET
    play_command: PlayCommand | Unset = UNSET
    controlling_user_id: UUID | Unset = UNSET
    subtitle_stream_index: int | None | Unset = UNSET
    audio_stream_index: int | None | Unset = UNSET
    media_source_id: None | str | Unset = UNSET
    start_index: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_ids: list[str] | None | Unset
        if isinstance(self.item_ids, Unset):
            item_ids = UNSET
        elif isinstance(self.item_ids, list):
            item_ids = []
            for item_ids_type_0_item_data in self.item_ids:
                item_ids_type_0_item = str(item_ids_type_0_item_data)
                item_ids.append(item_ids_type_0_item)

        else:
            item_ids = self.item_ids

        start_position_ticks: int | None | Unset
        if isinstance(self.start_position_ticks, Unset):
            start_position_ticks = UNSET
        else:
            start_position_ticks = self.start_position_ticks

        play_command: str | Unset = UNSET
        if not isinstance(self.play_command, Unset):
            play_command = self.play_command.value

        controlling_user_id: str | Unset = UNSET
        if not isinstance(self.controlling_user_id, Unset):
            controlling_user_id = str(self.controlling_user_id)

        subtitle_stream_index: int | None | Unset
        if isinstance(self.subtitle_stream_index, Unset):
            subtitle_stream_index = UNSET
        else:
            subtitle_stream_index = self.subtitle_stream_index

        audio_stream_index: int | None | Unset
        if isinstance(self.audio_stream_index, Unset):
            audio_stream_index = UNSET
        else:
            audio_stream_index = self.audio_stream_index

        media_source_id: None | str | Unset
        if isinstance(self.media_source_id, Unset):
            media_source_id = UNSET
        else:
            media_source_id = self.media_source_id

        start_index: int | None | Unset
        if isinstance(self.start_index, Unset):
            start_index = UNSET
        else:
            start_index = self.start_index

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if play_command is not UNSET:
            field_dict["PlayCommand"] = play_command
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_item_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                item_ids_type_0 = []
                _item_ids_type_0 = data
                for item_ids_type_0_item_data in _item_ids_type_0:
                    item_ids_type_0_item = UUID(item_ids_type_0_item_data)

                    item_ids_type_0.append(item_ids_type_0_item)

                return item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        item_ids = _parse_item_ids(d.pop("ItemIds", UNSET))

        def _parse_start_position_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_position_ticks = _parse_start_position_ticks(
            d.pop("StartPositionTicks", UNSET)
        )

        _play_command = d.pop("PlayCommand", UNSET)
        play_command: PlayCommand | Unset
        if isinstance(_play_command, Unset):
            play_command = UNSET
        else:
            play_command = PlayCommand(_play_command)

        _controlling_user_id = d.pop("ControllingUserId", UNSET)
        controlling_user_id: UUID | Unset
        if isinstance(_controlling_user_id, Unset):
            controlling_user_id = UNSET
        else:
            controlling_user_id = UUID(_controlling_user_id)

        def _parse_subtitle_stream_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subtitle_stream_index = _parse_subtitle_stream_index(
            d.pop("SubtitleStreamIndex", UNSET)
        )

        def _parse_audio_stream_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_stream_index = _parse_audio_stream_index(d.pop("AudioStreamIndex", UNSET))

        def _parse_media_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_source_id = _parse_media_source_id(d.pop("MediaSourceId", UNSET))

        def _parse_start_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_index = _parse_start_index(d.pop("StartIndex", UNSET))

        play_request = cls(
            item_ids=item_ids,
            start_position_ticks=start_position_ticks,
            play_command=play_command,
            controlling_user_id=controlling_user_id,
            subtitle_stream_index=subtitle_stream_index,
            audio_stream_index=audio_stream_index,
            media_source_id=media_source_id,
            start_index=start_index,
        )

        return play_request
