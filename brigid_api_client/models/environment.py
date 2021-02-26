import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Environment")


@attr.s(auto_attribs=True)
class Environment:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    application: str
    ecs_services: List[str]
    machine_name: str
    name: str
    notes: str
    deployments: List[str]
    related_links: List[str]
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        application = self.application
        ecs_services = self.ecs_services

        machine_name = self.machine_name
        name = self.name
        notes = self.notes
        deployments = self.deployments

        related_links = self.related_links

        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "application": application,
                "ecs_services": ecs_services,
                "machine_name": machine_name,
                "name": name,
                "notes": notes,
                "deployments": deployments,
                "related_links": related_links,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        application = d.pop("application")

        ecs_services = cast(List[str], d.pop("ecs_services"))

        machine_name = d.pop("machine_name")

        name = d.pop("name")

        notes = d.pop("notes")

        deployments = cast(List[str], d.pop("deployments"))

        related_links = cast(List[str], d.pop("related_links"))

        created = isoparse(d.pop("created"))

        environment = cls(
            url=url,
            id=id,
            application=application,
            ecs_services=ecs_services,
            machine_name=machine_name,
            name=name,
            notes=notes,
            deployments=deployments,
            related_links=related_links,
            created=created,
        )

        environment.additional_properties = d
        return environment

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
