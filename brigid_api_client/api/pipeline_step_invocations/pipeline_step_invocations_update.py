from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.step_invocation import StepInvocation
from ...types import Response

LIST_FILTERS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: StepInvocation,
) -> Dict[str, Any]:
    url = "{}/api/v1/pipeline-step-invocations/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[StepInvocation]:
    if response.status_code == 200:
        response_200 = StepInvocation.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[StepInvocation]:
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
    json_body: StepInvocation,
) -> Response[StepInvocation]:
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
    json_body: StepInvocation,
) -> Optional[StepInvocation]:
    """ An invocation of a Pipeline Step. """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: StepInvocation,
) -> Response[StepInvocation]:
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
    json_body: StepInvocation,
) -> Optional[StepInvocation]:
    """ An invocation of a Pipeline Step. """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
        )
    ).parsed
