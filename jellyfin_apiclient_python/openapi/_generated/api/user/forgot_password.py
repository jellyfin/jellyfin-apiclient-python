from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forgot_password_dto import ForgotPasswordDto
from ...models.forgot_password_result import ForgotPasswordResult
from ...types import Response


def _get_kwargs(
    *,
    body: ForgotPasswordDto | ForgotPasswordDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Users/ForgotPassword",
    }

    if isinstance(body, ForgotPasswordDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ForgotPasswordDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ForgotPasswordResult | None:
    if response.status_code == 200:
        response_200 = ForgotPasswordResult.from_dict(response.json())

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
) -> Response[Any | ForgotPasswordResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordDto | ForgotPasswordDto,
) -> Response[Any | ForgotPasswordResult]:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ForgotPasswordResult]
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
    body: ForgotPasswordDto | ForgotPasswordDto,
) -> Any | ForgotPasswordResult | None:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ForgotPasswordResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordDto | ForgotPasswordDto,
) -> Response[Any | ForgotPasswordResult]:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ForgotPasswordResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordDto | ForgotPasswordDto,
) -> Any | ForgotPasswordResult | None:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ForgotPasswordResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
