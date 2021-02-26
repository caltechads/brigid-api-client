from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_software_list import PaginatedSoftwareList
from ...models.software_list_expand import SoftwareListExpand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    author_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, SoftwareListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/software/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, SoftwareListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "author_username": author_username,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedSoftwareList]:
    if response.status_code == 200:
        response_200 = PaginatedSoftwareList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedSoftwareList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    author_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, SoftwareListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedSoftwareList]:
    kwargs = _get_kwargs(
        client=client,
        author_username=author_username,
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
    author_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, SoftwareListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedSoftwareList]:
    """ A piece of software. """

    return sync_detailed(
        client=client,
        author_username=author_username,
        expand=expand,
        limit=limit,
        machine_name=machine_name,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    author_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, SoftwareListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedSoftwareList]:
    kwargs = _get_kwargs(
        client=client,
        author_username=author_username,
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
    author_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, SoftwareListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    machine_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedSoftwareList]:
    """ A piece of software. """

    return (
        await asyncio_detailed(
            client=client,
            author_username=author_username,
            expand=expand,
            limit=limit,
            machine_name=machine_name,
            name=name,
            offset=offset,
        )
    ).parsed
