import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTeam")


@attr.s(auto_attribs=True)
class PatchedTeam:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    directory_name: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    abbr: Union[Unset, Optional[str]] = UNSET
    organization: Union[Unset, str] = UNSET
    aws_accounts: Union[Unset, List[str]] = UNSET
    aws_vpcs: Union[Unset, List[str]] = UNSET
    owned_applications: Union[Unset, List[str]] = UNSET
    users: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        directory_name = self.directory_name
        friendly_name = self.friendly_name
        abbr = self.abbr
        organization = self.organization
        aws_accounts: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_accounts, Unset):
            aws_accounts = self.aws_accounts

        aws_vpcs: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_vpcs, Unset):
            aws_vpcs = self.aws_vpcs

        owned_applications: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.owned_applications, Unset):
            owned_applications = self.owned_applications

        users: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

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
        if directory_name is not UNSET:
            field_dict["directory_name"] = directory_name
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if abbr is not UNSET:
            field_dict["abbr"] = abbr
        if organization is not UNSET:
            field_dict["organization"] = organization
        if aws_accounts is not UNSET:
            field_dict["aws_accounts"] = aws_accounts
        if aws_vpcs is not UNSET:
            field_dict["aws_vpcs"] = aws_vpcs
        if owned_applications is not UNSET:
            field_dict["owned_applications"] = owned_applications
        if users is not UNSET:
            field_dict["users"] = users
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        directory_name = d.pop("directory_name", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        abbr = d.pop("abbr", UNSET)

        organization = d.pop("organization", UNSET)

        aws_accounts = cast(List[str], d.pop("aws_accounts", UNSET))

        aws_vpcs = cast(List[str], d.pop("aws_vpcs", UNSET))

        owned_applications = cast(List[str], d.pop("owned_applications", UNSET))

        users = cast(List[str], d.pop("users", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_team = cls(
            url=url,
            id=id,
            directory_name=directory_name,
            friendly_name=friendly_name,
            abbr=abbr,
            organization=organization,
            aws_accounts=aws_accounts,
            aws_vpcs=aws_vpcs,
            owned_applications=owned_applications,
            users=users,
            created=created,
        )

        patched_team.additional_properties = d
        return patched_team

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
