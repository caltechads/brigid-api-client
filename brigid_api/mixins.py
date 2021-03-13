import json
from urllib.parse import parse_qs, urlparse


class Endpoint:
    class DoesNotExist(Exception):
        pass

    class MultipleObjectsReturned(Exception):
        pass

    class OperationFailed(Exception):
        def __init__(self, msg, errors=None):
            super().__init__()
            self.msg = msg
            if not errors:
                self.errors = {}
            else:
                self.errors = errors

    UNSET = "unset"

    id_resolver_filter = None

    object_class = None
    list_class = None
    create_class = None
    retrieve_class = None
    partial_update_class = None
    partial_update_payload_class = None
    destroy_class = None

    @classmethod
    def list_filters(cls):
        return cls.list_class.LIST_FILTERS

    def parse_detailed_json_response(self, response):
        try:
            results = json.loads(response.content.decode("utf8"))
        except json.decoder.JSONDecodeError as e:
            raise self.OperationFailed(
                "Parsing of JSON response from API endpoint failed.",
                errors={"results": str(e)},
            )
        return results

    def __init__(self, client):
        self.client = client

    def object_repr(self, **kwargs):
        args = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        return f"{self.object_class.__name__}({args})"

    def resolve_object_id(self, identifier):
        """
        If `identifier` is not an integer, use the list endpoint to try to resolve it based on filtering by
        `self.id_resolver_filter`.  Return the integer id of the object in question.

        This allows our single object endpoints to accept either an ID or a name for our objects so that end users
        don't have to do any lookups before using those endpoints.

        :param identifier Union[int, str]: an id or name for a single object

        :rtype: int
        """
        try:
            obj_id = int(identifier)
        except ValueError:
            if self.id_resolver_filter:
                if callable(self.id_resolver_filter):
                    kwargs = self.id_resolver_filter(identifier)
                else:
                    kwargs = {self.id_resolver_filter: identifier}
                results = self.list(**kwargs)
                if len(results) > 1:
                    raise self.MultipleObjectsReturned(
                        f'More than one {self.object_class.__name__} object matches "{identifier}".  Be more specific.'
                    )
                elif len(results) == 0:
                    raise self.DoesNotExist(
                        f'No {self.object_class.__name__} object matching "{identifier}" was found.'
                    )
                    return
                else:
                    obj_id = results[0].id
            else:
                raise self.OperationFailed(
                    f'No {self.object_class.__name__} object matching "{identifier}" was found.'
                )

        return obj_id

    @classmethod
    def id_resolver_filter_format(cls):
        if callable(cls.id_resolver_filter):
            assert hasattr(
                cls.id_resolver_filter, "__resolver_format__"
            ), "You must set the __resolver_format__ attribute on your id_resolver_filter method."
            identifier_desc = f'a string that looks like "{cls.id_resolver_filter.__resolver_format__}"'
        else:
            identifier_desc = f"{cls.object_class.__name__}.{cls.id_resolver_filter}"
        return identifier_desc

    def list(self, **kwargs):
        response = self.list_class.sync(client=self.client, **kwargs)
        if not response:
            return []
        return response.results

    def create(self, **kwargs):
        payload = self.object_class(**kwargs)
        response = self.create_class.sync_detailed(
            client=self.client, json_body=payload
        )
        if response.status_code == 201:
            return response.parsed
        else:
            results = self.parse_detailed_json_response(response)
            raise self.OperationFailed(
                f"Creation of {self.object_class.__name__} object failed",
                errors=results,
            )

    def retrieve(self, identifier, **kwargs):
        object_id = self.resolve_object_id(identifier)
        response = self.retrieve_class.sync_detailed(
            client=self.client, id=object_id, **kwargs
        )
        if response.status_code == 200:
            return response.parsed
        elif response.status_code == 404:
            raise self.DoesNotExist(
                f"No {self.object_class.__name__} object with id={object_id} was found."
            )
        else:
            results = self.parse_detailed_json_response(response)
            raise self.OperationFailed(
                f"Retrieval of {self.object_repr(id=object_id)} failed.",
                errors=results,
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
        results = self.parse_detailed_json_response(response)
        if "id" in results:
            return {k: v for k, v in results.items() if k in kwargs}
        else:
            raise self.OperationFailed(
                f"Update of {self.object_repr(id=object_id)} failed",
                errors=results,
            )

    def delete(self, identifier):
        object_id = self.resolve_object_id(identifier)
        response = self.destroy_class.sync_detailed(client=self.client, id=object_id)
        if response.status_code != 204:
            raise self.OperationFailed(
                f"Delete of {self.object_repr(id=object_id)} failed", errors=[]
            )


class PagedResultsMixin:
    def list(self, **kwargs):
        response = self.list_class.sync(client=self.client, **kwargs)
        if not response:
            return []
        results = response.results
        while response.next:
            params = parse_qs(urlparse(response.next).query)
            kwargs['offset'] = int(params["offset"][0])
            kwargs['limit'] = int(params["limit"][0])
            response = self.list_class.sync(client=self.client, **kwargs)
            results.extend(response.results)
        return results
