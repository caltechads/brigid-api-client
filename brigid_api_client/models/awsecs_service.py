import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="AWSECSService")


@attr.s(auto_attribs=True)
class AWSECSService:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    ecs_cluster: str
    name: str
    environment: str
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        ecs_cluster = self.ecs_cluster
        name = self.name
        environment = self.environment
        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "ecs_cluster": ecs_cluster,
                "name": name,
                "environment": environment,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        ecs_cluster = d.pop("ecs_cluster")

        name = d.pop("name")

        environment = d.pop("environment")

        created = isoparse(d.pop("created"))

        awsecs_service = cls(
            url=url,
            id=id,
            ecs_cluster=ecs_cluster,
            name=name,
            environment=environment,
            created=created,
        )

        awsecs_service.additional_properties = d
        return awsecs_service

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
