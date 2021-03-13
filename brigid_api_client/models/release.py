import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Release")


@attr.s(auto_attribs=True)
class Release:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    software: str
    version: str
    sha: str
    released_by: str
    docker_image_builds: List[str]
    deployments: List[str]
    pipeline_invocations: List[str]
    step_invocations: List[str]
    test_results: List[str]
    created: datetime.datetime
    modified: datetime.datetime
    changelog: Union[Unset, Optional[str]] = UNSET
    release_time: Union[Unset, Optional[datetime.datetime]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        software = self.software
        version = self.version
        sha = self.sha
        released_by = self.released_by
        docker_image_builds = self.docker_image_builds

        deployments = self.deployments

        pipeline_invocations = self.pipeline_invocations

        step_invocations = self.step_invocations

        test_results = self.test_results

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        changelog = self.changelog
        release_time: Union[Unset, str] = UNSET
        if not isinstance(self.release_time, Unset):
            release_time = self.release_time.isoformat() if self.release_time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "software": software,
                "version": version,
                "sha": sha,
                "released_by": released_by,
                "docker_image_builds": docker_image_builds,
                "deployments": deployments,
                "pipeline_invocations": pipeline_invocations,
                "step_invocations": step_invocations,
                "test_results": test_results,
                "created": created,
                "modified": modified,
            }
        )
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if release_time is not UNSET:
            field_dict["release_time"] = release_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        software = d.pop("software")

        version = d.pop("version")

        sha = d.pop("sha")

        released_by = d.pop("released_by")

        docker_image_builds = cast(List[str], d.pop("docker_image_builds"))

        deployments = cast(List[str], d.pop("deployments"))

        pipeline_invocations = cast(List[str], d.pop("pipeline_invocations"))

        step_invocations = cast(List[str], d.pop("step_invocations"))

        test_results = cast(List[str], d.pop("test_results"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        changelog = d.pop("changelog", UNSET)

        release_time = None
        _release_time = d.pop("release_time", UNSET)
        if _release_time is not None and not isinstance(_release_time, Unset):
            release_time = isoparse(_release_time)

        release = cls(
            url=url,
            id=id,
            software=software,
            version=version,
            sha=sha,
            released_by=released_by,
            docker_image_builds=docker_image_builds,
            deployments=deployments,
            pipeline_invocations=pipeline_invocations,
            step_invocations=step_invocations,
            test_results=test_results,
            created=created,
            modified=modified,
            changelog=changelog,
            release_time=release_time,
        )

        release.additional_properties = d
        return release

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
