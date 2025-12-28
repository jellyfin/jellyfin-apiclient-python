from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.session_info_dto import SessionInfoDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    controllable_by_user_id: UUID | Unset = UNSET,
    device_id: str | Unset = UNSET,
    active_within_seconds: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_controllable_by_user_id: str | Unset = UNSET
    if not isinstance(controllable_by_user_id, Unset):
        json_controllable_by_user_id = str(controllable_by_user_id)
    params["controllableByUserId"] = json_controllable_by_user_id

    params["deviceId"] = device_id

    params["activeWithinSeconds"] = active_within_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[SessionInfoDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SessionInfoDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[SessionInfoDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: UUID | Unset = UNSET,
    device_id: str | Unset = UNSET,
    active_within_seconds: int | Unset = UNSET,
) -> Response[Any | list[SessionInfoDto]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (UUID | Unset):
        device_id (str | Unset):
        active_within_seconds (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[SessionInfoDto]]
    """

    kwargs = _get_kwargs(
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: UUID | Unset = UNSET,
    device_id: str | Unset = UNSET,
    active_within_seconds: int | Unset = UNSET,
) -> Any | list[SessionInfoDto] | None:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (UUID | Unset):
        device_id (str | Unset):
        active_within_seconds (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[SessionInfoDto]
    """

    return sync_detailed(
        client=client,
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: UUID | Unset = UNSET,
    device_id: str | Unset = UNSET,
    active_within_seconds: int | Unset = UNSET,
) -> Response[Any | list[SessionInfoDto]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (UUID | Unset):
        device_id (str | Unset):
        active_within_seconds (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[SessionInfoDto]]
    """

    kwargs = _get_kwargs(
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: UUID | Unset = UNSET,
    device_id: str | Unset = UNSET,
    active_within_seconds: int | Unset = UNSET,
) -> Any | list[SessionInfoDto] | None:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (UUID | Unset):
        device_id (str | Unset):
        active_within_seconds (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[SessionInfoDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            controllable_by_user_id=controllable_by_user_id,
            device_id=device_id,
            active_within_seconds=active_within_seconds,
        )
    ).parsed
