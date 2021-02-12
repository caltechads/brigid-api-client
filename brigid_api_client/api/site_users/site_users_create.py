from typing import Any, Dict, Optional

import httpx
from attr import asdict

from ...client import AuthenticatedClient
from ...models.site_user import SiteUser
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: SiteUser,
    json_body: SiteUser,
) -> Dict[str, Any]:
    url = "{}/api/v1/site-users/".format(client.base_url)

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
    if response.status_code == 201:
        response_201 = SiteUser.from_dict(response.json())

        return response_201
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
    form_data: SiteUser,
    json_body: SiteUser,
) -> Response[SiteUser]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: SiteUser,
    json_body: SiteUser,
) -> Optional[SiteUser]:
    """  """

    return sync_detailed(
        client=client,
        form_data=form_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: SiteUser,
    json_body: SiteUser,
) -> Response[SiteUser]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: SiteUser,
    json_body: SiteUser,
) -> Optional[SiteUser]:
    """  """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            json_body=json_body,
        )
    ).parsed
