from http import HTTPStatus
from io import BytesIO
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    item_id: UUID | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    index: int | Unset = UNSET,
    start_position_ticks: int | Unset = UNSET,
    format_: str | Unset = UNSET,
    end_position_ticks: int | Unset = UNSET,
    copy_timestamps: bool | Unset = False,
    add_vtt_time_map: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_item_id: str | Unset = UNSET
    if not isinstance(item_id, Unset):
        json_item_id = str(item_id)
    params["itemId"] = json_item_id

    params["mediaSourceId"] = media_source_id

    params["index"] = index

    params["startPositionTicks"] = start_position_ticks

    params["format"] = format_

    params["endPositionTicks"] = end_position_ticks

    params["copyTimestamps"] = copy_timestamps

    params["addVttTimeMap"] = add_vtt_time_map

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{route_item_id}/{route_media_source_id}/Subtitles/{route_index}/{route_start_position_ticks}/Stream.{route_format}".format(
            route_item_id=route_item_id,
            route_media_source_id=route_media_source_id,
            route_index=route_index,
            route_start_position_ticks=route_start_position_ticks,
            route_format=route_format,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: UUID | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    index: int | Unset = UNSET,
    start_position_ticks: int | Unset = UNSET,
    format_: str | Unset = UNSET,
    end_position_ticks: int | Unset = UNSET,
    copy_timestamps: bool | Unset = False,
    add_vtt_time_map: bool | Unset = False,
) -> Response[Any | File]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (UUID | Unset):
        media_source_id (str | Unset):
        index (int | Unset):
        start_position_ticks (int | Unset):
        format_ (str | Unset):
        end_position_ticks (int | Unset):
        copy_timestamps (bool | Unset):  Default: False.
        add_vtt_time_map (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: UUID | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    index: int | Unset = UNSET,
    start_position_ticks: int | Unset = UNSET,
    format_: str | Unset = UNSET,
    end_position_ticks: int | Unset = UNSET,
    copy_timestamps: bool | Unset = False,
    add_vtt_time_map: bool | Unset = False,
) -> Any | File | None:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (UUID | Unset):
        media_source_id (str | Unset):
        index (int | Unset):
        start_position_ticks (int | Unset):
        format_ (str | Unset):
        end_position_ticks (int | Unset):
        copy_timestamps (bool | Unset):  Default: False.
        add_vtt_time_map (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return sync_detailed(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        client=client,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    ).parsed


async def asyncio_detailed(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: UUID | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    index: int | Unset = UNSET,
    start_position_ticks: int | Unset = UNSET,
    format_: str | Unset = UNSET,
    end_position_ticks: int | Unset = UNSET,
    copy_timestamps: bool | Unset = False,
    add_vtt_time_map: bool | Unset = False,
) -> Response[Any | File]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (UUID | Unset):
        media_source_id (str | Unset):
        index (int | Unset):
        start_position_ticks (int | Unset):
        format_ (str | Unset):
        end_position_ticks (int | Unset):
        copy_timestamps (bool | Unset):  Default: False.
        add_vtt_time_map (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: UUID | Unset = UNSET,
    media_source_id: str | Unset = UNSET,
    index: int | Unset = UNSET,
    start_position_ticks: int | Unset = UNSET,
    format_: str | Unset = UNSET,
    end_position_ticks: int | Unset = UNSET,
    copy_timestamps: bool | Unset = False,
    add_vtt_time_map: bool | Unset = False,
) -> Any | File | None:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (UUID | Unset):
        media_source_id (str | Unset):
        index (int | Unset):
        start_position_ticks (int | Unset):
        format_ (str | Unset):
        end_position_ticks (int | Unset):
        copy_timestamps (bool | Unset):  Default: False.
        add_vtt_time_map (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return (
        await asyncio_detailed(
            route_item_id=route_item_id,
            route_media_source_id=route_media_source_id,
            route_index=route_index,
            route_start_position_ticks=route_start_position_ticks,
            route_format=route_format,
            client=client,
            item_id=item_id,
            media_source_id=media_source_id,
            index=index,
            start_position_ticks=start_position_ticks,
            format_=format_,
            end_position_ticks=end_position_ticks,
            copy_timestamps=copy_timestamps,
            add_vtt_time_map=add_vtt_time_map,
        )
    ).parsed
