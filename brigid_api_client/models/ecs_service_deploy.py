import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ECSServiceDeploy")


@attr.s(auto_attribs=True)
class ECSServiceDeploy:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    deployment: str
    docker_image_build: str
    ecs_service: str
    task_definition: str
    created: datetime.datetime
    successful: Union[Unset, bool] = UNSET
    elapsed_seconds: Union[Unset, Optional[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        deployment = self.deployment
        docker_image_build = self.docker_image_build
        ecs_service = self.ecs_service
        task_definition = self.task_definition
        created = self.created.isoformat()

        successful = self.successful
        elapsed_seconds = self.elapsed_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "deployment": deployment,
                "docker_image_build": docker_image_build,
                "ecs_service": ecs_service,
                "task_definition": task_definition,
                "created": created,
            }
        )
        if successful is not UNSET:
            field_dict["successful"] = successful
        if elapsed_seconds is not UNSET:
            field_dict["elapsed_seconds"] = elapsed_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        deployment = d.pop("deployment")

        docker_image_build = d.pop("docker_image_build")

        ecs_service = d.pop("ecs_service")

        task_definition = d.pop("task_definition")

        created = isoparse(d.pop("created"))

        successful = d.pop("successful", UNSET)

        elapsed_seconds = d.pop("elapsed_seconds", UNSET)

        ecs_service_deploy = cls(
            url=url,
            id=id,
            deployment=deployment,
            docker_image_build=docker_image_build,
            ecs_service=ecs_service,
            task_definition=task_definition,
            created=created,
            successful=successful,
            elapsed_seconds=elapsed_seconds,
        )

        ecs_service_deploy.additional_properties = d
        return ecs_service_deploy

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
