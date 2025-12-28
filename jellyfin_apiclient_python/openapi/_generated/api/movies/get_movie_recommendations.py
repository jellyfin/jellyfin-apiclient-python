from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.item_fields import ItemFields
from ...models.recommendation_dto import RecommendationDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    category_limit: int | Unset = 5,
    item_limit: int | Unset = 8,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_parent_id: str | Unset = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parentId"] = json_parent_id

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["categoryLimit"] = category_limit

    params["itemLimit"] = item_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Movies/Recommendations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[RecommendationDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RecommendationDto.from_dict(response_200_item_data)

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
) -> Response[Any | list[RecommendationDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    category_limit: int | Unset = 5,
    item_limit: int | Unset = 8,
) -> Response[Any | list[RecommendationDto]]:
    """Gets movie recommendations.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        category_limit (int | Unset):  Default: 5.
        item_limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RecommendationDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        category_limit=category_limit,
        item_limit=item_limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    category_limit: int | Unset = 5,
    item_limit: int | Unset = 8,
) -> Any | list[RecommendationDto] | None:
    """Gets movie recommendations.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        category_limit (int | Unset):  Default: 5.
        item_limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RecommendationDto]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        category_limit=category_limit,
        item_limit=item_limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    category_limit: int | Unset = 5,
    item_limit: int | Unset = 8,
) -> Response[Any | list[RecommendationDto]]:
    """Gets movie recommendations.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        category_limit (int | Unset):  Default: 5.
        item_limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RecommendationDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        category_limit=category_limit,
        item_limit=item_limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    category_limit: int | Unset = 5,
    item_limit: int | Unset = 8,
) -> Any | list[RecommendationDto] | None:
    """Gets movie recommendations.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        category_limit (int | Unset):  Default: 5.
        item_limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RecommendationDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            fields=fields,
            category_limit=category_limit,
            item_limit=item_limit,
        )
    ).parsed
