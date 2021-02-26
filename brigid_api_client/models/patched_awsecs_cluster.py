import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAWSECSCluster")


@attr.s(auto_attribs=True)
class PatchedAWSECSCluster:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    aws_vpc: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, Optional[str]] = UNSET
    aws_ecs_services: Union[Unset, List[str]] = UNSET
    aws_ecs_tasks: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        aws_vpc = self.aws_vpc
        name = self.name
        description = self.description
        aws_ecs_services: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_ecs_services, Unset):
            aws_ecs_services = self.aws_ecs_services

        aws_ecs_tasks: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_ecs_tasks, Unset):
            aws_ecs_tasks = self.aws_ecs_tasks

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
        if aws_vpc is not UNSET:
            field_dict["aws_vpc"] = aws_vpc
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if aws_ecs_services is not UNSET:
            field_dict["aws_ecs_services"] = aws_ecs_services
        if aws_ecs_tasks is not UNSET:
            field_dict["aws_ecs_tasks"] = aws_ecs_tasks
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        aws_vpc = d.pop("aws_vpc", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        aws_ecs_services = cast(List[str], d.pop("aws_ecs_services", UNSET))

        aws_ecs_tasks = cast(List[str], d.pop("aws_ecs_tasks", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_awsecs_cluster = cls(
            url=url,
            id=id,
            aws_vpc=aws_vpc,
            name=name,
            description=description,
            aws_ecs_services=aws_ecs_services,
            aws_ecs_tasks=aws_ecs_tasks,
            created=created,
        )

        patched_awsecs_cluster.additional_properties = d
        return patched_awsecs_cluster

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
