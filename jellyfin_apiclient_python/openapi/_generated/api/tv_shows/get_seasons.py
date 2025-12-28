from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    series_id: UUID,
    *,
    user_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    is_special_season: bool | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["isSpecialSeason"] = is_special_season

    params["isMissing"] = is_missing

    json_adjacent_to: str | Unset = UNSET
    if not isinstance(adjacent_to, Unset):
        json_adjacent_to = str(adjacent_to)
    params["adjacentTo"] = json_adjacent_to

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Shows/{series_id}/Seasons".format(
            series_id=series_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BaseItemDtoQueryResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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
) -> Response[Any | BaseItemDtoQueryResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    series_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    is_special_season: bool | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult | ProblemDetails]:
    """Gets seasons for a tv series.

    Args:
        series_id (UUID):
        user_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        is_special_season (bool | Unset):
        is_missing (bool | Unset):
        adjacent_to (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        user_id=user_id,
        fields=fields,
        is_special_season=is_special_season,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    is_special_season: bool | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | ProblemDetails | None:
    """Gets seasons for a tv series.

    Args:
        series_id (UUID):
        user_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        is_special_season (bool | Unset):
        is_missing (bool | Unset):
        adjacent_to (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult | ProblemDetails
    """

    return sync_detailed(
        series_id=series_id,
        client=client,
        user_id=user_id,
        fields=fields,
        is_special_season=is_special_season,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
    ).parsed


async def asyncio_detailed(
    series_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    is_special_season: bool | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
) -> Response[Any | BaseItemDtoQueryResult | ProblemDetails]:
    """Gets seasons for a tv series.

    Args:
        series_id (UUID):
        user_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        is_special_season (bool | Unset):
        is_missing (bool | Unset):
        adjacent_to (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        user_id=user_id,
        fields=fields,
        is_special_season=is_special_season,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_id: UUID,
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    is_special_season: bool | Unset = UNSET,
    is_missing: bool | Unset = UNSET,
    adjacent_to: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
) -> Any | BaseItemDtoQueryResult | ProblemDetails | None:
    """Gets seasons for a tv series.

    Args:
        series_id (UUID):
        user_id (UUID | Unset):
        fields (list[ItemFields] | Unset):
        is_special_season (bool | Unset):
        is_missing (bool | Unset):
        adjacent_to (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult | ProblemDetails
    """

    return (
        await asyncio_detailed(
            series_id=series_id,
            client=client,
            user_id=user_id,
            fields=fields,
            is_special_season=is_special_season,
            is_missing=is_missing,
            adjacent_to=adjacent_to,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
        )
    ).parsed
