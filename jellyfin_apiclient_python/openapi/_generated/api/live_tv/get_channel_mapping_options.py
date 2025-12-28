from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel_mapping_options_dto import ChannelMappingOptionsDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["providerId"] = provider_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/ChannelMappingOptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ChannelMappingOptionsDto | None:
    if response.status_code == 200:
        response_200 = ChannelMappingOptionsDto.from_dict(response.json())

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
) -> Response[Any | ChannelMappingOptionsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider_id: str | Unset = UNSET,
) -> Response[Any | ChannelMappingOptionsDto]:
    """Get channel mapping options.

    Args:
        provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChannelMappingOptionsDto]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    provider_id: str | Unset = UNSET,
) -> Any | ChannelMappingOptionsDto | None:
    """Get channel mapping options.

    Args:
        provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChannelMappingOptionsDto
    """

    return sync_detailed(
        client=client,
        provider_id=provider_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider_id: str | Unset = UNSET,
) -> Response[Any | ChannelMappingOptionsDto]:
    """Get channel mapping options.

    Args:
        provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChannelMappingOptionsDto]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider_id: str | Unset = UNSET,
) -> Any | ChannelMappingOptionsDto | None:
    """Get channel mapping options.

    Args:
        provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChannelMappingOptionsDto
    """

    return (
        await asyncio_detailed(
            client=client,
            provider_id=provider_id,
        )
    ).parsed
