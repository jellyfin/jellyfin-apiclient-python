from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.all_theme_media_result import AllThemeMediaResult
from ...models.item_sort_by import ItemSortBy
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    user_id: UUID | Unset = UNSET,
    inherit_from_parent: bool | Unset = False,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["inheritFromParent"] = inherit_from_parent

    json_sort_by: list[str] | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    json_sort_order: list[str] | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/{item_id}/ThemeMedia".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AllThemeMediaResult | Any | None:
    if response.status_code == 200:
        response_200 = AllThemeMediaResult.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
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
) -> Response[AllThemeMediaResult | Any]:
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
    user_id: UUID | Unset = UNSET,
    inherit_from_parent: bool | Unset = False,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
) -> Response[AllThemeMediaResult | Any]:
    """Get theme songs and videos for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        inherit_from_parent (bool | Unset):  Default: False.
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllThemeMediaResult | Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        user_id=user_id,
        inherit_from_parent=inherit_from_parent,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    inherit_from_parent: bool | Unset = False,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
) -> AllThemeMediaResult | Any | None:
    """Get theme songs and videos for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        inherit_from_parent (bool | Unset):  Default: False.
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllThemeMediaResult | Any
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        user_id=user_id,
        inherit_from_parent=inherit_from_parent,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    inherit_from_parent: bool | Unset = False,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
) -> Response[AllThemeMediaResult | Any]:
    """Get theme songs and videos for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        inherit_from_parent (bool | Unset):  Default: False.
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllThemeMediaResult | Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        user_id=user_id,
        inherit_from_parent=inherit_from_parent,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    inherit_from_parent: bool | Unset = False,
    sort_by: list[ItemSortBy] | Unset = UNSET,
    sort_order: list[SortOrder] | Unset = UNSET,
) -> AllThemeMediaResult | Any | None:
    """Get theme songs and videos for an item.

    Args:
        item_id (UUID):
        user_id (UUID | Unset):
        inherit_from_parent (bool | Unset):  Default: False.
        sort_by (list[ItemSortBy] | Unset):
        sort_order (list[SortOrder] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllThemeMediaResult | Any
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            user_id=user_id,
            inherit_from_parent=inherit_from_parent,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
