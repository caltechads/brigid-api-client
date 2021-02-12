from typing import Any, Dict, Optional

import httpx
from attr import asdict

from ...client import AuthenticatedClient
from ...models.organization import Organization
from ...models.patched_organization import PatchedOrganization
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    form_data: PatchedOrganization,
    json_body: PatchedOrganization,
) -> Dict[str, Any]:
    url = "{}/api/v1/organizations/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Organization]:
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Organization]:
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
    form_data: PatchedOrganization,
    json_body: PatchedOrganization,
) -> Response[Organization]:
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
    form_data: PatchedOrganization,
    json_body: PatchedOrganization,
) -> Optional[Organization]:
    """Organizations own Teams.

    * `directory_name` is the exact name that Oracle HR has for the Organization if the org is a Caltech organization,
       while `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is
       pretty obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing.
    * Organizations have both a full name (\"Division of Biology and Biological Engineering\")  and an
      abbriviation (\"BBE\")."""

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
    form_data: PatchedOrganization,
    json_body: PatchedOrganization,
) -> Response[Organization]:
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
    form_data: PatchedOrganization,
    json_body: PatchedOrganization,
) -> Optional[Organization]:
    """Organizations own Teams.

    * `directory_name` is the exact name that Oracle HR has for the Organization if the org is a Caltech organization,
       while `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is
       pretty obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing.
    * Organizations have both a full name (\"Division of Biology and Biological Engineering\")  and an
      abbriviation (\"BBE\")."""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            form_data=form_data,
            json_body=json_body,
        )
    ).parsed
