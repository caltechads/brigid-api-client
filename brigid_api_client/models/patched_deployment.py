import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDeployment")


@attr.s(auto_attribs=True)
class PatchedDeployment:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    environment: Union[Unset, str] = UNSET
    release: Union[Unset, List[str]] = UNSET
    ecs_service_deploys: Union[Unset, List[str]] = UNSET
    ecs_task_deploys: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        environment = self.environment
        release: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.release, Unset):
            release = self.release

        ecs_service_deploys: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.ecs_service_deploys, Unset):
            ecs_service_deploys = self.ecs_service_deploys

        ecs_task_deploys: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.ecs_task_deploys, Unset):
            ecs_task_deploys = self.ecs_task_deploys

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
        if environment is not UNSET:
            field_dict["environment"] = environment
        if release is not UNSET:
            field_dict["release"] = release
        if ecs_service_deploys is not UNSET:
            field_dict["ecs_service_deploys"] = ecs_service_deploys
        if ecs_task_deploys is not UNSET:
            field_dict["ecs_task_deploys"] = ecs_task_deploys
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        environment = d.pop("environment", UNSET)

        release = cast(List[str], d.pop("release", UNSET))

        ecs_service_deploys = cast(List[str], d.pop("ecs_service_deploys", UNSET))

        ecs_task_deploys = cast(List[str], d.pop("ecs_task_deploys", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_deployment = cls(
            url=url,
            id=id,
            environment=environment,
            release=release,
            ecs_service_deploys=ecs_service_deploys,
            ecs_task_deploys=ecs_task_deploys,
            created=created,
        )

        patched_deployment.additional_properties = d
        return patched_deployment

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
