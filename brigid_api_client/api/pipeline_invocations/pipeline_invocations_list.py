from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_pipeline_invocation_list import PaginatedPipelineInvocationList
from ...models.pipeline_invocations_list_expand import PipelineInvocationsListExpand
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "application_machine_name": "str",
    "application_name": "str",
    "aws_account_name": "str",
    "fullname": "str",
    "pipeline_name": "str",
    "sha": "str",
    "username": "str",
    "version": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineInvocationsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/pipeline-invocations/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, PipelineInvocationsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_machine_name": application_machine_name,
        "application_name": application_name,
        "aws_account_name": aws_account_name,
        "expand": json_expand,
        "fullname": fullname,
        "limit": limit,
        "offset": offset,
        "pipeline_name": pipeline_name,
        "sha": sha,
        "username": username,
        "version": version,
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
) -> Optional[PaginatedPipelineInvocationList]:
    if response.status_code == 200:
        response_200 = PaginatedPipelineInvocationList.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[PaginatedPipelineInvocationList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineInvocationsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedPipelineInvocationList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        aws_account_name=aws_account_name,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        pipeline_name=pipeline_name,
        sha=sha,
        username=username,
        version=version,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineInvocationsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedPipelineInvocationList]:
    """ An PipelineInvocation -- something that gets deployed and which Caltech people use via the web. """

    return sync_detailed(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        aws_account_name=aws_account_name,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        pipeline_name=pipeline_name,
        sha=sha,
        username=username,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineInvocationsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedPipelineInvocationList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        aws_account_name=aws_account_name,
        expand=expand,
        fullname=fullname,
        limit=limit,
        offset=offset,
        pipeline_name=pipeline_name,
        sha=sha,
        username=username,
        version=version,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    aws_account_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineInvocationsListExpand] = UNSET,
    fullname: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedPipelineInvocationList]:
    """ An PipelineInvocation -- something that gets deployed and which Caltech people use via the web. """

    return (
        await asyncio_detailed(
            client=client,
            application_machine_name=application_machine_name,
            application_name=application_name,
            aws_account_name=aws_account_name,
            expand=expand,
            fullname=fullname,
            limit=limit,
            offset=offset,
            pipeline_name=pipeline_name,
            sha=sha,
            username=username,
            version=version,
        )
    ).parsed
