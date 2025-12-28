from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.package_info import PackageInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    assembly_guid: UUID | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_assembly_guid: str | Unset = UNSET
    if not isinstance(assembly_guid, Unset):
        json_assembly_guid = str(assembly_guid)
    params["assemblyGuid"] = json_assembly_guid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Packages/{name}".format(
            name=name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PackageInfo | None:
    if response.status_code == 200:
        response_200 = PackageInfo.from_dict(response.json())

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
) -> Response[Any | PackageInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: UUID | Unset = UNSET,
) -> Response[Any | PackageInfo]:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PackageInfo]
    """

    kwargs = _get_kwargs(
        name=name,
        assembly_guid=assembly_guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: UUID | Unset = UNSET,
) -> Any | PackageInfo | None:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PackageInfo
    """

    return sync_detailed(
        name=name,
        client=client,
        assembly_guid=assembly_guid,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: UUID | Unset = UNSET,
) -> Response[Any | PackageInfo]:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PackageInfo]
    """

    kwargs = _get_kwargs(
        name=name,
        assembly_guid=assembly_guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: UUID | Unset = UNSET,
) -> Any | PackageInfo | None:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PackageInfo
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            assembly_guid=assembly_guid,
        )
    ).parsed
