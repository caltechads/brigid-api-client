import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Application")


@attr.s(auto_attribs=True)
class Application:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    ecosystem: str
    primary_software: str
    dependent_software: List[str]
    machine_name: str
    name: str
    description: str
    pipelines: List[str]
    owning_team: str
    created: datetime.datetime
    trello_board_url: Union[Unset, Optional[str]] = UNSET
    documentation_url: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        ecosystem = self.ecosystem
        primary_software = self.primary_software
        dependent_software = self.dependent_software

        machine_name = self.machine_name
        name = self.name
        description = self.description
        pipelines = self.pipelines

        owning_team = self.owning_team
        created = self.created.isoformat()

        trello_board_url = self.trello_board_url
        documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "ecosystem": ecosystem,
                "primary_software": primary_software,
                "dependent_software": dependent_software,
                "machine_name": machine_name,
                "name": name,
                "description": description,
                "pipelines": pipelines,
                "owning_team": owning_team,
                "created": created,
            }
        )
        if trello_board_url is not UNSET:
            field_dict["trello_board_url"] = trello_board_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        ecosystem = d.pop("ecosystem")

        primary_software = d.pop("primary_software")

        dependent_software = cast(List[str], d.pop("dependent_software"))

        machine_name = d.pop("machine_name")

        name = d.pop("name")

        description = d.pop("description")

        pipelines = cast(List[str], d.pop("pipelines"))

        owning_team = d.pop("owning_team")

        created = isoparse(d.pop("created"))

        trello_board_url = d.pop("trello_board_url", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        application = cls(
            url=url,
            id=id,
            ecosystem=ecosystem,
            primary_software=primary_software,
            dependent_software=dependent_software,
            machine_name=machine_name,
            name=name,
            description=description,
            pipelines=pipelines,
            owning_team=owning_team,
            created=created,
            trello_board_url=trello_board_url,
            documentation_url=documentation_url,
        )

        application.additional_properties = d
        return application

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
