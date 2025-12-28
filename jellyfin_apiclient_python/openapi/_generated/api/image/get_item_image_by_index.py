from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_format import ImageFormat
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    image_type: ImageType,
    image_index: int,
    *,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    quality: int | Unset = UNSET,
    fill_width: int | Unset = UNSET,
    fill_height: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    format_: ImageFormat | Unset = UNSET,
    percent_played: float | Unset = UNSET,
    unplayed_count: int | Unset = UNSET,
    blur: int | Unset = UNSET,
    background_color: str | Unset = UNSET,
    foreground_layer: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["width"] = width

    params["height"] = height

    params["quality"] = quality

    params["fillWidth"] = fill_width

    params["fillHeight"] = fill_height

    params["tag"] = tag

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["percentPlayed"] = percent_played

    params["unplayedCount"] = unplayed_count

    params["blur"] = blur

    params["backgroundColor"] = background_color

    params["foregroundLayer"] = foreground_layer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/{item_id}/Images/{image_type}/{image_index}".format(
            item_id=item_id,
            image_type=image_type,
            image_index=image_index,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
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
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: UUID,
    image_type: ImageType,
    image_index: int,
    *,
    client: AuthenticatedClient | Client,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    quality: int | Unset = UNSET,
    fill_width: int | Unset = UNSET,
    fill_height: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    format_: ImageFormat | Unset = UNSET,
    percent_played: float | Unset = UNSET,
    unplayed_count: int | Unset = UNSET,
    blur: int | Unset = UNSET,
    background_color: str | Unset = UNSET,
    foreground_layer: str | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Gets the item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        max_width (int | Unset):
        max_height (int | Unset):
        width (int | Unset):
        height (int | Unset):
        quality (int | Unset):
        fill_width (int | Unset):
        fill_height (int | Unset):
        tag (str | Unset):
        format_ (ImageFormat | Unset): Enum ImageOutputFormat.
        percent_played (float | Unset):
        unplayed_count (int | Unset):
        blur (int | Unset):
        background_color (str | Unset):
        foreground_layer (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        image_type=image_type,
        image_index=image_index,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        tag=tag,
        format_=format_,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    image_type: ImageType,
    image_index: int,
    *,
    client: AuthenticatedClient | Client,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    quality: int | Unset = UNSET,
    fill_width: int | Unset = UNSET,
    fill_height: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    format_: ImageFormat | Unset = UNSET,
    percent_played: float | Unset = UNSET,
    unplayed_count: int | Unset = UNSET,
    blur: int | Unset = UNSET,
    background_color: str | Unset = UNSET,
    foreground_layer: str | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Gets the item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        max_width (int | Unset):
        max_height (int | Unset):
        width (int | Unset):
        height (int | Unset):
        quality (int | Unset):
        fill_width (int | Unset):
        fill_height (int | Unset):
        tag (str | Unset):
        format_ (ImageFormat | Unset): Enum ImageOutputFormat.
        percent_played (float | Unset):
        unplayed_count (int | Unset):
        blur (int | Unset):
        background_color (str | Unset):
        foreground_layer (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        image_type=image_type,
        image_index=image_index,
        client=client,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        tag=tag,
        format_=format_,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    image_type: ImageType,
    image_index: int,
    *,
    client: AuthenticatedClient | Client,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    quality: int | Unset = UNSET,
    fill_width: int | Unset = UNSET,
    fill_height: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    format_: ImageFormat | Unset = UNSET,
    percent_played: float | Unset = UNSET,
    unplayed_count: int | Unset = UNSET,
    blur: int | Unset = UNSET,
    background_color: str | Unset = UNSET,
    foreground_layer: str | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Gets the item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        max_width (int | Unset):
        max_height (int | Unset):
        width (int | Unset):
        height (int | Unset):
        quality (int | Unset):
        fill_width (int | Unset):
        fill_height (int | Unset):
        tag (str | Unset):
        format_ (ImageFormat | Unset): Enum ImageOutputFormat.
        percent_played (float | Unset):
        unplayed_count (int | Unset):
        blur (int | Unset):
        background_color (str | Unset):
        foreground_layer (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        image_type=image_type,
        image_index=image_index,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        tag=tag,
        format_=format_,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    image_type: ImageType,
    image_index: int,
    *,
    client: AuthenticatedClient | Client,
    max_width: int | Unset = UNSET,
    max_height: int | Unset = UNSET,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,
    quality: int | Unset = UNSET,
    fill_width: int | Unset = UNSET,
    fill_height: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    format_: ImageFormat | Unset = UNSET,
    percent_played: float | Unset = UNSET,
    unplayed_count: int | Unset = UNSET,
    blur: int | Unset = UNSET,
    background_color: str | Unset = UNSET,
    foreground_layer: str | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Gets the item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        max_width (int | Unset):
        max_height (int | Unset):
        width (int | Unset):
        height (int | Unset):
        quality (int | Unset):
        fill_width (int | Unset):
        fill_height (int | Unset):
        tag (str | Unset):
        format_ (ImageFormat | Unset): Enum ImageOutputFormat.
        percent_played (float | Unset):
        unplayed_count (int | Unset):
        blur (int | Unset):
        background_color (str | Unset):
        foreground_layer (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            image_type=image_type,
            image_index=image_index,
            client=client,
            max_width=max_width,
            max_height=max_height,
            width=width,
            height=height,
            quality=quality,
            fill_width=fill_width,
            fill_height=fill_height,
            tag=tag,
            format_=format_,
            percent_played=percent_played,
            unplayed_count=unplayed_count,
            blur=blur,
            background_color=background_color,
            foreground_layer=foreground_layer,
        )
    ).parsed
