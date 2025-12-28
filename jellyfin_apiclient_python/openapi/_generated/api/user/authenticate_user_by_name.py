from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authenticate_user_by_name import AuthenticateUserByName
from ...models.authentication_result import AuthenticationResult
from ...types import Response


def _get_kwargs(
    *,
    body: AuthenticateUserByName | AuthenticateUserByName,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Users/AuthenticateByName",
    }

    if isinstance(body, AuthenticateUserByName):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AuthenticateUserByName):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AuthenticationResult | None:
    if response.status_code == 200:
        response_200 = AuthenticationResult.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AuthenticationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticateUserByName | AuthenticateUserByName,
) -> Response[Any | AuthenticationResult]:
    """Authenticates a user by name.

    Args:
        body (AuthenticateUserByName): The authenticate user by name request body.
        body (AuthenticateUserByName): The authenticate user by name request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuthenticationResult]
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
    client: AuthenticatedClient | Client,
    body: AuthenticateUserByName | AuthenticateUserByName,
) -> Any | AuthenticationResult | None:
    """Authenticates a user by name.

    Args:
        body (AuthenticateUserByName): The authenticate user by name request body.
        body (AuthenticateUserByName): The authenticate user by name request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuthenticationResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticateUserByName | AuthenticateUserByName,
) -> Response[Any | AuthenticationResult]:
    """Authenticates a user by name.

    Args:
        body (AuthenticateUserByName): The authenticate user by name request body.
        body (AuthenticateUserByName): The authenticate user by name request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuthenticationResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticateUserByName | AuthenticateUserByName,
) -> Any | AuthenticationResult | None:
    """Authenticates a user by name.

    Args:
        body (AuthenticateUserByName): The authenticate user by name request body.
        body (AuthenticateUserByName): The authenticate user by name request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuthenticationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
