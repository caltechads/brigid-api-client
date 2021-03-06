import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSoftware")


@attr.s(auto_attribs=True)
class PatchedSoftware:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    machine_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    git_repo_url: Union[Unset, str] = UNSET
    artifact_repo_url: Union[Unset, str] = UNSET
    trello_board_url: Union[Unset, Optional[str]] = UNSET
    documentation_url: Union[Unset, Optional[str]] = UNSET
    applications: Union[Unset, List[str]] = UNSET
    authors: Union[Unset, List[str]] = UNSET
    repo_created: Union[Unset, Optional[datetime.datetime]] = UNSET
    repo_modified: Union[Unset, Optional[datetime.datetime]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        machine_name = self.machine_name
        name = self.name
        description = self.description
        git_repo_url = self.git_repo_url
        artifact_repo_url = self.artifact_repo_url
        trello_board_url = self.trello_board_url
        documentation_url = self.documentation_url
        applications: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.applications, Unset):
            applications = self.applications

        authors: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        repo_created: Union[Unset, str] = UNSET
        if not isinstance(self.repo_created, Unset):
            repo_created = self.repo_created.isoformat() if self.repo_created else None

        repo_modified: Union[Unset, str] = UNSET
        if not isinstance(self.repo_modified, Unset):
            repo_modified = (
                self.repo_modified.isoformat() if self.repo_modified else None
            )

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
        if machine_name is not UNSET:
            field_dict["machine_name"] = machine_name
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if git_repo_url is not UNSET:
            field_dict["git_repo_url"] = git_repo_url
        if artifact_repo_url is not UNSET:
            field_dict["artifact_repo_url"] = artifact_repo_url
        if trello_board_url is not UNSET:
            field_dict["trello_board_url"] = trello_board_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if applications is not UNSET:
            field_dict["applications"] = applications
        if authors is not UNSET:
            field_dict["authors"] = authors
        if repo_created is not UNSET:
            field_dict["repo_created"] = repo_created
        if repo_modified is not UNSET:
            field_dict["repo_modified"] = repo_modified
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

        machine_name = d.pop("machine_name", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        git_repo_url = d.pop("git_repo_url", UNSET)

        artifact_repo_url = d.pop("artifact_repo_url", UNSET)

        trello_board_url = d.pop("trello_board_url", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        applications = cast(List[str], d.pop("applications", UNSET))

        authors = cast(List[str], d.pop("authors", UNSET))

        repo_created = None
        _repo_created = d.pop("repo_created", UNSET)
        if _repo_created is not None and not isinstance(_repo_created, Unset):
            repo_created = isoparse(_repo_created)

        repo_modified = None
        _repo_modified = d.pop("repo_modified", UNSET)
        if _repo_modified is not None and not isinstance(_repo_modified, Unset):
            repo_modified = isoparse(_repo_modified)

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        modified: Union[Unset, datetime.datetime] = UNSET
        _modified = d.pop("modified", UNSET)
        if not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        patched_software = cls(
            url=url,
            id=id,
            machine_name=machine_name,
            name=name,
            description=description,
            git_repo_url=git_repo_url,
            artifact_repo_url=artifact_repo_url,
            trello_board_url=trello_board_url,
            documentation_url=documentation_url,
            applications=applications,
            authors=authors,
            repo_created=repo_created,
            repo_modified=repo_modified,
            created=created,
            modified=modified,
        )

        patched_software.additional_properties = d
        return patched_software

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
