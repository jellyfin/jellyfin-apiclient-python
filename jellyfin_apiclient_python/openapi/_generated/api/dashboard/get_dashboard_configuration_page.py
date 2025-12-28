from http import HTTPStatus
from io import BytesIO
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/web/ConfigurationPage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200

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
) -> Response[Any | File | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
) -> Response[Any | File | ProblemDetails]:
    """Gets a dashboard configuration page.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
) -> Any | File | ProblemDetails | None:
    """Gets a dashboard configuration page.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | ProblemDetails
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
) -> Response[Any | File | ProblemDetails]:
    """Gets a dashboard configuration page.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
) -> Any | File | ProblemDetails | None:
    """Gets a dashboard configuration page.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
