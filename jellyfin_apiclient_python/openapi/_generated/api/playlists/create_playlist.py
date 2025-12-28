from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_playlist_dto import CreatePlaylistDto
from ...models.media_type import MediaType
from ...models.playlist_creation_result import PlaylistCreationResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreatePlaylistDto | CreatePlaylistDto,
    name: str | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    media_type: MediaType | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = []
        for ids_item_data in ids:
            ids_item = str(ids_item_data)
            json_ids.append(ids_item)

    params["ids"] = json_ids

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_media_type: str | Unset = UNSET
    if not isinstance(media_type, Unset):
        json_media_type = media_type.value

    params["mediaType"] = json_media_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Playlists",
        "params": params,
    }

    if isinstance(body, CreatePlaylistDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePlaylistDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PlaylistCreationResult | None:
    if response.status_code == 200:
        response_200 = PlaylistCreationResult.from_dict(response.json())

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
) -> Response[Any | PlaylistCreationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreatePlaylistDto | CreatePlaylistDto,
    name: str | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    media_type: MediaType | Unset = UNSET,
) -> Response[Any | PlaylistCreationResult]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (str | Unset):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        media_type (MediaType | Unset): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistCreationResult]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreatePlaylistDto | CreatePlaylistDto,
    name: str | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    media_type: MediaType | Unset = UNSET,
) -> Any | PlaylistCreationResult | None:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (str | Unset):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        media_type (MediaType | Unset): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistCreationResult
    """

    return sync_detailed(
        client=client,
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreatePlaylistDto | CreatePlaylistDto,
    name: str | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    media_type: MediaType | Unset = UNSET,
) -> Response[Any | PlaylistCreationResult]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (str | Unset):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        media_type (MediaType | Unset): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistCreationResult]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreatePlaylistDto | CreatePlaylistDto,
    name: str | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    media_type: MediaType | Unset = UNSET,
) -> Any | PlaylistCreationResult | None:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (str | Unset):
        ids (list[UUID] | Unset):
        user_id (UUID | Unset):
        media_type (MediaType | Unset): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistCreationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
        )
    ).parsed
