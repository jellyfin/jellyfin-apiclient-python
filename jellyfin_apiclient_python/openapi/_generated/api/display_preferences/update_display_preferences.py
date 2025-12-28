from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.display_preferences_dto import DisplayPreferencesDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    display_preferences_id: str,
    *,
    body: DisplayPreferencesDto | DisplayPreferencesDto,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/DisplayPreferences/{display_preferences_id}".format(
            display_preferences_id=display_preferences_id,
        ),
        "params": params,
    }

    if isinstance(body, DisplayPreferencesDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DisplayPreferencesDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 503:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    body: DisplayPreferencesDto | DisplayPreferencesDto,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> Response[Any]:
    """Update Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (UUID | Unset):
        client_query (str):
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        body=body,
        user_id=user_id,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    body: DisplayPreferencesDto | DisplayPreferencesDto,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> Response[Any]:
    """Update Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (UUID | Unset):
        client_query (str):
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        body=body,
        user_id=user_id,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
