from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.action_response import ActionResponse
from ...models.software_import import SoftwareImport
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SoftwareImport,
) -> Dict[str, Any]:
    url = "{}/api/v1/software/import/".format(client.base_url)

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
    json_body: SoftwareImport,
) -> Response[ActionResponse]:
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
    json_body: SoftwareImport,
) -> Optional[ActionResponse]:
    """ Given a provider and a git repository identifier, create or update a Software object for that repo. """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SoftwareImport,
) -> Response[ActionResponse]:
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
    json_body: SoftwareImport,
) -> Optional[ActionResponse]:
    """ Given a provider and a git repository identifier, create or update a Software object for that repo. """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
