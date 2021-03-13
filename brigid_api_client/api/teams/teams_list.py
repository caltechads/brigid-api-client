from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_team_list import PaginatedTeamList
from ...models.teams_list_expand import TeamsListExpand
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "abbr": "str",
    "directory_name": "str",
    "friendly_name": "str",
    "organization_abbr": "str",
    "organization_directory_name": "str",
    "organization_friendly_name": "str",
    "organization_id": "int",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, TeamsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    organization_abbr: Union[Unset, Optional[str]] = UNSET,
    organization_directory_name: Union[Unset, str] = UNSET,
    organization_friendly_name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/teams/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, TeamsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "abbr": abbr,
        "directory_name": directory_name,
        "expand": json_expand,
        "friendly_name": friendly_name,
        "limit": limit,
        "offset": offset,
        "organization_abbr": organization_abbr,
        "organization_directory_name": organization_directory_name,
        "organization_friendly_name": organization_friendly_name,
        "organization_id": organization_id,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedTeamList]:
    if response.status_code == 200:
        response_200 = PaginatedTeamList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedTeamList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, TeamsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    organization_abbr: Union[Unset, Optional[str]] = UNSET,
    organization_directory_name: Union[Unset, str] = UNSET,
    organization_friendly_name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, int] = UNSET,
) -> Response[PaginatedTeamList]:
    kwargs = _get_kwargs(
        client=client,
        abbr=abbr,
        directory_name=directory_name,
        expand=expand,
        friendly_name=friendly_name,
        limit=limit,
        offset=offset,
        organization_abbr=organization_abbr,
        organization_directory_name=organization_directory_name,
        organization_friendly_name=organization_friendly_name,
        organization_id=organization_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, TeamsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    organization_abbr: Union[Unset, Optional[str]] = UNSET,
    organization_directory_name: Union[Unset, str] = UNSET,
    organization_friendly_name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, int] = UNSET,
) -> Optional[PaginatedTeamList]:
    """Users belong to Teams, and Teams belong to Organizations.

    * `directory_name` is the exact name that Oracle HR has for the Team (if this team is a Caltech Department), while
    `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is pretty
    obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing
    * Teams have both a full name (\"Division of Biology and Biological Engineering\")  and an abbriviation (\"BBE\")."""

    return sync_detailed(
        client=client,
        abbr=abbr,
        directory_name=directory_name,
        expand=expand,
        friendly_name=friendly_name,
        limit=limit,
        offset=offset,
        organization_abbr=organization_abbr,
        organization_directory_name=organization_directory_name,
        organization_friendly_name=organization_friendly_name,
        organization_id=organization_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, TeamsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    organization_abbr: Union[Unset, Optional[str]] = UNSET,
    organization_directory_name: Union[Unset, str] = UNSET,
    organization_friendly_name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, int] = UNSET,
) -> Response[PaginatedTeamList]:
    kwargs = _get_kwargs(
        client=client,
        abbr=abbr,
        directory_name=directory_name,
        expand=expand,
        friendly_name=friendly_name,
        limit=limit,
        offset=offset,
        organization_abbr=organization_abbr,
        organization_directory_name=organization_directory_name,
        organization_friendly_name=organization_friendly_name,
        organization_id=organization_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, TeamsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    organization_abbr: Union[Unset, Optional[str]] = UNSET,
    organization_directory_name: Union[Unset, str] = UNSET,
    organization_friendly_name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, int] = UNSET,
) -> Optional[PaginatedTeamList]:
    """Users belong to Teams, and Teams belong to Organizations.

    * `directory_name` is the exact name that Oracle HR has for the Team (if this team is a Caltech Department), while
    `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is pretty
    obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing
    * Teams have both a full name (\"Division of Biology and Biological Engineering\")  and an abbriviation (\"BBE\")."""

    return (
        await asyncio_detailed(
            client=client,
            abbr=abbr,
            directory_name=directory_name,
            expand=expand,
            friendly_name=friendly_name,
            limit=limit,
            offset=offset,
            organization_abbr=organization_abbr,
            organization_directory_name=organization_directory_name,
            organization_friendly_name=organization_friendly_name,
            organization_id=organization_id,
        )
    ).parsed
