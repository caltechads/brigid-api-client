from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.aws_vpcs_list_expand import AwsVpcsListExpand
from ...models.paginated_awsvpc_list import PaginatedAWSVPCList
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "aws_account_name": "str",
    "contact_fullname": "str",
    "contact_username": "str",
    "ecs_cluster_name": "str",
    "name": "str",
    "team_name": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    ecs_cluster_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsVpcsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/aws-vpcs/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, AwsVpcsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "aws_account_name": aws_account_name,
        "contact_fullname": contact_fullname,
        "contact_username": contact_username,
        "ecs_cluster_name": ecs_cluster_name,
        "expand": json_expand,
        "limit": limit,
        "name": name,
        "offset": offset,
        "team_name": team_name,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedAWSVPCList]:
    if response.status_code == 200:
        response_200 = PaginatedAWSVPCList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedAWSVPCList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    ecs_cluster_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsVpcsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedAWSVPCList]:
    kwargs = _get_kwargs(
        client=client,
        aws_account_name=aws_account_name,
        contact_fullname=contact_fullname,
        contact_username=contact_username,
        ecs_cluster_name=ecs_cluster_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        team_name=team_name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    ecs_cluster_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsVpcsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedAWSVPCList]:
    """ An AWS VPC -- the kind in which your VPCs exist. """

    return sync_detailed(
        client=client,
        aws_account_name=aws_account_name,
        contact_fullname=contact_fullname,
        contact_username=contact_username,
        ecs_cluster_name=ecs_cluster_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        team_name=team_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    ecs_cluster_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsVpcsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedAWSVPCList]:
    kwargs = _get_kwargs(
        client=client,
        aws_account_name=aws_account_name,
        contact_fullname=contact_fullname,
        contact_username=contact_username,
        ecs_cluster_name=ecs_cluster_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        team_name=team_name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    contact_fullname: Union[Unset, str] = UNSET,
    contact_username: Union[Unset, str] = UNSET,
    ecs_cluster_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsVpcsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedAWSVPCList]:
    """ An AWS VPC -- the kind in which your VPCs exist. """

    return (
        await asyncio_detailed(
            client=client,
            aws_account_name=aws_account_name,
            contact_fullname=contact_fullname,
            contact_username=contact_username,
            ecs_cluster_name=ecs_cluster_name,
            expand=expand,
            limit=limit,
            name=name,
            offset=offset,
            team_name=team_name,
        )
    ).parsed
