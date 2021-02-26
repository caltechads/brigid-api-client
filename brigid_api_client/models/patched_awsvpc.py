import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAWSVPC")


@attr.s(auto_attribs=True)
class PatchedAWSVPC:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    aws_account: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    cidr_range: Union[Unset, str] = UNSET
    team: Union[Unset, str] = UNSET
    contacts: Union[Unset, List[str]] = UNSET
    aws_ecs_clusters: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        aws_account = self.aws_account
        name = self.name
        cidr_range = self.cidr_range
        team = self.team
        contacts: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts

        aws_ecs_clusters: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_ecs_clusters, Unset):
            aws_ecs_clusters = self.aws_ecs_clusters

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
        if aws_account is not UNSET:
            field_dict["aws_account"] = aws_account
        if name is not UNSET:
            field_dict["name"] = name
        if cidr_range is not UNSET:
            field_dict["cidr_range"] = cidr_range
        if team is not UNSET:
            field_dict["team"] = team
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if aws_ecs_clusters is not UNSET:
            field_dict["aws_ecs_clusters"] = aws_ecs_clusters
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        aws_account = d.pop("aws_account", UNSET)

        name = d.pop("name", UNSET)

        cidr_range = d.pop("cidr_range", UNSET)

        team = d.pop("team", UNSET)

        contacts = cast(List[str], d.pop("contacts", UNSET))

        aws_ecs_clusters = cast(List[str], d.pop("aws_ecs_clusters", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_awsvpc = cls(
            url=url,
            id=id,
            aws_account=aws_account,
            name=name,
            cidr_range=cidr_range,
            team=team,
            contacts=contacts,
            aws_ecs_clusters=aws_ecs_clusters,
            created=created,
        )

        patched_awsvpc.additional_properties = d
        return patched_awsvpc

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
