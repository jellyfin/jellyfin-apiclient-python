from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.media_stream_protocol import MediaStreamProtocol
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    container: list[str] | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    device_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    transcoding_audio_channels: int | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    transcoding_container: str | Unset = UNSET,
    transcoding_protocol: MediaStreamProtocol | Unset = UNSET,
    max_audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    enable_remote_media: bool | Unset = UNSET,
    enable_audio_vbr_encoding: bool | Unset = True,
    break_on_non_key_frames: bool | Unset = False,
    enable_redirection: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_container: list[str] | Unset = UNSET
    if not isinstance(container, Unset):
        json_container = container

    params["container"] = json_container

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["audioCodec"] = audio_codec

    params["maxAudioChannels"] = max_audio_channels

    params["transcodingAudioChannels"] = transcoding_audio_channels

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["audioBitRate"] = audio_bit_rate

    params["startTimeTicks"] = start_time_ticks

    params["transcodingContainer"] = transcoding_container

    json_transcoding_protocol: str | Unset = UNSET
    if not isinstance(transcoding_protocol, Unset):
        json_transcoding_protocol = transcoding_protocol.value

    params["transcodingProtocol"] = json_transcoding_protocol

    params["maxAudioSampleRate"] = max_audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["enableRemoteMedia"] = enable_remote_media

    params["enableAudioVbrEncoding"] = enable_audio_vbr_encoding

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["enableRedirection"] = enable_redirection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/Audio/{item_id}/universal".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails]:
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
    container: list[str] | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    device_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    transcoding_audio_channels: int | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    transcoding_container: str | Unset = UNSET,
    transcoding_protocol: MediaStreamProtocol | Unset = UNSET,
    max_audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    enable_remote_media: bool | Unset = UNSET,
    enable_audio_vbr_encoding: bool | Unset = True,
    break_on_non_key_frames: bool | Unset = False,
    enable_redirection: bool | Unset = True,
) -> Response[Any | ProblemDetails]:
    """Gets an audio stream.

    Args:
        item_id (UUID):
        container (list[str] | Unset):
        media_source_id (str | Unset):
        device_id (str | Unset):
        user_id (UUID | Unset):
        audio_codec (str | Unset):
        max_audio_channels (int | Unset):
        transcoding_audio_channels (int | Unset):
        max_streaming_bitrate (int | Unset):
        audio_bit_rate (int | Unset):
        start_time_ticks (int | Unset):
        transcoding_container (str | Unset):
        transcoding_protocol (MediaStreamProtocol | Unset): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (int | Unset):
        max_audio_bit_depth (int | Unset):
        enable_remote_media (bool | Unset):
        enable_audio_vbr_encoding (bool | Unset):  Default: True.
        break_on_non_key_frames (bool | Unset):  Default: False.
        enable_redirection (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        enable_audio_vbr_encoding=enable_audio_vbr_encoding,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    container: list[str] | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    device_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    transcoding_audio_channels: int | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    transcoding_container: str | Unset = UNSET,
    transcoding_protocol: MediaStreamProtocol | Unset = UNSET,
    max_audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    enable_remote_media: bool | Unset = UNSET,
    enable_audio_vbr_encoding: bool | Unset = True,
    break_on_non_key_frames: bool | Unset = False,
    enable_redirection: bool | Unset = True,
) -> Any | ProblemDetails | None:
    """Gets an audio stream.

    Args:
        item_id (UUID):
        container (list[str] | Unset):
        media_source_id (str | Unset):
        device_id (str | Unset):
        user_id (UUID | Unset):
        audio_codec (str | Unset):
        max_audio_channels (int | Unset):
        transcoding_audio_channels (int | Unset):
        max_streaming_bitrate (int | Unset):
        audio_bit_rate (int | Unset):
        start_time_ticks (int | Unset):
        transcoding_container (str | Unset):
        transcoding_protocol (MediaStreamProtocol | Unset): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (int | Unset):
        max_audio_bit_depth (int | Unset):
        enable_remote_media (bool | Unset):
        enable_audio_vbr_encoding (bool | Unset):  Default: True.
        break_on_non_key_frames (bool | Unset):  Default: False.
        enable_redirection (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        enable_audio_vbr_encoding=enable_audio_vbr_encoding,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    container: list[str] | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    device_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    transcoding_audio_channels: int | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    transcoding_container: str | Unset = UNSET,
    transcoding_protocol: MediaStreamProtocol | Unset = UNSET,
    max_audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    enable_remote_media: bool | Unset = UNSET,
    enable_audio_vbr_encoding: bool | Unset = True,
    break_on_non_key_frames: bool | Unset = False,
    enable_redirection: bool | Unset = True,
) -> Response[Any | ProblemDetails]:
    """Gets an audio stream.

    Args:
        item_id (UUID):
        container (list[str] | Unset):
        media_source_id (str | Unset):
        device_id (str | Unset):
        user_id (UUID | Unset):
        audio_codec (str | Unset):
        max_audio_channels (int | Unset):
        transcoding_audio_channels (int | Unset):
        max_streaming_bitrate (int | Unset):
        audio_bit_rate (int | Unset):
        start_time_ticks (int | Unset):
        transcoding_container (str | Unset):
        transcoding_protocol (MediaStreamProtocol | Unset): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (int | Unset):
        max_audio_bit_depth (int | Unset):
        enable_remote_media (bool | Unset):
        enable_audio_vbr_encoding (bool | Unset):  Default: True.
        break_on_non_key_frames (bool | Unset):  Default: False.
        enable_redirection (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        enable_audio_vbr_encoding=enable_audio_vbr_encoding,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    container: list[str] | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    device_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    audio_codec: str | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    transcoding_audio_channels: int | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    audio_bit_rate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    transcoding_container: str | Unset = UNSET,
    transcoding_protocol: MediaStreamProtocol | Unset = UNSET,
    max_audio_sample_rate: int | Unset = UNSET,
    max_audio_bit_depth: int | Unset = UNSET,
    enable_remote_media: bool | Unset = UNSET,
    enable_audio_vbr_encoding: bool | Unset = True,
    break_on_non_key_frames: bool | Unset = False,
    enable_redirection: bool | Unset = True,
) -> Any | ProblemDetails | None:
    """Gets an audio stream.

    Args:
        item_id (UUID):
        container (list[str] | Unset):
        media_source_id (str | Unset):
        device_id (str | Unset):
        user_id (UUID | Unset):
        audio_codec (str | Unset):
        max_audio_channels (int | Unset):
        transcoding_audio_channels (int | Unset):
        max_streaming_bitrate (int | Unset):
        audio_bit_rate (int | Unset):
        start_time_ticks (int | Unset):
        transcoding_container (str | Unset):
        transcoding_protocol (MediaStreamProtocol | Unset): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (int | Unset):
        max_audio_bit_depth (int | Unset):
        enable_remote_media (bool | Unset):
        enable_audio_vbr_encoding (bool | Unset):  Default: True.
        break_on_non_key_frames (bool | Unset):  Default: False.
        enable_redirection (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            container=container,
            media_source_id=media_source_id,
            device_id=device_id,
            user_id=user_id,
            audio_codec=audio_codec,
            max_audio_channels=max_audio_channels,
            transcoding_audio_channels=transcoding_audio_channels,
            max_streaming_bitrate=max_streaming_bitrate,
            audio_bit_rate=audio_bit_rate,
            start_time_ticks=start_time_ticks,
            transcoding_container=transcoding_container,
            transcoding_protocol=transcoding_protocol,
            max_audio_sample_rate=max_audio_sample_rate,
            max_audio_bit_depth=max_audio_bit_depth,
            enable_remote_media=enable_remote_media,
            enable_audio_vbr_encoding=enable_audio_vbr_encoding,
            break_on_non_key_frames=break_on_non_key_frames,
            enable_redirection=enable_redirection,
        )
    ).parsed
