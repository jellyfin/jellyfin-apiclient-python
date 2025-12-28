from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto import BaseItemDto
from ...models.base_item_kind import BaseItemKind
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    limit: int | Unset = 20,
    group_items: bool | Unset = True,
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

    json_include_item_types: list[str] | Unset = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    params["isPlayed"] = is_played

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["enableUserData"] = enable_user_data

    params["limit"] = limit

    params["groupItems"] = group_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/Latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[BaseItemDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BaseItemDto.from_dict(response_200_item_data)

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
) -> Response[Any | list[BaseItemDto]]:
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
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    limit: int | Unset = 20,
    group_items: bool | Unset = True,
) -> Response[Any | list[BaseItemDto]]:
    """Gets latest media.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        is_played (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        limit (int | Unset):  Default: 20.
        group_items (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[BaseItemDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        include_item_types=include_item_types,
        is_played=is_played,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        limit=limit,
        group_items=group_items,
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
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    limit: int | Unset = 20,
    group_items: bool | Unset = True,
) -> Any | list[BaseItemDto] | None:
    """Gets latest media.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        is_played (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        limit (int | Unset):  Default: 20.
        group_items (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[BaseItemDto]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        include_item_types=include_item_types,
        is_played=is_played,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        limit=limit,
        group_items=group_items,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    limit: int | Unset = 20,
    group_items: bool | Unset = True,
) -> Response[Any | list[BaseItemDto]]:
    """Gets latest media.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        is_played (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        limit (int | Unset):  Default: 20.
        group_items (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[BaseItemDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        include_item_types=include_item_types,
        is_played=is_played,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        limit=limit,
        group_items=group_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    is_played: bool | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    limit: int | Unset = 20,
    group_items: bool | Unset = True,
) -> Any | list[BaseItemDto] | None:
    """Gets latest media.

    Args:
        user_id (UUID | Unset):
        parent_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        include_item_types (list[BaseItemKind] | Unset):
        is_played (bool | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        limit (int | Unset):  Default: 20.
        group_items (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[BaseItemDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            fields=fields,
            include_item_types=include_item_types,
            is_played=is_played,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            limit=limit,
            group_items=group_items,
        )
    ).parsed
