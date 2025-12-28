from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.remote_subtitle_info import RemoteSubtitleInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    language: str,
    *,
    is_perfect_match: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["isPerfectMatch"] = is_perfect_match

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/{item_id}/RemoteSearch/Subtitles/{language}".format(
            item_id=item_id,
            language=language,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[RemoteSubtitleInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RemoteSubtitleInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | ProblemDetails | list[RemoteSubtitleInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: UUID,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[RemoteSubtitleInfo]]:
    """Search remote subtitles.

    Args:
        item_id (UUID):
        language (str):
        is_perfect_match (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[RemoteSubtitleInfo]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        language=language,
        is_perfect_match=is_perfect_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[RemoteSubtitleInfo] | None:
    """Search remote subtitles.

    Args:
        item_id (UUID):
        language (str):
        is_perfect_match (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[RemoteSubtitleInfo]
    """

    return sync_detailed(
        item_id=item_id,
        language=language,
        client=client,
        is_perfect_match=is_perfect_match,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[RemoteSubtitleInfo]]:
    """Search remote subtitles.

    Args:
        item_id (UUID):
        language (str):
        is_perfect_match (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[RemoteSubtitleInfo]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        language=language,
        is_perfect_match=is_perfect_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[RemoteSubtitleInfo] | None:
    """Search remote subtitles.

    Args:
        item_id (UUID):
        language (str):
        is_perfect_match (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[RemoteSubtitleInfo]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            language=language,
            client=client,
            is_perfect_match=is_perfect_match,
        )
    ).parsed
