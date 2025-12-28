from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.configuration_page_info import ConfigurationPageInfo
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enable_in_main_menu: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["enableInMainMenu"] = enable_in_main_menu

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/web/ConfigurationPages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[ConfigurationPageInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ConfigurationPageInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | ProblemDetails | list[ConfigurationPageInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[ConfigurationPageInfo]]:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[ConfigurationPageInfo]]
    """

    kwargs = _get_kwargs(
        enable_in_main_menu=enable_in_main_menu,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[ConfigurationPageInfo] | None:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[ConfigurationPageInfo]
    """

    return sync_detailed(
        client=client,
        enable_in_main_menu=enable_in_main_menu,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[ConfigurationPageInfo]]:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[ConfigurationPageInfo]]
    """

    kwargs = _get_kwargs(
        enable_in_main_menu=enable_in_main_menu,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[ConfigurationPageInfo] | None:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[ConfigurationPageInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            enable_in_main_menu=enable_in_main_menu,
        )
    ).parsed
