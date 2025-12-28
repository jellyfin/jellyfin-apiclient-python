from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    item_id: str,
    playlist_id: str,
    segment_id: str,
    segment_container: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{item_id}/hls/{playlist_id}/{segment_id}.{segment_container}".format(
            item_id=item_id,
            playlist_id=playlist_id,
            segment_id=segment_id,
            segment_container=segment_container,
        ),
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
    item_id: str,
    playlist_id: str,
    segment_id: str,
    segment_container: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails]:
    """Gets a hls video segment.

    Args:
        item_id (str):
        playlist_id (str):
        segment_id (str):
        segment_container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        playlist_id=playlist_id,
        segment_id=segment_id,
        segment_container=segment_container,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    playlist_id: str,
    segment_id: str,
    segment_container: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ProblemDetails | None:
    """Gets a hls video segment.

    Args:
        item_id (str):
        playlist_id (str):
        segment_id (str):
        segment_container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        playlist_id=playlist_id,
        segment_id=segment_id,
        segment_container=segment_container,
        client=client,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    playlist_id: str,
    segment_id: str,
    segment_container: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails]:
    """Gets a hls video segment.

    Args:
        item_id (str):
        playlist_id (str):
        segment_id (str):
        segment_container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        playlist_id=playlist_id,
        segment_id=segment_id,
        segment_container=segment_container,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    playlist_id: str,
    segment_id: str,
    segment_container: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ProblemDetails | None:
    """Gets a hls video segment.

    Args:
        item_id (str):
        playlist_id (str):
        segment_id (str):
        segment_container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            playlist_id=playlist_id,
            segment_id=segment_id,
            segment_container=segment_container,
            client=client,
        )
    ).parsed
