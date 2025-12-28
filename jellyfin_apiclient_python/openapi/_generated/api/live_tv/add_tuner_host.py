from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tuner_host_info import TunerHostInfo
from ...types import Response


def _get_kwargs(
    *,
    body: TunerHostInfo | TunerHostInfo,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/LiveTv/TunerHosts",
    }

    if isinstance(body, TunerHostInfo):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TunerHostInfo):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TunerHostInfo | None:
    if response.status_code == 200:
        response_200 = TunerHostInfo.from_dict(response.json())

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
) -> Response[Any | TunerHostInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TunerHostInfo | TunerHostInfo,
) -> Response[Any | TunerHostInfo]:
    """Adds a tuner host.

    Args:
        body (TunerHostInfo):
        body (TunerHostInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TunerHostInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TunerHostInfo | TunerHostInfo,
) -> Any | TunerHostInfo | None:
    """Adds a tuner host.

    Args:
        body (TunerHostInfo):
        body (TunerHostInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TunerHostInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TunerHostInfo | TunerHostInfo,
) -> Response[Any | TunerHostInfo]:
    """Adds a tuner host.

    Args:
        body (TunerHostInfo):
        body (TunerHostInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TunerHostInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TunerHostInfo | TunerHostInfo,
) -> Any | TunerHostInfo | None:
    """Adds a tuner host.

    Args:
        body (TunerHostInfo):
        body (TunerHostInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TunerHostInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
