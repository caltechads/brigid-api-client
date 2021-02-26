import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAWSAccount")


@attr.s(auto_attribs=True)
class PatchedAWSAccount:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    account_number: Union[Unset, int] = UNSET
    team: Union[Unset, str] = UNSET
    contacts: Union[Unset, List[str]] = UNSET
    pipelines: Union[Unset, List[str]] = UNSET
    aws_vpcs: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        name = self.name
        account_number = self.account_number
        team = self.team
        contacts: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts

        pipelines: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.pipelines, Unset):
            pipelines = self.pipelines

        aws_vpcs: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_vpcs, Unset):
            aws_vpcs = self.aws_vpcs

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
        if name is not UNSET:
            field_dict["name"] = name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if team is not UNSET:
            field_dict["team"] = team
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if aws_vpcs is not UNSET:
            field_dict["aws_vpcs"] = aws_vpcs
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        account_number = d.pop("account_number", UNSET)

        team = d.pop("team", UNSET)

        contacts = cast(List[str], d.pop("contacts", UNSET))

        pipelines = cast(List[str], d.pop("pipelines", UNSET))

        aws_vpcs = cast(List[str], d.pop("aws_vpcs", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_aws_account = cls(
            url=url,
            id=id,
            name=name,
            account_number=account_number,
            team=team,
            contacts=contacts,
            pipelines=pipelines,
            aws_vpcs=aws_vpcs,
            created=created,
        )

        patched_aws_account.additional_properties = d
        return patched_aws_account

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
