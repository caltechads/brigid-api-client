from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.awsvpc import AWSVPC
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: AWSVPC,
) -> Dict[str, Any]:
    url = "{}/api/v1/aws-vpcs/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[AWSVPC]:
    if response.status_code == 201:
        response_201 = AWSVPC.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[AWSVPC]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AWSVPC,
) -> Response[AWSVPC]:
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
    json_body: AWSVPC,
) -> Optional[AWSVPC]:
    """ An AWS VPC -- the kind in which your VPCs exist. """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AWSVPC,
) -> Response[AWSVPC]:
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
    json_body: AWSVPC,
) -> Optional[AWSVPC]:
    """ An AWS VPC -- the kind in which your VPCs exist. """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
