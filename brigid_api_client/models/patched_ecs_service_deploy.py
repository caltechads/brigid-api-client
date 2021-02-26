import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedECSServiceDeploy")


@attr.s(auto_attribs=True)
class PatchedECSServiceDeploy:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    deployment: Union[Unset, str] = UNSET
    docker_image_build: Union[Unset, str] = UNSET
    ecs_service: Union[Unset, str] = UNSET
    task_definition: Union[Unset, str] = UNSET
    successful: Union[Unset, bool] = UNSET
    elapsed_seconds: Union[Unset, Optional[int]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        deployment = self.deployment
        docker_image_build = self.docker_image_build
        ecs_service = self.ecs_service
        task_definition = self.task_definition
        successful = self.successful
        elapsed_seconds = self.elapsed_seconds
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
        if deployment is not UNSET:
            field_dict["deployment"] = deployment
        if docker_image_build is not UNSET:
            field_dict["docker_image_build"] = docker_image_build
        if ecs_service is not UNSET:
            field_dict["ecs_service"] = ecs_service
        if task_definition is not UNSET:
            field_dict["task_definition"] = task_definition
        if successful is not UNSET:
            field_dict["successful"] = successful
        if elapsed_seconds is not UNSET:
            field_dict["elapsed_seconds"] = elapsed_seconds
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        deployment = d.pop("deployment", UNSET)

        docker_image_build = d.pop("docker_image_build", UNSET)

        ecs_service = d.pop("ecs_service", UNSET)

        task_definition = d.pop("task_definition", UNSET)

        successful = d.pop("successful", UNSET)

        elapsed_seconds = d.pop("elapsed_seconds", UNSET)

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_ecs_service_deploy = cls(
            url=url,
            id=id,
            deployment=deployment,
            docker_image_build=docker_image_build,
            ecs_service=ecs_service,
            task_definition=task_definition,
            successful=successful,
            elapsed_seconds=elapsed_seconds,
            created=created,
        )

        patched_ecs_service_deploy.additional_properties = d
        return patched_ecs_service_deploy

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
