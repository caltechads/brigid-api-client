from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.ecosystems_list_expand import EcosystemsListExpand
from ...models.paginated_ecosystem_list import PaginatedEcosystemList
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "application_machine_name": "str",
    "application_name": "str",
    "description": "str",
    "name": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcosystemsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/ecosystems/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, EcosystemsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_machine_name": application_machine_name,
        "application_name": application_name,
        "description": description,
        "expand": json_expand,
        "limit": limit,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedEcosystemList]:
    if response.status_code == 200:
        response_200 = PaginatedEcosystemList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedEcosystemList]:
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
    description: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcosystemsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedEcosystemList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        description=description,
        expand=expand,
        limit=limit,
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
    description: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcosystemsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedEcosystemList]:
    """ A collection of related applications. """

    return sync_detailed(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        description=description,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcosystemsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedEcosystemList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        description=description,
        expand=expand,
        limit=limit,
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
    description: Union[Unset, str] = UNSET,
    expand: Union[Unset, EcosystemsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedEcosystemList]:
    """ A collection of related applications. """

    return (
        await asyncio_detailed(
            client=client,
            application_machine_name=application_machine_name,
            application_name=application_name,
            description=description,
            expand=expand,
            limit=limit,
            name=name,
            offset=offset,
        )
    ).parsed
