from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...models.remote_image_result import RemoteImageResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    type_: ImageType | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    provider_name: str | Unset = UNSET,
    include_all_languages: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["startIndex"] = start_index

    params["limit"] = limit

    params["providerName"] = provider_name

    params["includeAllLanguages"] = include_all_languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/{item_id}/RemoteImages".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | RemoteImageResult | None:
    if response.status_code == 200:
        response_200 = RemoteImageResult.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | RemoteImageResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    type_: ImageType | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    provider_name: str | Unset = UNSET,
    include_all_languages: bool | Unset = False,
) -> Response[Any | ProblemDetails | RemoteImageResult]:
    """Gets available remote images for an item.

    Args:
        item_id (UUID):
        type_ (ImageType | Unset): Enum ImageType.
        start_index (int | Unset):
        limit (int | Unset):
        provider_name (str | Unset):
        include_all_languages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | RemoteImageResult]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        type_=type_,
        start_index=start_index,
        limit=limit,
        provider_name=provider_name,
        include_all_languages=include_all_languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    type_: ImageType | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    provider_name: str | Unset = UNSET,
    include_all_languages: bool | Unset = False,
) -> Any | ProblemDetails | RemoteImageResult | None:
    """Gets available remote images for an item.

    Args:
        item_id (UUID):
        type_ (ImageType | Unset): Enum ImageType.
        start_index (int | Unset):
        limit (int | Unset):
        provider_name (str | Unset):
        include_all_languages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | RemoteImageResult
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        type_=type_,
        start_index=start_index,
        limit=limit,
        provider_name=provider_name,
        include_all_languages=include_all_languages,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    type_: ImageType | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    provider_name: str | Unset = UNSET,
    include_all_languages: bool | Unset = False,
) -> Response[Any | ProblemDetails | RemoteImageResult]:
    """Gets available remote images for an item.

    Args:
        item_id (UUID):
        type_ (ImageType | Unset): Enum ImageType.
        start_index (int | Unset):
        limit (int | Unset):
        provider_name (str | Unset):
        include_all_languages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | RemoteImageResult]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        type_=type_,
        start_index=start_index,
        limit=limit,
        provider_name=provider_name,
        include_all_languages=include_all_languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    type_: ImageType | Unset = UNSET,
    start_index: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    provider_name: str | Unset = UNSET,
    include_all_languages: bool | Unset = False,
) -> Any | ProblemDetails | RemoteImageResult | None:
    """Gets available remote images for an item.

    Args:
        item_id (UUID):
        type_ (ImageType | Unset): Enum ImageType.
        start_index (int | Unset):
        limit (int | Unset):
        provider_name (str | Unset):
        include_all_languages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | RemoteImageResult
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            type_=type_,
            start_index=start_index,
            limit=limit,
            provider_name=provider_name,
            include_all_languages=include_all_languages,
        )
    ).parsed
