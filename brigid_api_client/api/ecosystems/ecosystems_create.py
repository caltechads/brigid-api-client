from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.ecosystem import Ecosystem
from ...types import Response

LIST_FILTERS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: Ecosystem,
) -> Dict[str, Any]:
    url = "{}/api/v1/ecosystems/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "verify": False,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Ecosystem]:
    if response.status_code == 201:
        response_201 = Ecosystem.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Ecosystem]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: Ecosystem,
) -> Response[Ecosystem]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: Ecosystem,
) -> Optional[Ecosystem]:
    """ A collection of related applications. """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: Ecosystem,
) -> Response[Ecosystem]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: Ecosystem,
) -> Optional[Ecosystem]:
    """ A collection of related applications. """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
