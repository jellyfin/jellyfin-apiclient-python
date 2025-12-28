from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_manifest_dto import BackupManifestDto
from ...models.backup_options_dto import BackupOptionsDto
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: BackupOptionsDto | BackupOptionsDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Backup/Create",
    }

    if isinstance(body, BackupOptionsDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BackupOptionsDto):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BackupManifestDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BackupManifestDto.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

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
) -> Response[Any | BackupManifestDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BackupOptionsDto | BackupOptionsDto,
) -> Response[Any | BackupManifestDto | ProblemDetails]:
    """Creates a new Backup.

    Args:
        body (BackupOptionsDto): Defines the optional contents of the backup archive.
        body (BackupOptionsDto): Defines the optional contents of the backup archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BackupManifestDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BackupOptionsDto | BackupOptionsDto,
) -> Any | BackupManifestDto | ProblemDetails | None:
    """Creates a new Backup.

    Args:
        body (BackupOptionsDto): Defines the optional contents of the backup archive.
        body (BackupOptionsDto): Defines the optional contents of the backup archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BackupManifestDto | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BackupOptionsDto | BackupOptionsDto,
) -> Response[Any | BackupManifestDto | ProblemDetails]:
    """Creates a new Backup.

    Args:
        body (BackupOptionsDto): Defines the optional contents of the backup archive.
        body (BackupOptionsDto): Defines the optional contents of the backup archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BackupManifestDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BackupOptionsDto | BackupOptionsDto,
) -> Any | BackupManifestDto | ProblemDetails | None:
    """Creates a new Backup.

    Args:
        body (BackupOptionsDto): Defines the optional contents of the backup archive.
        body (BackupOptionsDto): Defines the optional contents of the backup archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BackupManifestDto | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
