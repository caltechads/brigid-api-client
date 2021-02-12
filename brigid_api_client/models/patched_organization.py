from typing import Any, Dict, List, Optional, Union, cast

import attr

from ..types import UNSET, Unset


@attr.s(auto_attribs=True)
class PatchedOrganization:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    directory_name: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    abbr: Union[Unset, Optional[str]] = UNSET
    teams: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        directory_name = self.directory_name
        friendly_name = self.friendly_name
        abbr = self.abbr
        teams: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if id is not UNSET:
            field_dict["id"] = id
        if directory_name is not UNSET:
            field_dict["directory_name"] = directory_name
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if abbr is not UNSET:
            field_dict["abbr"] = abbr
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "PatchedOrganization":
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        directory_name = d.pop("directory_name", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        abbr = d.pop("abbr", UNSET)

        teams = cast(List[str], d.pop("teams", UNSET))

        patched_organization = PatchedOrganization(
            url=url,
            id=id,
            directory_name=directory_name,
            friendly_name=friendly_name,
            abbr=abbr,
            teams=teams,
        )

        patched_organization.additional_properties = d
        return patched_organization

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
