from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_person_type_list import PaginatedPersonTypeList
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "name": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/person-types/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedPersonTypeList]:
    if response.status_code == 200:
        response_200 = PaginatedPersonTypeList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedPersonTypeList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedPersonTypeList]:
    kwargs = _get_kwargs(
        client=client,
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
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedPersonTypeList]:
    """ Users are tagged with Person Types. """

    return sync_detailed(
        client=client,
        limit=limit,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedPersonTypeList]:
    kwargs = _get_kwargs(
        client=client,
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
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedPersonTypeList]:
    """ Users are tagged with Person Types. """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            name=name,
            offset=offset,
        )
    ).parsed
