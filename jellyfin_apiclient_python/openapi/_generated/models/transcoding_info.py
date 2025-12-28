from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.transcoding_info_hardware_acceleration_type import (
    TranscodingInfoHardwareAccelerationType,
)
from ..models.transcoding_info_transcode_reasons import TranscodingInfoTranscodeReasons
from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodingInfo")


@_attrs_define
class TranscodingInfo:
    """Class holding information on a running transcode.

    Attributes:
        audio_codec (None | str | Unset): Gets or sets the thread count used for encoding.
        video_codec (None | str | Unset): Gets or sets the thread count used for encoding.
        container (None | str | Unset): Gets or sets the thread count used for encoding.
        is_video_direct (bool | Unset): Gets or sets a value indicating whether the video is passed through.
        is_audio_direct (bool | Unset): Gets or sets a value indicating whether the audio is passed through.
        bitrate (int | None | Unset): Gets or sets the bitrate.
        framerate (float | None | Unset): Gets or sets the framerate.
        completion_percentage (float | None | Unset): Gets or sets the completion percentage.
        width (int | None | Unset): Gets or sets the video width.
        height (int | None | Unset): Gets or sets the video height.
        audio_channels (int | None | Unset): Gets or sets the audio channels.
        hardware_acceleration_type (TranscodingInfoHardwareAccelerationType | Unset): Gets or sets the hardware
            acceleration type.
        transcode_reasons (TranscodingInfoTranscodeReasons | Unset): Gets or sets the transcode reasons.
    """

    audio_codec: None | str | Unset = UNSET
    video_codec: None | str | Unset = UNSET
    container: None | str | Unset = UNSET
    is_video_direct: bool | Unset = UNSET
    is_audio_direct: bool | Unset = UNSET
    bitrate: int | None | Unset = UNSET
    framerate: float | None | Unset = UNSET
    completion_percentage: float | None | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    audio_channels: int | None | Unset = UNSET
    hardware_acceleration_type: TranscodingInfoHardwareAccelerationType | Unset = UNSET
    transcode_reasons: TranscodingInfoTranscodeReasons | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_codec: None | str | Unset
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        video_codec: None | str | Unset
        if isinstance(self.video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = self.video_codec

        container: None | str | Unset
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        is_video_direct = self.is_video_direct

        is_audio_direct = self.is_audio_direct

        bitrate: int | None | Unset
        if isinstance(self.bitrate, Unset):
            bitrate = UNSET
        else:
            bitrate = self.bitrate

        framerate: float | None | Unset
        if isinstance(self.framerate, Unset):
            framerate = UNSET
        else:
            framerate = self.framerate

        completion_percentage: float | None | Unset
        if isinstance(self.completion_percentage, Unset):
            completion_percentage = UNSET
        else:
            completion_percentage = self.completion_percentage

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        audio_channels: int | None | Unset
        if isinstance(self.audio_channels, Unset):
            audio_channels = UNSET
        else:
            audio_channels = self.audio_channels

        hardware_acceleration_type: str | Unset = UNSET
        if not isinstance(self.hardware_acceleration_type, Unset):
            hardware_acceleration_type = self.hardware_acceleration_type.value

        transcode_reasons: str | Unset = UNSET
        if not isinstance(self.transcode_reasons, Unset):
            transcode_reasons = self.transcode_reasons.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if container is not UNSET:
            field_dict["Container"] = container
        if is_video_direct is not UNSET:
            field_dict["IsVideoDirect"] = is_video_direct
        if is_audio_direct is not UNSET:
            field_dict["IsAudioDirect"] = is_audio_direct
        if bitrate is not UNSET:
            field_dict["Bitrate"] = bitrate
        if framerate is not UNSET:
            field_dict["Framerate"] = framerate
        if completion_percentage is not UNSET:
            field_dict["CompletionPercentage"] = completion_percentage
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if audio_channels is not UNSET:
            field_dict["AudioChannels"] = audio_channels
        if hardware_acceleration_type is not UNSET:
            field_dict["HardwareAccelerationType"] = hardware_acceleration_type
        if transcode_reasons is not UNSET:
            field_dict["TranscodeReasons"] = transcode_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audio_codec = _parse_audio_codec(d.pop("AudioCodec", UNSET))

        def _parse_video_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_codec = _parse_video_codec(d.pop("VideoCodec", UNSET))

        def _parse_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container = _parse_container(d.pop("Container", UNSET))

        is_video_direct = d.pop("IsVideoDirect", UNSET)

        is_audio_direct = d.pop("IsAudioDirect", UNSET)

        def _parse_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bitrate = _parse_bitrate(d.pop("Bitrate", UNSET))

        def _parse_framerate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        framerate = _parse_framerate(d.pop("Framerate", UNSET))

        def _parse_completion_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        completion_percentage = _parse_completion_percentage(
            d.pop("CompletionPercentage", UNSET)
        )

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_audio_channels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_channels = _parse_audio_channels(d.pop("AudioChannels", UNSET))

        _hardware_acceleration_type = d.pop("HardwareAccelerationType", UNSET)
        hardware_acceleration_type: TranscodingInfoHardwareAccelerationType | Unset
        if isinstance(_hardware_acceleration_type, Unset):
            hardware_acceleration_type = UNSET
        else:
            hardware_acceleration_type = TranscodingInfoHardwareAccelerationType(
                _hardware_acceleration_type
            )

        _transcode_reasons = d.pop("TranscodeReasons", UNSET)
        transcode_reasons: TranscodingInfoTranscodeReasons | Unset
        if isinstance(_transcode_reasons, Unset):
            transcode_reasons = UNSET
        else:
            transcode_reasons = TranscodingInfoTranscodeReasons(_transcode_reasons)

        transcoding_info = cls(
            audio_codec=audio_codec,
            video_codec=video_codec,
            container=container,
            is_video_direct=is_video_direct,
            is_audio_direct=is_audio_direct,
            bitrate=bitrate,
            framerate=framerate,
            completion_percentage=completion_percentage,
            width=width,
            height=height,
            audio_channels=audio_channels,
            hardware_acceleration_type=hardware_acceleration_type,
            transcode_reasons=transcode_reasons,
        )

        return transcoding_info
