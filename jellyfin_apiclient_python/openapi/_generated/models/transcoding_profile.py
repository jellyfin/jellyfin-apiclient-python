from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..models.encoding_context import EncodingContext
from ..models.media_stream_protocol import MediaStreamProtocol
from ..models.transcode_seek_info import TranscodeSeekInfo
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="TranscodingProfile")


@_attrs_define
class TranscodingProfile:
    """A class for transcoding profile information.
    Note for client developers: Conditions defined in MediaBrowser.Model.Dlna.CodecProfile has higher priority and can
    override values defined here.

        Attributes:
            container (str | Unset): Gets or sets the container.
            type_ (DlnaProfileType | Unset):
            video_codec (str | Unset): Gets or sets the video codec.
            audio_codec (str | Unset): Gets or sets the audio codec.
            protocol (MediaStreamProtocol | Unset): Media streaming protocol.
                Lowercase for backwards compatibility.
            estimate_content_length (bool | Unset): Gets or sets a value indicating whether the content length should be
                estimated. Default: False.
            enable_mpegts_m2_ts_mode (bool | Unset): Gets or sets a value indicating whether M2TS mode is enabled. Default:
                False.
            transcode_seek_info (TranscodeSeekInfo | Unset):  Default: TranscodeSeekInfo.AUTO.
            copy_timestamps (bool | Unset): Gets or sets a value indicating whether timestamps should be copied. Default:
                False.
            context (EncodingContext | Unset):  Default: EncodingContext.STREAMING.
            enable_subtitles_in_manifest (bool | Unset): Gets or sets a value indicating whether subtitles are allowed in
                the manifest. Default: False.
            max_audio_channels (None | str | Unset): Gets or sets the maximum audio channels.
            min_segments (int | Unset): Gets or sets the minimum amount of segments. Default: 0.
            segment_length (int | Unset): Gets or sets the segment length. Default: 0.
            break_on_non_key_frames (bool | Unset): Gets or sets a value indicating whether breaking the video stream on
                non-keyframes is supported. Default: False.
            conditions (list[ProfileCondition] | Unset): Gets or sets the profile conditions.
            enable_audio_vbr_encoding (bool | Unset): Gets or sets a value indicating whether variable bitrate encoding is
                supported. Default: True.
    """

    container: str | Unset = UNSET
    type_: DlnaProfileType | Unset = UNSET
    video_codec: str | Unset = UNSET
    audio_codec: str | Unset = UNSET
    protocol: MediaStreamProtocol | Unset = UNSET
    estimate_content_length: bool | Unset = False
    enable_mpegts_m2_ts_mode: bool | Unset = False
    transcode_seek_info: TranscodeSeekInfo | Unset = TranscodeSeekInfo.AUTO
    copy_timestamps: bool | Unset = False
    context: EncodingContext | Unset = EncodingContext.STREAMING
    enable_subtitles_in_manifest: bool | Unset = False
    max_audio_channels: None | str | Unset = UNSET
    min_segments: int | Unset = 0
    segment_length: int | Unset = 0
    break_on_non_key_frames: bool | Unset = False
    conditions: list[ProfileCondition] | Unset = UNSET
    enable_audio_vbr_encoding: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        container = self.container

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        video_codec = self.video_codec

        audio_codec = self.audio_codec

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        estimate_content_length = self.estimate_content_length

        enable_mpegts_m2_ts_mode = self.enable_mpegts_m2_ts_mode

        transcode_seek_info: str | Unset = UNSET
        if not isinstance(self.transcode_seek_info, Unset):
            transcode_seek_info = self.transcode_seek_info.value

        copy_timestamps = self.copy_timestamps

        context: str | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.value

        enable_subtitles_in_manifest = self.enable_subtitles_in_manifest

        max_audio_channels: None | str | Unset
        if isinstance(self.max_audio_channels, Unset):
            max_audio_channels = UNSET
        else:
            max_audio_channels = self.max_audio_channels

        min_segments = self.min_segments

        segment_length = self.segment_length

        break_on_non_key_frames = self.break_on_non_key_frames

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        enable_audio_vbr_encoding = self.enable_audio_vbr_encoding

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if container is not UNSET:
            field_dict["Container"] = container
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if protocol is not UNSET:
            field_dict["Protocol"] = protocol
        if estimate_content_length is not UNSET:
            field_dict["EstimateContentLength"] = estimate_content_length
        if enable_mpegts_m2_ts_mode is not UNSET:
            field_dict["EnableMpegtsM2TsMode"] = enable_mpegts_m2_ts_mode
        if transcode_seek_info is not UNSET:
            field_dict["TranscodeSeekInfo"] = transcode_seek_info
        if copy_timestamps is not UNSET:
            field_dict["CopyTimestamps"] = copy_timestamps
        if context is not UNSET:
            field_dict["Context"] = context
        if enable_subtitles_in_manifest is not UNSET:
            field_dict["EnableSubtitlesInManifest"] = enable_subtitles_in_manifest
        if max_audio_channels is not UNSET:
            field_dict["MaxAudioChannels"] = max_audio_channels
        if min_segments is not UNSET:
            field_dict["MinSegments"] = min_segments
        if segment_length is not UNSET:
            field_dict["SegmentLength"] = segment_length
        if break_on_non_key_frames is not UNSET:
            field_dict["BreakOnNonKeyFrames"] = break_on_non_key_frames
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if enable_audio_vbr_encoding is not UNSET:
            field_dict["EnableAudioVbrEncoding"] = enable_audio_vbr_encoding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = dict(src_dict)
        container = d.pop("Container", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: DlnaProfileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DlnaProfileType(_type_)

        video_codec = d.pop("VideoCodec", UNSET)

        audio_codec = d.pop("AudioCodec", UNSET)

        _protocol = d.pop("Protocol", UNSET)
        protocol: MediaStreamProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = MediaStreamProtocol(_protocol)

        estimate_content_length = d.pop("EstimateContentLength", UNSET)

        enable_mpegts_m2_ts_mode = d.pop("EnableMpegtsM2TsMode", UNSET)

        _transcode_seek_info = d.pop("TranscodeSeekInfo", UNSET)
        transcode_seek_info: TranscodeSeekInfo | Unset
        if isinstance(_transcode_seek_info, Unset):
            transcode_seek_info = UNSET
        else:
            transcode_seek_info = TranscodeSeekInfo(_transcode_seek_info)

        copy_timestamps = d.pop("CopyTimestamps", UNSET)

        _context = d.pop("Context", UNSET)
        context: EncodingContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = EncodingContext(_context)

        enable_subtitles_in_manifest = d.pop("EnableSubtitlesInManifest", UNSET)

        def _parse_max_audio_channels(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_audio_channels = _parse_max_audio_channels(d.pop("MaxAudioChannels", UNSET))

        min_segments = d.pop("MinSegments", UNSET)

        segment_length = d.pop("SegmentLength", UNSET)

        break_on_non_key_frames = d.pop("BreakOnNonKeyFrames", UNSET)

        _conditions = d.pop("Conditions", UNSET)
        conditions: list[ProfileCondition] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ProfileCondition.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        enable_audio_vbr_encoding = d.pop("EnableAudioVbrEncoding", UNSET)

        transcoding_profile = cls(
            container=container,
            type_=type_,
            video_codec=video_codec,
            audio_codec=audio_codec,
            protocol=protocol,
            estimate_content_length=estimate_content_length,
            enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
            transcode_seek_info=transcode_seek_info,
            copy_timestamps=copy_timestamps,
            context=context,
            enable_subtitles_in_manifest=enable_subtitles_in_manifest,
            max_audio_channels=max_audio_channels,
            min_segments=min_segments,
            segment_length=segment_length,
            break_on_non_key_frames=break_on_non_key_frames,
            conditions=conditions,
            enable_audio_vbr_encoding=enable_audio_vbr_encoding,
        )

        return transcoding_profile
