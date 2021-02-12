from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.team import Team
from ...models.teams_retrieve_expand import TeamsRetrieveExpand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, TeamsRetrieveExpand] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/teams/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()

    json_expand: Union[Unset, TeamsRetrieveExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {}
    if expand is not UNSET:
        params["expand"] = json_expand

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Team]:
    if response.status_code == 200:
        response_200 = Team.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Team]:
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
    expand: Union[Unset, TeamsRetrieveExpand] = UNSET,
) -> Response[Team]:
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
    expand: Union[Unset, TeamsRetrieveExpand] = UNSET,
) -> Optional[Team]:
    """Users belong to Teams, and Teams belong to Organizations.

    * `directory_name` is the exact name that Oracle HR has for the Team (if this team is a Caltech Department), while
    `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is pretty
    obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing
    * Teams have both a full name (\"Division of Biology and Biological Engineering\")  and an abbriviation (\"BBE\")."""

    return sync_detailed(
        client=client,
        id=id,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, TeamsRetrieveExpand] = UNSET,
) -> Response[Team]:
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
    expand: Union[Unset, TeamsRetrieveExpand] = UNSET,
) -> Optional[Team]:
    """Users belong to Teams, and Teams belong to Organizations.

    * `directory_name` is the exact name that Oracle HR has for the Team (if this team is a Caltech Department), while
    `friendly_name` is a name that someone set for that.  We have both because `directory_name` sometimes is pretty
    obscure.  Most of the time `directory_name` and `friendly_name` will be set to the same thing
    * Teams have both a full name (\"Division of Biology and Biological Engineering\")  and an abbriviation (\"BBE\")."""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            expand=expand,
        )
    ).parsed