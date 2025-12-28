from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    collection_id: UUID,
    *,
    ids: list[UUID],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ids = []
    for ids_item_data in ids:
        ids_item = str(ids_item_data)
        json_ids.append(ids_item)

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/Collections/{collection_id}/Items".format(
            collection_id=collection_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 503:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID],
) -> Response[Any]:
    """Removes items from a collection.

    Args:
        collection_id (UUID):
        ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID],
) -> Response[Any]:
    """Removes items from a collection.

    Args:
        collection_id (UUID):
        ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
