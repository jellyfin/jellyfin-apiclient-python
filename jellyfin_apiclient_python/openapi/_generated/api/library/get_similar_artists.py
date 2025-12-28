from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_exclude_artist_ids: list[str] | Unset = UNSET
    if not isinstance(exclude_artist_ids, Unset):
        json_exclude_artist_ids = []
        for exclude_artist_ids_item_data in exclude_artist_ids:
            exclude_artist_ids_item = str(exclude_artist_ids_item_data)
            json_exclude_artist_ids.append(exclude_artist_ids_item)

    params["excludeArtistIds"] = json_exclude_artist_ids

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["limit"] = limit

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Artists/{item_id}/Similar".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BaseItemDtoQueryResult | None:
    if response.status_code == 200:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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
) -> Response[Any | BaseItemDtoQueryResult]:
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
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            exclude_artist_ids=exclude_artist_ids,
            user_id=user_id,
            limit=limit,
            fields=fields,
        )
    ).parsed
