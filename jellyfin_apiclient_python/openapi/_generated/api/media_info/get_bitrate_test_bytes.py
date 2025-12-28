from http import HTTPStatus
from io import BytesIO
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    size: int | Unset = 102400,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Playback/BitrateTest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[Any | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    size: int | Unset = 102400,
) -> Response[Any | File]:
    """Tests the network with a request with the size of the bitrate.

    Args:
        size (int | Unset):  Default: 102400.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    size: int | Unset = 102400,
) -> Any | File | None:
    """Tests the network with a request with the size of the bitrate.

    Args:
        size (int | Unset):  Default: 102400.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return sync_detailed(
        client=client,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    size: int | Unset = 102400,
) -> Response[Any | File]:
    """Tests the network with a request with the size of the bitrate.

    Args:
        size (int | Unset):  Default: 102400.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    size: int | Unset = 102400,
) -> Any | File | None:
    """Tests the network with a request with the size of the bitrate.

    Args:
        size (int | Unset):  Default: 102400.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return (
        await asyncio_detailed(
            client=client,
            size=size,
        )
    ).parsed
