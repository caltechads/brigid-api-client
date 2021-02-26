from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.aws_services_list_expand import AwsServicesListExpand
from ...models.paginated_awsecs_service_list import PaginatedAWSECSServiceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_name: Union[Unset, str] = UNSET,
    cluster_name: Union[Unset, str] = UNSET,
    environment: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsServicesListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/aws-services/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, AwsServicesListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_name": application_name,
        "cluster_name": cluster_name,
        "environment": environment,
        "expand": json_expand,
        "limit": limit,
        "name": name,
        "offset": offset,
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
) -> Optional[PaginatedAWSECSServiceList]:
    if response.status_code == 200:
        response_200 = PaginatedAWSECSServiceList.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[PaginatedAWSECSServiceList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    application_name: Union[Unset, str] = UNSET,
    cluster_name: Union[Unset, str] = UNSET,
    environment: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsServicesListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedAWSECSServiceList]:
    kwargs = _get_kwargs(
        client=client,
        application_name=application_name,
        cluster_name=cluster_name,
        environment=environment,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    application_name: Union[Unset, str] = UNSET,
    cluster_name: Union[Unset, str] = UNSET,
    environment: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsServicesListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedAWSECSServiceList]:
    """ An AWS ECS Cluster. """

    return sync_detailed(
        client=client,
        application_name=application_name,
        cluster_name=cluster_name,
        environment=environment,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_name: Union[Unset, str] = UNSET,
    cluster_name: Union[Unset, str] = UNSET,
    environment: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsServicesListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[PaginatedAWSECSServiceList]:
    kwargs = _get_kwargs(
        client=client,
        application_name=application_name,
        cluster_name=cluster_name,
        environment=environment,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_name: Union[Unset, str] = UNSET,
    cluster_name: Union[Unset, str] = UNSET,
    environment: Union[Unset, str] = UNSET,
    expand: Union[Unset, AwsServicesListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[PaginatedAWSECSServiceList]:
    """ An AWS ECS Cluster. """

    return (
        await asyncio_detailed(
            client=client,
            application_name=application_name,
            cluster_name=cluster_name,
            environment=environment,
            expand=expand,
            limit=limit,
            name=name,
            offset=offset,
        )
    ).parsed
