import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteUser")


@attr.s(auto_attribs=True)
class SiteUser:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    username: str
    fullname: str
    date_joined: datetime.datetime
    person_types: List[str]
    team: str
    aws_accounts: List[str]
    aws_vpcs: List[str]
    owned_applications: List[str]
    step_invocations: List[str]
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    employee_number: Union[Unset, Optional[int]] = UNSET
    caltech_status: Union[Unset, Optional[str]] = UNSET
    notes: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        username = self.username
        fullname = self.fullname
        date_joined = self.date_joined.isoformat()

        person_types = self.person_types

        team = self.team
        aws_accounts = self.aws_accounts

        aws_vpcs = self.aws_vpcs

        owned_applications = self.owned_applications

        step_invocations = self.step_invocations

        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        is_active = self.is_active
        employee_number = self.employee_number
        caltech_status = self.caltech_status
        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "username": username,
                "fullname": fullname,
                "date_joined": date_joined,
                "person_types": person_types,
                "team": team,
                "aws_accounts": aws_accounts,
                "aws_vpcs": aws_vpcs,
                "owned_applications": owned_applications,
                "step_invocations": step_invocations,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if employee_number is not UNSET:
            field_dict["employee_number"] = employee_number
        if caltech_status is not UNSET:
            field_dict["caltech_status"] = caltech_status
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        username = d.pop("username")

        fullname = d.pop("fullname")

        date_joined = isoparse(d.pop("date_joined"))

        person_types = cast(List[str], d.pop("person_types"))

        team = d.pop("team")

        aws_accounts = cast(List[str], d.pop("aws_accounts"))

        aws_vpcs = cast(List[str], d.pop("aws_vpcs"))

        owned_applications = cast(List[str], d.pop("owned_applications"))

        step_invocations = cast(List[str], d.pop("step_invocations"))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        employee_number = d.pop("employee_number", UNSET)

        caltech_status = d.pop("caltech_status", UNSET)

        notes = d.pop("notes", UNSET)

        site_user = cls(
            url=url,
            id=id,
            username=username,
            fullname=fullname,
            date_joined=date_joined,
            person_types=person_types,
            team=team,
            aws_accounts=aws_accounts,
            aws_vpcs=aws_vpcs,
            owned_applications=owned_applications,
            step_invocations=step_invocations,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            employee_number=employee_number,
            caltech_status=caltech_status,
            notes=notes,
        )

        site_user.additional_properties = d
        return site_user

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
