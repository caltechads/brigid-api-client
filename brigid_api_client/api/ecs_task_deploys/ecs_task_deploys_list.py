from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.ecs_task_deploys_list_expand import EcsTaskDeploysListExpand
from ...models.paginated_ecs_task_deploy_list import PaginatedECSTaskDeployList
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "application_machine_name": "str",
    "application_name": "str",
    "ecs_task_family": "str",
    "environment_machine_name": "str",
    "environment_name": "str",
    "fullname": "str",
    "sha": "str",
    "username": "str",
    "version": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    environment_machine_name: Union[Unset, str] = UNSET,
    environment_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcsTaskDeploysListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/ecs-task-deploys/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, EcsTaskDeploysListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_machine_name": application_machine_name,
        "application_name": application_name,
        "ecs_task_family": ecs_task_family,
        "environment_machine_name": environment_machine_name,
        "environment_name": environment_name,
        "expand": json_expand,
        "fullname": fullname,
        "limit": limit,
        "offset": offset,
        "sha": sha,
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
) -> Optional[PaginatedECSTaskDeployList]:
    if response.status_code == 200:
        response_200 = PaginatedECSTaskDeployList.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[PaginatedECSTaskDeployList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    environment_machine_name: Union[Unset, str] = UNSET,
    environment_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcsTaskDeploysListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedECSTaskDeployList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        ecs_task_family=ecs_task_family,
        environment_machine_name=environment_machine_name,
        environment_name=environment_name,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        sha=sha,
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
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    environment_machine_name: Union[Unset, str] = UNSET,
    environment_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcsTaskDeploysListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedECSTaskDeployList]:
    """ An Deployment of an ECS Service. """

    return sync_detailed(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        ecs_task_family=ecs_task_family,
        environment_machine_name=environment_machine_name,
        environment_name=environment_name,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        sha=sha,
        username=username,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    environment_machine_name: Union[Unset, str] = UNSET,
    environment_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcsTaskDeploysListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedECSTaskDeployList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        ecs_task_family=ecs_task_family,
        environment_machine_name=environment_machine_name,
        environment_name=environment_name,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        sha=sha,
        username=username,
        version=version,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    environment_machine_name: Union[Unset, str] = UNSET,
    environment_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcsTaskDeploysListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedECSTaskDeployList]:
    """ An Deployment of an ECS Service. """

    return (
        await asyncio_detailed(
            client=client,
            application_machine_name=application_machine_name,
            application_name=application_name,
            ecs_task_family=ecs_task_family,
            environment_machine_name=environment_machine_name,
            environment_name=environment_name,
            expand=expand,
            fullname=fullname,
            limit=limit,
            offset=offset,
            sha=sha,
            username=username,
            version=version,
        )
    ).parsed
