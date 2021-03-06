from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.docker_image_builds_list_expand import DockerImageBuildsListExpand
from ...models.paginated_docker_image_build_list import PaginatedDockerImageBuildList
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "fullname": "str",
    "sha": "str",
    "software_machine_name": "str",
    "software_name": "str",
    "username": "str",
    "version": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, DockerImageBuildsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/docker-image-builds/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, DockerImageBuildsListExpand] = UNSET
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[PaginatedDockerImageBuildList]:
    if response.status_code == 200:
        response_200 = PaginatedDockerImageBuildList.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[PaginatedDockerImageBuildList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, DockerImageBuildsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedDockerImageBuildList]:
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
    expand: Union[Unset, DockerImageBuildsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDockerImageBuildList]:
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
    expand: Union[Unset, DockerImageBuildsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedDockerImageBuildList]:
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
    expand: Union[Unset, DockerImageBuildsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDockerImageBuildList]:
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
