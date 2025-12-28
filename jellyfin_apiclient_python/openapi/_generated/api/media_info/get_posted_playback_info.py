from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.playback_info_dto import PlaybackInfoDto
from ...models.playback_info_response import PlaybackInfoResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    body: PlaybackInfoDto | PlaybackInfoDto,
    user_id: UUID | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    auto_open_live_stream: bool | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    enable_transcoding: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["startTimeTicks"] = start_time_ticks

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["maxAudioChannels"] = max_audio_channels

    params["mediaSourceId"] = media_source_id

    params["liveStreamId"] = live_stream_id

    params["autoOpenLiveStream"] = auto_open_live_stream

    params["enableDirectPlay"] = enable_direct_play

    params["enableDirectStream"] = enable_direct_stream

    params["enableTranscoding"] = enable_transcoding

    params["allowVideoStreamCopy"] = allow_video_stream_copy

    params["allowAudioStreamCopy"] = allow_audio_stream_copy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Items/{item_id}/PlaybackInfo".format(
            item_id=item_id,
        ),
        "params": params,
    }

    if isinstance(body, PlaybackInfoDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PlaybackInfoDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PlaybackInfoResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PlaybackInfoResponse.from_dict(response.json())

        return response_200

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
) -> Response[Any | PlaybackInfoResponse | ProblemDetails]:
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
    body: PlaybackInfoDto | PlaybackInfoDto,
    user_id: UUID | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    auto_open_live_stream: bool | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    enable_transcoding: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
) -> Response[Any | PlaybackInfoResponse | ProblemDetails]:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        media_source_id (str | Unset):
        live_stream_id (str | Unset):
        auto_open_live_stream (bool | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        enable_transcoding (bool | Unset):
        allow_video_stream_copy (bool | Unset):
        allow_audio_stream_copy (bool | Unset):
        body (PlaybackInfoDto): Playback info dto.
        body (PlaybackInfoDto): Playback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaybackInfoResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        user_id=user_id,
        max_streaming_bitrate=max_streaming_bitrate,
        start_time_ticks=start_time_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        max_audio_channels=max_audio_channels,
        media_source_id=media_source_id,
        live_stream_id=live_stream_id,
        auto_open_live_stream=auto_open_live_stream,
        enable_direct_play=enable_direct_play,
        enable_direct_stream=enable_direct_stream,
        enable_transcoding=enable_transcoding,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PlaybackInfoDto | PlaybackInfoDto,
    user_id: UUID | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    auto_open_live_stream: bool | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    enable_transcoding: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
) -> Any | PlaybackInfoResponse | ProblemDetails | None:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        media_source_id (str | Unset):
        live_stream_id (str | Unset):
        auto_open_live_stream (bool | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        enable_transcoding (bool | Unset):
        allow_video_stream_copy (bool | Unset):
        allow_audio_stream_copy (bool | Unset):
        body (PlaybackInfoDto): Playback info dto.
        body (PlaybackInfoDto): Playback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaybackInfoResponse | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
        user_id=user_id,
        max_streaming_bitrate=max_streaming_bitrate,
        start_time_ticks=start_time_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        max_audio_channels=max_audio_channels,
        media_source_id=media_source_id,
        live_stream_id=live_stream_id,
        auto_open_live_stream=auto_open_live_stream,
        enable_direct_play=enable_direct_play,
        enable_direct_stream=enable_direct_stream,
        enable_transcoding=enable_transcoding,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PlaybackInfoDto | PlaybackInfoDto,
    user_id: UUID | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    auto_open_live_stream: bool | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    enable_transcoding: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
) -> Response[Any | PlaybackInfoResponse | ProblemDetails]:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        media_source_id (str | Unset):
        live_stream_id (str | Unset):
        auto_open_live_stream (bool | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        enable_transcoding (bool | Unset):
        allow_video_stream_copy (bool | Unset):
        allow_audio_stream_copy (bool | Unset):
        body (PlaybackInfoDto): Playback info dto.
        body (PlaybackInfoDto): Playback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaybackInfoResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        user_id=user_id,
        max_streaming_bitrate=max_streaming_bitrate,
        start_time_ticks=start_time_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        max_audio_channels=max_audio_channels,
        media_source_id=media_source_id,
        live_stream_id=live_stream_id,
        auto_open_live_stream=auto_open_live_stream,
        enable_direct_play=enable_direct_play,
        enable_direct_stream=enable_direct_stream,
        enable_transcoding=enable_transcoding,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PlaybackInfoDto | PlaybackInfoDto,
    user_id: UUID | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    auto_open_live_stream: bool | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    enable_transcoding: bool | Unset = UNSET,
    allow_video_stream_copy: bool | Unset = UNSET,
    allow_audio_stream_copy: bool | Unset = UNSET,
) -> Any | PlaybackInfoResponse | ProblemDetails | None:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        media_source_id (str | Unset):
        live_stream_id (str | Unset):
        auto_open_live_stream (bool | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        enable_transcoding (bool | Unset):
        allow_video_stream_copy (bool | Unset):
        allow_audio_stream_copy (bool | Unset):
        body (PlaybackInfoDto): Playback info dto.
        body (PlaybackInfoDto): Playback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaybackInfoResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
            user_id=user_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            media_source_id=media_source_id,
            live_stream_id=live_stream_id,
            auto_open_live_stream=auto_open_live_stream,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            enable_transcoding=enable_transcoding,
            allow_video_stream_copy=allow_video_stream_copy,
            allow_audio_stream_copy=allow_audio_stream_copy,
        )
    ).parsed
