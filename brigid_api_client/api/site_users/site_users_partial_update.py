from typing import Any, Dict, Optional

import httpx
from attr import asdict

from ...client import AuthenticatedClient
from ...models.patched_site_user import PatchedSiteUser
from ...models.site_user import SiteUser
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    form_data: PatchedSiteUser,
    json_body: PatchedSiteUser,
) -> Dict[str, Any]:
    url = "{}/api/v1/site-users/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "data": asdict(form_data),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SiteUser]:
    if response.status_code == 200:
        response_200 = SiteUser.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SiteUser]:
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
    form_data: PatchedSiteUser,
    json_body: PatchedSiteUser,
) -> Response[SiteUser]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        form_data=form_data,
        json_body=json_body,
    )

    response = httpx.patch(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int,
    form_data: PatchedSiteUser,
    json_body: PatchedSiteUser,
) -> Optional[SiteUser]:
    """  """

    return sync_detailed(
        client=client,
        id=id,
        form_data=form_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    form_data: PatchedSiteUser,
    json_body: PatchedSiteUser,
) -> Response[SiteUser]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        form_data=form_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int,
    form_data: PatchedSiteUser,
    json_body: PatchedSiteUser,
) -> Optional[SiteUser]:
    """  """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            form_data=form_data,
            json_body=json_body,
        )
    ).parsed
