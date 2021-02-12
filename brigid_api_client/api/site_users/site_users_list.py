from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_site_user_list import PaginatedSiteUserList
from ...models.site_users_list_expand import SiteUsersListExpand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    employee_number: Union[Unset, Optional[int]] = UNSET,
    expand: Union[Unset, SiteUsersListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_type: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/site-users/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    json_expand: Union[Unset, SiteUsersListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {}
    if employee_number is not UNSET:
        params["employee_number"] = employee_number
    if expand is not UNSET:
        params["expand"] = json_expand
    if fullname is not UNSET:
        params["fullname"] = fullname
    if limit is not UNSET:
        params["limit"] = limit
    if offset is not UNSET:
        params["offset"] = offset
    if person_type is not UNSET:
        params["person_type"] = person_type
    if team_name is not UNSET:
        params["team_name"] = team_name
    if username is not UNSET:
        params["username"] = username

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedSiteUserList]:
    if response.status_code == 200:
        response_200 = PaginatedSiteUserList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedSiteUserList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_number: Union[Unset, Optional[int]] = UNSET,
    expand: Union[Unset, SiteUsersListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_type: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[PaginatedSiteUserList]:
    kwargs = _get_kwargs(
        client=client,
        employee_number=employee_number,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        person_type=person_type,
        team_name=team_name,
        username=username,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_number: Union[Unset, Optional[int]] = UNSET,
    expand: Union[Unset, SiteUsersListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_type: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[PaginatedSiteUserList]:
    """  """

    return sync_detailed(
        client=client,
        employee_number=employee_number,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        person_type=person_type,
        team_name=team_name,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_number: Union[Unset, Optional[int]] = UNSET,
    expand: Union[Unset, SiteUsersListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_type: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[PaginatedSiteUserList]:
    kwargs = _get_kwargs(
        client=client,
        employee_number=employee_number,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        person_type=person_type,
        team_name=team_name,
        username=username,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_number: Union[Unset, Optional[int]] = UNSET,
    expand: Union[Unset, SiteUsersListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_type: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[PaginatedSiteUserList]:
    """  """

    return (
        await asyncio_detailed(
            client=client,
            employee_number=employee_number,
            expand=expand,
            fullname=fullname,
            limit=limit,
            offset=offset,
            person_type=person_type,
            team_name=team_name,
            username=username,
        )
    ).parsed
