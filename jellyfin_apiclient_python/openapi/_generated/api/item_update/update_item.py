from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto import BaseItemDto
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    item_id: UUID,
    *,
    body: BaseItemDto | BaseItemDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Items/{item_id}".format(
            item_id=item_id,
        ),
    }

    if isinstance(body, BaseItemDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BaseItemDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: BaseItemDto | BaseItemDto,
) -> Response[Any | ProblemDetails]:
    """Updates an item.

    Args:
        item_id (UUID):
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BaseItemDto | BaseItemDto,
) -> Any | ProblemDetails | None:
    """Updates an item.

    Args:
        item_id (UUID):
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BaseItemDto | BaseItemDto,
) -> Response[Any | ProblemDetails]:
    """Updates an item.

    Args:
        item_id (UUID):
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BaseItemDto | BaseItemDto,
) -> Any | ProblemDetails | None:
    """Updates an item.

    Args:
        item_id (UUID):
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        body (BaseItemDto): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
