from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.series_timer_info_dto import SeriesTimerInfoDto
from ...types import Response


def _get_kwargs(
    timer_id: str,
    *,
    body: SeriesTimerInfoDto | SeriesTimerInfoDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/LiveTv/SeriesTimers/{timer_id}".format(
            timer_id=timer_id,
        ),
    }

    if isinstance(body, SeriesTimerInfoDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SeriesTimerInfoDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    timer_id: str,
    *,
    client: AuthenticatedClient,
    body: SeriesTimerInfoDto | SeriesTimerInfoDto,
) -> Response[Any]:
    """Updates a live tv series timer.

    Args:
        timer_id (str):
        body (SeriesTimerInfoDto): Class SeriesTimerInfoDto.
        body (SeriesTimerInfoDto): Class SeriesTimerInfoDto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        timer_id=timer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    timer_id: str,
    *,
    client: AuthenticatedClient,
    body: SeriesTimerInfoDto | SeriesTimerInfoDto,
) -> Response[Any]:
    """Updates a live tv series timer.

    Args:
        timer_id (str):
        body (SeriesTimerInfoDto): Class SeriesTimerInfoDto.
        body (SeriesTimerInfoDto): Class SeriesTimerInfoDto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        timer_id=timer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
