from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.update_user_item_data_dto import UpdateUserItemDataDto
from ...models.user_item_data_dto import UserItemDataDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    body: UpdateUserItemDataDto | UpdateUserItemDataDto,
    user_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/UserItems/{item_id}/UserData".format(
            item_id=item_id,
        ),
        "params": params,
    }

    if isinstance(body, UpdateUserItemDataDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUserItemDataDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | UserItemDataDto | None:
    if response.status_code == 200:
        response_200 = UserItemDataDto.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | UserItemDataDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateUserItemDataDto | UpdateUserItemDataDto,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | ProblemDetails | UserItemDataDto]:
    """Update Item User Data.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | UserItemDataDto]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateUserItemDataDto | UpdateUserItemDataDto,
    user_id: UUID | Unset = UNSET,
) -> Any | ProblemDetails | UserItemDataDto | None:
    """Update Item User Data.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | UserItemDataDto
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateUserItemDataDto | UpdateUserItemDataDto,
    user_id: UUID | Unset = UNSET,
) -> Response[Any | ProblemDetails | UserItemDataDto]:
    """Update Item User Data.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | UserItemDataDto]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateUserItemDataDto | UpdateUserItemDataDto,
    user_id: UUID | Unset = UNSET,
) -> Any | ProblemDetails | UserItemDataDto | None:
    """Update Item User Data.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | UserItemDataDto
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
            user_id=user_id,
        )
    ).parsed
