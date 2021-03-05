from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.pipeline_invocation import PipelineInvocation
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PipelineInvocation,
) -> Dict[str, Any]:
    url = "{}/api/v1/pipeline-invocations/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: PipelineInvocation,
) -> Response[PipelineInvocation]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PipelineInvocation,
) -> Optional[PipelineInvocation]:
    """ An PipelineInvocation -- something that gets deployed and which Caltech people use via the web. """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PipelineInvocation,
) -> Response[PipelineInvocation]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PipelineInvocation,
) -> Optional[PipelineInvocation]:
    """ An PipelineInvocation -- something that gets deployed and which Caltech people use via the web. """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
        )
    ).parsed
