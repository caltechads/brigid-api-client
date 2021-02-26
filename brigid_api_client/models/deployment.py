import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Deployment")


@attr.s(auto_attribs=True)
class Deployment:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    environment: str
    release: List[str]
    ecs_service_deploys: List[str]
    ecs_task_deploys: List[str]
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        environment = self.environment
        release = self.release

        ecs_service_deploys = self.ecs_service_deploys

        ecs_task_deploys = self.ecs_task_deploys

        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "environment": environment,
                "release": release,
                "ecs_service_deploys": ecs_service_deploys,
                "ecs_task_deploys": ecs_task_deploys,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        environment = d.pop("environment")

        release = cast(List[str], d.pop("release"))

        ecs_service_deploys = cast(List[str], d.pop("ecs_service_deploys"))

        ecs_task_deploys = cast(List[str], d.pop("ecs_task_deploys"))

        created = isoparse(d.pop("created"))

        deployment = cls(
            url=url,
            id=id,
            environment=environment,
            release=release,
            ecs_service_deploys=ecs_service_deploys,
            ecs_task_deploys=ecs_task_deploys,
            created=created,
        )

        deployment.additional_properties = d
        return deployment

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
