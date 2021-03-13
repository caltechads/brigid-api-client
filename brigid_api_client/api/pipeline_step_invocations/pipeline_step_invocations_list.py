from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_step_invocation_list import PaginatedStepInvocationList
from ...models.pipeline_step_invocations_list_expand import (
    PipelineStepInvocationsListExpand,
)
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "application_machine_name": "str",
    "application_name": "str",
    "invoker_fullname": "str",
    "invoker_username": "str",
    "pipeline_name": "str",
    "released_by_fullname": "str",
    "released_by_username": "str",
    "sha": "str",
    "version": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineStepInvocationsListExpand] = UNSET,
    invoker_fullname: Union[Unset, str] = UNSET,
    invoker_username: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    released_by_fullname: Union[Unset, str] = UNSET,
    released_by_username: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/pipeline-step-invocations/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, PipelineStepInvocationsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_machine_name": application_machine_name,
        "application_name": application_name,
        "expand": json_expand,
        "invoker_fullname": invoker_fullname,
        "invoker_username": invoker_username,
        "limit": limit,
        "offset": offset,
        "pipeline_name": pipeline_name,
        "released_by_fullname": released_by_fullname,
        "released_by_username": released_by_username,
        "sha": sha,
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
) -> Optional[PaginatedStepInvocationList]:
    if response.status_code == 200:
        response_200 = PaginatedStepInvocationList.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[PaginatedStepInvocationList]:
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
    expand: Union[Unset, PipelineStepInvocationsListExpand] = UNSET,
    invoker_fullname: Union[Unset, str] = UNSET,
    invoker_username: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    released_by_fullname: Union[Unset, str] = UNSET,
    released_by_username: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedStepInvocationList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        expand=expand,
        invoker_fullname=invoker_fullname,
        invoker_username=invoker_username,
        limit=limit,
        offset=offset,
        pipeline_name=pipeline_name,
        released_by_fullname=released_by_fullname,
        released_by_username=released_by_username,
        sha=sha,
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
    expand: Union[Unset, PipelineStepInvocationsListExpand] = UNSET,
    invoker_fullname: Union[Unset, str] = UNSET,
    invoker_username: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    released_by_fullname: Union[Unset, str] = UNSET,
    released_by_username: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedStepInvocationList]:
    """ An invocation of a Pipeline Step. """

    return sync_detailed(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        expand=expand,
        invoker_fullname=invoker_fullname,
        invoker_username=invoker_username,
        limit=limit,
        offset=offset,
        pipeline_name=pipeline_name,
        released_by_fullname=released_by_fullname,
        released_by_username=released_by_username,
        sha=sha,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineStepInvocationsListExpand] = UNSET,
    invoker_fullname: Union[Unset, str] = UNSET,
    invoker_username: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    released_by_fullname: Union[Unset, str] = UNSET,
    released_by_username: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[PaginatedStepInvocationList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        expand=expand,
        invoker_fullname=invoker_fullname,
        invoker_username=invoker_username,
        limit=limit,
        offset=offset,
        pipeline_name=pipeline_name,
        released_by_fullname=released_by_fullname,
        released_by_username=released_by_username,
        sha=sha,
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
    expand: Union[Unset, PipelineStepInvocationsListExpand] = UNSET,
    invoker_fullname: Union[Unset, str] = UNSET,
    invoker_username: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    released_by_fullname: Union[Unset, str] = UNSET,
    released_by_username: Union[Unset, str] = UNSET,
    sha: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Optional[PaginatedStepInvocationList]:
    """ An invocation of a Pipeline Step. """

    return (
        await asyncio_detailed(
            client=client,
            application_machine_name=application_machine_name,
            application_name=application_name,
            expand=expand,
            invoker_fullname=invoker_fullname,
            invoker_username=invoker_username,
            limit=limit,
            offset=offset,
            pipeline_name=pipeline_name,
            released_by_fullname=released_by_fullname,
            released_by_username=released_by_username,
            sha=sha,
            version=version,
        )
    ).parsed
