from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    image_type: ImageType,
    *,
    image_index: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["imageIndex"] = image_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/Items/{item_id}/Images/{image_type}".format(
            item_id=item_id,
            image_type=image_type,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    *,
    client: AuthenticatedClient,
    image_index: int | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Delete an item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int | Unset):

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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    image_index: int | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Delete an item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        image_type=image_type,
        client=client,
        image_index=image_index,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    image_index: int | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Delete an item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int | Unset):

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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    image_index: int | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Delete an item's image.

    Args:
        item_id (UUID):
        image_type (ImageType): Enum ImageType.
        image_index (int | Unset):

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
            client=client,
            image_index=image_index,
        )
    ).parsed
