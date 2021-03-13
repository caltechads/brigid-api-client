from giturlparse import parse

from brigid_api_client.api.releases import (
    releases_create,
    releases_destroy,
    releases_import,
    releases_import_all,
    releases_list,
    releases_partial_update,
    releases_retrieve,
    releases_sync,
)
from brigid_api_client.api.software import (
    software_create,
    software_destroy,
    software_import,
    software_list,
    software_partial_update,
    software_retrieve,
    software_sync,
)
from brigid_api_client.models import (
    PatchedRelease,
    PatchedSoftware,
    Release,
    ReleaseImport,
    ReleaseImportAll,
    Software,
    SoftwareImport,
)

from .mixins import Endpoint, PagedResultsMixin


class SoftwareEndpoint(PagedResultsMixin, Endpoint):

    object_class = Software
    id_resolver_filter = "machine_name"
    list_class = software_list
    retrieve_class = software_retrieve
    partial_update_class = software_partial_update
    partial_update_payload_class = PatchedSoftware
    create_class = software_create
    destroy_class = software_destroy

    def import_repository(self, repository):
        p = parse(repository)
        payload = SoftwareImport(
            service=p.platform, repository=p.repo, workspace=p.owner
        )
        response = software_import.sync_detailed(client=self.client, json_body=payload)
        results = self.parse_detailed_json_response(response)
        if response.status_code in [200, 201]:
            if response.status_code == 201:
                created = True
            else:
                created = False
            return results["id"], created
        else:
            raise self.OperationFailed(
                f"Import of {repository} failed.", errors=results["errors"]
            )

    def sync(self, identifier):
        obj_id = self.resolve_object_id(identifier)
        response = software_sync.sync_detailed(client=self.client, id=obj_id)
        results = self.parse_detailed_json_response(response)
        if response.status_code == 200:
            return results["id"]
        elif response.status_code == 404:
            raise self.DoesNotExist(
                f"No {self.object_class.__name__} object with id={obj_id} was found."
            )
        else:
            raise self.OperationFailed(
                "Repository sync of {self.object_repr(id=obj_id)} failed.",
                errors=results["errors"],
            )


class ReleasesEndpoint(PagedResultsMixin, Endpoint):

    object_class = Release
    list_class = releases_list
    retrieve_class = releases_retrieve
    partial_update_class = releases_partial_update
    partial_update_payload_class = PatchedRelease
    create_class = releases_create
    destroy_class = releases_destroy

    def id_resolver_filter(self, identifier):
        try:
            software_name, version = identifier.split(":")
        except ValueError:
            raise self.OperationFailed(
                "Release IDENTIFIER must be either a Release.id or a string that looks like"
                '"{Software.name}:{Release.version}"',
                errors=[],
            )
        return {"software_name": software_name, "version": version}

    id_resolver_filter.__resolver_format__ = "{Software.machine_name}:{Release.version}"

    def import_release(self, identifier, version):
        software_id = SoftwareEndpoint(self.client).resolve_object_id(identifier)
        payload = ReleaseImport(software_id=software_id, version=version)
        response = releases_import.sync_detailed(client=self.client, json_body=payload)
        results = self.parse_detailed_json_response(response)
        if response.status_code in [200, 201]:
            if response.status_code == 201:
                created = True
            else:
                created = False
            return results["id"], created
        else:
            raise self.OperationFailed(
                f"Import of {identifier}:{version} failed.", errors=results["errors"]
            )

    def import_all_releases(self, identifier):
        software_id = SoftwareEndpoint(self.client).resolve_object_id(identifier)
        payload = ReleaseImportAll(software_id=software_id)
        response = releases_import_all.sync_detailed(
            client=self.client, json_body=payload
        )
        results = self.parse_detailed_json_response(response)
        if response.status_code == 200:
            return results["messages"]
        else:
            raise self.OperationFailed(
                f'Import of all releases for Software("{identifier}") failed.',
                errors=results["errors"],
            )

    def sync(self, identifier):
        obj_id = self.resolve_object_id(identifier)
        response = releases_sync.sync_detailed(client=self.client, id=obj_id)
        results = self.parse_detailed_json_response(response)
        if response.status_code == 200:
            return results["id"]
        elif response.status_code == 404:
            raise self.DoesNotExist(
                f"No {self.object_class.__name__} object with id={obj_id} was found."
            )
        else:
            raise self.OperationFailed(
                "Release sync of {self.object_repr(id=obj_id)} failed.",
                errors=results["errors"],
            )
