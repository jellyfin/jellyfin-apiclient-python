from http import HTTPStatus
from io import BytesIO
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import File, Response


def _get_kwargs(
    video_id: UUID,
    media_source_id: str,
    index: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{video_id}/{media_source_id}/Attachments/{index}".format(
            video_id=video_id,
            media_source_id=media_source_id,
            index=index,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

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
) -> Response[Any | File | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    video_id: UUID,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | File | ProblemDetails]:
    """Get video attachment.

    Args:
        video_id (UUID):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | ProblemDetails]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        media_source_id=media_source_id,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    video_id: UUID,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | File | ProblemDetails | None:
    """Get video attachment.

    Args:
        video_id (UUID):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | ProblemDetails
    """

    return sync_detailed(
        video_id=video_id,
        media_source_id=media_source_id,
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    video_id: UUID,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | File | ProblemDetails]:
    """Get video attachment.

    Args:
        video_id (UUID):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | ProblemDetails]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        media_source_id=media_source_id,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    video_id: UUID,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | File | ProblemDetails | None:
    """Get video attachment.

    Args:
        video_id (UUID):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | ProblemDetails
    """

    return (
        await asyncio_detailed(
            video_id=video_id,
            media_source_id=media_source_id,
            index=index,
            client=client,
        )
    ).parsed
