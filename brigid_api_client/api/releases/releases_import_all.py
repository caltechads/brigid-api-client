from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.release_import_all import ReleaseImportAll
from ...models.release_import_all_response import ReleaseImportAllResponse
from ...types import Response

LIST_FILTERS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseImportAll,
) -> Dict[str, Any]:
    url = "{}/api/v1/releases/import_all/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ReleaseImportAllResponse]:
    if response.status_code == 200:
        response_200 = ReleaseImportAllResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ReleaseImportAllResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseImportAll,
) -> Response[ReleaseImportAllResponse]:
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
    json_body: ReleaseImportAll,
) -> Optional[ReleaseImportAllResponse]:
    """ Given a provider and a git repository identifier, create or update a Software object for that repo. """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseImportAll,
) -> Response[ReleaseImportAllResponse]:
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
    json_body: ReleaseImportAll,
) -> Optional[ReleaseImportAllResponse]:
    """ Given a provider and a git repository identifier, create or update a Software object for that repo. """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
