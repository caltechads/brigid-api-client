import json

from giturlparse import parse

from brigid_api_client.models import Software, SoftwareImport, PatchedSoftware
from brigid_api_client.api.software import (
    software_list,
    software_import,
    software_sync,
    software_partial_update,
    software_retrieve
)

from .mixins import PagedResultsMixin, Endpoint


class SoftwareEndpoint(PagedResultsMixin, Endpoint):

    object_class = Software
    id_resolver_filter = 'machine_name'
    list_class = software_list
    retrieve_class = software_retrieve
    partial_update_class = software_partial_update
    partial_update_payload_class = PatchedSoftware

    def import_repository(self, repository):
        p = parse(repository)
        payload = SoftwareImport(service=p.platform, repository=p.repo, workspace=p.owner)
        response = software_import.sync_detailed(client=self.client, json_body=payload)
        try:
            results = json.loads(response.content.decode('utf8'))
        except json.decoder.JSONDecodeError:
            print(response.content)
        if response.status_code in [200, 201]:
            if response.status_code == 201:
                created = True
            else:
                created = False
            return results['id'], created
        else:
            raise self.OperationFailed(f'Import of {repository} failed.', errors=results['errors'])
