from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.series_timer_info_dto import SeriesTimerInfoDto
from ...types import Response


def _get_kwargs(
    timer_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/SeriesTimers/{timer_id}".format(
            timer_id=timer_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | SeriesTimerInfoDto | None:
    if response.status_code == 200:
        response_200 = SeriesTimerInfoDto.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | SeriesTimerInfoDto]:
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
) -> Response[Any | ProblemDetails | SeriesTimerInfoDto]:
    """Gets a live tv series timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | SeriesTimerInfoDto]
    """

    kwargs = _get_kwargs(
        timer_id=timer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    timer_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | SeriesTimerInfoDto | None:
    """Gets a live tv series timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | SeriesTimerInfoDto
    """

    return sync_detailed(
        timer_id=timer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    timer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | SeriesTimerInfoDto]:
    """Gets a live tv series timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | SeriesTimerInfoDto]
    """

    kwargs = _get_kwargs(
        timer_id=timer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    timer_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | SeriesTimerInfoDto | None:
    """Gets a live tv series timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | SeriesTimerInfoDto
    """

    return (
        await asyncio_detailed(
            timer_id=timer_id,
            client=client,
        )
    ).parsed
