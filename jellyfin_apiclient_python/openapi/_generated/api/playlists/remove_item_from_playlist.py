from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    *,
    entry_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_entry_ids: list[str] | Unset = UNSET
    if not isinstance(entry_ids, Unset):
        json_entry_ids = entry_ids

    params["entryIds"] = json_entry_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/Playlists/{playlist_id}/Items".format(
            playlist_id=playlist_id,
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
        response_403 = ProblemDetails.from_dict(response.json())

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
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    entry_ids: list[str] | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Removes items from a playlist.

    Args:
        playlist_id (str):
        entry_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        entry_ids=entry_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    entry_ids: list[str] | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Removes items from a playlist.

    Args:
        playlist_id (str):
        entry_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        entry_ids=entry_ids,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    entry_ids: list[str] | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Removes items from a playlist.

    Args:
        playlist_id (str):
        entry_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        entry_ids=entry_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    entry_ids: list[str] | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Removes items from a playlist.

    Args:
        playlist_id (str):
        entry_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            entry_ids=entry_ids,
        )
    ).parsed
