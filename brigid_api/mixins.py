import json
from urllib.parse import urlparse, parse_qs


class Endpoint:

    class DoesNotExist(Exception):
        pass

    class MultipleItemsReturned(Exception):
        pass

    class OperationFailed(Exception):

        def __init__(self, msg, errors=None):
            super().__init__()
            self.msg = msg
            if not errors:
                self.errors = {}
            else:
                self.errors = errors

    UNSET = 'unset'

    id_resolver_filter = None

    object_class = None
    list_class = None
    retrieve_class = None
    partial_update_class = None
    partial_update_payload_class = None

    def __init__(self, client):
        self.client = client

    def resolve_object_id(self, identifier):
        try:
            obj_id = int(identifier)
        except ValueError:
            # This is a machine_name
            results = self.list(**{self.id_resolver_filter: identifier})
            if len(results) > 1:
                raise self.MultipleItemsReturned(
                    f'More than one {self.object_class.__name} object matches "{identifier}".  Be more specific.'
                )
            elif len(results) == 0:
                raise self.DoesNotExist(f'No {self.object_class.__name__} object matching "{identifier}" was found.')
                return
            else:
                obj_id = results[0].id
        return obj_id

    def retrieve(self, identifier, **kwargs):
        object_id = self.resolve_object_id(identifier)
        response = self.retrieve_class.sync_detailed(client=self.client, id=object_id, **kwargs)
        if response.status_code == 200:
            return response.parsed
        elif response.status_code == 404:
            raise self.DoesNotExist(f'No {self.object_class.__name__} object with id={object_id} was found.')
        else:
            try:
                results = json.loads(response.content.decode('utf8'))
            except json.decoder.JSONDecodeError:
                print(response.content)
            raise self.OperationFailed(
                f'Retrieval of {self.object_class.__name__}(id={object_id}) failed.',
                errors=results
            )

    def partial_update(self, identifier, **kwargs):
        object_id = self.resolve_object_id(identifier)
        payload = self.partial_update_payload_class()
        for k, v in kwargs.items():
            if v != self.UNSET:
                setattr(payload, k, v)
        response = self.partial_update_class.sync_detailed(
            client=self.client,
            id=object_id,
            json_body=payload,
        )
        try:
            results = json.loads(response.content.decode('utf8'))
        except json.decoder.JSONDecodeError:
            print(response.content)
        if 'id' in results:
            return {k: v for k, v in results if k in kwargs}
        else:
            raise self.UpdateFailed(
                f'Update of {self.object_class.__name__}(id={object_id}) failed',
                errors=results
            )


class PagedResultsMixin:

    def list(self, **kwargs):
        response = self.list_class.sync(
            client=self.client,
            **kwargs
        )
        if not response:
            return []
        results = response.results
        while response.next:
            params = parse_qs(urlparse(response.next).query)
            offset = int(params['offset'][0])
            limit = int(params['limit'][0])
            response = function(
                client=self.client,
                limit=limit,
                offset=offset,
                **kwargs
            )
            results.extend(response.results)
        return results
