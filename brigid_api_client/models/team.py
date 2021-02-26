import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Team")


@attr.s(auto_attribs=True)
class Team:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    directory_name: str
    friendly_name: str
    organization: str
    aws_accounts: List[str]
    aws_vpcs: List[str]
    owned_applications: List[str]
    users: List[str]
    created: datetime.datetime
    abbr: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        directory_name = self.directory_name
        friendly_name = self.friendly_name
        organization = self.organization
        aws_accounts = self.aws_accounts

        aws_vpcs = self.aws_vpcs

        owned_applications = self.owned_applications

        users = self.users

        created = self.created.isoformat()

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
                "aws_accounts": aws_accounts,
                "aws_vpcs": aws_vpcs,
                "owned_applications": owned_applications,
                "users": users,
                "created": created,
            }
        )
        if abbr is not UNSET:
            field_dict["abbr"] = abbr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        directory_name = d.pop("directory_name")

        friendly_name = d.pop("friendly_name")

        organization = d.pop("organization")

        aws_accounts = cast(List[str], d.pop("aws_accounts"))

        aws_vpcs = cast(List[str], d.pop("aws_vpcs"))

        owned_applications = cast(List[str], d.pop("owned_applications"))

        users = cast(List[str], d.pop("users"))

        created = isoparse(d.pop("created"))

        abbr = d.pop("abbr", UNSET)

        team = cls(
            url=url,
            id=id,
            directory_name=directory_name,
            friendly_name=friendly_name,
            organization=organization,
            aws_accounts=aws_accounts,
            aws_vpcs=aws_vpcs,
            owned_applications=owned_applications,
            users=users,
            created=created,
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
