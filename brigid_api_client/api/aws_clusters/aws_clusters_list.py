from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.aws_clusters_list_expand import AwsClustersListExpand
from ...models.paginated_awsecs_cluster_list import PaginatedAWSECSClusterList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsClustersListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    service_name: Union[Unset, str] = UNSET,
    task_family: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/aws-clusters/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, AwsClustersListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "aws_account_name": aws_account_name,
        "expand": json_expand,
        "limit": limit,
        "name": name,
        "offset": offset,
        "service_name": service_name,
        "task_family": task_family,
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[PaginatedAWSECSClusterList]:
    if response.status_code == 200:
        response_200 = PaginatedAWSECSClusterList.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[PaginatedAWSECSClusterList]:
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
    expand: Union[Unset, AwsClustersListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    service_name: Union[Unset, str] = UNSET,
    task_family: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedAWSECSClusterList]:
    kwargs = _get_kwargs(
        client=client,
        aws_account_name=aws_account_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        service_name=service_name,
        task_family=task_family,
        vpc_name=vpc_name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsClustersListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    service_name: Union[Unset, str] = UNSET,
    task_family: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedAWSECSClusterList]:
    """ An AWS ECS Cluster. """

    return sync_detailed(
        client=client,
        aws_account_name=aws_account_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        service_name=service_name,
        task_family=task_family,
        vpc_name=vpc_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsClustersListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    service_name: Union[Unset, str] = UNSET,
    task_family: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Response[PaginatedAWSECSClusterList]:
    kwargs = _get_kwargs(
        client=client,
        aws_account_name=aws_account_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        service_name=service_name,
        task_family=task_family,
        vpc_name=vpc_name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsClustersListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    service_name: Union[Unset, str] = UNSET,
    task_family: Union[Unset, str] = UNSET,
    vpc_name: Union[Unset, str] = UNSET,
) -> Optional[PaginatedAWSECSClusterList]:
    """ An AWS ECS Cluster. """

    return (
        await asyncio_detailed(
            client=client,
            aws_account_name=aws_account_name,
            expand=expand,
            limit=limit,
            name=name,
            offset=offset,
            service_name=service_name,
            task_family=task_family,
            vpc_name=vpc_name,
        )
    ).parsed
