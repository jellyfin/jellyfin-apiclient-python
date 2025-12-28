from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.encoding_context import EncodingContext
from ...models.get_master_hls_video_playlist_stream_options import (
    GetMasterHlsVideoPlaylistStreamOptions,
)
from ...models.subtitle_delivery_method import SubtitleDeliveryMethod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    static: bool | Unset = UNSET,
    params: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    device_profile_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    segment_container: str | Unset = UNSET,
    segment_length: int | Unset = UNSET,
    min_segments: int | Unset = UNSET,
    media_source_id: str,
    device_id: str | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    enable_auto_stream_copy: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
    break_on_non_key_frames: bool | Unset = UNSET,
    audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    audio_channels: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    profile: str | Unset = UNSET,
    level: str | Unset = UNSET,
    framerate: float | Unset = UNSET,
    max_framerate: float | Unset = UNSET,
    copy_timestamps: bool | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    video_bit_rate: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    subtitle_method: SubtitleDeliveryMethod | Unset = UNSET,
    max_ref_frames: int | Unset = UNSET,
    max_video_bit_depth: int | Unset = UNSET,
    require_avc: bool | Unset = UNSET,
    de_interlace: bool | Unset = UNSET,
    require_non_anamorphic: bool | Unset = UNSET,
    transcoding_max_audio_channels: int | Unset = UNSET,
    cpu_core_limit: int | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    enable_mpegts_m2_ts_mode: bool | Unset = UNSET,
    video_codec: str | Unset = UNSET,
    subtitle_codec: str | Unset = UNSET,
    transcode_reasons: str | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    video_stream_index: int | Unset = UNSET,
    context: EncodingContext | Unset = UNSET,
    stream_options: GetMasterHlsVideoPlaylistStreamOptions | Unset = UNSET,
    enable_adaptive_bitrate_streaming: bool | Unset = False,
    enable_trickplay: bool | Unset = True,
    enable_audio_vbr_encoding: bool | Unset = True,
    always_burn_in_subtitle_when_transcoding: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["static"] = static

    params["params"] = params

    params["tag"] = tag

    params["deviceProfileId"] = device_profile_id

    params["playSessionId"] = play_session_id

    params["segmentContainer"] = segment_container

    params["segmentLength"] = segment_length

    params["minSegments"] = min_segments

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    params["audioCodec"] = audio_codec

    params["enableAutoStreamCopy"] = enable_auto_stream_copy

    params["allowVideoStreamCopy"] = allow_video_stream_copy

    params["allowAudioStreamCopy"] = allow_audio_stream_copy

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["audioSampleRate"] = audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["audioBitRate"] = audio_bit_rate

    params["audioChannels"] = audio_channels

    params["maxAudioChannels"] = max_audio_channels

    params["profile"] = profile

    params["level"] = level

    params["framerate"] = framerate

    params["maxFramerate"] = max_framerate

    params["copyTimestamps"] = copy_timestamps

    params["startTimeTicks"] = start_time_ticks

    params["width"] = width

    params["height"] = height

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["videoBitRate"] = video_bit_rate

    params["subtitleStreamIndex"] = subtitle_stream_index

    json_subtitle_method: str | Unset = UNSET
    if not isinstance(subtitle_method, Unset):
        json_subtitle_method = subtitle_method.value

    params["subtitleMethod"] = json_subtitle_method

    params["maxRefFrames"] = max_ref_frames

    params["maxVideoBitDepth"] = max_video_bit_depth

    params["requireAvc"] = require_avc

    params["deInterlace"] = de_interlace

    params["requireNonAnamorphic"] = require_non_anamorphic

    params["transcodingMaxAudioChannels"] = transcoding_max_audio_channels

    params["cpuCoreLimit"] = cpu_core_limit

    params["liveStreamId"] = live_stream_id

    params["enableMpegtsM2TsMode"] = enable_mpegts_m2_ts_mode

    params["videoCodec"] = video_codec

    params["subtitleCodec"] = subtitle_codec

    params["transcodeReasons"] = transcode_reasons

    params["audioStreamIndex"] = audio_stream_index

    params["videoStreamIndex"] = video_stream_index

    json_context: str | Unset = UNSET
    if not isinstance(context, Unset):
        json_context = context.value

    params["context"] = json_context

    json_stream_options: dict[str, Any] | Unset = UNSET
    if not isinstance(stream_options, Unset):
        json_stream_options = stream_options.to_dict()
    if not isinstance(json_stream_options, Unset):
        params.update(json_stream_options)

    params["enableAdaptiveBitrateStreaming"] = enable_adaptive_bitrate_streaming

    params["enableTrickplay"] = enable_trickplay

    params["enableAudioVbrEncoding"] = enable_audio_vbr_encoding

    params["alwaysBurnInSubtitleWhenTranscoding"] = (
        always_burn_in_subtitle_when_transcoding
    )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{item_id}/master.m3u8".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 503:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    static: bool | Unset = UNSET,
    params: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    device_profile_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    segment_container: str | Unset = UNSET,
    segment_length: int | Unset = UNSET,
    min_segments: int | Unset = UNSET,
    media_source_id: str,
    device_id: str | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    enable_auto_stream_copy: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
    break_on_non_key_frames: bool | Unset = UNSET,
    audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    audio_channels: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    profile: str | Unset = UNSET,
    level: str | Unset = UNSET,
    framerate: float | Unset = UNSET,
    max_framerate: float | Unset = UNSET,
    copy_timestamps: bool | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    video_bit_rate: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    subtitle_method: SubtitleDeliveryMethod | Unset = UNSET,
    max_ref_frames: int | Unset = UNSET,
    max_video_bit_depth: int | Unset = UNSET,
    require_avc: bool | Unset = UNSET,
    de_interlace: bool | Unset = UNSET,
    require_non_anamorphic: bool | Unset = UNSET,
    transcoding_max_audio_channels: int | Unset = UNSET,
    cpu_core_limit: int | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    enable_mpegts_m2_ts_mode: bool | Unset = UNSET,
    video_codec: str | Unset = UNSET,
    subtitle_codec: str | Unset = UNSET,
    transcode_reasons: str | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    video_stream_index: int | Unset = UNSET,
    context: EncodingContext | Unset = UNSET,
    stream_options: GetMasterHlsVideoPlaylistStreamOptions | Unset = UNSET,
    enable_adaptive_bitrate_streaming: bool | Unset = False,
    enable_trickplay: bool | Unset = True,
    enable_audio_vbr_encoding: bool | Unset = True,
    always_burn_in_subtitle_when_transcoding: bool | Unset = False,
) -> Response[Any]:
    """Gets a video hls playlist stream.

    Args:
        item_id (UUID):
        static (bool | Unset):
        params (str | Unset):
        tag (str | Unset):
        device_profile_id (str | Unset):
        play_session_id (str | Unset):
        segment_container (str | Unset):
        segment_length (int | Unset):
        min_segments (int | Unset):
        media_source_id (str):
        device_id (str | Unset):
        audio_codec (str | Unset):
        enable_auto_stream_copy (bool | Unset):
        allow_video_stream_copy (bool | Unset):
        allow_audio_stream_copy (bool | Unset):
        break_on_non_key_frames (bool | Unset):
        audio_sample_rate (int | Unset):
        max_audio_bit_depth (int | Unset):
        audio_bit_rate (int | Unset):
        audio_channels (int | Unset):
        max_audio_channels (int | Unset):
        profile (str | Unset):
        level (str | Unset):
        framerate (float | Unset):
        max_framerate (float | Unset):
        copy_timestamps (bool | Unset):
        start_time_ticks (int | Unset):
        width (int | Unset):
        height (int | Unset):
        max_width (int | Unset):
        max_height (int | Unset):
        video_bit_rate (int | Unset):
        subtitle_stream_index (int | Unset):
        subtitle_method (SubtitleDeliveryMethod | Unset): Delivery method to use during playback
            of a specific subtitle format.
        max_ref_frames (int | Unset):
        max_video_bit_depth (int | Unset):
        require_avc (bool | Unset):
        de_interlace (bool | Unset):
        require_non_anamorphic (bool | Unset):
        transcoding_max_audio_channels (int | Unset):
        cpu_core_limit (int | Unset):
        live_stream_id (str | Unset):
        enable_mpegts_m2_ts_mode (bool | Unset):
        video_codec (str | Unset):
        subtitle_codec (str | Unset):
        transcode_reasons (str | Unset):
        audio_stream_index (int | Unset):
        video_stream_index (int | Unset):
        context (EncodingContext | Unset):
        stream_options (GetMasterHlsVideoPlaylistStreamOptions | Unset):
        enable_adaptive_bitrate_streaming (bool | Unset):  Default: False.
        enable_trickplay (bool | Unset):  Default: True.
        enable_audio_vbr_encoding (bool | Unset):  Default: True.
        always_burn_in_subtitle_when_transcoding (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        static=static,
        params=params,
        tag=tag,
        device_profile_id=device_profile_id,
        play_session_id=play_session_id,
        segment_container=segment_container,
        segment_length=segment_length,
        min_segments=min_segments,
        media_source_id=media_source_id,
        device_id=device_id,
        audio_codec=audio_codec,
        enable_auto_stream_copy=enable_auto_stream_copy,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
        break_on_non_key_frames=break_on_non_key_frames,
        audio_sample_rate=audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        audio_bit_rate=audio_bit_rate,
        audio_channels=audio_channels,
        max_audio_channels=max_audio_channels,
        profile=profile,
        level=level,
        framerate=framerate,
        max_framerate=max_framerate,
        copy_timestamps=copy_timestamps,
        start_time_ticks=start_time_ticks,
        width=width,
        height=height,
        max_width=max_width,
        max_height=max_height,
        video_bit_rate=video_bit_rate,
        subtitle_stream_index=subtitle_stream_index,
        subtitle_method=subtitle_method,
        max_ref_frames=max_ref_frames,
        max_video_bit_depth=max_video_bit_depth,
        require_avc=require_avc,
        de_interlace=de_interlace,
        require_non_anamorphic=require_non_anamorphic,
        transcoding_max_audio_channels=transcoding_max_audio_channels,
        cpu_core_limit=cpu_core_limit,
        live_stream_id=live_stream_id,
        enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
        video_codec=video_codec,
        subtitle_codec=subtitle_codec,
        transcode_reasons=transcode_reasons,
        audio_stream_index=audio_stream_index,
        video_stream_index=video_stream_index,
        context=context,
        stream_options=stream_options,
        enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming,
        enable_trickplay=enable_trickplay,
        enable_audio_vbr_encoding=enable_audio_vbr_encoding,
        always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    static: bool | Unset = UNSET,
    params: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    device_profile_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    segment_container: str | Unset = UNSET,
    segment_length: int | Unset = UNSET,
    min_segments: int | Unset = UNSET,
    media_source_id: str,
    device_id: str | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    enable_auto_stream_copy: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
    break_on_non_key_frames: bool | Unset = UNSET,
    audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    audio_channels: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    profile: str | Unset = UNSET,
    level: str | Unset = UNSET,
    framerate: float | Unset = UNSET,
    max_framerate: float | Unset = UNSET,
    copy_timestamps: bool | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    video_bit_rate: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    subtitle_method: SubtitleDeliveryMethod | Unset = UNSET,
    max_ref_frames: int | Unset = UNSET,
    max_video_bit_depth: int | Unset = UNSET,
    require_avc: bool | Unset = UNSET,
    de_interlace: bool | Unset = UNSET,
    require_non_anamorphic: bool | Unset = UNSET,
    transcoding_max_audio_channels: int | Unset = UNSET,
    cpu_core_limit: int | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    enable_mpegts_m2_ts_mode: bool | Unset = UNSET,
    video_codec: str | Unset = UNSET,
    subtitle_codec: str | Unset = UNSET,
    transcode_reasons: str | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    video_stream_index: int | Unset = UNSET,
    context: EncodingContext | Unset = UNSET,
    stream_options: GetMasterHlsVideoPlaylistStreamOptions | Unset = UNSET,
    enable_adaptive_bitrate_streaming: bool | Unset = False,
    enable_trickplay: bool | Unset = True,
    enable_audio_vbr_encoding: bool | Unset = True,
    always_burn_in_subtitle_when_transcoding: bool | Unset = False,
) -> Response[Any]:
    """Gets a video hls playlist stream.

    Args:
        item_id (UUID):
        static (bool | Unset):
        params (str | Unset):
        tag (str | Unset):
        device_profile_id (str | Unset):
        play_session_id (str | Unset):
        segment_container (str | Unset):
        segment_length (int | Unset):
        min_segments (int | Unset):
        media_source_id (str):
        device_id (str | Unset):
        audio_codec (str | Unset):
        enable_auto_stream_copy (bool | Unset):
        allow_video_stream_copy (bool | Unset):
        allow_audio_stream_copy (bool | Unset):
        break_on_non_key_frames (bool | Unset):
        audio_sample_rate (int | Unset):
        max_audio_bit_depth (int | Unset):
        audio_bit_rate (int | Unset):
        audio_channels (int | Unset):
        max_audio_channels (int | Unset):
        profile (str | Unset):
        level (str | Unset):
        framerate (float | Unset):
        max_framerate (float | Unset):
        copy_timestamps (bool | Unset):
        start_time_ticks (int | Unset):
        width (int | Unset):
        height (int | Unset):
        max_width (int | Unset):
        max_height (int | Unset):
        video_bit_rate (int | Unset):
        subtitle_stream_index (int | Unset):
        subtitle_method (SubtitleDeliveryMethod | Unset): Delivery method to use during playback
            of a specific subtitle format.
        max_ref_frames (int | Unset):
        max_video_bit_depth (int | Unset):
        require_avc (bool | Unset):
        de_interlace (bool | Unset):
        require_non_anamorphic (bool | Unset):
        transcoding_max_audio_channels (int | Unset):
        cpu_core_limit (int | Unset):
        live_stream_id (str | Unset):
        enable_mpegts_m2_ts_mode (bool | Unset):
        video_codec (str | Unset):
        subtitle_codec (str | Unset):
        transcode_reasons (str | Unset):
        audio_stream_index (int | Unset):
        video_stream_index (int | Unset):
        context (EncodingContext | Unset):
        stream_options (GetMasterHlsVideoPlaylistStreamOptions | Unset):
        enable_adaptive_bitrate_streaming (bool | Unset):  Default: False.
        enable_trickplay (bool | Unset):  Default: True.
        enable_audio_vbr_encoding (bool | Unset):  Default: True.
        always_burn_in_subtitle_when_transcoding (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        static=static,
        params=params,
        tag=tag,
        device_profile_id=device_profile_id,
        play_session_id=play_session_id,
        segment_container=segment_container,
        segment_length=segment_length,
        min_segments=min_segments,
        media_source_id=media_source_id,
        device_id=device_id,
        audio_codec=audio_codec,
        enable_auto_stream_copy=enable_auto_stream_copy,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
        break_on_non_key_frames=break_on_non_key_frames,
        audio_sample_rate=audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        audio_bit_rate=audio_bit_rate,
        audio_channels=audio_channels,
        max_audio_channels=max_audio_channels,
        profile=profile,
        level=level,
        framerate=framerate,
        max_framerate=max_framerate,
        copy_timestamps=copy_timestamps,
        start_time_ticks=start_time_ticks,
        width=width,
        height=height,
        max_width=max_width,
        max_height=max_height,
        video_bit_rate=video_bit_rate,
        subtitle_stream_index=subtitle_stream_index,
        subtitle_method=subtitle_method,
        max_ref_frames=max_ref_frames,
        max_video_bit_depth=max_video_bit_depth,
        require_avc=require_avc,
        de_interlace=de_interlace,
        require_non_anamorphic=require_non_anamorphic,
        transcoding_max_audio_channels=transcoding_max_audio_channels,
        cpu_core_limit=cpu_core_limit,
        live_stream_id=live_stream_id,
        enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
        video_codec=video_codec,
        subtitle_codec=subtitle_codec,
        transcode_reasons=transcode_reasons,
        audio_stream_index=audio_stream_index,
        video_stream_index=video_stream_index,
        context=context,
        stream_options=stream_options,
        enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming,
        enable_trickplay=enable_trickplay,
        enable_audio_vbr_encoding=enable_audio_vbr_encoding,
        always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
