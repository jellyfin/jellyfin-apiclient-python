from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.book_info_remote_search_query import BookInfoRemoteSearchQuery
from ...models.remote_search_result import RemoteSearchResult
from ...types import Response


def _get_kwargs(
    *,
    body: BookInfoRemoteSearchQuery | BookInfoRemoteSearchQuery,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Items/RemoteSearch/Book",
    }

    if isinstance(body, BookInfoRemoteSearchQuery):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BookInfoRemoteSearchQuery):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[RemoteSearchResult] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RemoteSearchResult.from_dict(response_200_item_data)

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
) -> Response[Any | list[RemoteSearchResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BookInfoRemoteSearchQuery | BookInfoRemoteSearchQuery,
) -> Response[Any | list[RemoteSearchResult]]:
    """Get book remote search.

    Args:
        body (BookInfoRemoteSearchQuery):
        body (BookInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RemoteSearchResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BookInfoRemoteSearchQuery | BookInfoRemoteSearchQuery,
) -> Any | list[RemoteSearchResult] | None:
    """Get book remote search.

    Args:
        body (BookInfoRemoteSearchQuery):
        body (BookInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RemoteSearchResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BookInfoRemoteSearchQuery | BookInfoRemoteSearchQuery,
) -> Response[Any | list[RemoteSearchResult]]:
    """Get book remote search.

    Args:
        body (BookInfoRemoteSearchQuery):
        body (BookInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RemoteSearchResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BookInfoRemoteSearchQuery | BookInfoRemoteSearchQuery,
) -> Any | list[RemoteSearchResult] | None:
    """Get book remote search.

    Args:
        body (BookInfoRemoteSearchQuery):
        body (BookInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RemoteSearchResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
