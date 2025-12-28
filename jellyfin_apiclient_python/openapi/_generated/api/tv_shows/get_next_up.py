import datetime
from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    series_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    next_up_date_cutoff: datetime.datetime | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    disable_first_episode: bool | Unset = False,
    enable_resumable: bool | Unset = True,
    enable_rewatching: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_series_id: str | Unset = UNSET
    if not isinstance(series_id, Unset):
        json_series_id = str(series_id)
    params["seriesId"] = json_series_id

    json_parent_id: str | Unset = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parentId"] = json_parent_id

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

    json_next_up_date_cutoff: str | Unset = UNSET
    if not isinstance(next_up_date_cutoff, Unset):
        json_next_up_date_cutoff = next_up_date_cutoff.isoformat()
    params["nextUpDateCutoff"] = json_next_up_date_cutoff

    params["enableTotalRecordCount"] = enable_total_record_count

    params["disableFirstEpisode"] = disable_first_episode

    params["enableResumable"] = enable_resumable

    params["enableRewatching"] = enable_rewatching

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Shows/NextUp",
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
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    series_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    next_up_date_cutoff: datetime.datetime | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    disable_first_episode: bool | Unset = False,
    enable_resumable: bool | Unset = True,
    enable_rewatching: bool | Unset = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets a list of next up episodes.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):
        series_id (UUID | Unset):
        parent_id (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        next_up_date_cutoff (datetime.datetime | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        disable_first_episode (bool | Unset):  Default: False.
        enable_resumable (bool | Unset):  Default: True.
        enable_rewatching (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        fields=fields,
        series_id=series_id,
        parent_id=parent_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        next_up_date_cutoff=next_up_date_cutoff,
        enable_total_record_count=enable_total_record_count,
        disable_first_episode=disable_first_episode,
        enable_resumable=enable_resumable,
        enable_rewatching=enable_rewatching,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    series_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    next_up_date_cutoff: datetime.datetime | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    disable_first_episode: bool | Unset = False,
    enable_resumable: bool | Unset = True,
    enable_rewatching: bool | Unset = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets a list of next up episodes.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):
        series_id (UUID | Unset):
        parent_id (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        next_up_date_cutoff (datetime.datetime | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        disable_first_episode (bool | Unset):  Default: False.
        enable_resumable (bool | Unset):  Default: True.
        enable_rewatching (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        fields=fields,
        series_id=series_id,
        parent_id=parent_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        next_up_date_cutoff=next_up_date_cutoff,
        enable_total_record_count=enable_total_record_count,
        disable_first_episode=disable_first_episode,
        enable_resumable=enable_resumable,
        enable_rewatching=enable_rewatching,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    series_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    next_up_date_cutoff: datetime.datetime | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    disable_first_episode: bool | Unset = False,
    enable_resumable: bool | Unset = True,
    enable_rewatching: bool | Unset = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets a list of next up episodes.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):
        series_id (UUID | Unset):
        parent_id (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        next_up_date_cutoff (datetime.datetime | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        disable_first_episode (bool | Unset):  Default: False.
        enable_resumable (bool | Unset):  Default: True.
        enable_rewatching (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        fields=fields,
        series_id=series_id,
        parent_id=parent_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        next_up_date_cutoff=next_up_date_cutoff,
        enable_total_record_count=enable_total_record_count,
        disable_first_episode=disable_first_episode,
        enable_resumable=enable_resumable,
        enable_rewatching=enable_rewatching,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    series_id: UUID | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    next_up_date_cutoff: datetime.datetime | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
    disable_first_episode: bool | Unset = False,
    enable_resumable: bool | Unset = True,
    enable_rewatching: bool | Unset = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets a list of next up episodes.

    Args:
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        fields (list[ItemFields] | Unset):
        series_id (UUID | Unset):
        parent_id (UUID | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        enable_user_data (bool | Unset):
        next_up_date_cutoff (datetime.datetime | Unset):
        enable_total_record_count (bool | Unset):  Default: True.
        disable_first_episode (bool | Unset):  Default: False.
        enable_resumable (bool | Unset):  Default: True.
        enable_rewatching (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            fields=fields,
            series_id=series_id,
            parent_id=parent_id,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            next_up_date_cutoff=next_up_date_cutoff,
            enable_total_record_count=enable_total_record_count,
            disable_first_episode=disable_first_episode,
            enable_resumable=enable_resumable,
            enable_rewatching=enable_rewatching,
        )
    ).parsed
