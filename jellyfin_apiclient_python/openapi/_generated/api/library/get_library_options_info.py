from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_type import CollectionType
from ...models.library_options_result_dto import LibraryOptionsResultDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    library_content_type: CollectionType | Unset = UNSET,
    is_new_library: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_library_content_type: str | Unset = UNSET
    if not isinstance(library_content_type, Unset):
        json_library_content_type = library_content_type.value

    params["libraryContentType"] = json_library_content_type

    params["isNewLibrary"] = is_new_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Libraries/AvailableOptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LibraryOptionsResultDto | None:
    if response.status_code == 200:
        response_200 = LibraryOptionsResultDto.from_dict(response.json())

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
) -> Response[Any | LibraryOptionsResultDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    library_content_type: CollectionType | Unset = UNSET,
    is_new_library: bool | Unset = False,
) -> Response[Any | LibraryOptionsResultDto]:
    """Gets the library options info.

    Args:
        library_content_type (CollectionType | Unset): Collection type.
        is_new_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LibraryOptionsResultDto]
    """

    kwargs = _get_kwargs(
        library_content_type=library_content_type,
        is_new_library=is_new_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    library_content_type: CollectionType | Unset = UNSET,
    is_new_library: bool | Unset = False,
) -> Any | LibraryOptionsResultDto | None:
    """Gets the library options info.

    Args:
        library_content_type (CollectionType | Unset): Collection type.
        is_new_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LibraryOptionsResultDto
    """

    return sync_detailed(
        client=client,
        library_content_type=library_content_type,
        is_new_library=is_new_library,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    library_content_type: CollectionType | Unset = UNSET,
    is_new_library: bool | Unset = False,
) -> Response[Any | LibraryOptionsResultDto]:
    """Gets the library options info.

    Args:
        library_content_type (CollectionType | Unset): Collection type.
        is_new_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LibraryOptionsResultDto]
    """

    kwargs = _get_kwargs(
        library_content_type=library_content_type,
        is_new_library=is_new_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    library_content_type: CollectionType | Unset = UNSET,
    is_new_library: bool | Unset = False,
) -> Any | LibraryOptionsResultDto | None:
    """Gets the library options info.

    Args:
        library_content_type (CollectionType | Unset): Collection type.
        is_new_library (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LibraryOptionsResultDto
    """

    return (
        await asyncio_detailed(
            client=client,
            library_content_type=library_content_type,
            is_new_library=is_new_library,
        )
    ).parsed
