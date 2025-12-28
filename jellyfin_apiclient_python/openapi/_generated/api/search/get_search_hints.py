from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_kind import BaseItemKind
from ...models.media_type import MediaType
from ...models.search_hint_result import SearchHintResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    search_term: str,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    include_people: bool | Unset = True,
    include_media: bool | Unset = True,
    include_genres: bool | Unset = True,
    include_studios: bool | Unset = True,
    include_artists: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["startIndex"] = start_index

    params["limit"] = limit

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["searchTerm"] = search_term

    json_include_item_types: list[str] | Unset = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    json_exclude_item_types: list[str] | Unset = UNSET
    if not isinstance(exclude_item_types, Unset):
        json_exclude_item_types = []
        for exclude_item_types_item_data in exclude_item_types:
            exclude_item_types_item = exclude_item_types_item_data.value
            json_exclude_item_types.append(exclude_item_types_item)

    params["excludeItemTypes"] = json_exclude_item_types

    json_media_types: list[str] | Unset = UNSET
    if not isinstance(media_types, Unset):
        json_media_types = []
        for media_types_item_data in media_types:
            media_types_item = media_types_item_data.value
            json_media_types.append(media_types_item)

    params["mediaTypes"] = json_media_types

    json_parent_id: str | Unset = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parentId"] = json_parent_id

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["includePeople"] = include_people

    params["includeMedia"] = include_media

    params["includeGenres"] = include_genres

    params["includeStudios"] = include_studios

    params["includeArtists"] = include_artists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Search/Hints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SearchHintResult | None:
    if response.status_code == 200:
        response_200 = SearchHintResult.from_dict(response.json())

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
) -> Response[Any | SearchHintResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    search_term: str,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    include_people: bool | Unset = True,
    include_media: bool | Unset = True,
    include_genres: bool | Unset = True,
    include_studios: bool | Unset = True,
    include_artists: bool | Unset = True,
) -> Response[Any | SearchHintResult]:
    """Gets the search hint result.

    Args:
        start_index (int | Unset):
        limit (int | Unset):
        user_id (UUID | Unset):
        search_term (str):
        include_item_types (list[BaseItemKind] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):
        parent_id (UUID | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        include_people (bool | Unset):  Default: True.
        include_media (bool | Unset):  Default: True.
        include_genres (bool | Unset):  Default: True.
        include_studios (bool | Unset):  Default: True.
        include_artists (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchHintResult]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        user_id=user_id,
        search_term=search_term,
        include_item_types=include_item_types,
        exclude_item_types=exclude_item_types,
        media_types=media_types,
        parent_id=parent_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        include_people=include_people,
        include_media=include_media,
        include_genres=include_genres,
        include_studios=include_studios,
        include_artists=include_artists,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    search_term: str,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    include_people: bool | Unset = True,
    include_media: bool | Unset = True,
    include_genres: bool | Unset = True,
    include_studios: bool | Unset = True,
    include_artists: bool | Unset = True,
) -> Any | SearchHintResult | None:
    """Gets the search hint result.

    Args:
        start_index (int | Unset):
        limit (int | Unset):
        user_id (UUID | Unset):
        search_term (str):
        include_item_types (list[BaseItemKind] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):
        parent_id (UUID | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        include_people (bool | Unset):  Default: True.
        include_media (bool | Unset):  Default: True.
        include_genres (bool | Unset):  Default: True.
        include_studios (bool | Unset):  Default: True.
        include_artists (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchHintResult
    """

    return sync_detailed(
        client=client,
        start_index=start_index,
        limit=limit,
        user_id=user_id,
        search_term=search_term,
        include_item_types=include_item_types,
        exclude_item_types=exclude_item_types,
        media_types=media_types,
        parent_id=parent_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        include_people=include_people,
        include_media=include_media,
        include_genres=include_genres,
        include_studios=include_studios,
        include_artists=include_artists,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    search_term: str,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    include_people: bool | Unset = True,
    include_media: bool | Unset = True,
    include_genres: bool | Unset = True,
    include_studios: bool | Unset = True,
    include_artists: bool | Unset = True,
) -> Response[Any | SearchHintResult]:
    """Gets the search hint result.

    Args:
        start_index (int | Unset):
        limit (int | Unset):
        user_id (UUID | Unset):
        search_term (str):
        include_item_types (list[BaseItemKind] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):
        parent_id (UUID | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        include_people (bool | Unset):  Default: True.
        include_media (bool | Unset):  Default: True.
        include_genres (bool | Unset):  Default: True.
        include_studios (bool | Unset):  Default: True.
        include_artists (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchHintResult]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        user_id=user_id,
        search_term=search_term,
        include_item_types=include_item_types,
        exclude_item_types=exclude_item_types,
        media_types=media_types,
        parent_id=parent_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        include_people=include_people,
        include_media=include_media,
        include_genres=include_genres,
        include_studios=include_studios,
        include_artists=include_artists,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    search_term: str,
    include_item_types: list[BaseItemKind] | Unset = UNSET,
    exclude_item_types: list[BaseItemKind] | Unset = UNSET,
    media_types: list[MediaType] | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
    is_movie: bool | Unset = UNSET,
    is_series: bool | Unset = UNSET,
    is_news: bool | Unset = UNSET,
    is_kids: bool | Unset = UNSET,
    is_sports: bool | Unset = UNSET,
    include_people: bool | Unset = True,
    include_media: bool | Unset = True,
    include_genres: bool | Unset = True,
    include_studios: bool | Unset = True,
    include_artists: bool | Unset = True,
) -> Any | SearchHintResult | None:
    """Gets the search hint result.

    Args:
        start_index (int | Unset):
        limit (int | Unset):
        user_id (UUID | Unset):
        search_term (str):
        include_item_types (list[BaseItemKind] | Unset):
        exclude_item_types (list[BaseItemKind] | Unset):
        media_types (list[MediaType] | Unset):
        parent_id (UUID | Unset):
        is_movie (bool | Unset):
        is_series (bool | Unset):
        is_news (bool | Unset):
        is_kids (bool | Unset):
        is_sports (bool | Unset):
        include_people (bool | Unset):  Default: True.
        include_media (bool | Unset):  Default: True.
        include_genres (bool | Unset):  Default: True.
        include_studios (bool | Unset):  Default: True.
        include_artists (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchHintResult
    """

    return (
        await asyncio_detailed(
            client=client,
            start_index=start_index,
            limit=limit,
            user_id=user_id,
            search_term=search_term,
            include_item_types=include_item_types,
            exclude_item_types=exclude_item_types,
            media_types=media_types,
            parent_id=parent_id,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            include_people=include_people,
            include_media=include_media,
            include_genres=include_genres,
            include_studios=include_studios,
            include_artists=include_artists,
        )
    ).parsed
