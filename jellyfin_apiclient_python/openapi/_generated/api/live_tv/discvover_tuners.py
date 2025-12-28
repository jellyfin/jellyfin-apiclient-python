from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tuner_host_info import TunerHostInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    new_devices_only: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["newDevicesOnly"] = new_devices_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Tuners/Discvover",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[TunerHostInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TunerHostInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[TunerHostInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    new_devices_only: bool | Unset = False,
) -> Response[Any | list[TunerHostInfo]]:
    """Discover tuners.

    Args:
        new_devices_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[TunerHostInfo]]
    """

    kwargs = _get_kwargs(
        new_devices_only=new_devices_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    new_devices_only: bool | Unset = False,
) -> Any | list[TunerHostInfo] | None:
    """Discover tuners.

    Args:
        new_devices_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[TunerHostInfo]
    """

    return sync_detailed(
        client=client,
        new_devices_only=new_devices_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    new_devices_only: bool | Unset = False,
) -> Response[Any | list[TunerHostInfo]]:
    """Discover tuners.

    Args:
        new_devices_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[TunerHostInfo]]
    """

    kwargs = _get_kwargs(
        new_devices_only=new_devices_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    new_devices_only: bool | Unset = False,
) -> Any | list[TunerHostInfo] | None:
    """Discover tuners.

    Args:
        new_devices_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[TunerHostInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            new_devices_only=new_devices_only,
        )
    ).parsed
