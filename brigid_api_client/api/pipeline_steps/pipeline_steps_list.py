from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_step_list import PaginatedStepList
from ...models.pipeline_steps_list_expand import PipelineStepsListExpand
from ...types import UNSET, Response, Unset

LIST_FILTERS = {
    "application_machine_name": "str",
    "application_name": "str",
    "name": "str",
    "pipeline_name": "str",
    "step_type": "str",
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineStepsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    step_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/pipeline-steps/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, PipelineStepsListExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "application_machine_name": application_machine_name,
        "application_name": application_name,
        "expand": json_expand,
        "limit": limit,
        "name": name,
        "offset": offset,
        "pipeline_name": pipeline_name,
        "step_type": step_type,
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedStepList]:
    if response.status_code == 200:
        response_200 = PaginatedStepList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedStepList]:
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
    expand: Union[Unset, PipelineStepsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    step_type: Union[Unset, str] = UNSET,
) -> Response[PaginatedStepList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        pipeline_name=pipeline_name,
        step_type=step_type,
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
    expand: Union[Unset, PipelineStepsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    step_type: Union[Unset, str] = UNSET,
) -> Optional[PaginatedStepList]:
    """ An Pipeline Step -- a discrete action that is part of a Pipeline. """

    return sync_detailed(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        pipeline_name=pipeline_name,
        step_type=step_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineStepsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    step_type: Union[Unset, str] = UNSET,
) -> Response[PaginatedStepList]:
    kwargs = _get_kwargs(
        client=client,
        application_machine_name=application_machine_name,
        application_name=application_name,
        expand=expand,
        limit=limit,
        name=name,
        offset=offset,
        pipeline_name=pipeline_name,
        step_type=step_type,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_machine_name: Union[Unset, str] = UNSET,
    application_name: Union[Unset, str] = UNSET,
    expand: Union[Unset, PipelineStepsListExpand] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pipeline_name: Union[Unset, str] = UNSET,
    step_type: Union[Unset, str] = UNSET,
) -> Optional[PaginatedStepList]:
    """ An Pipeline Step -- a discrete action that is part of a Pipeline. """

    return (
        await asyncio_detailed(
            client=client,
            application_machine_name=application_machine_name,
            application_name=application_name,
            expand=expand,
            limit=limit,
            name=name,
            offset=offset,
            pipeline_name=pipeline_name,
            step_type=step_type,
        )
    ).parsed
