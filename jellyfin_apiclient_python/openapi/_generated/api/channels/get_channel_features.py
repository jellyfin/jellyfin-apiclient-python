from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel_features import ChannelFeatures
from ...types import Response


def _get_kwargs(
    channel_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Channels/{channel_id}/Features".format(
            channel_id=channel_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ChannelFeatures | None:
    if response.status_code == 200:
        response_200 = ChannelFeatures.from_dict(response.json())

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
) -> Response[Any | ChannelFeatures]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ChannelFeatures]:
    """Get channel features.

    Args:
        channel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChannelFeatures]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ChannelFeatures | None:
    """Get channel features.

    Args:
        channel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChannelFeatures
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ChannelFeatures]:
    """Get channel features.

    Args:
        channel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChannelFeatures]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ChannelFeatures | None:
    """Get channel features.

    Args:
        channel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChannelFeatures
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
