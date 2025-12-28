from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.audio_spatial_format import AudioSpatialFormat
from ..models.media_stream_delivery_method import MediaStreamDeliveryMethod
from ..models.media_stream_type import MediaStreamType
from ..models.video_range import VideoRange
from ..models.video_range_type import VideoRangeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaStream")


@_attrs_define
class MediaStream:
    """Class MediaStream.

    Attributes:
        codec (None | str | Unset): Gets or sets the codec.
        codec_tag (None | str | Unset): Gets or sets the codec tag.
        language (None | str | Unset): Gets or sets the language.
        color_range (None | str | Unset): Gets or sets the color range.
        color_space (None | str | Unset): Gets or sets the color space.
        color_transfer (None | str | Unset): Gets or sets the color transfer.
        color_primaries (None | str | Unset): Gets or sets the color primaries.
        dv_version_major (int | None | Unset): Gets or sets the Dolby Vision version major.
        dv_version_minor (int | None | Unset): Gets or sets the Dolby Vision version minor.
        dv_profile (int | None | Unset): Gets or sets the Dolby Vision profile.
        dv_level (int | None | Unset): Gets or sets the Dolby Vision level.
        rpu_present_flag (int | None | Unset): Gets or sets the Dolby Vision rpu present flag.
        el_present_flag (int | None | Unset): Gets or sets the Dolby Vision el present flag.
        bl_present_flag (int | None | Unset): Gets or sets the Dolby Vision bl present flag.
        dv_bl_signal_compatibility_id (int | None | Unset): Gets or sets the Dolby Vision bl signal compatibility id.
        rotation (int | None | Unset): Gets or sets the Rotation in degrees.
        comment (None | str | Unset): Gets or sets the comment.
        time_base (None | str | Unset): Gets or sets the time base.
        codec_time_base (None | str | Unset): Gets or sets the codec time base.
        title (None | str | Unset): Gets or sets the title.
        hdr_10_plus_present_flag (bool | None | Unset):
        video_range (VideoRange | Unset): An enum representing video ranges. Default: VideoRange.UNKNOWN.
        video_range_type (VideoRangeType | Unset): An enum representing types of video ranges. Default:
            VideoRangeType.UNKNOWN.
        video_do_vi_title (None | str | Unset): Gets the video dovi title.
        audio_spatial_format (AudioSpatialFormat | Unset): An enum representing formats of spatial audio. Default:
            AudioSpatialFormat.NONE.
        localized_undefined (None | str | Unset):
        localized_default (None | str | Unset):
        localized_forced (None | str | Unset):
        localized_external (None | str | Unset):
        localized_hearing_impaired (None | str | Unset):
        display_title (None | str | Unset):
        nal_length_size (None | str | Unset):
        is_interlaced (bool | Unset): Gets or sets a value indicating whether this instance is interlaced.
        is_avc (bool | None | Unset):
        channel_layout (None | str | Unset): Gets or sets the channel layout.
        bit_rate (int | None | Unset): Gets or sets the bit rate.
        bit_depth (int | None | Unset): Gets or sets the bit depth.
        ref_frames (int | None | Unset): Gets or sets the reference frames.
        packet_length (int | None | Unset): Gets or sets the length of the packet.
        channels (int | None | Unset): Gets or sets the channels.
        sample_rate (int | None | Unset): Gets or sets the sample rate.
        is_default (bool | Unset): Gets or sets a value indicating whether this instance is default.
        is_forced (bool | Unset): Gets or sets a value indicating whether this instance is forced.
        is_hearing_impaired (bool | Unset): Gets or sets a value indicating whether this instance is for the hearing
            impaired.
        height (int | None | Unset): Gets or sets the height.
        width (int | None | Unset): Gets or sets the width.
        average_frame_rate (float | None | Unset): Gets or sets the average frame rate.
        real_frame_rate (float | None | Unset): Gets or sets the real frame rate.
        reference_frame_rate (float | None | Unset): Gets the framerate used as reference.
            Prefer AverageFrameRate, if that is null or an unrealistic value
            then fallback to RealFrameRate.
        profile (None | str | Unset): Gets or sets the profile.
        type_ (MediaStreamType | Unset): Enum MediaStreamType.
        aspect_ratio (None | str | Unset): Gets or sets the aspect ratio.
        index (int | Unset): Gets or sets the index.
        score (int | None | Unset): Gets or sets the score.
        is_external (bool | Unset): Gets or sets a value indicating whether this instance is external.
        delivery_method (MediaStreamDeliveryMethod | Unset): Gets or sets the method.
        delivery_url (None | str | Unset): Gets or sets the delivery URL.
        is_external_url (bool | None | Unset): Gets or sets a value indicating whether this instance is external URL.
        is_text_subtitle_stream (bool | Unset):
        supports_external_stream (bool | Unset): Gets or sets a value indicating whether [supports external stream].
        path (None | str | Unset): Gets or sets the filename.
        pixel_format (None | str | Unset): Gets or sets the pixel format.
        level (float | None | Unset): Gets or sets the level.
        is_anamorphic (bool | None | Unset): Gets or sets whether this instance is anamorphic.
    """

    codec: None | str | Unset = UNSET
    codec_tag: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    color_range: None | str | Unset = UNSET
    color_space: None | str | Unset = UNSET
    color_transfer: None | str | Unset = UNSET
    color_primaries: None | str | Unset = UNSET
    dv_version_major: int | None | Unset = UNSET
    dv_version_minor: int | None | Unset = UNSET
    dv_profile: int | None | Unset = UNSET
    dv_level: int | None | Unset = UNSET
    rpu_present_flag: int | None | Unset = UNSET
    el_present_flag: int | None | Unset = UNSET
    bl_present_flag: int | None | Unset = UNSET
    dv_bl_signal_compatibility_id: int | None | Unset = UNSET
    rotation: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    time_base: None | str | Unset = UNSET
    codec_time_base: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    hdr_10_plus_present_flag: bool | None | Unset = UNSET
    video_range: VideoRange | Unset = VideoRange.UNKNOWN
    video_range_type: VideoRangeType | Unset = VideoRangeType.UNKNOWN
    video_do_vi_title: None | str | Unset = UNSET
    audio_spatial_format: AudioSpatialFormat | Unset = AudioSpatialFormat.NONE
    localized_undefined: None | str | Unset = UNSET
    localized_default: None | str | Unset = UNSET
    localized_forced: None | str | Unset = UNSET
    localized_external: None | str | Unset = UNSET
    localized_hearing_impaired: None | str | Unset = UNSET
    display_title: None | str | Unset = UNSET
    nal_length_size: None | str | Unset = UNSET
    is_interlaced: bool | Unset = UNSET
    is_avc: bool | None | Unset = UNSET
    channel_layout: None | str | Unset = UNSET
    bit_rate: int | None | Unset = UNSET
    bit_depth: int | None | Unset = UNSET
    ref_frames: int | None | Unset = UNSET
    packet_length: int | None | Unset = UNSET
    channels: int | None | Unset = UNSET
    sample_rate: int | None | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_forced: bool | Unset = UNSET
    is_hearing_impaired: bool | Unset = UNSET
    height: int | None | Unset = UNSET
    width: int | None | Unset = UNSET
    average_frame_rate: float | None | Unset = UNSET
    real_frame_rate: float | None | Unset = UNSET
    reference_frame_rate: float | None | Unset = UNSET
    profile: None | str | Unset = UNSET
    type_: MediaStreamType | Unset = UNSET
    aspect_ratio: None | str | Unset = UNSET
    index: int | Unset = UNSET
    score: int | None | Unset = UNSET
    is_external: bool | Unset = UNSET
    delivery_method: MediaStreamDeliveryMethod | Unset = UNSET
    delivery_url: None | str | Unset = UNSET
    is_external_url: bool | None | Unset = UNSET
    is_text_subtitle_stream: bool | Unset = UNSET
    supports_external_stream: bool | Unset = UNSET
    path: None | str | Unset = UNSET
    pixel_format: None | str | Unset = UNSET
    level: float | None | Unset = UNSET
    is_anamorphic: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        codec: None | str | Unset
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        codec_tag: None | str | Unset
        if isinstance(self.codec_tag, Unset):
            codec_tag = UNSET
        else:
            codec_tag = self.codec_tag

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        color_range: None | str | Unset
        if isinstance(self.color_range, Unset):
            color_range = UNSET
        else:
            color_range = self.color_range

        color_space: None | str | Unset
        if isinstance(self.color_space, Unset):
            color_space = UNSET
        else:
            color_space = self.color_space

        color_transfer: None | str | Unset
        if isinstance(self.color_transfer, Unset):
            color_transfer = UNSET
        else:
            color_transfer = self.color_transfer

        color_primaries: None | str | Unset
        if isinstance(self.color_primaries, Unset):
            color_primaries = UNSET
        else:
            color_primaries = self.color_primaries

        dv_version_major: int | None | Unset
        if isinstance(self.dv_version_major, Unset):
            dv_version_major = UNSET
        else:
            dv_version_major = self.dv_version_major

        dv_version_minor: int | None | Unset
        if isinstance(self.dv_version_minor, Unset):
            dv_version_minor = UNSET
        else:
            dv_version_minor = self.dv_version_minor

        dv_profile: int | None | Unset
        if isinstance(self.dv_profile, Unset):
            dv_profile = UNSET
        else:
            dv_profile = self.dv_profile

        dv_level: int | None | Unset
        if isinstance(self.dv_level, Unset):
            dv_level = UNSET
        else:
            dv_level = self.dv_level

        rpu_present_flag: int | None | Unset
        if isinstance(self.rpu_present_flag, Unset):
            rpu_present_flag = UNSET
        else:
            rpu_present_flag = self.rpu_present_flag

        el_present_flag: int | None | Unset
        if isinstance(self.el_present_flag, Unset):
            el_present_flag = UNSET
        else:
            el_present_flag = self.el_present_flag

        bl_present_flag: int | None | Unset
        if isinstance(self.bl_present_flag, Unset):
            bl_present_flag = UNSET
        else:
            bl_present_flag = self.bl_present_flag

        dv_bl_signal_compatibility_id: int | None | Unset
        if isinstance(self.dv_bl_signal_compatibility_id, Unset):
            dv_bl_signal_compatibility_id = UNSET
        else:
            dv_bl_signal_compatibility_id = self.dv_bl_signal_compatibility_id

        rotation: int | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        time_base: None | str | Unset
        if isinstance(self.time_base, Unset):
            time_base = UNSET
        else:
            time_base = self.time_base

        codec_time_base: None | str | Unset
        if isinstance(self.codec_time_base, Unset):
            codec_time_base = UNSET
        else:
            codec_time_base = self.codec_time_base

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        hdr_10_plus_present_flag: bool | None | Unset
        if isinstance(self.hdr_10_plus_present_flag, Unset):
            hdr_10_plus_present_flag = UNSET
        else:
            hdr_10_plus_present_flag = self.hdr_10_plus_present_flag

        video_range: str | Unset = UNSET
        if not isinstance(self.video_range, Unset):
            video_range = self.video_range.value

        video_range_type: str | Unset = UNSET
        if not isinstance(self.video_range_type, Unset):
            video_range_type = self.video_range_type.value

        video_do_vi_title: None | str | Unset
        if isinstance(self.video_do_vi_title, Unset):
            video_do_vi_title = UNSET
        else:
            video_do_vi_title = self.video_do_vi_title

        audio_spatial_format: str | Unset = UNSET
        if not isinstance(self.audio_spatial_format, Unset):
            audio_spatial_format = self.audio_spatial_format.value

        localized_undefined: None | str | Unset
        if isinstance(self.localized_undefined, Unset):
            localized_undefined = UNSET
        else:
            localized_undefined = self.localized_undefined

        localized_default: None | str | Unset
        if isinstance(self.localized_default, Unset):
            localized_default = UNSET
        else:
            localized_default = self.localized_default

        localized_forced: None | str | Unset
        if isinstance(self.localized_forced, Unset):
            localized_forced = UNSET
        else:
            localized_forced = self.localized_forced

        localized_external: None | str | Unset
        if isinstance(self.localized_external, Unset):
            localized_external = UNSET
        else:
            localized_external = self.localized_external

        localized_hearing_impaired: None | str | Unset
        if isinstance(self.localized_hearing_impaired, Unset):
            localized_hearing_impaired = UNSET
        else:
            localized_hearing_impaired = self.localized_hearing_impaired

        display_title: None | str | Unset
        if isinstance(self.display_title, Unset):
            display_title = UNSET
        else:
            display_title = self.display_title

        nal_length_size: None | str | Unset
        if isinstance(self.nal_length_size, Unset):
            nal_length_size = UNSET
        else:
            nal_length_size = self.nal_length_size

        is_interlaced = self.is_interlaced

        is_avc: bool | None | Unset
        if isinstance(self.is_avc, Unset):
            is_avc = UNSET
        else:
            is_avc = self.is_avc

        channel_layout: None | str | Unset
        if isinstance(self.channel_layout, Unset):
            channel_layout = UNSET
        else:
            channel_layout = self.channel_layout

        bit_rate: int | None | Unset
        if isinstance(self.bit_rate, Unset):
            bit_rate = UNSET
        else:
            bit_rate = self.bit_rate

        bit_depth: int | None | Unset
        if isinstance(self.bit_depth, Unset):
            bit_depth = UNSET
        else:
            bit_depth = self.bit_depth

        ref_frames: int | None | Unset
        if isinstance(self.ref_frames, Unset):
            ref_frames = UNSET
        else:
            ref_frames = self.ref_frames

        packet_length: int | None | Unset
        if isinstance(self.packet_length, Unset):
            packet_length = UNSET
        else:
            packet_length = self.packet_length

        channels: int | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        else:
            channels = self.channels

        sample_rate: int | None | Unset
        if isinstance(self.sample_rate, Unset):
            sample_rate = UNSET
        else:
            sample_rate = self.sample_rate

        is_default = self.is_default

        is_forced = self.is_forced

        is_hearing_impaired = self.is_hearing_impaired

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        average_frame_rate: float | None | Unset
        if isinstance(self.average_frame_rate, Unset):
            average_frame_rate = UNSET
        else:
            average_frame_rate = self.average_frame_rate

        real_frame_rate: float | None | Unset
        if isinstance(self.real_frame_rate, Unset):
            real_frame_rate = UNSET
        else:
            real_frame_rate = self.real_frame_rate

        reference_frame_rate: float | None | Unset
        if isinstance(self.reference_frame_rate, Unset):
            reference_frame_rate = UNSET
        else:
            reference_frame_rate = self.reference_frame_rate

        profile: None | str | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        aspect_ratio: None | str | Unset
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        index = self.index

        score: int | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        is_external = self.is_external

        delivery_method: str | Unset = UNSET
        if not isinstance(self.delivery_method, Unset):
            delivery_method = self.delivery_method.value

        delivery_url: None | str | Unset
        if isinstance(self.delivery_url, Unset):
            delivery_url = UNSET
        else:
            delivery_url = self.delivery_url

        is_external_url: bool | None | Unset
        if isinstance(self.is_external_url, Unset):
            is_external_url = UNSET
        else:
            is_external_url = self.is_external_url

        is_text_subtitle_stream = self.is_text_subtitle_stream

        supports_external_stream = self.supports_external_stream

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        pixel_format: None | str | Unset
        if isinstance(self.pixel_format, Unset):
            pixel_format = UNSET
        else:
            pixel_format = self.pixel_format

        level: float | None | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        is_anamorphic: bool | None | Unset
        if isinstance(self.is_anamorphic, Unset):
            is_anamorphic = UNSET
        else:
            is_anamorphic = self.is_anamorphic

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if codec_tag is not UNSET:
            field_dict["CodecTag"] = codec_tag
        if language is not UNSET:
            field_dict["Language"] = language
        if color_range is not UNSET:
            field_dict["ColorRange"] = color_range
        if color_space is not UNSET:
            field_dict["ColorSpace"] = color_space
        if color_transfer is not UNSET:
            field_dict["ColorTransfer"] = color_transfer
        if color_primaries is not UNSET:
            field_dict["ColorPrimaries"] = color_primaries
        if dv_version_major is not UNSET:
            field_dict["DvVersionMajor"] = dv_version_major
        if dv_version_minor is not UNSET:
            field_dict["DvVersionMinor"] = dv_version_minor
        if dv_profile is not UNSET:
            field_dict["DvProfile"] = dv_profile
        if dv_level is not UNSET:
            field_dict["DvLevel"] = dv_level
        if rpu_present_flag is not UNSET:
            field_dict["RpuPresentFlag"] = rpu_present_flag
        if el_present_flag is not UNSET:
            field_dict["ElPresentFlag"] = el_present_flag
        if bl_present_flag is not UNSET:
            field_dict["BlPresentFlag"] = bl_present_flag
        if dv_bl_signal_compatibility_id is not UNSET:
            field_dict["DvBlSignalCompatibilityId"] = dv_bl_signal_compatibility_id
        if rotation is not UNSET:
            field_dict["Rotation"] = rotation
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if time_base is not UNSET:
            field_dict["TimeBase"] = time_base
        if codec_time_base is not UNSET:
            field_dict["CodecTimeBase"] = codec_time_base
        if title is not UNSET:
            field_dict["Title"] = title
        if hdr_10_plus_present_flag is not UNSET:
            field_dict["Hdr10PlusPresentFlag"] = hdr_10_plus_present_flag
        if video_range is not UNSET:
            field_dict["VideoRange"] = video_range
        if video_range_type is not UNSET:
            field_dict["VideoRangeType"] = video_range_type
        if video_do_vi_title is not UNSET:
            field_dict["VideoDoViTitle"] = video_do_vi_title
        if audio_spatial_format is not UNSET:
            field_dict["AudioSpatialFormat"] = audio_spatial_format
        if localized_undefined is not UNSET:
            field_dict["LocalizedUndefined"] = localized_undefined
        if localized_default is not UNSET:
            field_dict["LocalizedDefault"] = localized_default
        if localized_forced is not UNSET:
            field_dict["LocalizedForced"] = localized_forced
        if localized_external is not UNSET:
            field_dict["LocalizedExternal"] = localized_external
        if localized_hearing_impaired is not UNSET:
            field_dict["LocalizedHearingImpaired"] = localized_hearing_impaired
        if display_title is not UNSET:
            field_dict["DisplayTitle"] = display_title
        if nal_length_size is not UNSET:
            field_dict["NalLengthSize"] = nal_length_size
        if is_interlaced is not UNSET:
            field_dict["IsInterlaced"] = is_interlaced
        if is_avc is not UNSET:
            field_dict["IsAVC"] = is_avc
        if channel_layout is not UNSET:
            field_dict["ChannelLayout"] = channel_layout
        if bit_rate is not UNSET:
            field_dict["BitRate"] = bit_rate
        if bit_depth is not UNSET:
            field_dict["BitDepth"] = bit_depth
        if ref_frames is not UNSET:
            field_dict["RefFrames"] = ref_frames
        if packet_length is not UNSET:
            field_dict["PacketLength"] = packet_length
        if channels is not UNSET:
            field_dict["Channels"] = channels
        if sample_rate is not UNSET:
            field_dict["SampleRate"] = sample_rate
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default
        if is_forced is not UNSET:
            field_dict["IsForced"] = is_forced
        if is_hearing_impaired is not UNSET:
            field_dict["IsHearingImpaired"] = is_hearing_impaired
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if average_frame_rate is not UNSET:
            field_dict["AverageFrameRate"] = average_frame_rate
        if real_frame_rate is not UNSET:
            field_dict["RealFrameRate"] = real_frame_rate
        if reference_frame_rate is not UNSET:
            field_dict["ReferenceFrameRate"] = reference_frame_rate
        if profile is not UNSET:
            field_dict["Profile"] = profile
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if index is not UNSET:
            field_dict["Index"] = index
        if score is not UNSET:
            field_dict["Score"] = score
        if is_external is not UNSET:
            field_dict["IsExternal"] = is_external
        if delivery_method is not UNSET:
            field_dict["DeliveryMethod"] = delivery_method
        if delivery_url is not UNSET:
            field_dict["DeliveryUrl"] = delivery_url
        if is_external_url is not UNSET:
            field_dict["IsExternalUrl"] = is_external_url
        if is_text_subtitle_stream is not UNSET:
            field_dict["IsTextSubtitleStream"] = is_text_subtitle_stream
        if supports_external_stream is not UNSET:
            field_dict["SupportsExternalStream"] = supports_external_stream
        if path is not UNSET:
            field_dict["Path"] = path
        if pixel_format is not UNSET:
            field_dict["PixelFormat"] = pixel_format
        if level is not UNSET:
            field_dict["Level"] = level
        if is_anamorphic is not UNSET:
            field_dict["IsAnamorphic"] = is_anamorphic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec = _parse_codec(d.pop("Codec", UNSET))

        def _parse_codec_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec_tag = _parse_codec_tag(d.pop("CodecTag", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("Language", UNSET))

        def _parse_color_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_range = _parse_color_range(d.pop("ColorRange", UNSET))

        def _parse_color_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_space = _parse_color_space(d.pop("ColorSpace", UNSET))

        def _parse_color_transfer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_transfer = _parse_color_transfer(d.pop("ColorTransfer", UNSET))

        def _parse_color_primaries(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_primaries = _parse_color_primaries(d.pop("ColorPrimaries", UNSET))

        def _parse_dv_version_major(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dv_version_major = _parse_dv_version_major(d.pop("DvVersionMajor", UNSET))

        def _parse_dv_version_minor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dv_version_minor = _parse_dv_version_minor(d.pop("DvVersionMinor", UNSET))

        def _parse_dv_profile(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dv_profile = _parse_dv_profile(d.pop("DvProfile", UNSET))

        def _parse_dv_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dv_level = _parse_dv_level(d.pop("DvLevel", UNSET))

        def _parse_rpu_present_flag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rpu_present_flag = _parse_rpu_present_flag(d.pop("RpuPresentFlag", UNSET))

        def _parse_el_present_flag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        el_present_flag = _parse_el_present_flag(d.pop("ElPresentFlag", UNSET))

        def _parse_bl_present_flag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bl_present_flag = _parse_bl_present_flag(d.pop("BlPresentFlag", UNSET))

        def _parse_dv_bl_signal_compatibility_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dv_bl_signal_compatibility_id = _parse_dv_bl_signal_compatibility_id(
            d.pop("DvBlSignalCompatibilityId", UNSET)
        )

        def _parse_rotation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rotation = _parse_rotation(d.pop("Rotation", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("Comment", UNSET))

        def _parse_time_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_base = _parse_time_base(d.pop("TimeBase", UNSET))

        def _parse_codec_time_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec_time_base = _parse_codec_time_base(d.pop("CodecTimeBase", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("Title", UNSET))

        def _parse_hdr_10_plus_present_flag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hdr_10_plus_present_flag = _parse_hdr_10_plus_present_flag(
            d.pop("Hdr10PlusPresentFlag", UNSET)
        )

        _video_range = d.pop("VideoRange", UNSET)
        video_range: VideoRange | Unset
        if isinstance(_video_range, Unset):
            video_range = UNSET
        else:
            video_range = VideoRange(_video_range)

        _video_range_type = d.pop("VideoRangeType", UNSET)
        video_range_type: VideoRangeType | Unset
        if isinstance(_video_range_type, Unset):
            video_range_type = UNSET
        else:
            video_range_type = VideoRangeType(_video_range_type)

        def _parse_video_do_vi_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_do_vi_title = _parse_video_do_vi_title(d.pop("VideoDoViTitle", UNSET))

        _audio_spatial_format = d.pop("AudioSpatialFormat", UNSET)
        audio_spatial_format: AudioSpatialFormat | Unset
        if isinstance(_audio_spatial_format, Unset):
            audio_spatial_format = UNSET
        else:
            audio_spatial_format = AudioSpatialFormat(_audio_spatial_format)

        def _parse_localized_undefined(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_undefined = _parse_localized_undefined(
            d.pop("LocalizedUndefined", UNSET)
        )

        def _parse_localized_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_default = _parse_localized_default(d.pop("LocalizedDefault", UNSET))

        def _parse_localized_forced(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_forced = _parse_localized_forced(d.pop("LocalizedForced", UNSET))

        def _parse_localized_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_external = _parse_localized_external(
            d.pop("LocalizedExternal", UNSET)
        )

        def _parse_localized_hearing_impaired(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_hearing_impaired = _parse_localized_hearing_impaired(
            d.pop("LocalizedHearingImpaired", UNSET)
        )

        def _parse_display_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_title = _parse_display_title(d.pop("DisplayTitle", UNSET))

        def _parse_nal_length_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nal_length_size = _parse_nal_length_size(d.pop("NalLengthSize", UNSET))

        is_interlaced = d.pop("IsInterlaced", UNSET)

        def _parse_is_avc(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_avc = _parse_is_avc(d.pop("IsAVC", UNSET))

        def _parse_channel_layout(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_layout = _parse_channel_layout(d.pop("ChannelLayout", UNSET))

        def _parse_bit_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bit_rate = _parse_bit_rate(d.pop("BitRate", UNSET))

        def _parse_bit_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bit_depth = _parse_bit_depth(d.pop("BitDepth", UNSET))

        def _parse_ref_frames(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ref_frames = _parse_ref_frames(d.pop("RefFrames", UNSET))

        def _parse_packet_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        packet_length = _parse_packet_length(d.pop("PacketLength", UNSET))

        def _parse_channels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        channels = _parse_channels(d.pop("Channels", UNSET))

        def _parse_sample_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_rate = _parse_sample_rate(d.pop("SampleRate", UNSET))

        is_default = d.pop("IsDefault", UNSET)

        is_forced = d.pop("IsForced", UNSET)

        is_hearing_impaired = d.pop("IsHearingImpaired", UNSET)

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_average_frame_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_frame_rate = _parse_average_frame_rate(d.pop("AverageFrameRate", UNSET))

        def _parse_real_frame_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        real_frame_rate = _parse_real_frame_rate(d.pop("RealFrameRate", UNSET))

        def _parse_reference_frame_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reference_frame_rate = _parse_reference_frame_rate(
            d.pop("ReferenceFrameRate", UNSET)
        )

        def _parse_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile = _parse_profile(d.pop("Profile", UNSET))

        _type_ = d.pop("Type", UNSET)
        type_: MediaStreamType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MediaStreamType(_type_)

        def _parse_aspect_ratio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aspect_ratio = _parse_aspect_ratio(d.pop("AspectRatio", UNSET))

        index = d.pop("Index", UNSET)

        def _parse_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        score = _parse_score(d.pop("Score", UNSET))

        is_external = d.pop("IsExternal", UNSET)

        _delivery_method = d.pop("DeliveryMethod", UNSET)
        delivery_method: MediaStreamDeliveryMethod | Unset
        if isinstance(_delivery_method, Unset):
            delivery_method = UNSET
        else:
            delivery_method = MediaStreamDeliveryMethod(_delivery_method)

        def _parse_delivery_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_url = _parse_delivery_url(d.pop("DeliveryUrl", UNSET))

        def _parse_is_external_url(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_external_url = _parse_is_external_url(d.pop("IsExternalUrl", UNSET))

        is_text_subtitle_stream = d.pop("IsTextSubtitleStream", UNSET)

        supports_external_stream = d.pop("SupportsExternalStream", UNSET)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_pixel_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pixel_format = _parse_pixel_format(d.pop("PixelFormat", UNSET))

        def _parse_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        level = _parse_level(d.pop("Level", UNSET))

        def _parse_is_anamorphic(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_anamorphic = _parse_is_anamorphic(d.pop("IsAnamorphic", UNSET))

        media_stream = cls(
            codec=codec,
            codec_tag=codec_tag,
            language=language,
            color_range=color_range,
            color_space=color_space,
            color_transfer=color_transfer,
            color_primaries=color_primaries,
            dv_version_major=dv_version_major,
            dv_version_minor=dv_version_minor,
            dv_profile=dv_profile,
            dv_level=dv_level,
            rpu_present_flag=rpu_present_flag,
            el_present_flag=el_present_flag,
            bl_present_flag=bl_present_flag,
            dv_bl_signal_compatibility_id=dv_bl_signal_compatibility_id,
            rotation=rotation,
            comment=comment,
            time_base=time_base,
            codec_time_base=codec_time_base,
            title=title,
            hdr_10_plus_present_flag=hdr_10_plus_present_flag,
            video_range=video_range,
            video_range_type=video_range_type,
            video_do_vi_title=video_do_vi_title,
            audio_spatial_format=audio_spatial_format,
            localized_undefined=localized_undefined,
            localized_default=localized_default,
            localized_forced=localized_forced,
            localized_external=localized_external,
            localized_hearing_impaired=localized_hearing_impaired,
            display_title=display_title,
            nal_length_size=nal_length_size,
            is_interlaced=is_interlaced,
            is_avc=is_avc,
            channel_layout=channel_layout,
            bit_rate=bit_rate,
            bit_depth=bit_depth,
            ref_frames=ref_frames,
            packet_length=packet_length,
            channels=channels,
            sample_rate=sample_rate,
            is_default=is_default,
            is_forced=is_forced,
            is_hearing_impaired=is_hearing_impaired,
            height=height,
            width=width,
            average_frame_rate=average_frame_rate,
            real_frame_rate=real_frame_rate,
            reference_frame_rate=reference_frame_rate,
            profile=profile,
            type_=type_,
            aspect_ratio=aspect_ratio,
            index=index,
            score=score,
            is_external=is_external,
            delivery_method=delivery_method,
            delivery_url=delivery_url,
            is_external_url=is_external_url,
            is_text_subtitle_stream=is_text_subtitle_stream,
            supports_external_stream=supports_external_stream,
            path=path,
            pixel_format=pixel_format,
            level=level,
            is_anamorphic=is_anamorphic,
        )

        return media_stream
