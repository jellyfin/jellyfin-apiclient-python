from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sort_by: str | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sortBy"] = sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/SeriesTimers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SeriesTimerInfoDtoQueryResult | None:
    if response.status_code == 200:
        response_200 = SeriesTimerInfoDtoQueryResult.from_dict(response.json())

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
) -> Response[Any | SeriesTimerInfoDtoQueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
) -> Response[Any | SeriesTimerInfoDtoQueryResult]:
    """Gets live tv series timers.

    Args:
        sort_by (str | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SeriesTimerInfoDtoQueryResult]
    """

    kwargs = _get_kwargs(
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
) -> Any | SeriesTimerInfoDtoQueryResult | None:
    """Gets live tv series timers.

    Args:
        sort_by (str | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SeriesTimerInfoDtoQueryResult
    """

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
) -> Response[Any | SeriesTimerInfoDtoQueryResult]:
    """Gets live tv series timers.

    Args:
        sort_by (str | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SeriesTimerInfoDtoQueryResult]
    """

    kwargs = _get_kwargs(
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = UNSET,
    sort_order: SortOrder | Unset = UNSET,
) -> Any | SeriesTimerInfoDtoQueryResult | None:
    """Gets live tv series timers.

    Args:
        sort_by (str | Unset):
        sort_order (SortOrder | Unset): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SeriesTimerInfoDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
