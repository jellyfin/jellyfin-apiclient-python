from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.task_info import TaskInfo
from ...types import Response


def _get_kwargs(
    task_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ScheduledTasks/{task_id}".format(
            task_id=task_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | TaskInfo | None:
    if response.status_code == 200:
        response_200 = TaskInfo.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | TaskInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | TaskInfo]:
    """Get task by id.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | TaskInfo]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | TaskInfo | None:
    """Get task by id.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | TaskInfo
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | TaskInfo]:
    """Get task by id.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | TaskInfo]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | TaskInfo | None:
    """Get task by id.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | TaskInfo
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
        )
    ).parsed
