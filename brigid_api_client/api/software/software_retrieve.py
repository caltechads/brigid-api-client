from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.software import Software
from ...models.software_retrieve_expand import SoftwareRetrieveExpand
from ...types import UNSET, Response, Unset

LIST_FILTERS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, SoftwareRetrieveExpand] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/software/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, SoftwareRetrieveExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "expand": json_expand,
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


def _parse_response(*, response: httpx.Response) -> Optional[Software]:
    if response.status_code == 200:
        response_200 = Software.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Software]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, SoftwareRetrieveExpand] = UNSET,
) -> Response[Software]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        expand=expand,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, SoftwareRetrieveExpand] = UNSET,
) -> Optional[Software]:
    """ A piece of software. """

    return sync_detailed(
        client=client,
        id=id,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, SoftwareRetrieveExpand] = UNSET,
) -> Response[Software]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        expand=expand,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, SoftwareRetrieveExpand] = UNSET,
) -> Optional[Software]:
    """ A piece of software. """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            expand=expand,
        )
    ).parsed
