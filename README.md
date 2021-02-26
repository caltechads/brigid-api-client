# brigid-api-client

A client library for accessing Brigid API.

## Usage

First, create a client:

```python
from brigid_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://brigid-prod.api.caltech.edu", token="SuperSecretToken")
```

Now call your endpoint and use your models.  Example::

```python
from brigid_api_client.models import Organization
from brigid_api_client.api.organizations import organizations_retrieve
from brigid_api_client.types import Response

org: Organization = organizations_retrieve.sync(client=client, id=1)
# or if you need more info (e.g. status_code)
response: Response[Organization] = organizations_retrieve.sync_detailed(client=client, id=1)
```

Or do the same thing with an async version:

```python
from brigid_api_client.models import Organization
from brigid_api_client.async_api.organizations import organizations_retrieve
from brigid_api_client.types import Response

org: Organization = await organizations_retrieve.asyncio(client=client, id=1)
response: Response[Organization] = await organizations_retrieve.asyncio_detailed(client=client, id=1)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:

    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but the async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (e.g. `organzations` above)
1. Any endpoint which did not have a tag will be in `brigid_api_client.api.default`

## Updating this client from your local copy of Brigid

First you should have `openapi-python-client` installed into your global python interpreter.

```
$ cd ..
$ wget --no-check-certificate -O schema.yml https://localhost:8063/api/v1/schema/
$ openapi-python-client update --path schema.yml  --custom-template-path=./brigid-api-client/templates/  
```

Then edit `brigid_api_client/client.py` and, in `AuthenticatedClient` , change "`Bearer`" to "`Token`".
