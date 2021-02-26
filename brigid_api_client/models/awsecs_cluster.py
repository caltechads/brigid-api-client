import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AWSECSCluster")


@attr.s(auto_attribs=True)
class AWSECSCluster:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    aws_vpc: str
    name: str
    aws_ecs_services: List[str]
    aws_ecs_tasks: List[str]
    created: datetime.datetime
    description: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        aws_vpc = self.aws_vpc
        name = self.name
        aws_ecs_services = self.aws_ecs_services

        aws_ecs_tasks = self.aws_ecs_tasks

        created = self.created.isoformat()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "aws_vpc": aws_vpc,
                "name": name,
                "aws_ecs_services": aws_ecs_services,
                "aws_ecs_tasks": aws_ecs_tasks,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        aws_vpc = d.pop("aws_vpc")

        name = d.pop("name")

        aws_ecs_services = cast(List[str], d.pop("aws_ecs_services"))

        aws_ecs_tasks = cast(List[str], d.pop("aws_ecs_tasks"))

        created = isoparse(d.pop("created"))

        description = d.pop("description", UNSET)

        awsecs_cluster = cls(
            url=url,
            id=id,
            aws_vpc=aws_vpc,
            name=name,
            aws_ecs_services=aws_ecs_services,
            aws_ecs_tasks=aws_ecs_tasks,
            created=created,
            description=description,
        )

        awsecs_cluster.additional_properties = d
        return awsecs_cluster

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
