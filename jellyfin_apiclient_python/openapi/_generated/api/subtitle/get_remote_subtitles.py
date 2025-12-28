from http import HTTPStatus
from io import BytesIO
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    subtitle_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Providers/Subtitles/Subtitles/{subtitle_id}".format(
            subtitle_id=subtitle_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

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
) -> Response[Any | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subtitle_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | File]:
    """Gets the remote subtitles.

    Args:
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        subtitle_id=subtitle_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subtitle_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | File | None:
    """Gets the remote subtitles.

    Args:
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return sync_detailed(
        subtitle_id=subtitle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subtitle_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | File]:
    """Gets the remote subtitles.

    Args:
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        subtitle_id=subtitle_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subtitle_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | File | None:
    """Gets the remote subtitles.

    Args:
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return (
        await asyncio_detailed(
            subtitle_id=subtitle_id,
            client=client,
        )
    ).parsed
