from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.media_protocol import MediaProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="OpenLiveStreamDto")


@_attrs_define
class OpenLiveStreamDto:
    """Open live stream dto.

    Attributes:
        open_token (None | str | Unset): Gets or sets the open token.
        user_id (None | Unset | UUID): Gets or sets the user id.
        play_session_id (None | str | Unset): Gets or sets the play session id.
        max_streaming_bitrate (int | None | Unset): Gets or sets the max streaming bitrate.
        start_time_ticks (int | None | Unset): Gets or sets the start time in ticks.
        audio_stream_index (int | None | Unset): Gets or sets the audio stream index.
        subtitle_stream_index (int | None | Unset): Gets or sets the subtitle stream index.
        max_audio_channels (int | None | Unset): Gets or sets the max audio channels.
        item_id (None | Unset | UUID): Gets or sets the item id.
        enable_direct_play (bool | None | Unset): Gets or sets a value indicating whether to enable direct play.
        enable_direct_stream (bool | None | Unset): Gets or sets a value indicating whether to enable direct stream.
        always_burn_in_subtitle_when_transcoding (bool | None | Unset): Gets or sets a value indicating whether always
            burn in subtitles when transcoding.
        device_profile (DeviceProfile | None | Unset): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of
            metadata which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including
            codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        direct_play_protocols (list[MediaProtocol] | Unset): Gets or sets the device play protocols.
    """

    open_token: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    play_session_id: None | str | Unset = UNSET
    max_streaming_bitrate: int | None | Unset = UNSET
    start_time_ticks: int | None | Unset = UNSET
    audio_stream_index: int | None | Unset = UNSET
    subtitle_stream_index: int | None | Unset = UNSET
    max_audio_channels: int | None | Unset = UNSET
    item_id: None | Unset | UUID = UNSET
    enable_direct_play: bool | None | Unset = UNSET
    enable_direct_stream: bool | None | Unset = UNSET
    always_burn_in_subtitle_when_transcoding: bool | None | Unset = UNSET
    device_profile: DeviceProfile | None | Unset = UNSET
    direct_play_protocols: list[MediaProtocol] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.device_profile import DeviceProfile

        open_token: None | str | Unset
        if isinstance(self.open_token, Unset):
            open_token = UNSET
        else:
            open_token = self.open_token

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        play_session_id: None | str | Unset
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        max_streaming_bitrate: int | None | Unset
        if isinstance(self.max_streaming_bitrate, Unset):
            max_streaming_bitrate = UNSET
        else:
            max_streaming_bitrate = self.max_streaming_bitrate

        start_time_ticks: int | None | Unset
        if isinstance(self.start_time_ticks, Unset):
            start_time_ticks = UNSET
        else:
            start_time_ticks = self.start_time_ticks

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

        max_audio_channels: int | None | Unset
        if isinstance(self.max_audio_channels, Unset):
            max_audio_channels = UNSET
        else:
            max_audio_channels = self.max_audio_channels

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        enable_direct_play: bool | None | Unset
        if isinstance(self.enable_direct_play, Unset):
            enable_direct_play = UNSET
        else:
            enable_direct_play = self.enable_direct_play

        enable_direct_stream: bool | None | Unset
        if isinstance(self.enable_direct_stream, Unset):
            enable_direct_stream = UNSET
        else:
            enable_direct_stream = self.enable_direct_stream

        always_burn_in_subtitle_when_transcoding: bool | None | Unset
        if isinstance(self.always_burn_in_subtitle_when_transcoding, Unset):
            always_burn_in_subtitle_when_transcoding = UNSET
        else:
            always_burn_in_subtitle_when_transcoding = (
                self.always_burn_in_subtitle_when_transcoding
            )

        device_profile: dict[str, Any] | None | Unset
        if isinstance(self.device_profile, Unset):
            device_profile = UNSET
        elif isinstance(self.device_profile, DeviceProfile):
            device_profile = self.device_profile.to_dict()
        else:
            device_profile = self.device_profile

        direct_play_protocols: list[str] | Unset = UNSET
        if not isinstance(self.direct_play_protocols, Unset):
            direct_play_protocols = []
            for direct_play_protocols_item_data in self.direct_play_protocols:
                direct_play_protocols_item = direct_play_protocols_item_data.value
                direct_play_protocols.append(direct_play_protocols_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if open_token is not UNSET:
            field_dict["OpenToken"] = open_token
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if max_streaming_bitrate is not UNSET:
            field_dict["MaxStreamingBitrate"] = max_streaming_bitrate
        if start_time_ticks is not UNSET:
            field_dict["StartTimeTicks"] = start_time_ticks
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if max_audio_channels is not UNSET:
            field_dict["MaxAudioChannels"] = max_audio_channels
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if enable_direct_play is not UNSET:
            field_dict["EnableDirectPlay"] = enable_direct_play
        if enable_direct_stream is not UNSET:
            field_dict["EnableDirectStream"] = enable_direct_stream
        if always_burn_in_subtitle_when_transcoding is not UNSET:
            field_dict["AlwaysBurnInSubtitleWhenTranscoding"] = (
                always_burn_in_subtitle_when_transcoding
            )
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if direct_play_protocols is not UNSET:
            field_dict["DirectPlayProtocols"] = direct_play_protocols

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = dict(src_dict)

        def _parse_open_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_token = _parse_open_token(d.pop("OpenToken", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        def _parse_play_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        def _parse_max_streaming_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_streaming_bitrate = _parse_max_streaming_bitrate(
            d.pop("MaxStreamingBitrate", UNSET)
        )

        def _parse_start_time_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time_ticks = _parse_start_time_ticks(d.pop("StartTimeTicks", UNSET))

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

        def _parse_max_audio_channels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_audio_channels = _parse_max_audio_channels(d.pop("MaxAudioChannels", UNSET))

        def _parse_item_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                item_id_type_0 = UUID(data)

                return item_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        item_id = _parse_item_id(d.pop("ItemId", UNSET))

        def _parse_enable_direct_play(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_direct_play = _parse_enable_direct_play(d.pop("EnableDirectPlay", UNSET))

        def _parse_enable_direct_stream(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_direct_stream = _parse_enable_direct_stream(
            d.pop("EnableDirectStream", UNSET)
        )

        def _parse_always_burn_in_subtitle_when_transcoding(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        always_burn_in_subtitle_when_transcoding = (
            _parse_always_burn_in_subtitle_when_transcoding(
                d.pop("AlwaysBurnInSubtitleWhenTranscoding", UNSET)
            )
        )

        def _parse_device_profile(data: object) -> DeviceProfile | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_profile_type_1 = DeviceProfile.from_dict(data)

                return device_profile_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeviceProfile | None | Unset, data)

        device_profile = _parse_device_profile(d.pop("DeviceProfile", UNSET))

        _direct_play_protocols = d.pop("DirectPlayProtocols", UNSET)
        direct_play_protocols: list[MediaProtocol] | Unset = UNSET
        if _direct_play_protocols is not UNSET:
            direct_play_protocols = []
            for direct_play_protocols_item_data in _direct_play_protocols:
                direct_play_protocols_item = MediaProtocol(
                    direct_play_protocols_item_data
                )

                direct_play_protocols.append(direct_play_protocols_item)

        open_live_stream_dto = cls(
            open_token=open_token,
            user_id=user_id,
            play_session_id=play_session_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            item_id=item_id,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding,
            device_profile=device_profile,
            direct_play_protocols=direct_play_protocols,
        )

        return open_live_stream_dto
