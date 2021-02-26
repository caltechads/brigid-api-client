import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="AWSVPC")


@attr.s(auto_attribs=True)
class AWSVPC:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    aws_account: str
    name: str
    cidr_range: str
    team: str
    contacts: List[str]
    aws_ecs_clusters: List[str]
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        aws_account = self.aws_account
        name = self.name
        cidr_range = self.cidr_range
        team = self.team
        contacts = self.contacts

        aws_ecs_clusters = self.aws_ecs_clusters

        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "aws_account": aws_account,
                "name": name,
                "cidr_range": cidr_range,
                "team": team,
                "contacts": contacts,
                "aws_ecs_clusters": aws_ecs_clusters,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        aws_account = d.pop("aws_account")

        name = d.pop("name")

        cidr_range = d.pop("cidr_range")

        team = d.pop("team")

        contacts = cast(List[str], d.pop("contacts"))

        aws_ecs_clusters = cast(List[str], d.pop("aws_ecs_clusters"))

        created = isoparse(d.pop("created"))

        awsvpc = cls(
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

        awsvpc.additional_properties = d
        return awsvpc

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
