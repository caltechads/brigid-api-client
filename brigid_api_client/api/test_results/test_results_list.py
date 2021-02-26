from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_test_result_list import PaginatedTestResultList
from ...models.test_results_list_expand import TestResultsListExpand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, TestResultsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/test-results/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, TestResultsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "expand": json_expand,
        "fullname": fullname,
        "limit": limit,
        "offset": offset,
        "sha": sha,
        "software_machine_name": software_machine_name,
        "software_name": software_name,
        "username": username,
        "version": version,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
        "verify": False,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedTestResultList]:
    if response.status_code == 200:
        response_200 = PaginatedTestResultList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedTestResultList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, TestResultsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedTestResultList]:
    kwargs = _get_kwargs(
        client=client,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        sha=sha,
        software_machine_name=software_machine_name,
        software_name=software_name,
        username=username,
        version=version,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, TestResultsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTestResultList]:
    """ An AWS ECS Cluster. """

    return sync_detailed(
        client=client,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        sha=sha,
        software_machine_name=software_machine_name,
        software_name=software_name,
        username=username,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, TestResultsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedTestResultList]:
    kwargs = _get_kwargs(
        client=client,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        sha=sha,
        software_machine_name=software_machine_name,
        software_name=software_name,
        username=username,
        version=version,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, TestResultsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTestResultList]:
    """ An AWS ECS Cluster. """

    return (
        await asyncio_detailed(
            client=client,
            expand=expand,
            fullname=fullname,
            limit=limit,
            offset=offset,
            sha=sha,
            software_machine_name=software_machine_name,
            software_name=software_name,
            username=username,
            version=version,
        )
    ).parsed
