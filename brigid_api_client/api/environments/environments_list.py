from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.environments_list_expand import EnvironmentsListExpand
from ...models.paginated_environment_list import PaginatedEnvironmentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, EnvironmentsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/environments/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, EnvironmentsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_machine_name": application_machine_name,
        "application_name": application_name,
        "ecs_service_name": ecs_service_name,
        "ecs_task_family": ecs_task_family,
        "expand": json_expand,
        "limit": limit,
        "machine_name": machine_name,
        "name": name,
        "offset": offset,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedEnvironmentList]:
    if response.status_code == 200:
        response_200 = PaginatedEnvironmentList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedEnvironmentList]:
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
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, EnvironmentsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedEnvironmentList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        ecs_service_name=ecs_service_name,
        ecs_task_family=ecs_task_family,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
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
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, EnvironmentsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedEnvironmentList]:
    """ An Environment for an Application (e.g. \"test\", \"prod\") """

    return sync_detailed(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        ecs_service_name=ecs_service_name,
        ecs_task_family=ecs_task_family,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, EnvironmentsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedEnvironmentList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        ecs_service_name=ecs_service_name,
        ecs_task_family=ecs_task_family,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, EnvironmentsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedEnvironmentList]:
    """ An Environment for an Application (e.g. \"test\", \"prod\") """

    return (
        await asyncio_detailed(
            client=client,
            application_machine_name=application_machine_name,
            application_name=application_name,
            ecs_service_name=ecs_service_name,
            ecs_task_family=ecs_task_family,
            expand=expand,
            limit=limit,
            machine_name=machine_name,
            name=name,
            offset=offset,
        )
    ).parsed
