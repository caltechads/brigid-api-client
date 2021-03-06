import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_release_list import PaginatedReleaseList
from ...models.releases_list_expand import ReleasesListExpand
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "fullname": "str",
    "released_after": "datetime.datetime",
    "released_before": "datetime.datetime",
    "software_machine_name": "str",
    "software_name": "str",
    "username": "str",
    "version": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, ReleasesListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    released_after: Union[Unset, Optional[datetime.datetime]] = UNSET,
    released_before: Union[Unset, Optional[datetime.datetime]] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/releases/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, ReleasesListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    json_released_after: Union[Unset, str] = UNSET
    if not isinstance(released_after, Unset):
        json_released_after = released_after.isoformat() if released_after else None

    json_released_before: Union[Unset, str] = UNSET
    if not isinstance(released_before, Unset):
        json_released_before = released_before.isoformat() if released_before else None

    params: Dict[str, Any] = {
        "expand": json_expand,
        "fullname": fullname,
        "limit": limit,
        "offset": offset,
        "released_after": json_released_after,
        "released_before": json_released_before,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedReleaseList]:
    if response.status_code == 200:
        response_200 = PaginatedReleaseList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedReleaseList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, ReleasesListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    released_after: Union[Unset, Optional[datetime.datetime]] = UNSET,
    released_before: Union[Unset, Optional[datetime.datetime]] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedReleaseList]:
    kwargs = _get_kwargs(
        client=client,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        released_after=released_after,
        released_before=released_before,
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
    expand: Union[Unset, ReleasesListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    released_after: Union[Unset, Optional[datetime.datetime]] = UNSET,
    released_before: Union[Unset, Optional[datetime.datetime]] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedReleaseList]:
    """ An AWS VPC -- the kind in which your VPCs exist. """

    return sync_detailed(
        client=client,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        released_after=released_after,
        released_before=released_before,
        software_machine_name=software_machine_name,
        software_name=software_name,
        username=username,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, ReleasesListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    released_after: Union[Unset, Optional[datetime.datetime]] = UNSET,
    released_before: Union[Unset, Optional[datetime.datetime]] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedReleaseList]:
    kwargs = _get_kwargs(
        client=client,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        released_after=released_after,
        released_before=released_before,
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
    expand: Union[Unset, ReleasesListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    released_after: Union[Unset, Optional[datetime.datetime]] = UNSET,
    released_before: Union[Unset, Optional[datetime.datetime]] = UNSET,
    software_machine_name: Union[Unset, str] = UNSET,
    software_name: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedReleaseList]:
    """ An AWS VPC -- the kind in which your VPCs exist. """

    return (
        await asyncio_detailed(
            client=client,
            expand=expand,
            fullname=fullname,
            limit=limit,
            offset=offset,
            released_after=released_after,
            released_before=released_before,
            software_machine_name=software_machine_name,
            software_name=software_name,
            username=username,
            version=version,
        )
    ).parsed
