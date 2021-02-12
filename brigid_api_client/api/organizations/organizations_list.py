from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.organizations_list_expand import OrganizationsListExpand
from ...models.paginated_organization_list import PaginatedOrganizationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, OrganizationsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/organizations/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    json_expand: Union[Unset, OrganizationsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {}
    if abbr is not UNSET:
        params["abbr"] = abbr
    if directory_name is not UNSET:
        params["directory_name"] = directory_name
    if expand is not UNSET:
        params["expand"] = json_expand
    if friendly_name is not UNSET:
        params["friendly_name"] = friendly_name
    if limit is not UNSET:
        params["limit"] = limit
    if offset is not UNSET:
        params["offset"] = offset

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedOrganizationList]:
    if response.status_code == 200:
        response_200 = PaginatedOrganizationList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedOrganizationList]:
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
    expand: Union[Unset, OrganizationsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedOrganizationList]:
    kwargs = _get_kwargs(
        client=client,
        abbr=abbr,
        directory_name=directory_name,
        expand=expand,
        friendly_name=friendly_name,
        limit=limit,
        offset=offset,
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
    expand: Union[Unset, OrganizationsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedOrganizationList]:
    """Organizations own Teams.

    * `directory_name` is the exact name that Oracle HR has for the Organization if the org is a Caltech organization,
       while `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is
       pretty obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing.
    * Organizations have both a full name (\"Division of Biology and Biological Engineering\")  and an
      abbriviation (\"BBE\")."""

    return sync_detailed(
        client=client,
        abbr=abbr,
        directory_name=directory_name,
        expand=expand,
        friendly_name=friendly_name,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, OrganizationsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedOrganizationList]:
    kwargs = _get_kwargs(
        client=client,
        abbr=abbr,
        directory_name=directory_name,
        expand=expand,
        friendly_name=friendly_name,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    abbr: Union[Unset, Optional[str]] = UNSET,
    directory_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, OrganizationsListExpand] = UNSET,
    friendly_name: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedOrganizationList]:
    """Organizations own Teams.

    * `directory_name` is the exact name that Oracle HR has for the Organization if the org is a Caltech organization,
       while `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is
       pretty obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing.
    * Organizations have both a full name (\"Division of Biology and Biological Engineering\")  and an
      abbriviation (\"BBE\")."""

    return (
        await asyncio_detailed(
            client=client,
            abbr=abbr,
            directory_name=directory_name,
            expand=expand,
            friendly_name=friendly_name,
            limit=limit,
            offset=offset,
        )
    ).parsed
