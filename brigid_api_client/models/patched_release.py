import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRelease")


@attr.s(auto_attribs=True)
class PatchedRelease:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    software: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    changelog: Union[Unset, Optional[str]] = UNSET
    released_by: Union[Unset, str] = UNSET
    release_time: Union[Unset, Optional[datetime.datetime]] = UNSET
    docker_image_builds: Union[Unset, List[str]] = UNSET
    deployments: Union[Unset, List[str]] = UNSET
    pipeline_invocations: Union[Unset, List[str]] = UNSET
    step_invocations: Union[Unset, List[str]] = UNSET
    test_results: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        software = self.software
        version = self.version
        sha = self.sha
        changelog = self.changelog
        released_by = self.released_by
        release_time: Union[Unset, str] = UNSET
        if not isinstance(self.release_time, Unset):
            release_time = self.release_time.isoformat() if self.release_time else None

        docker_image_builds: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.docker_image_builds, Unset):
            docker_image_builds = self.docker_image_builds

        deployments: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = self.deployments

        pipeline_invocations: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.pipeline_invocations, Unset):
            pipeline_invocations = self.pipeline_invocations

        step_invocations: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.step_invocations, Unset):
            step_invocations = self.step_invocations

        test_results: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.test_results, Unset):
            test_results = self.test_results

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if id is not UNSET:
            field_dict["id"] = id
        if software is not UNSET:
            field_dict["software"] = software
        if version is not UNSET:
            field_dict["version"] = version
        if sha is not UNSET:
            field_dict["sha"] = sha
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if released_by is not UNSET:
            field_dict["released_by"] = released_by
        if release_time is not UNSET:
            field_dict["release_time"] = release_time
        if docker_image_builds is not UNSET:
            field_dict["docker_image_builds"] = docker_image_builds
        if deployments is not UNSET:
            field_dict["deployments"] = deployments
        if pipeline_invocations is not UNSET:
            field_dict["pipeline_invocations"] = pipeline_invocations
        if step_invocations is not UNSET:
            field_dict["step_invocations"] = step_invocations
        if test_results is not UNSET:
            field_dict["test_results"] = test_results
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        software = d.pop("software", UNSET)

        version = d.pop("version", UNSET)

        sha = d.pop("sha", UNSET)

        changelog = d.pop("changelog", UNSET)

        released_by = d.pop("released_by", UNSET)

        release_time = None
        _release_time = d.pop("release_time", UNSET)
        if _release_time is not None and not isinstance(_release_time, Unset):
            release_time = isoparse(_release_time)

        docker_image_builds = cast(List[str], d.pop("docker_image_builds", UNSET))

        deployments = cast(List[str], d.pop("deployments", UNSET))

        pipeline_invocations = cast(List[str], d.pop("pipeline_invocations", UNSET))

        step_invocations = cast(List[str], d.pop("step_invocations", UNSET))

        test_results = cast(List[str], d.pop("test_results", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        modified: Union[Unset, datetime.datetime] = UNSET
        _modified = d.pop("modified", UNSET)
        if not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        patched_release = cls(
            url=url,
            id=id,
            software=software,
            version=version,
            sha=sha,
            changelog=changelog,
            released_by=released_by,
            release_time=release_time,
            docker_image_builds=docker_image_builds,
            deployments=deployments,
            pipeline_invocations=pipeline_invocations,
            step_invocations=step_invocations,
            test_results=test_results,
            created=created,
            modified=modified,
        )

        patched_release.additional_properties = d
        return patched_release

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
