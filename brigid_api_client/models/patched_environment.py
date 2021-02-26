import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEnvironment")


@attr.s(auto_attribs=True)
class PatchedEnvironment:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    application: Union[Unset, str] = UNSET
    ecs_services: Union[Unset, List[str]] = UNSET
    machine_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    deployments: Union[Unset, List[str]] = UNSET
    related_links: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        application = self.application
        ecs_services: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.ecs_services, Unset):
            ecs_services = self.ecs_services

        machine_name = self.machine_name
        name = self.name
        notes = self.notes
        deployments: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = self.deployments

        related_links: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.related_links, Unset):
            related_links = self.related_links

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if id is not UNSET:
            field_dict["id"] = id
        if application is not UNSET:
            field_dict["application"] = application
        if ecs_services is not UNSET:
            field_dict["ecs_services"] = ecs_services
        if machine_name is not UNSET:
            field_dict["machine_name"] = machine_name
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if deployments is not UNSET:
            field_dict["deployments"] = deployments
        if related_links is not UNSET:
            field_dict["related_links"] = related_links
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        application = d.pop("application", UNSET)

        ecs_services = cast(List[str], d.pop("ecs_services", UNSET))

        machine_name = d.pop("machine_name", UNSET)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        deployments = cast(List[str], d.pop("deployments", UNSET))

        related_links = cast(List[str], d.pop("related_links", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_environment = cls(
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

        patched_environment.additional_properties = d
        return patched_environment

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
