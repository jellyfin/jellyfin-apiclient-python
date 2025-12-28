from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.media_segment_dto_query_result import MediaSegmentDtoQueryResult
from ...models.media_segment_type import MediaSegmentType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    include_segment_types: list[MediaSegmentType] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include_segment_types: list[str] | Unset = UNSET
    if not isinstance(include_segment_types, Unset):
        json_include_segment_types = []
        for include_segment_types_item_data in include_segment_types:
            include_segment_types_item = include_segment_types_item_data.value
            json_include_segment_types.append(include_segment_types_item)

    params["includeSegmentTypes"] = json_include_segment_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/MediaSegments/{item_id}".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MediaSegmentDtoQueryResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = MediaSegmentDtoQueryResult.from_dict(response.json())

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
) -> Response[Any | MediaSegmentDtoQueryResult | ProblemDetails]:
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
    include_segment_types: list[MediaSegmentType] | Unset = UNSET,
) -> Response[Any | MediaSegmentDtoQueryResult | ProblemDetails]:
    """Gets all media segments based on an itemId.

    Args:
        item_id (UUID):
        include_segment_types (list[MediaSegmentType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MediaSegmentDtoQueryResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        include_segment_types=include_segment_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    include_segment_types: list[MediaSegmentType] | Unset = UNSET,
) -> Any | MediaSegmentDtoQueryResult | ProblemDetails | None:
    """Gets all media segments based on an itemId.

    Args:
        item_id (UUID):
        include_segment_types (list[MediaSegmentType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MediaSegmentDtoQueryResult | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        include_segment_types=include_segment_types,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    include_segment_types: list[MediaSegmentType] | Unset = UNSET,
) -> Response[Any | MediaSegmentDtoQueryResult | ProblemDetails]:
    """Gets all media segments based on an itemId.

    Args:
        item_id (UUID):
        include_segment_types (list[MediaSegmentType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MediaSegmentDtoQueryResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        include_segment_types=include_segment_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    include_segment_types: list[MediaSegmentType] | Unset = UNSET,
) -> Any | MediaSegmentDtoQueryResult | ProblemDetails | None:
    """Gets all media segments based on an itemId.

    Args:
        item_id (UUID):
        include_segment_types (list[MediaSegmentType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MediaSegmentDtoQueryResult | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            include_segment_types=include_segment_types,
        )
    ).parsed
