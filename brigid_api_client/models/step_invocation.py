import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StepInvocation")


@attr.s(auto_attribs=True)
class StepInvocation:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    step: str
    release: str
    invoker: List[str]
    created: datetime.datetime
    origin: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        step = self.step
        release = self.release
        invoker = self.invoker

        created = self.created.isoformat()

        origin = self.origin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "step": step,
                "release": release,
                "invoker": invoker,
                "created": created,
            }
        )
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        step = d.pop("step")

        release = d.pop("release")

        invoker = cast(List[str], d.pop("invoker"))

        created = isoparse(d.pop("created"))

        origin = d.pop("origin", UNSET)

        step_invocation = cls(
            url=url,
            id=id,
            step=step,
            release=release,
            invoker=invoker,
            created=created,
            origin=origin,
        )

        step_invocation.additional_properties = d
        return step_invocation

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
