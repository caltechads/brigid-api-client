from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.applications_list_expand import ApplicationsListExpand
from ...models.paginated_application_list import PaginatedApplicationList
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "ecs_service_name": "str",
    "ecs_task_family": "str",
    "machine_name": "str",
    "name": "str",
    "owner_fullname": "str",
    "owner_username": "str",
    "team_abbr": "str",
    "team_name": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, ApplicationsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner_fullname: Union[Unset, str] = UNSET,
    owner_username: Union[Unset, str] = UNSET,
    team_abbr: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/applications/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, ApplicationsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "ecs_service_name": ecs_service_name,
        "ecs_task_family": ecs_task_family,
        "expand": json_expand,
        "limit": limit,
        "machine_name": machine_name,
        "name": name,
        "offset": offset,
        "owner_fullname": owner_fullname,
        "owner_username": owner_username,
        "team_abbr": team_abbr,
        "team_name": team_name,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedApplicationList]:
    if response.status_code == 200:
        response_200 = PaginatedApplicationList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedApplicationList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, ApplicationsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner_fullname: Union[Unset, str] = UNSET,
    owner_username: Union[Unset, str] = UNSET,
    team_abbr: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedApplicationList]:
    kwargs = _get_kwargs(
        client=client,
        ecs_service_name=ecs_service_name,
        ecs_task_family=ecs_task_family,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
        owner_fullname=owner_fullname,
        owner_username=owner_username,
        team_abbr=team_abbr,
        team_name=team_name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, ApplicationsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner_fullname: Union[Unset, str] = UNSET,
    owner_username: Union[Unset, str] = UNSET,
    team_abbr: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedApplicationList]:
    """ An Application -- something that gets deployed and which Caltech people use via the web. """

    return sync_detailed(
        client=client,
        ecs_service_name=ecs_service_name,
        ecs_task_family=ecs_task_family,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
        owner_fullname=owner_fullname,
        owner_username=owner_username,
        team_abbr=team_abbr,
        team_name=team_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, ApplicationsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner_fullname: Union[Unset, str] = UNSET,
    owner_username: Union[Unset, str] = UNSET,
    team_abbr: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedApplicationList]:
    kwargs = _get_kwargs(
        client=client,
        ecs_service_name=ecs_service_name,
        ecs_task_family=ecs_task_family,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
        owner_fullname=owner_fullname,
        owner_username=owner_username,
        team_abbr=team_abbr,
        team_name=team_name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ecs_service_name: Union[Unset, str] = UNSET,
    ecs_task_family: Union[Unset, str] = UNSET,
    expand: Union[Unset, ApplicationsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner_fullname: Union[Unset, str] = UNSET,
    owner_username: Union[Unset, str] = UNSET,
    team_abbr: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedApplicationList]:
    """ An Application -- something that gets deployed and which Caltech people use via the web. """

    return (
        await asyncio_detailed(
            client=client,
            ecs_service_name=ecs_service_name,
            ecs_task_family=ecs_task_family,
            expand=expand,
            limit=limit,
            machine_name=machine_name,
            name=name,
            offset=offset,
            owner_fullname=owner_fullname,
            owner_username=owner_username,
            team_abbr=team_abbr,
            team_name=team_name,
        )
    ).parsed
