import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAWSECSService")


@attr.s(auto_attribs=True)
class PatchedAWSECSService:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    ecs_cluster: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        ecs_cluster = self.ecs_cluster
        name = self.name
        environment = self.environment
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
        if ecs_cluster is not UNSET:
            field_dict["ecs_cluster"] = ecs_cluster
        if name is not UNSET:
            field_dict["name"] = name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        ecs_cluster = d.pop("ecs_cluster", UNSET)

        name = d.pop("name", UNSET)

        environment = d.pop("environment", UNSET)

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_awsecs_service = cls(
            url=url,
            id=id,
            ecs_cluster=ecs_cluster,
            name=name,
            environment=environment,
            created=created,
        )

        patched_awsecs_service.additional_properties = d
        return patched_awsecs_service

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
