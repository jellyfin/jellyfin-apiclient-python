from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.media_protocol import MediaProtocol
from ..models.media_source_info_encoder_protocol import MediaSourceInfoEncoderProtocol
from ..models.media_source_info_iso_type import MediaSourceInfoIsoType
from ..models.media_source_info_timestamp import MediaSourceInfoTimestamp
from ..models.media_source_info_video_3d_format import MediaSourceInfoVideo3DFormat
from ..models.media_source_info_video_type import MediaSourceInfoVideoType
from ..models.media_source_type import MediaSourceType
from ..models.media_stream_protocol import MediaStreamProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_attachment import MediaAttachment
    from ..models.media_source_info_required_http_headers_type_0 import (
        MediaSourceInfoRequiredHttpHeadersType0,
    )
    from ..models.media_stream import MediaStream


T = TypeVar("T", bound="MediaSourceInfo")


@_attrs_define
class MediaSourceInfo:
    """
    Attributes:
        protocol (MediaProtocol | Unset):
        id (None | str | Unset):
        path (None | str | Unset):
        encoder_path (None | str | Unset):
        encoder_protocol (MediaSourceInfoEncoderProtocol | Unset):
        type_ (MediaSourceType | Unset):
        container (None | str | Unset):
        size (int | None | Unset):
        name (None | str | Unset):
        is_remote (bool | Unset): Gets or sets a value indicating whether the media is remote.
            Differentiate internet url vs local network.
        e_tag (None | str | Unset):
        run_time_ticks (int | None | Unset):
        read_at_native_framerate (bool | Unset):
        ignore_dts (bool | Unset):
        ignore_index (bool | Unset):
        gen_pts_input (bool | Unset):
        supports_transcoding (bool | Unset):
        supports_direct_stream (bool | Unset):
        supports_direct_play (bool | Unset):
        is_infinite_stream (bool | Unset):
        use_most_compatible_transcoding_profile (bool | Unset):  Default: False.
        requires_opening (bool | Unset):
        open_token (None | str | Unset):
        requires_closing (bool | Unset):
        live_stream_id (None | str | Unset):
        buffer_ms (int | None | Unset):
        requires_looping (bool | Unset):
        supports_probing (bool | Unset):
        video_type (MediaSourceInfoVideoType | Unset):
        iso_type (MediaSourceInfoIsoType | Unset):
        video_3d_format (MediaSourceInfoVideo3DFormat | Unset):
        media_streams (list[MediaStream] | None | Unset):
        media_attachments (list[MediaAttachment] | None | Unset):
        formats (list[str] | None | Unset):
        bitrate (int | None | Unset):
        fallback_max_streaming_bitrate (int | None | Unset):
        timestamp (MediaSourceInfoTimestamp | Unset):
        required_http_headers (MediaSourceInfoRequiredHttpHeadersType0 | None | Unset):
        transcoding_url (None | str | Unset):
        transcoding_sub_protocol (MediaStreamProtocol | Unset): Media streaming protocol.
            Lowercase for backwards compatibility.
        transcoding_container (None | str | Unset):
        analyze_duration_ms (int | None | Unset):
        default_audio_stream_index (int | None | Unset):
        default_subtitle_stream_index (int | None | Unset):
        has_segments (bool | Unset):
    """

    protocol: MediaProtocol | Unset = UNSET
    id: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    encoder_path: None | str | Unset = UNSET
    encoder_protocol: MediaSourceInfoEncoderProtocol | Unset = UNSET
    type_: MediaSourceType | Unset = UNSET
    container: None | str | Unset = UNSET
    size: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    is_remote: bool | Unset = UNSET
    e_tag: None | str | Unset = UNSET
    run_time_ticks: int | None | Unset = UNSET
    read_at_native_framerate: bool | Unset = UNSET
    ignore_dts: bool | Unset = UNSET
    ignore_index: bool | Unset = UNSET
    gen_pts_input: bool | Unset = UNSET
    supports_transcoding: bool | Unset = UNSET
    supports_direct_stream: bool | Unset = UNSET
    supports_direct_play: bool | Unset = UNSET
    is_infinite_stream: bool | Unset = UNSET
    use_most_compatible_transcoding_profile: bool | Unset = False
    requires_opening: bool | Unset = UNSET
    open_token: None | str | Unset = UNSET
    requires_closing: bool | Unset = UNSET
    live_stream_id: None | str | Unset = UNSET
    buffer_ms: int | None | Unset = UNSET
    requires_looping: bool | Unset = UNSET
    supports_probing: bool | Unset = UNSET
    video_type: MediaSourceInfoVideoType | Unset = UNSET
    iso_type: MediaSourceInfoIsoType | Unset = UNSET
    video_3d_format: MediaSourceInfoVideo3DFormat | Unset = UNSET
    media_streams: list[MediaStream] | None | Unset = UNSET
    media_attachments: list[MediaAttachment] | None | Unset = UNSET
    formats: list[str] | None | Unset = UNSET
    bitrate: int | None | Unset = UNSET
    fallback_max_streaming_bitrate: int | None | Unset = UNSET
    timestamp: MediaSourceInfoTimestamp | Unset = UNSET
    required_http_headers: MediaSourceInfoRequiredHttpHeadersType0 | None | Unset = (
        UNSET
    )
    transcoding_url: None | str | Unset = UNSET
    transcoding_sub_protocol: MediaStreamProtocol | Unset = UNSET
    transcoding_container: None | str | Unset = UNSET
    analyze_duration_ms: int | None | Unset = UNSET
    default_audio_stream_index: int | None | Unset = UNSET
    default_subtitle_stream_index: int | None | Unset = UNSET
    has_segments: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_source_info_required_http_headers_type_0 import (
            MediaSourceInfoRequiredHttpHeadersType0,
        )

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        encoder_path: None | str | Unset
        if isinstance(self.encoder_path, Unset):
            encoder_path = UNSET
        else:
            encoder_path = self.encoder_path

        encoder_protocol: str | Unset = UNSET
        if not isinstance(self.encoder_protocol, Unset):
            encoder_protocol = self.encoder_protocol.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        container: None | str | Unset
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_remote = self.is_remote

        e_tag: None | str | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        run_time_ticks: int | None | Unset
        if isinstance(self.run_time_ticks, Unset):
            run_time_ticks = UNSET
        else:
            run_time_ticks = self.run_time_ticks

        read_at_native_framerate = self.read_at_native_framerate

        ignore_dts = self.ignore_dts

        ignore_index = self.ignore_index

        gen_pts_input = self.gen_pts_input

        supports_transcoding = self.supports_transcoding

        supports_direct_stream = self.supports_direct_stream

        supports_direct_play = self.supports_direct_play

        is_infinite_stream = self.is_infinite_stream

        use_most_compatible_transcoding_profile = (
            self.use_most_compatible_transcoding_profile
        )

        requires_opening = self.requires_opening

        open_token: None | str | Unset
        if isinstance(self.open_token, Unset):
            open_token = UNSET
        else:
            open_token = self.open_token

        requires_closing = self.requires_closing

        live_stream_id: None | str | Unset
        if isinstance(self.live_stream_id, Unset):
            live_stream_id = UNSET
        else:
            live_stream_id = self.live_stream_id

        buffer_ms: int | None | Unset
        if isinstance(self.buffer_ms, Unset):
            buffer_ms = UNSET
        else:
            buffer_ms = self.buffer_ms

        requires_looping = self.requires_looping

        supports_probing = self.supports_probing

        video_type: str | Unset = UNSET
        if not isinstance(self.video_type, Unset):
            video_type = self.video_type.value

        iso_type: str | Unset = UNSET
        if not isinstance(self.iso_type, Unset):
            iso_type = self.iso_type.value

        video_3d_format: str | Unset = UNSET
        if not isinstance(self.video_3d_format, Unset):
            video_3d_format = self.video_3d_format.value

        media_streams: list[dict[str, Any]] | None | Unset
        if isinstance(self.media_streams, Unset):
            media_streams = UNSET
        elif isinstance(self.media_streams, list):
            media_streams = []
            for media_streams_type_0_item_data in self.media_streams:
                media_streams_type_0_item = media_streams_type_0_item_data.to_dict()
                media_streams.append(media_streams_type_0_item)

        else:
            media_streams = self.media_streams

        media_attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.media_attachments, Unset):
            media_attachments = UNSET
        elif isinstance(self.media_attachments, list):
            media_attachments = []
            for media_attachments_type_0_item_data in self.media_attachments:
                media_attachments_type_0_item = (
                    media_attachments_type_0_item_data.to_dict()
                )
                media_attachments.append(media_attachments_type_0_item)

        else:
            media_attachments = self.media_attachments

        formats: list[str] | None | Unset
        if isinstance(self.formats, Unset):
            formats = UNSET
        elif isinstance(self.formats, list):
            formats = self.formats

        else:
            formats = self.formats

        bitrate: int | None | Unset
        if isinstance(self.bitrate, Unset):
            bitrate = UNSET
        else:
            bitrate = self.bitrate

        fallback_max_streaming_bitrate: int | None | Unset
        if isinstance(self.fallback_max_streaming_bitrate, Unset):
            fallback_max_streaming_bitrate = UNSET
        else:
            fallback_max_streaming_bitrate = self.fallback_max_streaming_bitrate

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.value

        required_http_headers: dict[str, Any] | None | Unset
        if isinstance(self.required_http_headers, Unset):
            required_http_headers = UNSET
        elif isinstance(
            self.required_http_headers, MediaSourceInfoRequiredHttpHeadersType0
        ):
            required_http_headers = self.required_http_headers.to_dict()
        else:
            required_http_headers = self.required_http_headers

        transcoding_url: None | str | Unset
        if isinstance(self.transcoding_url, Unset):
            transcoding_url = UNSET
        else:
            transcoding_url = self.transcoding_url

        transcoding_sub_protocol: str | Unset = UNSET
        if not isinstance(self.transcoding_sub_protocol, Unset):
            transcoding_sub_protocol = self.transcoding_sub_protocol.value

        transcoding_container: None | str | Unset
        if isinstance(self.transcoding_container, Unset):
            transcoding_container = UNSET
        else:
            transcoding_container = self.transcoding_container

        analyze_duration_ms: int | None | Unset
        if isinstance(self.analyze_duration_ms, Unset):
            analyze_duration_ms = UNSET
        else:
            analyze_duration_ms = self.analyze_duration_ms

        default_audio_stream_index: int | None | Unset
        if isinstance(self.default_audio_stream_index, Unset):
            default_audio_stream_index = UNSET
        else:
            default_audio_stream_index = self.default_audio_stream_index

        default_subtitle_stream_index: int | None | Unset
        if isinstance(self.default_subtitle_stream_index, Unset):
            default_subtitle_stream_index = UNSET
        else:
            default_subtitle_stream_index = self.default_subtitle_stream_index

        has_segments = self.has_segments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if protocol is not UNSET:
            field_dict["Protocol"] = protocol
        if id is not UNSET:
            field_dict["Id"] = id
        if path is not UNSET:
            field_dict["Path"] = path
        if encoder_path is not UNSET:
            field_dict["EncoderPath"] = encoder_path
        if encoder_protocol is not UNSET:
            field_dict["EncoderProtocol"] = encoder_protocol
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if container is not UNSET:
            field_dict["Container"] = container
        if size is not UNSET:
            field_dict["Size"] = size
        if name is not UNSET:
            field_dict["Name"] = name
        if is_remote is not UNSET:
            field_dict["IsRemote"] = is_remote
        if e_tag is not UNSET:
            field_dict["ETag"] = e_tag
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if read_at_native_framerate is not UNSET:
            field_dict["ReadAtNativeFramerate"] = read_at_native_framerate
        if ignore_dts is not UNSET:
            field_dict["IgnoreDts"] = ignore_dts
        if ignore_index is not UNSET:
            field_dict["IgnoreIndex"] = ignore_index
        if gen_pts_input is not UNSET:
            field_dict["GenPtsInput"] = gen_pts_input
        if supports_transcoding is not UNSET:
            field_dict["SupportsTranscoding"] = supports_transcoding
        if supports_direct_stream is not UNSET:
            field_dict["SupportsDirectStream"] = supports_direct_stream
        if supports_direct_play is not UNSET:
            field_dict["SupportsDirectPlay"] = supports_direct_play
        if is_infinite_stream is not UNSET:
            field_dict["IsInfiniteStream"] = is_infinite_stream
        if use_most_compatible_transcoding_profile is not UNSET:
            field_dict["UseMostCompatibleTranscodingProfile"] = (
                use_most_compatible_transcoding_profile
            )
        if requires_opening is not UNSET:
            field_dict["RequiresOpening"] = requires_opening
        if open_token is not UNSET:
            field_dict["OpenToken"] = open_token
        if requires_closing is not UNSET:
            field_dict["RequiresClosing"] = requires_closing
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if buffer_ms is not UNSET:
            field_dict["BufferMs"] = buffer_ms
        if requires_looping is not UNSET:
            field_dict["RequiresLooping"] = requires_looping
        if supports_probing is not UNSET:
            field_dict["SupportsProbing"] = supports_probing
        if video_type is not UNSET:
            field_dict["VideoType"] = video_type
        if iso_type is not UNSET:
            field_dict["IsoType"] = iso_type
        if video_3d_format is not UNSET:
            field_dict["Video3DFormat"] = video_3d_format
        if media_streams is not UNSET:
            field_dict["MediaStreams"] = media_streams
        if media_attachments is not UNSET:
            field_dict["MediaAttachments"] = media_attachments
        if formats is not UNSET:
            field_dict["Formats"] = formats
        if bitrate is not UNSET:
            field_dict["Bitrate"] = bitrate
        if fallback_max_streaming_bitrate is not UNSET:
            field_dict["FallbackMaxStreamingBitrate"] = fallback_max_streaming_bitrate
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if required_http_headers is not UNSET:
            field_dict["RequiredHttpHeaders"] = required_http_headers
        if transcoding_url is not UNSET:
            field_dict["TranscodingUrl"] = transcoding_url
        if transcoding_sub_protocol is not UNSET:
            field_dict["TranscodingSubProtocol"] = transcoding_sub_protocol
        if transcoding_container is not UNSET:
            field_dict["TranscodingContainer"] = transcoding_container
        if analyze_duration_ms is not UNSET:
            field_dict["AnalyzeDurationMs"] = analyze_duration_ms
        if default_audio_stream_index is not UNSET:
            field_dict["DefaultAudioStreamIndex"] = default_audio_stream_index
        if default_subtitle_stream_index is not UNSET:
            field_dict["DefaultSubtitleStreamIndex"] = default_subtitle_stream_index
        if has_segments is not UNSET:
            field_dict["HasSegments"] = has_segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_attachment import MediaAttachment
        from ..models.media_source_info_required_http_headers_type_0 import (
            MediaSourceInfoRequiredHttpHeadersType0,
        )
        from ..models.media_stream import MediaStream

        d = dict(src_dict)
        _protocol = d.pop("Protocol", UNSET)
        protocol: MediaProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = MediaProtocol(_protocol)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_encoder_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encoder_path = _parse_encoder_path(d.pop("EncoderPath", UNSET))

        _encoder_protocol = d.pop("EncoderProtocol", UNSET)
        encoder_protocol: MediaSourceInfoEncoderProtocol | Unset
        if isinstance(_encoder_protocol, Unset):
            encoder_protocol = UNSET
        else:
            encoder_protocol = MediaSourceInfoEncoderProtocol(_encoder_protocol)

        _type_ = d.pop("Type", UNSET)
        type_: MediaSourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MediaSourceType(_type_)

        def _parse_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("Size", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        is_remote = d.pop("IsRemote", UNSET)

        def _parse_e_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_tag = _parse_e_tag(d.pop("ETag", UNSET))

        def _parse_run_time_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        run_time_ticks = _parse_run_time_ticks(d.pop("RunTimeTicks", UNSET))

        read_at_native_framerate = d.pop("ReadAtNativeFramerate", UNSET)

        ignore_dts = d.pop("IgnoreDts", UNSET)

        ignore_index = d.pop("IgnoreIndex", UNSET)

        gen_pts_input = d.pop("GenPtsInput", UNSET)

        supports_transcoding = d.pop("SupportsTranscoding", UNSET)

        supports_direct_stream = d.pop("SupportsDirectStream", UNSET)

        supports_direct_play = d.pop("SupportsDirectPlay", UNSET)

        is_infinite_stream = d.pop("IsInfiniteStream", UNSET)

        use_most_compatible_transcoding_profile = d.pop(
            "UseMostCompatibleTranscodingProfile", UNSET
        )

        requires_opening = d.pop("RequiresOpening", UNSET)

        def _parse_open_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_token = _parse_open_token(d.pop("OpenToken", UNSET))

        requires_closing = d.pop("RequiresClosing", UNSET)

        def _parse_live_stream_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        live_stream_id = _parse_live_stream_id(d.pop("LiveStreamId", UNSET))

        def _parse_buffer_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        buffer_ms = _parse_buffer_ms(d.pop("BufferMs", UNSET))

        requires_looping = d.pop("RequiresLooping", UNSET)

        supports_probing = d.pop("SupportsProbing", UNSET)

        _video_type = d.pop("VideoType", UNSET)
        video_type: MediaSourceInfoVideoType | Unset
        if isinstance(_video_type, Unset):
            video_type = UNSET
        else:
            video_type = MediaSourceInfoVideoType(_video_type)

        _iso_type = d.pop("IsoType", UNSET)
        iso_type: MediaSourceInfoIsoType | Unset
        if isinstance(_iso_type, Unset):
            iso_type = UNSET
        else:
            iso_type = MediaSourceInfoIsoType(_iso_type)

        _video_3d_format = d.pop("Video3DFormat", UNSET)
        video_3d_format: MediaSourceInfoVideo3DFormat | Unset
        if isinstance(_video_3d_format, Unset):
            video_3d_format = UNSET
        else:
            video_3d_format = MediaSourceInfoVideo3DFormat(_video_3d_format)

        def _parse_media_streams(data: object) -> list[MediaStream] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_streams_type_0 = []
                _media_streams_type_0 = data
                for media_streams_type_0_item_data in _media_streams_type_0:
                    media_streams_type_0_item = MediaStream.from_dict(
                        media_streams_type_0_item_data
                    )

                    media_streams_type_0.append(media_streams_type_0_item)

                return media_streams_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MediaStream] | None | Unset, data)

        media_streams = _parse_media_streams(d.pop("MediaStreams", UNSET))

        def _parse_media_attachments(
            data: object,
        ) -> list[MediaAttachment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_attachments_type_0 = []
                _media_attachments_type_0 = data
                for media_attachments_type_0_item_data in _media_attachments_type_0:
                    media_attachments_type_0_item = MediaAttachment.from_dict(
                        media_attachments_type_0_item_data
                    )

                    media_attachments_type_0.append(media_attachments_type_0_item)

                return media_attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MediaAttachment] | None | Unset, data)

        media_attachments = _parse_media_attachments(d.pop("MediaAttachments", UNSET))

        def _parse_formats(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = cast(list[str], data)

                return formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        formats = _parse_formats(d.pop("Formats", UNSET))

        def _parse_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bitrate = _parse_bitrate(d.pop("Bitrate", UNSET))

        def _parse_fallback_max_streaming_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fallback_max_streaming_bitrate = _parse_fallback_max_streaming_bitrate(
            d.pop("FallbackMaxStreamingBitrate", UNSET)
        )

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: MediaSourceInfoTimestamp | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = MediaSourceInfoTimestamp(_timestamp)

        def _parse_required_http_headers(
            data: object,
        ) -> MediaSourceInfoRequiredHttpHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                required_http_headers_type_0 = (
                    MediaSourceInfoRequiredHttpHeadersType0.from_dict(data)
                )

                return required_http_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MediaSourceInfoRequiredHttpHeadersType0 | None | Unset, data)

        required_http_headers = _parse_required_http_headers(
            d.pop("RequiredHttpHeaders", UNSET)
        )

        def _parse_transcoding_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcoding_url = _parse_transcoding_url(d.pop("TranscodingUrl", UNSET))

        _transcoding_sub_protocol = d.pop("TranscodingSubProtocol", UNSET)
        transcoding_sub_protocol: MediaStreamProtocol | Unset
        if isinstance(_transcoding_sub_protocol, Unset):
            transcoding_sub_protocol = UNSET
        else:
            transcoding_sub_protocol = MediaStreamProtocol(_transcoding_sub_protocol)

        def _parse_transcoding_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcoding_container = _parse_transcoding_container(
            d.pop("TranscodingContainer", UNSET)
        )

        def _parse_analyze_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        analyze_duration_ms = _parse_analyze_duration_ms(
            d.pop("AnalyzeDurationMs", UNSET)
        )

        def _parse_default_audio_stream_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_audio_stream_index = _parse_default_audio_stream_index(
            d.pop("DefaultAudioStreamIndex", UNSET)
        )

        def _parse_default_subtitle_stream_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_subtitle_stream_index = _parse_default_subtitle_stream_index(
            d.pop("DefaultSubtitleStreamIndex", UNSET)
        )

        has_segments = d.pop("HasSegments", UNSET)

        media_source_info = cls(
            protocol=protocol,
            id=id,
            path=path,
            encoder_path=encoder_path,
            encoder_protocol=encoder_protocol,
            type_=type_,
            container=container,
            size=size,
            name=name,
            is_remote=is_remote,
            e_tag=e_tag,
            run_time_ticks=run_time_ticks,
            read_at_native_framerate=read_at_native_framerate,
            ignore_dts=ignore_dts,
            ignore_index=ignore_index,
            gen_pts_input=gen_pts_input,
            supports_transcoding=supports_transcoding,
            supports_direct_stream=supports_direct_stream,
            supports_direct_play=supports_direct_play,
            is_infinite_stream=is_infinite_stream,
            use_most_compatible_transcoding_profile=use_most_compatible_transcoding_profile,
            requires_opening=requires_opening,
            open_token=open_token,
            requires_closing=requires_closing,
            live_stream_id=live_stream_id,
            buffer_ms=buffer_ms,
            requires_looping=requires_looping,
            supports_probing=supports_probing,
            video_type=video_type,
            iso_type=iso_type,
            video_3d_format=video_3d_format,
            media_streams=media_streams,
            media_attachments=media_attachments,
            formats=formats,
            bitrate=bitrate,
            fallback_max_streaming_bitrate=fallback_max_streaming_bitrate,
            timestamp=timestamp,
            required_http_headers=required_http_headers,
            transcoding_url=transcoding_url,
            transcoding_sub_protocol=transcoding_sub_protocol,
            transcoding_container=transcoding_container,
            analyze_duration_ms=analyze_duration_ms,
            default_audio_stream_index=default_audio_stream_index,
            default_subtitle_stream_index=default_subtitle_stream_index,
            has_segments=has_segments,
        )

        return media_source_info
