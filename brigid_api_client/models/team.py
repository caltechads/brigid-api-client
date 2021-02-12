from typing import Any, Dict, List, Optional, Union

import attr

from ..types import UNSET, Unset


@attr.s(auto_attribs=True)
class Team:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    directory_name: str
    friendly_name: str
    organization: str
    abbr: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        directory_name = self.directory_name
        friendly_name = self.friendly_name
        organization = self.organization
        abbr = self.abbr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "directory_name": directory_name,
                "friendly_name": friendly_name,
                "organization": organization,
            }
        )
        if abbr is not UNSET:
            field_dict["abbr"] = abbr

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Team":
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        directory_name = d.pop("directory_name")

        friendly_name = d.pop("friendly_name")

        organization = d.pop("organization")

        abbr = d.pop("abbr", UNSET)

        team = Team(
            url=url,
            id=id,
            directory_name=directory_name,
            friendly_name=friendly_name,
            organization=organization,
            abbr=abbr,
        )

        team.additional_properties = d
        return team

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
