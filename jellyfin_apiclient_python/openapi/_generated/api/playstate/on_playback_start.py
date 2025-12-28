from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.play_method import PlayMethod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    media_source_id: str | Unset = UNSET,
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    play_method: PlayMethod | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    can_seek: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mediaSourceId"] = media_source_id

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    json_play_method: str | Unset = UNSET
    if not isinstance(play_method, Unset):
        json_play_method = play_method.value

    params["playMethod"] = json_play_method

    params["liveStreamId"] = live_stream_id

    params["playSessionId"] = play_session_id

    params["canSeek"] = can_seek

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/PlayingItems/{item_id}".format(
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
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    play_method: PlayMethod | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    can_seek: bool | Unset = False,
) -> Response[Any]:
    """Reports that a session has begun playing an item.

    Args:
        item_id (UUID):
        media_source_id (str | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        play_method (PlayMethod | Unset):
        live_stream_id (str | Unset):
        play_session_id (str | Unset):
        can_seek (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        can_seek=can_seek,
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
    audio_stream_index: int | Unset = UNSET,
    subtitle_stream_index: int | Unset = UNSET,
    play_method: PlayMethod | Unset = UNSET,
    live_stream_id: str | Unset = UNSET,
    play_session_id: str | Unset = UNSET,
    can_seek: bool | Unset = False,
) -> Response[Any]:
    """Reports that a session has begun playing an item.

    Args:
        item_id (UUID):
        media_source_id (str | Unset):
        audio_stream_index (int | Unset):
        subtitle_stream_index (int | Unset):
        play_method (PlayMethod | Unset):
        live_stream_id (str | Unset):
        play_session_id (str | Unset):
        can_seek (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        can_seek=can_seek,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
