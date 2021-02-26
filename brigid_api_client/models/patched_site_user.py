import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSiteUser")


@attr.s(auto_attribs=True)
class PatchedSiteUser:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    fullname: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    employee_number: Union[Unset, Optional[int]] = UNSET
    caltech_status: Union[Unset, Optional[str]] = UNSET
    person_types: Union[Unset, List[str]] = UNSET
    team: Union[Unset, str] = UNSET
    notes: Union[Unset, Optional[str]] = UNSET
    aws_accounts: Union[Unset, List[str]] = UNSET
    aws_vpcs: Union[Unset, List[str]] = UNSET
    owned_applications: Union[Unset, List[str]] = UNSET
    step_invocations: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        fullname = self.fullname
        email = self.email
        is_active = self.is_active
        date_joined: Union[Unset, str] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        employee_number = self.employee_number
        caltech_status = self.caltech_status
        person_types: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.person_types, Unset):
            person_types = self.person_types

        team = self.team
        notes = self.notes
        aws_accounts: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_accounts, Unset):
            aws_accounts = self.aws_accounts

        aws_vpcs: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.aws_vpcs, Unset):
            aws_vpcs = self.aws_vpcs

        owned_applications: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.owned_applications, Unset):
            owned_applications = self.owned_applications

        step_invocations: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.step_invocations, Unset):
            step_invocations = self.step_invocations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if fullname is not UNSET:
            field_dict["fullname"] = fullname
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if employee_number is not UNSET:
            field_dict["employee_number"] = employee_number
        if caltech_status is not UNSET:
            field_dict["caltech_status"] = caltech_status
        if person_types is not UNSET:
            field_dict["person_types"] = person_types
        if team is not UNSET:
            field_dict["team"] = team
        if notes is not UNSET:
            field_dict["notes"] = notes
        if aws_accounts is not UNSET:
            field_dict["aws_accounts"] = aws_accounts
        if aws_vpcs is not UNSET:
            field_dict["aws_vpcs"] = aws_vpcs
        if owned_applications is not UNSET:
            field_dict["owned_applications"] = owned_applications
        if step_invocations is not UNSET:
            field_dict["step_invocations"] = step_invocations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        fullname = d.pop("fullname", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        date_joined: Union[Unset, datetime.datetime] = UNSET
        _date_joined = d.pop("date_joined", UNSET)
        if not isinstance(_date_joined, Unset):
            date_joined = isoparse(_date_joined)

        employee_number = d.pop("employee_number", UNSET)

        caltech_status = d.pop("caltech_status", UNSET)

        person_types = cast(List[str], d.pop("person_types", UNSET))

        team = d.pop("team", UNSET)

        notes = d.pop("notes", UNSET)

        aws_accounts = cast(List[str], d.pop("aws_accounts", UNSET))

        aws_vpcs = cast(List[str], d.pop("aws_vpcs", UNSET))

        owned_applications = cast(List[str], d.pop("owned_applications", UNSET))

        step_invocations = cast(List[str], d.pop("step_invocations", UNSET))

        patched_site_user = cls(
            url=url,
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            fullname=fullname,
            email=email,
            is_active=is_active,
            date_joined=date_joined,
            employee_number=employee_number,
            caltech_status=caltech_status,
            person_types=person_types,
            team=team,
            notes=notes,
            aws_accounts=aws_accounts,
            aws_vpcs=aws_vpcs,
            owned_applications=owned_applications,
            step_invocations=step_invocations,
        )

        patched_site_user.additional_properties = d
        return patched_site_user

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
