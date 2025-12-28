from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.recording_status import RecordingStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    status: RecordingStatus | Unset = UNSET,
    is_in_progress: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_library_item: bool | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["channelId"] = channel_id

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["isInProgress"] = is_in_progress

    params["seriesTimerId"] = series_timer_id

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: list[str] | Unset = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["enableUserData"] = enable_user_data

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["isNews"] = is_news

    params["isLibraryItem"] = is_library_item

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Recordings",
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
    channel_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    status: RecordingStatus | Unset = UNSET,
    is_in_progress: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_library_item: bool | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets live tv recordings.

    Args:
        channel_id (str | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        status (RecordingStatus | Unset):
        is_in_progress (bool | Unset):
        series_timer_id (str | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        is_news (bool | Unset):
        is_library_item (bool | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        status=status,
        is_in_progress=is_in_progress,
        series_timer_id=series_timer_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        is_movie=is_movie,
        is_series=is_series,
        is_kids=is_kids,
        is_sports=is_sports,
        is_news=is_news,
        is_library_item=is_library_item,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    status: RecordingStatus | Unset = UNSET,
    is_in_progress: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_library_item: bool | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets live tv recordings.

    Args:
        channel_id (str | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        status (RecordingStatus | Unset):
        is_in_progress (bool | Unset):
        series_timer_id (str | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        is_news (bool | Unset):
        is_library_item (bool | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        status=status,
        is_in_progress=is_in_progress,
        series_timer_id=series_timer_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        is_movie=is_movie,
        is_series=is_series,
        is_kids=is_kids,
        is_sports=is_sports,
        is_news=is_news,
        is_library_item=is_library_item,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    status: RecordingStatus | Unset = UNSET,
    is_in_progress: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_library_item: bool | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets live tv recordings.

    Args:
        channel_id (str | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        status (RecordingStatus | Unset):
        is_in_progress (bool | Unset):
        series_timer_id (str | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        is_news (bool | Unset):
        is_library_item (bool | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BaseItemDtoQueryResult]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        status=status,
        is_in_progress=is_in_progress,
        series_timer_id=series_timer_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        is_movie=is_movie,
        is_series=is_series,
        is_kids=is_kids,
        is_sports=is_sports,
        is_news=is_news,
        is_library_item=is_library_item,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    status: RecordingStatus | Unset = UNSET,
    is_in_progress: bool | Unset = UNSET,
    series_timer_id: str | Unset = UNSET,
    enable_images: bool | Unset = UNSET,
    image_type_limit: int | Unset = UNSET,
    enable_image_types: list[ImageType] | Unset = UNSET,
    fields: list[ItemFields] | Unset = UNSET,
    enable_user_data: bool | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_library_item: bool | Unset = UNSET,
    enable_total_record_count: bool | Unset = True,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets live tv recordings.

    Args:
        channel_id (str | Unset):
        user_id (UUID | Unset):
        start_index (int | Unset):
        limit (int | Unset):
        status (RecordingStatus | Unset):
        is_in_progress (bool | Unset):
        series_timer_id (str | Unset):
        enable_images (bool | Unset):
        image_type_limit (int | Unset):
        enable_image_types (list[ImageType] | Unset):
        fields (list[ItemFields] | Unset):
        enable_user_data (bool | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        is_news (bool | Unset):
        is_library_item (bool | Unset):
        enable_total_record_count (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BaseItemDtoQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            status=status,
            is_in_progress=is_in_progress,
            series_timer_id=series_timer_id,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            fields=fields,
            enable_user_data=enable_user_data,
            is_movie=is_movie,
            is_series=is_series,
            is_kids=is_kids,
            is_sports=is_sports,
            is_news=is_news,
            is_library_item=is_library_item,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
