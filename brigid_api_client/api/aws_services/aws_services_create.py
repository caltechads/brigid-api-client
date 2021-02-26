from typing import Any, Dict, Optional

import httpx
from attr import asdict

from ...client import AuthenticatedClient
from ...models.awsecs_service import AWSECSService
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: AWSECSService,
    json_body: AWSECSService,
) -> Dict[str, Any]:
    url = "{}/api/v1/aws-services/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": asdict(form_data),
        "json": json_json_body,
        "verify": False,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AWSECSService]:
    if response.status_code == 201:
        response_201 = AWSECSService.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[AWSECSService]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AWSECSService,
    json_body: AWSECSService,
) -> Response[AWSECSService]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: AWSECSService,
    json_body: AWSECSService,
) -> Optional[AWSECSService]:
    """ An AWS ECS Cluster. """

    return sync_detailed(
        client=client,
        form_data=form_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AWSECSService,
    json_body: AWSECSService,
) -> Response[AWSECSService]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: AWSECSService,
    json_body: AWSECSService,
) -> Optional[AWSECSService]:
    """ An AWS ECS Cluster. """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            json_body=json_body,
        )
    ).parsed
