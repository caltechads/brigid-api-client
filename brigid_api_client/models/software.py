import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Software")


@attr.s(auto_attribs=True)
class Software:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    machine_name: str
    name: str
    description: str
    git_repo_url: str
    artifact_repo_url: str
    applications: List[str]
    authors: List[str]
    created: datetime.datetime
    modified: datetime.datetime
    trello_board_url: Union[Unset, Optional[str]] = UNSET
    documentation_url: Union[Unset, Optional[str]] = UNSET
    repo_created: Union[Unset, Optional[datetime.datetime]] = UNSET
    repo_modified: Union[Unset, Optional[datetime.datetime]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        machine_name = self.machine_name
        name = self.name
        description = self.description
        git_repo_url = self.git_repo_url
        artifact_repo_url = self.artifact_repo_url
        applications = self.applications

        authors = self.authors

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        trello_board_url = self.trello_board_url
        documentation_url = self.documentation_url
        repo_created: Union[Unset, str] = UNSET
        if not isinstance(self.repo_created, Unset):
            repo_created = self.repo_created.isoformat() if self.repo_created else None

        repo_modified: Union[Unset, str] = UNSET
        if not isinstance(self.repo_modified, Unset):
            repo_modified = (
                self.repo_modified.isoformat() if self.repo_modified else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "machine_name": machine_name,
                "name": name,
                "description": description,
                "git_repo_url": git_repo_url,
                "artifact_repo_url": artifact_repo_url,
                "applications": applications,
                "authors": authors,
                "created": created,
                "modified": modified,
            }
        )
        if trello_board_url is not UNSET:
            field_dict["trello_board_url"] = trello_board_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if repo_created is not UNSET:
            field_dict["repo_created"] = repo_created
        if repo_modified is not UNSET:
            field_dict["repo_modified"] = repo_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        machine_name = d.pop("machine_name")

        name = d.pop("name")

        description = d.pop("description")

        git_repo_url = d.pop("git_repo_url")

        artifact_repo_url = d.pop("artifact_repo_url")

        applications = cast(List[str], d.pop("applications"))

        authors = cast(List[str], d.pop("authors"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        trello_board_url = d.pop("trello_board_url", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        repo_created = None
        _repo_created = d.pop("repo_created", UNSET)
        if _repo_created is not None and not isinstance(_repo_created, Unset):
            repo_created = isoparse(_repo_created)

        repo_modified = None
        _repo_modified = d.pop("repo_modified", UNSET)
        if _repo_modified is not None and not isinstance(_repo_modified, Unset):
            repo_modified = isoparse(_repo_modified)

        software = cls(
            url=url,
            id=id,
            machine_name=machine_name,
            name=name,
            description=description,
            git_repo_url=git_repo_url,
            artifact_repo_url=artifact_repo_url,
            applications=applications,
            authors=authors,
            created=created,
            modified=modified,
            trello_board_url=trello_board_url,
            documentation_url=documentation_url,
            repo_created=repo_created,
            repo_modified=repo_modified,
        )

        software.additional_properties = d
        return software

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
