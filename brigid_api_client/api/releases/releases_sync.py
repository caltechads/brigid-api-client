from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.action_response import ActionResponse
from ...types import Response

LIST_FILTERS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Dict[str, Any]:
    url = "{}/api/v1/releases/{id}/sync/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "verify": False,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionResponse]:
    if response.status_code == 200:
        response_200 = ActionResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionResponse]:
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
) -> Response[ActionResponse]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Optional[ActionResponse]:
    """ Re-sync the data for this release from our upstream git provider. """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Response[ActionResponse]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Optional[ActionResponse]:
    """ Re-sync the data for this release from our upstream git provider. """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
