from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_person_types: list[str] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    appears_in_item_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["searchTerm"] = search_term

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_filters: list[str] | Unset = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    params["isFavorite"] = is_favorite

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    json_exclude_person_types: list[str] | Unset = UNSET
    if not isinstance(exclude_person_types, Unset):
        json_exclude_person_types = exclude_person_types

    params["excludePersonTypes"] = json_exclude_person_types

    json_person_types: list[str] | Unset = UNSET
    if not isinstance(person_types, Unset):
        json_person_types = person_types

    params["personTypes"] = json_person_types

    json_appears_in_item_id: str | Unset = UNSET
    if not isinstance(appears_in_item_id, Unset):
        json_appears_in_item_id = str(appears_in_item_id)
    params["appearsInItemId"] = json_appears_in_item_id

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["enableImages"] = enable_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Persons",
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
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_person_types: list[str] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    appears_in_item_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets all persons.

    Args:
        limit (int | Unset):
        search_term (str | Unset):
        fields (list[ItemFields] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_person_types (list[str] | Unset):
        person_types (list[str] | Unset):
        appears_in_item_id (UUID | Unset):
        user_id (UUID | Unset):
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search_term=search_term,
        fields=fields,
        filters=filters,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_person_types=exclude_person_types,
        person_types=person_types,
        appears_in_item_id=appears_in_item_id,
        user_id=user_id,
        enable_images=enable_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_person_types: list[str] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    appears_in_item_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets all persons.

    Args:
        limit (int | Unset):
        search_term (str | Unset):
        fields (list[ItemFields] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_person_types (list[str] | Unset):
        person_types (list[str] | Unset):
        appears_in_item_id (UUID | Unset):
        user_id (UUID | Unset):
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        limit=limit,
        search_term=search_term,
        fields=fields,
        filters=filters,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_person_types=exclude_person_types,
        person_types=person_types,
        appears_in_item_id=appears_in_item_id,
        user_id=user_id,
        enable_images=enable_images,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_person_types: list[str] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    appears_in_item_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets all persons.

    Args:
        limit (int | Unset):
        search_term (str | Unset):
        fields (list[ItemFields] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_person_types (list[str] | Unset):
        person_types (list[str] | Unset):
        appears_in_item_id (UUID | Unset):
        user_id (UUID | Unset):
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search_term=search_term,
        fields=fields,
        filters=filters,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_person_types=exclude_person_types,
        person_types=person_types,
        appears_in_item_id=appears_in_item_id,
        user_id=user_id,
        enable_images=enable_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    search_term: str | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    filters: list[ItemFilter] | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    exclude_person_types: list[str] | Unset = UNSET,
    person_types: list[str] | Unset = UNSET,
    appears_in_item_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets all persons.

    Args:
        limit (int | Unset):
        search_term (str | Unset):
        fields (list[ItemFields] | Unset):
        filters (list[ItemFilter] | Unset):
        is_favorite (bool | Unset):
        enable_user_data (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        exclude_person_types (list[str] | Unset):
        person_types (list[str] | Unset):
        appears_in_item_id (UUID | Unset):
        user_id (UUID | Unset):
        enable_images (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            search_term=search_term,
            fields=fields,
            filters=filters,
            is_favorite=is_favorite,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            exclude_person_types=exclude_person_types,
            person_types=person_types,
            appears_in_item_id=appears_in_item_id,
            user_id=user_id,
            enable_images=enable_images,
        )
    ).parsed
