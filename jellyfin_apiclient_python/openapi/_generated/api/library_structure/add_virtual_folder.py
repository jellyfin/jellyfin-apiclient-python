from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_virtual_folder_dto import AddVirtualFolderDto
from ...models.collection_type_options import CollectionTypeOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AddVirtualFolderDto | AddVirtualFolderDto,
    name: str | Unset = UNSET,
    collection_type: CollectionTypeOptions | Unset = UNSET,
    paths: list[str] | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    json_collection_type: str | Unset = UNSET
    if not isinstance(collection_type, Unset):
        json_collection_type = collection_type.value

    params["collectionType"] = json_collection_type

    json_paths: list[str] | Unset = UNSET
    if not isinstance(paths, Unset):
        json_paths = paths

    params["paths"] = json_paths

    params["refreshLibrary"] = refresh_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Library/VirtualFolders",
        "params": params,
    }

    if isinstance(body, AddVirtualFolderDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AddVirtualFolderDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: AddVirtualFolderDto | AddVirtualFolderDto,
    name: str | Unset = UNSET,
    collection_type: CollectionTypeOptions | Unset = UNSET,
    paths: list[str] | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> Response[Any]:
    """Adds a virtual folder.

    Args:
        name (str | Unset):
        collection_type (CollectionTypeOptions | Unset): The collection type options.
        paths (list[str] | Unset):
        refresh_library (bool | Unset):  Default: False.
        body (AddVirtualFolderDto): Add virtual folder dto.
        body (AddVirtualFolderDto): Add virtual folder dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        collection_type=collection_type,
        paths=paths,
        refresh_library=refresh_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AddVirtualFolderDto | AddVirtualFolderDto,
    name: str | Unset = UNSET,
    collection_type: CollectionTypeOptions | Unset = UNSET,
    paths: list[str] | Unset = UNSET,
    refresh_library: bool | Unset = False,
) -> Response[Any]:
    """Adds a virtual folder.

    Args:
        name (str | Unset):
        collection_type (CollectionTypeOptions | Unset): The collection type options.
        paths (list[str] | Unset):
        refresh_library (bool | Unset):  Default: False.
        body (AddVirtualFolderDto): Add virtual folder dto.
        body (AddVirtualFolderDto): Add virtual folder dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        collection_type=collection_type,
        paths=paths,
        refresh_library=refresh_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
