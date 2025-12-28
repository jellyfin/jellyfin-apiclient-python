from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.play_method import PlayMethod
from ...models.repeat_mode import RepeatMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    media_source_id: str | Unset = UNSET,
    position_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    volume_level: int | Unset = UNSET,
    play_method: PlayMethod | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    repeat_mode: RepeatMode | Unset = UNSET,
    is_paused: bool | Unset = False,
    is_muted: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mediaSourceId"] = media_source_id

    params["positionTicks"] = position_ticks

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["volumeLevel"] = volume_level

    json_play_method: str | Unset = UNSET
    if not isinstance(play_method, Unset):
        json_play_method = play_method.value

    params["playMethod"] = json_play_method

    params["liveStreamId"] = live_stream_id

    params["playSessionId"] = play_session_id

    json_repeat_mode: str | Unset = UNSET
    if not isinstance(repeat_mode, Unset):
        json_repeat_mode = repeat_mode.value

    params["repeatMode"] = json_repeat_mode

    params["isPaused"] = is_paused

    params["isMuted"] = is_muted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/PlayingItems/{item_id}/Progress".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

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
    media_source_id: str | Unset = UNSET,
    position_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    volume_level: int | Unset = UNSET,
    play_method: PlayMethod | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    repeat_mode: RepeatMode | Unset = UNSET,
    is_paused: bool | Unset = False,
    is_muted: bool | Unset = False,
) -> Response[Any]:
    """Reports a session's playback progress.

    Args:
        item_id (UUID):
        media_source_id (str | Unset):
        position_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        volume_level (int | Unset):
        play_method (PlayMethod | Unset):
        live_stream_id (str | Unset):
        play_session_id (str | Unset):
        repeat_mode (RepeatMode | Unset):
        is_paused (bool | Unset):  Default: False.
        is_muted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        position_ticks=position_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        volume_level=volume_level,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        repeat_mode=repeat_mode,
        is_paused=is_paused,
        is_muted=is_muted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    media_source_id: str | Unset = UNSET,
    position_ticks: int | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    volume_level: int | Unset = UNSET,
    play_method: PlayMethod | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    repeat_mode: RepeatMode | Unset = UNSET,
    is_paused: bool | Unset = False,
    is_muted: bool | Unset = False,
) -> Response[Any]:
    """Reports a session's playback progress.

    Args:
        item_id (UUID):
        media_source_id (str | Unset):
        position_ticks (int | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        volume_level (int | Unset):
        play_method (PlayMethod | Unset):
        live_stream_id (str | Unset):
        play_session_id (str | Unset):
        repeat_mode (RepeatMode | Unset):
        is_paused (bool | Unset):  Default: False.
        is_muted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        position_ticks=position_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        volume_level=volume_level,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        repeat_mode=repeat_mode,
        is_paused=is_paused,
        is_muted=is_muted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
