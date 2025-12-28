from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timer_info_dto_query_result import TimerInfoDtoQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_id: str | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_scheduled: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["channelId"] = channel_id

    params["seriesTimerId"] = series_timer_id

    params["isActive"] = is_active

    params["isScheduled"] = is_scheduled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Timers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TimerInfoDtoQueryResult | None:
    if response.status_code == 200:
        response_200 = TimerInfoDtoQueryResult.from_dict(response.json())

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
) -> Response[Any | TimerInfoDtoQueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_scheduled: bool | Unset = UNSET,
) -> Response[Any | TimerInfoDtoQueryResult]:
    """Gets the live tv timers.

    Args:
        channel_id (str | Unset):
        series_timer_id (str | Unset):
        is_active (bool | Unset):
        is_scheduled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TimerInfoDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        series_timer_id=series_timer_id,
        is_active=is_active,
        is_scheduled=is_scheduled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_scheduled: bool | Unset = UNSET,
) -> Any | TimerInfoDtoQueryResult | None:
    """Gets the live tv timers.

    Args:
        channel_id (str | Unset):
        series_timer_id (str | Unset):
        is_active (bool | Unset):
        is_scheduled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TimerInfoDtoQueryResult
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        series_timer_id=series_timer_id,
        is_active=is_active,
        is_scheduled=is_scheduled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_scheduled: bool | Unset = UNSET,
) -> Response[Any | TimerInfoDtoQueryResult]:
    """Gets the live tv timers.

    Args:
        channel_id (str | Unset):
        series_timer_id (str | Unset):
        is_active (bool | Unset):
        is_scheduled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TimerInfoDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        series_timer_id=series_timer_id,
        is_active=is_active,
        is_scheduled=is_scheduled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_scheduled: bool | Unset = UNSET,
) -> Any | TimerInfoDtoQueryResult | None:
    """Gets the live tv timers.

    Args:
        channel_id (str | Unset):
        series_timer_id (str | Unset):
        is_active (bool | Unset):
        is_scheduled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TimerInfoDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            series_timer_id=series_timer_id,
            is_active=is_active,
            is_scheduled=is_scheduled,
        )
    ).parsed
