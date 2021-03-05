import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="AWSAccount")


@attr.s(auto_attribs=True)
class AWSAccount:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    name: str
    account_number: int
    team: str
    contacts: List[str]
    pipelines: List[str]
    aws_vpcs: List[str]
    created: datetime.datetime
    modified: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        name = self.name
        account_number = self.account_number
        team = self.team
        contacts = self.contacts

        pipelines = self.pipelines

        aws_vpcs = self.aws_vpcs

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "name": name,
                "account_number": account_number,
                "team": team,
                "contacts": contacts,
                "pipelines": pipelines,
                "aws_vpcs": aws_vpcs,
                "created": created,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        name = d.pop("name")

        account_number = d.pop("account_number")

        team = d.pop("team")

        contacts = cast(List[str], d.pop("contacts"))

        pipelines = cast(List[str], d.pop("pipelines"))

        aws_vpcs = cast(List[str], d.pop("aws_vpcs"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        aws_account = cls(
            url=url,
            id=id,
            name=name,
            account_number=account_number,
            team=team,
            contacts=contacts,
            pipelines=pipelines,
            aws_vpcs=aws_vpcs,
            created=created,
            modified=modified,
        )

        aws_account.additional_properties = d
        return aws_account

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
