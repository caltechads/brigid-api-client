import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDockerImageBuild")


@attr.s(auto_attribs=True)
class PatchedDockerImageBuild:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    release: Union[Unset, str] = UNSET
    image_name: Union[Unset, str] = UNSET
    image_size_mb: Union[Unset, Optional[float]] = UNSET
    elapsed_seconds: Union[Unset, Optional[int]] = UNSET
    dependencies: Union[Unset, Optional[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        release = self.release
        image_name = self.image_name
        image_size_mb = self.image_size_mb
        elapsed_seconds = self.elapsed_seconds
        dependencies = self.dependencies
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
        if release is not UNSET:
            field_dict["release"] = release
        if image_name is not UNSET:
            field_dict["image_name"] = image_name
        if image_size_mb is not UNSET:
            field_dict["image_size_mb"] = image_size_mb
        if elapsed_seconds is not UNSET:
            field_dict["elapsed_seconds"] = elapsed_seconds
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        release = d.pop("release", UNSET)

        image_name = d.pop("image_name", UNSET)

        image_size_mb = d.pop("image_size_mb", UNSET)

        elapsed_seconds = d.pop("elapsed_seconds", UNSET)

        dependencies = d.pop("dependencies", UNSET)

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_docker_image_build = cls(
            url=url,
            id=id,
            release=release,
            image_name=image_name,
            image_size_mb=image_size_mb,
            elapsed_seconds=elapsed_seconds,
            dependencies=dependencies,
            created=created,
        )

        patched_docker_image_build.additional_properties = d
        return patched_docker_image_build

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
