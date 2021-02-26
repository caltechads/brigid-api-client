import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedApplication")


@attr.s(auto_attribs=True)
class PatchedApplication:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    ecosystem: Union[Unset, str] = UNSET
    primary_software: Union[Unset, str] = UNSET
    dependent_software: Union[Unset, List[str]] = UNSET
    machine_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    trello_board_url: Union[Unset, Optional[str]] = UNSET
    documentation_url: Union[Unset, Optional[str]] = UNSET
    pipelines: Union[Unset, List[str]] = UNSET
    owning_team: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        ecosystem = self.ecosystem
        primary_software = self.primary_software
        dependent_software: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.dependent_software, Unset):
            dependent_software = self.dependent_software

        machine_name = self.machine_name
        name = self.name
        description = self.description
        trello_board_url = self.trello_board_url
        documentation_url = self.documentation_url
        pipelines: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.pipelines, Unset):
            pipelines = self.pipelines

        owning_team = self.owning_team
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
        if ecosystem is not UNSET:
            field_dict["ecosystem"] = ecosystem
        if primary_software is not UNSET:
            field_dict["primary_software"] = primary_software
        if dependent_software is not UNSET:
            field_dict["dependent_software"] = dependent_software
        if machine_name is not UNSET:
            field_dict["machine_name"] = machine_name
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if trello_board_url is not UNSET:
            field_dict["trello_board_url"] = trello_board_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if owning_team is not UNSET:
            field_dict["owning_team"] = owning_team
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        ecosystem = d.pop("ecosystem", UNSET)

        primary_software = d.pop("primary_software", UNSET)

        dependent_software = cast(List[str], d.pop("dependent_software", UNSET))

        machine_name = d.pop("machine_name", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        trello_board_url = d.pop("trello_board_url", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        pipelines = cast(List[str], d.pop("pipelines", UNSET))

        owning_team = d.pop("owning_team", UNSET)

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_application = cls(
            url=url,
            id=id,
            ecosystem=ecosystem,
            primary_software=primary_software,
            dependent_software=dependent_software,
            machine_name=machine_name,
            name=name,
            description=description,
            trello_board_url=trello_board_url,
            documentation_url=documentation_url,
            pipelines=pipelines,
            owning_team=owning_team,
            created=created,
        )

        patched_application.additional_properties = d
        return patched_application

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
