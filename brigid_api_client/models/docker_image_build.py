import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DockerImageBuild")


@attr.s(auto_attribs=True)
class DockerImageBuild:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    release: str
    image_name: str
    created: datetime.datetime
    image_size_mb: Union[Unset, Optional[float]] = UNSET
    elapsed_seconds: Union[Unset, Optional[int]] = UNSET
    dependencies: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        release = self.release
        image_name = self.image_name
        created = self.created.isoformat()

        image_size_mb = self.image_size_mb
        elapsed_seconds = self.elapsed_seconds
        dependencies = self.dependencies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "release": release,
                "image_name": image_name,
                "created": created,
            }
        )
        if image_size_mb is not UNSET:
            field_dict["image_size_mb"] = image_size_mb
        if elapsed_seconds is not UNSET:
            field_dict["elapsed_seconds"] = elapsed_seconds
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        release = d.pop("release")

        image_name = d.pop("image_name")

        created = isoparse(d.pop("created"))

        image_size_mb = d.pop("image_size_mb", UNSET)

        elapsed_seconds = d.pop("elapsed_seconds", UNSET)

        dependencies = d.pop("dependencies", UNSET)

        docker_image_build = cls(
            url=url,
            id=id,
            release=release,
            image_name=image_name,
            created=created,
            image_size_mb=image_size_mb,
            elapsed_seconds=elapsed_seconds,
            dependencies=dependencies,
        )

        docker_image_build.additional_properties = d
        return docker_image_build

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
