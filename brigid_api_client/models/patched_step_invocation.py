import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedStepInvocation")


@attr.s(auto_attribs=True)
class PatchedStepInvocation:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    step: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    invoker: Union[Unset, List[str]] = UNSET
    origin: Union[Unset, Optional[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        step = self.step
        release = self.release
        invoker: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.invoker, Unset):
            invoker = self.invoker

        origin = self.origin
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
        if step is not UNSET:
            field_dict["step"] = step
        if release is not UNSET:
            field_dict["release"] = release
        if invoker is not UNSET:
            field_dict["invoker"] = invoker
        if origin is not UNSET:
            field_dict["origin"] = origin
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        step = d.pop("step", UNSET)

        release = d.pop("release", UNSET)

        invoker = cast(List[str], d.pop("invoker", UNSET))

        origin = d.pop("origin", UNSET)

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_step_invocation = cls(
            url=url,
            id=id,
            step=step,
            release=release,
            invoker=invoker,
            origin=origin,
            created=created,
        )

        patched_step_invocation.additional_properties = d
        return patched_step_invocation

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
