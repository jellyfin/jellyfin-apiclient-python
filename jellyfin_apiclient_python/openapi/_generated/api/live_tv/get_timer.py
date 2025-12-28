from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timer_info_dto import TimerInfoDto
from ...types import Response


def _get_kwargs(
    timer_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Timers/{timer_id}".format(
            timer_id=timer_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TimerInfoDto | None:
    if response.status_code == 200:
        response_200 = TimerInfoDto.from_dict(response.json())

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
) -> Response[Any | TimerInfoDto]:
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
) -> Response[Any | TimerInfoDto]:
    """Gets a timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TimerInfoDto]
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
) -> Any | TimerInfoDto | None:
    """Gets a timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TimerInfoDto
    """

    return sync_detailed(
        timer_id=timer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    timer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | TimerInfoDto]:
    """Gets a timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TimerInfoDto]
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
) -> Any | TimerInfoDto | None:
    """Gets a timer.

    Args:
        timer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TimerInfoDto
    """

    return (
        await asyncio_detailed(
            timer_id=timer_id,
            client=client,
        )
    ).parsed
