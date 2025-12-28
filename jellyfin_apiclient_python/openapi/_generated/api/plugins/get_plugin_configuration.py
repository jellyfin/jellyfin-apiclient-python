from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_plugin_configuration import BasePluginConfiguration
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    plugin_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Plugins/{plugin_id}/Configuration".format(
            plugin_id=plugin_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BasePluginConfiguration | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BasePluginConfiguration.from_dict(response.json())

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
) -> Response[Any | BasePluginConfiguration | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plugin_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | BasePluginConfiguration | ProblemDetails]:
    """Gets plugin configuration.

    Args:
        plugin_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BasePluginConfiguration | ProblemDetails]
    """

    kwargs = _get_kwargs(
        plugin_id=plugin_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plugin_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | BasePluginConfiguration | ProblemDetails | None:
    """Gets plugin configuration.

    Args:
        plugin_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BasePluginConfiguration | ProblemDetails
    """

    return sync_detailed(
        plugin_id=plugin_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    plugin_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | BasePluginConfiguration | ProblemDetails]:
    """Gets plugin configuration.

    Args:
        plugin_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BasePluginConfiguration | ProblemDetails]
    """

    kwargs = _get_kwargs(
        plugin_id=plugin_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plugin_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | BasePluginConfiguration | ProblemDetails | None:
    """Gets plugin configuration.

    Args:
        plugin_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BasePluginConfiguration | ProblemDetails
    """

    return (
        await asyncio_detailed(
            plugin_id=plugin_id,
            client=client,
        )
    ).parsed
