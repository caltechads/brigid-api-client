from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.pipeline_invocation import PipelineInvocation
from ...models.pipeline_invocations_retrieve_expand import (
    PipelineInvocationsRetrieveExpand,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, PipelineInvocationsRetrieveExpand] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/pipeline-invocations/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_expand: Union[Unset, PipelineInvocationsRetrieveExpand] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params: Dict[str, Any] = {
        "expand": json_expand,
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


def _parse_response(*, response: httpx.Response) -> Optional[PipelineInvocation]:
    if response.status_code == 200:
        response_200 = PipelineInvocation.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PipelineInvocation]:
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
    expand: Union[Unset, PipelineInvocationsRetrieveExpand] = UNSET,
) -> Response[PipelineInvocation]:
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
    expand: Union[Unset, PipelineInvocationsRetrieveExpand] = UNSET,
) -> Optional[PipelineInvocation]:
    """ An PipelineInvocation -- something that gets deployed and which Caltech people use via the web. """

    return sync_detailed(
        client=client,
        id=id,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    expand: Union[Unset, PipelineInvocationsRetrieveExpand] = UNSET,
) -> Response[PipelineInvocation]:
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
    expand: Union[Unset, PipelineInvocationsRetrieveExpand] = UNSET,
) -> Optional[PipelineInvocation]:
    """ An PipelineInvocation -- something that gets deployed and which Caltech people use via the web. """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            expand=expand,
        )
    ).parsed
