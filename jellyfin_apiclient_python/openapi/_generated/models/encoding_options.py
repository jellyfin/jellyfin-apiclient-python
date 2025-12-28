from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.deinterlace_method import DeinterlaceMethod
from ..models.down_mix_stereo_algorithms import DownMixStereoAlgorithms
from ..models.encoding_options_encoder_preset import EncodingOptionsEncoderPreset
from ..models.hardware_acceleration_type import HardwareAccelerationType
from ..models.tonemapping_algorithm import TonemappingAlgorithm
from ..models.tonemapping_mode import TonemappingMode
from ..models.tonemapping_range import TonemappingRange
from ..types import UNSET, Unset

T = TypeVar("T", bound="EncodingOptions")


@_attrs_define
class EncodingOptions:
    """Class EncodingOptions.

    Attributes:
        encoding_thread_count (int | Unset): Gets or sets the thread count used for encoding.
        transcoding_temp_path (None | str | Unset): Gets or sets the temporary transcoding path.
        fallback_font_path (None | str | Unset): Gets or sets the path to the fallback font.
        enable_fallback_font (bool | Unset): Gets or sets a value indicating whether to use the fallback font.
        enable_audio_vbr (bool | Unset): Gets or sets a value indicating whether audio VBR is enabled.
        down_mix_audio_boost (float | Unset): Gets or sets the audio boost applied when downmixing audio.
        down_mix_stereo_algorithm (DownMixStereoAlgorithms | Unset): An enum representing an algorithm to downmix
            surround sound to stereo.
        max_muxing_queue_size (int | Unset): Gets or sets the maximum size of the muxing queue.
        enable_throttling (bool | Unset): Gets or sets a value indicating whether throttling is enabled.
        throttle_delay_seconds (int | Unset): Gets or sets the delay after which throttling happens.
        enable_segment_deletion (bool | Unset): Gets or sets a value indicating whether segment deletion is enabled.
        segment_keep_seconds (int | Unset): Gets or sets seconds for which segments should be kept before being deleted.
        hardware_acceleration_type (HardwareAccelerationType | Unset): Enum containing hardware acceleration types.
        encoder_app_path (None | str | Unset): Gets or sets the FFmpeg path as set by the user via the UI.
        encoder_app_path_display (None | str | Unset): Gets or sets the current FFmpeg path being used by the system and
            displayed on the transcode page.
        vaapi_device (None | str | Unset): Gets or sets the VA-API device.
        qsv_device (None | str | Unset): Gets or sets the QSV device.
        enable_tonemapping (bool | Unset): Gets or sets a value indicating whether tonemapping is enabled.
        enable_vpp_tonemapping (bool | Unset): Gets or sets a value indicating whether VPP tonemapping is enabled.
        enable_video_toolbox_tonemapping (bool | Unset): Gets or sets a value indicating whether videotoolbox
            tonemapping is enabled.
        tonemapping_algorithm (TonemappingAlgorithm | Unset): Enum containing tonemapping algorithms.
        tonemapping_mode (TonemappingMode | Unset): Enum containing tonemapping modes.
        tonemapping_range (TonemappingRange | Unset): Enum containing tonemapping ranges.
        tonemapping_desat (float | Unset): Gets or sets the tone-mapping desaturation.
        tonemapping_peak (float | Unset): Gets or sets the tone-mapping peak.
        tonemapping_param (float | Unset): Gets or sets the tone-mapping parameters.
        vpp_tonemapping_brightness (float | Unset): Gets or sets the VPP tone-mapping brightness.
        vpp_tonemapping_contrast (float | Unset): Gets or sets the VPP tone-mapping contrast.
        h264_crf (int | Unset): Gets or sets the H264 CRF.
        h265_crf (int | Unset): Gets or sets the H265 CRF.
        encoder_preset (EncodingOptionsEncoderPreset | Unset): Gets or sets the encoder preset.
        deinterlace_double_rate (bool | Unset): Gets or sets a value indicating whether the framerate is doubled when
            deinterlacing.
        deinterlace_method (DeinterlaceMethod | Unset): Enum containing deinterlace methods.
        enable_decoding_color_depth_10_hevc (bool | Unset): Gets or sets a value indicating whether 10bit HEVC decoding
            is enabled.
        enable_decoding_color_depth_10_vp_9 (bool | Unset): Gets or sets a value indicating whether 10bit VP9 decoding
            is enabled.
        enable_decoding_color_depth_10_hevc_rext (bool | Unset): Gets or sets a value indicating whether 8/10bit HEVC
            RExt decoding is enabled.
        enable_decoding_color_depth_12_hevc_rext (bool | Unset): Gets or sets a value indicating whether 12bit HEVC RExt
            decoding is enabled.
        enable_enhanced_nvdec_decoder (bool | Unset): Gets or sets a value indicating whether the enhanced NVDEC is
            enabled.
        prefer_system_native_hw_decoder (bool | Unset): Gets or sets a value indicating whether the system native
            hardware decoder should be used.
        enable_intel_low_power_h264_hw_encoder (bool | Unset): Gets or sets a value indicating whether the Intel H264
            low-power hardware encoder should be used.
        enable_intel_low_power_hevc_hw_encoder (bool | Unset): Gets or sets a value indicating whether the Intel HEVC
            low-power hardware encoder should be used.
        enable_hardware_encoding (bool | Unset): Gets or sets a value indicating whether hardware encoding is enabled.
        allow_hevc_encoding (bool | Unset): Gets or sets a value indicating whether HEVC encoding is enabled.
        allow_av_1_encoding (bool | Unset): Gets or sets a value indicating whether AV1 encoding is enabled.
        enable_subtitle_extraction (bool | Unset): Gets or sets a value indicating whether subtitle extraction is
            enabled.
        hardware_decoding_codecs (list[str] | None | Unset): Gets or sets the codecs hardware encoding is used for.
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions (list[str] | None | Unset): Gets or sets the
            file extensions on-demand metadata based keyframe extraction is enabled for.
    """

    encoding_thread_count: int | Unset = UNSET
    transcoding_temp_path: None | str | Unset = UNSET
    fallback_font_path: None | str | Unset = UNSET
    enable_fallback_font: bool | Unset = UNSET
    enable_audio_vbr: bool | Unset = UNSET
    down_mix_audio_boost: float | Unset = UNSET
    down_mix_stereo_algorithm: DownMixStereoAlgorithms | Unset = UNSET
    max_muxing_queue_size: int | Unset = UNSET
    enable_throttling: bool | Unset = UNSET
    throttle_delay_seconds: int | Unset = UNSET
    enable_segment_deletion: bool | Unset = UNSET
    segment_keep_seconds: int | Unset = UNSET
    hardware_acceleration_type: HardwareAccelerationType | Unset = UNSET
    encoder_app_path: None | str | Unset = UNSET
    encoder_app_path_display: None | str | Unset = UNSET
    vaapi_device: None | str | Unset = UNSET
    qsv_device: None | str | Unset = UNSET
    enable_tonemapping: bool | Unset = UNSET
    enable_vpp_tonemapping: bool | Unset = UNSET
    enable_video_toolbox_tonemapping: bool | Unset = UNSET
    tonemapping_algorithm: TonemappingAlgorithm | Unset = UNSET
    tonemapping_mode: TonemappingMode | Unset = UNSET
    tonemapping_range: TonemappingRange | Unset = UNSET
    tonemapping_desat: float | Unset = UNSET
    tonemapping_peak: float | Unset = UNSET
    tonemapping_param: float | Unset = UNSET
    vpp_tonemapping_brightness: float | Unset = UNSET
    vpp_tonemapping_contrast: float | Unset = UNSET
    h264_crf: int | Unset = UNSET
    h265_crf: int | Unset = UNSET
    encoder_preset: EncodingOptionsEncoderPreset | Unset = UNSET
    deinterlace_double_rate: bool | Unset = UNSET
    deinterlace_method: DeinterlaceMethod | Unset = UNSET
    enable_decoding_color_depth_10_hevc: bool | Unset = UNSET
    enable_decoding_color_depth_10_vp_9: bool | Unset = UNSET
    enable_decoding_color_depth_10_hevc_rext: bool | Unset = UNSET
    enable_decoding_color_depth_12_hevc_rext: bool | Unset = UNSET
    enable_enhanced_nvdec_decoder: bool | Unset = UNSET
    prefer_system_native_hw_decoder: bool | Unset = UNSET
    enable_intel_low_power_h264_hw_encoder: bool | Unset = UNSET
    enable_intel_low_power_hevc_hw_encoder: bool | Unset = UNSET
    enable_hardware_encoding: bool | Unset = UNSET
    allow_hevc_encoding: bool | Unset = UNSET
    allow_av_1_encoding: bool | Unset = UNSET
    enable_subtitle_extraction: bool | Unset = UNSET
    hardware_decoding_codecs: list[str] | None | Unset = UNSET
    allow_on_demand_metadata_based_keyframe_extraction_for_extensions: (
        list[str] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        encoding_thread_count = self.encoding_thread_count

        transcoding_temp_path: None | str | Unset
        if isinstance(self.transcoding_temp_path, Unset):
            transcoding_temp_path = UNSET
        else:
            transcoding_temp_path = self.transcoding_temp_path

        fallback_font_path: None | str | Unset
        if isinstance(self.fallback_font_path, Unset):
            fallback_font_path = UNSET
        else:
            fallback_font_path = self.fallback_font_path

        enable_fallback_font = self.enable_fallback_font

        enable_audio_vbr = self.enable_audio_vbr

        down_mix_audio_boost = self.down_mix_audio_boost

        down_mix_stereo_algorithm: str | Unset = UNSET
        if not isinstance(self.down_mix_stereo_algorithm, Unset):
            down_mix_stereo_algorithm = self.down_mix_stereo_algorithm.value

        max_muxing_queue_size = self.max_muxing_queue_size

        enable_throttling = self.enable_throttling

        throttle_delay_seconds = self.throttle_delay_seconds

        enable_segment_deletion = self.enable_segment_deletion

        segment_keep_seconds = self.segment_keep_seconds

        hardware_acceleration_type: str | Unset = UNSET
        if not isinstance(self.hardware_acceleration_type, Unset):
            hardware_acceleration_type = self.hardware_acceleration_type.value

        encoder_app_path: None | str | Unset
        if isinstance(self.encoder_app_path, Unset):
            encoder_app_path = UNSET
        else:
            encoder_app_path = self.encoder_app_path

        encoder_app_path_display: None | str | Unset
        if isinstance(self.encoder_app_path_display, Unset):
            encoder_app_path_display = UNSET
        else:
            encoder_app_path_display = self.encoder_app_path_display

        vaapi_device: None | str | Unset
        if isinstance(self.vaapi_device, Unset):
            vaapi_device = UNSET
        else:
            vaapi_device = self.vaapi_device

        qsv_device: None | str | Unset
        if isinstance(self.qsv_device, Unset):
            qsv_device = UNSET
        else:
            qsv_device = self.qsv_device

        enable_tonemapping = self.enable_tonemapping

        enable_vpp_tonemapping = self.enable_vpp_tonemapping

        enable_video_toolbox_tonemapping = self.enable_video_toolbox_tonemapping

        tonemapping_algorithm: str | Unset = UNSET
        if not isinstance(self.tonemapping_algorithm, Unset):
            tonemapping_algorithm = self.tonemapping_algorithm.value

        tonemapping_mode: str | Unset = UNSET
        if not isinstance(self.tonemapping_mode, Unset):
            tonemapping_mode = self.tonemapping_mode.value

        tonemapping_range: str | Unset = UNSET
        if not isinstance(self.tonemapping_range, Unset):
            tonemapping_range = self.tonemapping_range.value

        tonemapping_desat = self.tonemapping_desat

        tonemapping_peak = self.tonemapping_peak

        tonemapping_param = self.tonemapping_param

        vpp_tonemapping_brightness = self.vpp_tonemapping_brightness

        vpp_tonemapping_contrast = self.vpp_tonemapping_contrast

        h264_crf = self.h264_crf

        h265_crf = self.h265_crf

        encoder_preset: str | Unset = UNSET
        if not isinstance(self.encoder_preset, Unset):
            encoder_preset = self.encoder_preset.value

        deinterlace_double_rate = self.deinterlace_double_rate

        deinterlace_method: str | Unset = UNSET
        if not isinstance(self.deinterlace_method, Unset):
            deinterlace_method = self.deinterlace_method.value

        enable_decoding_color_depth_10_hevc = self.enable_decoding_color_depth_10_hevc

        enable_decoding_color_depth_10_vp_9 = self.enable_decoding_color_depth_10_vp_9

        enable_decoding_color_depth_10_hevc_rext = (
            self.enable_decoding_color_depth_10_hevc_rext
        )

        enable_decoding_color_depth_12_hevc_rext = (
            self.enable_decoding_color_depth_12_hevc_rext
        )

        enable_enhanced_nvdec_decoder = self.enable_enhanced_nvdec_decoder

        prefer_system_native_hw_decoder = self.prefer_system_native_hw_decoder

        enable_intel_low_power_h264_hw_encoder = (
            self.enable_intel_low_power_h264_hw_encoder
        )

        enable_intel_low_power_hevc_hw_encoder = (
            self.enable_intel_low_power_hevc_hw_encoder
        )

        enable_hardware_encoding = self.enable_hardware_encoding

        allow_hevc_encoding = self.allow_hevc_encoding

        allow_av_1_encoding = self.allow_av_1_encoding

        enable_subtitle_extraction = self.enable_subtitle_extraction

        hardware_decoding_codecs: list[str] | None | Unset
        if isinstance(self.hardware_decoding_codecs, Unset):
            hardware_decoding_codecs = UNSET
        elif isinstance(self.hardware_decoding_codecs, list):
            hardware_decoding_codecs = self.hardware_decoding_codecs

        else:
            hardware_decoding_codecs = self.hardware_decoding_codecs

        allow_on_demand_metadata_based_keyframe_extraction_for_extensions: (
            list[str] | None | Unset
        )
        if isinstance(
            self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
            Unset,
        ):
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = UNSET
        elif isinstance(
            self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions, list
        ):
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
                self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            )

        else:
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
                self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if encoding_thread_count is not UNSET:
            field_dict["EncodingThreadCount"] = encoding_thread_count
        if transcoding_temp_path is not UNSET:
            field_dict["TranscodingTempPath"] = transcoding_temp_path
        if fallback_font_path is not UNSET:
            field_dict["FallbackFontPath"] = fallback_font_path
        if enable_fallback_font is not UNSET:
            field_dict["EnableFallbackFont"] = enable_fallback_font
        if enable_audio_vbr is not UNSET:
            field_dict["EnableAudioVbr"] = enable_audio_vbr
        if down_mix_audio_boost is not UNSET:
            field_dict["DownMixAudioBoost"] = down_mix_audio_boost
        if down_mix_stereo_algorithm is not UNSET:
            field_dict["DownMixStereoAlgorithm"] = down_mix_stereo_algorithm
        if max_muxing_queue_size is not UNSET:
            field_dict["MaxMuxingQueueSize"] = max_muxing_queue_size
        if enable_throttling is not UNSET:
            field_dict["EnableThrottling"] = enable_throttling
        if throttle_delay_seconds is not UNSET:
            field_dict["ThrottleDelaySeconds"] = throttle_delay_seconds
        if enable_segment_deletion is not UNSET:
            field_dict["EnableSegmentDeletion"] = enable_segment_deletion
        if segment_keep_seconds is not UNSET:
            field_dict["SegmentKeepSeconds"] = segment_keep_seconds
        if hardware_acceleration_type is not UNSET:
            field_dict["HardwareAccelerationType"] = hardware_acceleration_type
        if encoder_app_path is not UNSET:
            field_dict["EncoderAppPath"] = encoder_app_path
        if encoder_app_path_display is not UNSET:
            field_dict["EncoderAppPathDisplay"] = encoder_app_path_display
        if vaapi_device is not UNSET:
            field_dict["VaapiDevice"] = vaapi_device
        if qsv_device is not UNSET:
            field_dict["QsvDevice"] = qsv_device
        if enable_tonemapping is not UNSET:
            field_dict["EnableTonemapping"] = enable_tonemapping
        if enable_vpp_tonemapping is not UNSET:
            field_dict["EnableVppTonemapping"] = enable_vpp_tonemapping
        if enable_video_toolbox_tonemapping is not UNSET:
            field_dict["EnableVideoToolboxTonemapping"] = (
                enable_video_toolbox_tonemapping
            )
        if tonemapping_algorithm is not UNSET:
            field_dict["TonemappingAlgorithm"] = tonemapping_algorithm
        if tonemapping_mode is not UNSET:
            field_dict["TonemappingMode"] = tonemapping_mode
        if tonemapping_range is not UNSET:
            field_dict["TonemappingRange"] = tonemapping_range
        if tonemapping_desat is not UNSET:
            field_dict["TonemappingDesat"] = tonemapping_desat
        if tonemapping_peak is not UNSET:
            field_dict["TonemappingPeak"] = tonemapping_peak
        if tonemapping_param is not UNSET:
            field_dict["TonemappingParam"] = tonemapping_param
        if vpp_tonemapping_brightness is not UNSET:
            field_dict["VppTonemappingBrightness"] = vpp_tonemapping_brightness
        if vpp_tonemapping_contrast is not UNSET:
            field_dict["VppTonemappingContrast"] = vpp_tonemapping_contrast
        if h264_crf is not UNSET:
            field_dict["H264Crf"] = h264_crf
        if h265_crf is not UNSET:
            field_dict["H265Crf"] = h265_crf
        if encoder_preset is not UNSET:
            field_dict["EncoderPreset"] = encoder_preset
        if deinterlace_double_rate is not UNSET:
            field_dict["DeinterlaceDoubleRate"] = deinterlace_double_rate
        if deinterlace_method is not UNSET:
            field_dict["DeinterlaceMethod"] = deinterlace_method
        if enable_decoding_color_depth_10_hevc is not UNSET:
            field_dict["EnableDecodingColorDepth10Hevc"] = (
                enable_decoding_color_depth_10_hevc
            )
        if enable_decoding_color_depth_10_vp_9 is not UNSET:
            field_dict["EnableDecodingColorDepth10Vp9"] = (
                enable_decoding_color_depth_10_vp_9
            )
        if enable_decoding_color_depth_10_hevc_rext is not UNSET:
            field_dict["EnableDecodingColorDepth10HevcRext"] = (
                enable_decoding_color_depth_10_hevc_rext
            )
        if enable_decoding_color_depth_12_hevc_rext is not UNSET:
            field_dict["EnableDecodingColorDepth12HevcRext"] = (
                enable_decoding_color_depth_12_hevc_rext
            )
        if enable_enhanced_nvdec_decoder is not UNSET:
            field_dict["EnableEnhancedNvdecDecoder"] = enable_enhanced_nvdec_decoder
        if prefer_system_native_hw_decoder is not UNSET:
            field_dict["PreferSystemNativeHwDecoder"] = prefer_system_native_hw_decoder
        if enable_intel_low_power_h264_hw_encoder is not UNSET:
            field_dict["EnableIntelLowPowerH264HwEncoder"] = (
                enable_intel_low_power_h264_hw_encoder
            )
        if enable_intel_low_power_hevc_hw_encoder is not UNSET:
            field_dict["EnableIntelLowPowerHevcHwEncoder"] = (
                enable_intel_low_power_hevc_hw_encoder
            )
        if enable_hardware_encoding is not UNSET:
            field_dict["EnableHardwareEncoding"] = enable_hardware_encoding
        if allow_hevc_encoding is not UNSET:
            field_dict["AllowHevcEncoding"] = allow_hevc_encoding
        if allow_av_1_encoding is not UNSET:
            field_dict["AllowAv1Encoding"] = allow_av_1_encoding
        if enable_subtitle_extraction is not UNSET:
            field_dict["EnableSubtitleExtraction"] = enable_subtitle_extraction
        if hardware_decoding_codecs is not UNSET:
            field_dict["HardwareDecodingCodecs"] = hardware_decoding_codecs
        if (
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            is not UNSET
        ):
            field_dict["AllowOnDemandMetadataBasedKeyframeExtractionForExtensions"] = (
                allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encoding_thread_count = d.pop("EncodingThreadCount", UNSET)

        def _parse_transcoding_temp_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcoding_temp_path = _parse_transcoding_temp_path(
            d.pop("TranscodingTempPath", UNSET)
        )

        def _parse_fallback_font_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fallback_font_path = _parse_fallback_font_path(d.pop("FallbackFontPath", UNSET))

        enable_fallback_font = d.pop("EnableFallbackFont", UNSET)

        enable_audio_vbr = d.pop("EnableAudioVbr", UNSET)

        down_mix_audio_boost = d.pop("DownMixAudioBoost", UNSET)

        _down_mix_stereo_algorithm = d.pop("DownMixStereoAlgorithm", UNSET)
        down_mix_stereo_algorithm: DownMixStereoAlgorithms | Unset
        if isinstance(_down_mix_stereo_algorithm, Unset):
            down_mix_stereo_algorithm = UNSET
        else:
            down_mix_stereo_algorithm = DownMixStereoAlgorithms(
                _down_mix_stereo_algorithm
            )

        max_muxing_queue_size = d.pop("MaxMuxingQueueSize", UNSET)

        enable_throttling = d.pop("EnableThrottling", UNSET)

        throttle_delay_seconds = d.pop("ThrottleDelaySeconds", UNSET)

        enable_segment_deletion = d.pop("EnableSegmentDeletion", UNSET)

        segment_keep_seconds = d.pop("SegmentKeepSeconds", UNSET)

        _hardware_acceleration_type = d.pop("HardwareAccelerationType", UNSET)
        hardware_acceleration_type: HardwareAccelerationType | Unset
        if isinstance(_hardware_acceleration_type, Unset):
            hardware_acceleration_type = UNSET
        else:
            hardware_acceleration_type = HardwareAccelerationType(
                _hardware_acceleration_type
            )

        def _parse_encoder_app_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encoder_app_path = _parse_encoder_app_path(d.pop("EncoderAppPath", UNSET))

        def _parse_encoder_app_path_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encoder_app_path_display = _parse_encoder_app_path_display(
            d.pop("EncoderAppPathDisplay", UNSET)
        )

        def _parse_vaapi_device(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vaapi_device = _parse_vaapi_device(d.pop("VaapiDevice", UNSET))

        def _parse_qsv_device(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qsv_device = _parse_qsv_device(d.pop("QsvDevice", UNSET))

        enable_tonemapping = d.pop("EnableTonemapping", UNSET)

        enable_vpp_tonemapping = d.pop("EnableVppTonemapping", UNSET)

        enable_video_toolbox_tonemapping = d.pop("EnableVideoToolboxTonemapping", UNSET)

        _tonemapping_algorithm = d.pop("TonemappingAlgorithm", UNSET)
        tonemapping_algorithm: TonemappingAlgorithm | Unset
        if isinstance(_tonemapping_algorithm, Unset):
            tonemapping_algorithm = UNSET
        else:
            tonemapping_algorithm = TonemappingAlgorithm(_tonemapping_algorithm)

        _tonemapping_mode = d.pop("TonemappingMode", UNSET)
        tonemapping_mode: TonemappingMode | Unset
        if isinstance(_tonemapping_mode, Unset):
            tonemapping_mode = UNSET
        else:
            tonemapping_mode = TonemappingMode(_tonemapping_mode)

        _tonemapping_range = d.pop("TonemappingRange", UNSET)
        tonemapping_range: TonemappingRange | Unset
        if isinstance(_tonemapping_range, Unset):
            tonemapping_range = UNSET
        else:
            tonemapping_range = TonemappingRange(_tonemapping_range)

        tonemapping_desat = d.pop("TonemappingDesat", UNSET)

        tonemapping_peak = d.pop("TonemappingPeak", UNSET)

        tonemapping_param = d.pop("TonemappingParam", UNSET)

        vpp_tonemapping_brightness = d.pop("VppTonemappingBrightness", UNSET)

        vpp_tonemapping_contrast = d.pop("VppTonemappingContrast", UNSET)

        h264_crf = d.pop("H264Crf", UNSET)

        h265_crf = d.pop("H265Crf", UNSET)

        _encoder_preset = d.pop("EncoderPreset", UNSET)
        encoder_preset: EncodingOptionsEncoderPreset | Unset
        if isinstance(_encoder_preset, Unset):
            encoder_preset = UNSET
        else:
            encoder_preset = EncodingOptionsEncoderPreset(_encoder_preset)

        deinterlace_double_rate = d.pop("DeinterlaceDoubleRate", UNSET)

        _deinterlace_method = d.pop("DeinterlaceMethod", UNSET)
        deinterlace_method: DeinterlaceMethod | Unset
        if isinstance(_deinterlace_method, Unset):
            deinterlace_method = UNSET
        else:
            deinterlace_method = DeinterlaceMethod(_deinterlace_method)

        enable_decoding_color_depth_10_hevc = d.pop(
            "EnableDecodingColorDepth10Hevc", UNSET
        )

        enable_decoding_color_depth_10_vp_9 = d.pop(
            "EnableDecodingColorDepth10Vp9", UNSET
        )

        enable_decoding_color_depth_10_hevc_rext = d.pop(
            "EnableDecodingColorDepth10HevcRext", UNSET
        )

        enable_decoding_color_depth_12_hevc_rext = d.pop(
            "EnableDecodingColorDepth12HevcRext", UNSET
        )

        enable_enhanced_nvdec_decoder = d.pop("EnableEnhancedNvdecDecoder", UNSET)

        prefer_system_native_hw_decoder = d.pop("PreferSystemNativeHwDecoder", UNSET)

        enable_intel_low_power_h264_hw_encoder = d.pop(
            "EnableIntelLowPowerH264HwEncoder", UNSET
        )

        enable_intel_low_power_hevc_hw_encoder = d.pop(
            "EnableIntelLowPowerHevcHwEncoder", UNSET
        )

        enable_hardware_encoding = d.pop("EnableHardwareEncoding", UNSET)

        allow_hevc_encoding = d.pop("AllowHevcEncoding", UNSET)

        allow_av_1_encoding = d.pop("AllowAv1Encoding", UNSET)

        enable_subtitle_extraction = d.pop("EnableSubtitleExtraction", UNSET)

        def _parse_hardware_decoding_codecs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hardware_decoding_codecs_type_0 = cast(list[str], data)

                return hardware_decoding_codecs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        hardware_decoding_codecs = _parse_hardware_decoding_codecs(
            d.pop("HardwareDecodingCodecs", UNSET)
        )

        def _parse_allow_on_demand_metadata_based_keyframe_extraction_for_extensions(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allow_on_demand_metadata_based_keyframe_extraction_for_extensions_type_0 = cast(
                    list[str], data
                )

                return allow_on_demand_metadata_based_keyframe_extraction_for_extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
            _parse_allow_on_demand_metadata_based_keyframe_extraction_for_extensions(
                d.pop(
                    "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions", UNSET
                )
            )
        )

        encoding_options = cls(
            encoding_thread_count=encoding_thread_count,
            transcoding_temp_path=transcoding_temp_path,
            fallback_font_path=fallback_font_path,
            enable_fallback_font=enable_fallback_font,
            enable_audio_vbr=enable_audio_vbr,
            down_mix_audio_boost=down_mix_audio_boost,
            down_mix_stereo_algorithm=down_mix_stereo_algorithm,
            max_muxing_queue_size=max_muxing_queue_size,
            enable_throttling=enable_throttling,
            throttle_delay_seconds=throttle_delay_seconds,
            enable_segment_deletion=enable_segment_deletion,
            segment_keep_seconds=segment_keep_seconds,
            hardware_acceleration_type=hardware_acceleration_type,
            encoder_app_path=encoder_app_path,
            encoder_app_path_display=encoder_app_path_display,
            vaapi_device=vaapi_device,
            qsv_device=qsv_device,
            enable_tonemapping=enable_tonemapping,
            enable_vpp_tonemapping=enable_vpp_tonemapping,
            enable_video_toolbox_tonemapping=enable_video_toolbox_tonemapping,
            tonemapping_algorithm=tonemapping_algorithm,
            tonemapping_mode=tonemapping_mode,
            tonemapping_range=tonemapping_range,
            tonemapping_desat=tonemapping_desat,
            tonemapping_peak=tonemapping_peak,
            tonemapping_param=tonemapping_param,
            vpp_tonemapping_brightness=vpp_tonemapping_brightness,
            vpp_tonemapping_contrast=vpp_tonemapping_contrast,
            h264_crf=h264_crf,
            h265_crf=h265_crf,
            encoder_preset=encoder_preset,
            deinterlace_double_rate=deinterlace_double_rate,
            deinterlace_method=deinterlace_method,
            enable_decoding_color_depth_10_hevc=enable_decoding_color_depth_10_hevc,
            enable_decoding_color_depth_10_vp_9=enable_decoding_color_depth_10_vp_9,
            enable_decoding_color_depth_10_hevc_rext=enable_decoding_color_depth_10_hevc_rext,
            enable_decoding_color_depth_12_hevc_rext=enable_decoding_color_depth_12_hevc_rext,
            enable_enhanced_nvdec_decoder=enable_enhanced_nvdec_decoder,
            prefer_system_native_hw_decoder=prefer_system_native_hw_decoder,
            enable_intel_low_power_h264_hw_encoder=enable_intel_low_power_h264_hw_encoder,
            enable_intel_low_power_hevc_hw_encoder=enable_intel_low_power_hevc_hw_encoder,
            enable_hardware_encoding=enable_hardware_encoding,
            allow_hevc_encoding=allow_hevc_encoding,
            allow_av_1_encoding=allow_av_1_encoding,
            enable_subtitle_extraction=enable_subtitle_extraction,
            hardware_decoding_codecs=hardware_decoding_codecs,
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions=allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
        )

        return encoding_options
