from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.ecs_task_deploy import ECSTaskDeploy
from ...models.patched_ecs_task_deploy import PatchedECSTaskDeploy
from ...types import Response

LIST_FILTERS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PatchedECSTaskDeploy,
) -> Dict[str, Any]:
    url = "{}/api/v1/ecs-task-deploys/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[ECSTaskDeploy]:
    if response.status_code == 200:
        response_200 = ECSTaskDeploy.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ECSTaskDeploy]:
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
    json_body: PatchedECSTaskDeploy,
) -> Response[ECSTaskDeploy]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    response = httpx.patch(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PatchedECSTaskDeploy,
) -> Optional[ECSTaskDeploy]:
    """ An Deployment of an ECS Service. """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PatchedECSTaskDeploy,
) -> Response[ECSTaskDeploy]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int,
    json_body: PatchedECSTaskDeploy,
) -> Optional[ECSTaskDeploy]:
    """ An Deployment of an ECS Service. """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
        )
    ).parsed
