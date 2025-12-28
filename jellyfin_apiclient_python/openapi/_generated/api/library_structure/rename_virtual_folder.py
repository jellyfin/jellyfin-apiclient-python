from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    new_name: str | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["newName"] = new_name

    params["refreshLibrary"] = refresh_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Library/VirtualFolders/Name",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    new_name: str | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> Response[Any | ProblemDetails]:
    """Renames a virtual folder.

    Args:
        name (str | Unset):
        new_name (str | Unset):
        refresh_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        new_name=new_name,
        refresh_library=refresh_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    new_name: str | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> Any | ProblemDetails | None:
    """Renames a virtual folder.

    Args:
        name (str | Unset):
        new_name (str | Unset):
        refresh_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        client=client,
        name=name,
        new_name=new_name,
        refresh_library=refresh_library,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    new_name: str | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> Response[Any | ProblemDetails]:
    """Renames a virtual folder.

    Args:
        name (str | Unset):
        new_name (str | Unset):
        refresh_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        new_name=new_name,
        refresh_library=refresh_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    new_name: str | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> Any | ProblemDetails | None:
    """Renames a virtual folder.

    Args:
        name (str | Unset):
        new_name (str | Unset):
        refresh_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            new_name=new_name,
            refresh_library=refresh_library,
        )
    ).parsed
