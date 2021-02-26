from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.aws_accounts_list_expand import AwsAccountsListExpand
from ...models.paginated_aws_account_list import PaginatedAWSAccountList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsAccountsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/aws-accounts/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, AwsAccountsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "contact_fullname": contact_fullname,
        "contact_username": contact_username,
        "expand": json_expand,
        "limit": limit,
        "name": name,
        "offset": offset,
        "team_name": team_name,
        "vpc_name": vpc_name,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedAWSAccountList]:
    if response.status_code == 200:
        response_200 = PaginatedAWSAccountList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedAWSAccountList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsAccountsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedAWSAccountList]:
    kwargs = _get_kwargs(
        client=client,
        contact_fullname=contact_fullname,
        contact_username=contact_username,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        team_name=team_name,
        vpc_name=vpc_name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsAccountsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedAWSAccountList]:
    """ An AWS Account. """

    return sync_detailed(
        client=client,
        contact_fullname=contact_fullname,
        contact_username=contact_username,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        team_name=team_name,
        vpc_name=vpc_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsAccountsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedAWSAccountList]:
    kwargs = _get_kwargs(
        client=client,
        contact_fullname=contact_fullname,
        contact_username=contact_username,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        team_name=team_name,
        vpc_name=vpc_name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsAccountsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedAWSAccountList]:
    """ An AWS Account. """

    return (
        await asyncio_detailed(
            client=client,
            contact_fullname=contact_fullname,
            contact_username=contact_username,
            expand=expand,
            limit=limit,
            name=name,
            offset=offset,
            team_name=team_name,
            vpc_name=vpc_name,
        )
    ).parsed
