from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.playback_info_response_error_code import PlaybackInfoResponseErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_source_info import MediaSourceInfo


T = TypeVar("T", bound="PlaybackInfoResponse")


@_attrs_define
class PlaybackInfoResponse:
    """Class PlaybackInfoResponse.

    Attributes:
        media_sources (list[MediaSourceInfo] | Unset): Gets or sets the media sources.
        play_session_id (None | str | Unset): Gets or sets the play session identifier.
        error_code (PlaybackInfoResponseErrorCode | Unset): Gets or sets the error code.
    """

    media_sources: list[MediaSourceInfo] | Unset = UNSET
    play_session_id: None | str | Unset = UNSET
    error_code: PlaybackInfoResponseErrorCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media_sources, Unset):
            media_sources = []
            for media_sources_item_data in self.media_sources:
                media_sources_item = media_sources_item_data.to_dict()
                media_sources.append(media_sources_item)

        play_session_id: None | str | Unset
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_sources is not UNSET:
            field_dict["MediaSources"] = media_sources
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_source_info import MediaSourceInfo

        d = dict(src_dict)
        _media_sources = d.pop("MediaSources", UNSET)
        media_sources: list[MediaSourceInfo] | Unset = UNSET
        if _media_sources is not UNSET:
            media_sources = []
            for media_sources_item_data in _media_sources:
                media_sources_item = MediaSourceInfo.from_dict(media_sources_item_data)

                media_sources.append(media_sources_item)

        def _parse_play_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        _error_code = d.pop("ErrorCode", UNSET)
        error_code: PlaybackInfoResponseErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = PlaybackInfoResponseErrorCode(_error_code)

        playback_info_response = cls(
            media_sources=media_sources,
            play_session_id=play_session_id,
            error_code=error_code,
        )

        return playback_info_response
