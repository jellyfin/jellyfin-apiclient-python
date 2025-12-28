from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_stream_response import LiveStreamResponse
from ...models.open_live_stream_dto import OpenLiveStreamDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OpenLiveStreamDto | OpenLiveStreamDto,
    open_token: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    always_burn_in_subtitle_when_transcoding: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["openToken"] = open_token

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["playSessionId"] = play_session_id

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["startTimeTicks"] = start_time_ticks

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["maxAudioChannels"] = max_audio_channels

    json_item_id: str | Unset = UNSET
    if not isinstance(item_id, Unset):
        json_item_id = str(item_id)
    params["itemId"] = json_item_id

    params["enableDirectPlay"] = enable_direct_play

    params["enableDirectStream"] = enable_direct_stream

    params["alwaysBurnInSubtitleWhenTranscoding"] = (
        always_burn_in_subtitle_when_transcoding
    )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/LiveStreams/Open",
        "params": params,
    }

    if isinstance(body, OpenLiveStreamDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, OpenLiveStreamDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LiveStreamResponse | None:
    if response.status_code == 200:
        response_200 = LiveStreamResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LiveStreamResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenLiveStreamDto | OpenLiveStreamDto,
    open_token: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    always_burn_in_subtitle_when_transcoding: bool | Unset = UNSET,
) -> Response[Any | LiveStreamResponse]:
    """Opens a media source.

    Args:
        open_token (str | Unset):
        user_id (UUID | Unset):
        play_session_id (str | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        item_id (UUID | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        always_burn_in_subtitle_when_transcoding (bool | Unset):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LiveStreamResponse]
    """

    kwargs = _get_kwargs(
        body=body,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: OpenLiveStreamDto | OpenLiveStreamDto,
    open_token: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    always_burn_in_subtitle_when_transcoding: bool | Unset = UNSET,
) -> Any | LiveStreamResponse | None:
    """Opens a media source.

    Args:
        open_token (str | Unset):
        user_id (UUID | Unset):
        play_session_id (str | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        item_id (UUID | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        always_burn_in_subtitle_when_transcoding (bool | Unset):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LiveStreamResponse
    """

    return sync_detailed(
        client=client,
        body=body,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenLiveStreamDto | OpenLiveStreamDto,
    open_token: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    always_burn_in_subtitle_when_transcoding: bool | Unset = UNSET,
) -> Response[Any | LiveStreamResponse]:
    """Opens a media source.

    Args:
        open_token (str | Unset):
        user_id (UUID | Unset):
        play_session_id (str | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        item_id (UUID | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        always_burn_in_subtitle_when_transcoding (bool | Unset):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LiveStreamResponse]
    """

    kwargs = _get_kwargs(
        body=body,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OpenLiveStreamDto | OpenLiveStreamDto,
    open_token: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    max_streaming_bitrate: int | Unset = UNSET,
    start_time_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    max_audio_channels: int | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    enable_direct_play: bool | Unset = UNSET,
    enable_direct_stream: bool | Unset = UNSET,
    always_burn_in_subtitle_when_transcoding: bool | Unset = UNSET,
) -> Any | LiveStreamResponse | None:
    """Opens a media source.

    Args:
        open_token (str | Unset):
        user_id (UUID | Unset):
        play_session_id (str | Unset):
        max_streaming_bitrate (int | Unset):
        start_time_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        max_audio_channels (int | Unset):
        item_id (UUID | Unset):
        enable_direct_play (bool | Unset):
        enable_direct_stream (bool | Unset):
        always_burn_in_subtitle_when_transcoding (bool | Unset):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LiveStreamResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
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
        )
    ).parsed
