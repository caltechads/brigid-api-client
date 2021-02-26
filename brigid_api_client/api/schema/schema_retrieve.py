from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.schema_retrieve_format import SchemaRetrieveFormat
from ...models.schema_retrieve_response_200 import SchemaRetrieveResponse_200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format: Union[Unset, SchemaRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/schema/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_format: Union[Unset, SchemaRetrieveFormat] = UNSET
    if not isinstance(format, Unset):
        json_format = format

    params: Dict[str, Any] = {
        "format": json_format,
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
) -> Optional[SchemaRetrieveResponse_200]:
    if response.status_code == 200:
        response_200 = SchemaRetrieveResponse_200.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[SchemaRetrieveResponse_200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format: Union[Unset, SchemaRetrieveFormat] = UNSET,
) -> Response[SchemaRetrieveResponse_200]:
    kwargs = _get_kwargs(
        client=client,
        format=format,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format: Union[Unset, SchemaRetrieveFormat] = UNSET,
) -> Optional[SchemaRetrieveResponse_200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json"""

    return sync_detailed(
        client=client,
        format=format,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format: Union[Unset, SchemaRetrieveFormat] = UNSET,
) -> Response[SchemaRetrieveResponse_200]:
    kwargs = _get_kwargs(
        client=client,
        format=format,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format: Union[Unset, SchemaRetrieveFormat] = UNSET,
) -> Optional[SchemaRetrieveResponse_200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json"""

    return (
        await asyncio_detailed(
            client=client,
            format=format,
        )
    ).parsed
