from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forgot_password_pin_dto import ForgotPasswordPinDto
from ...models.pin_redeem_result import PinRedeemResult
from ...types import Response


def _get_kwargs(
    *,
    body: ForgotPasswordPinDto | ForgotPasswordPinDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Users/ForgotPassword/Pin",
    }

    if isinstance(body, ForgotPasswordPinDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ForgotPasswordPinDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PinRedeemResult | None:
    if response.status_code == 200:
        response_200 = PinRedeemResult.from_dict(response.json())

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
) -> Response[Any | PinRedeemResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordPinDto | ForgotPasswordPinDto,
) -> Response[Any | PinRedeemResult]:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PinRedeemResult]
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
    body: ForgotPasswordPinDto | ForgotPasswordPinDto,
) -> Any | PinRedeemResult | None:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PinRedeemResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordPinDto | ForgotPasswordPinDto,
) -> Response[Any | PinRedeemResult]:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PinRedeemResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordPinDto | ForgotPasswordPinDto,
) -> Any | PinRedeemResult | None:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PinRedeemResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
