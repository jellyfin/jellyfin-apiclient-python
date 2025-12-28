from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.display_preferences_dto import DisplayPreferencesDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    display_preferences_id: str,
    *,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/DisplayPreferences/{display_preferences_id}".format(
            display_preferences_id=display_preferences_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DisplayPreferencesDto | None:
    if response.status_code == 200:
        response_200 = DisplayPreferencesDto.from_dict(response.json())

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
) -> Response[Any | DisplayPreferencesDto]:
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
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> Response[Any | DisplayPreferencesDto]:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (UUID | Unset):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DisplayPreferencesDto]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        user_id=user_id,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> Any | DisplayPreferencesDto | None:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (UUID | Unset):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DisplayPreferencesDto
    """

    return sync_detailed(
        display_preferences_id=display_preferences_id,
        client=client,
        user_id=user_id,
        client_query=client_query,
    ).parsed


async def asyncio_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> Response[Any | DisplayPreferencesDto]:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (UUID | Unset):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DisplayPreferencesDto]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        user_id=user_id,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    client_query: str,
) -> Any | DisplayPreferencesDto | None:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (UUID | Unset):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DisplayPreferencesDto
    """

    return (
        await asyncio_detailed(
            display_preferences_id=display_preferences_id,
            client=client,
            user_id=user_id,
            client_query=client_query,
        )
    ).parsed
