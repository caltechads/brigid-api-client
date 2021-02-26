import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedStep")


@attr.s(auto_attribs=True)
class PatchedStep:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    step_type: Union[Unset, str] = UNSET
    pipeline: Union[Unset, str] = UNSET
    predecessor: Union[Unset, str] = UNSET
    decendents: Union[Unset, List[str]] = UNSET
    step_invocations: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        step_type = self.step_type
        pipeline = self.pipeline
        predecessor = self.predecessor
        decendents: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.decendents, Unset):
            decendents = self.decendents

        step_invocations: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.step_invocations, Unset):
            step_invocations = self.step_invocations

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
        if step_type is not UNSET:
            field_dict["step_type"] = step_type
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if predecessor is not UNSET:
            field_dict["predecessor"] = predecessor
        if decendents is not UNSET:
            field_dict["decendents"] = decendents
        if step_invocations is not UNSET:
            field_dict["step_invocations"] = step_invocations
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        step_type = d.pop("step_type", UNSET)

        pipeline = d.pop("pipeline", UNSET)

        predecessor = d.pop("predecessor", UNSET)

        decendents = cast(List[str], d.pop("decendents", UNSET))

        step_invocations = cast(List[str], d.pop("step_invocations", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_step = cls(
            url=url,
            id=id,
            step_type=step_type,
            pipeline=pipeline,
            predecessor=predecessor,
            decendents=decendents,
            step_invocations=step_invocations,
            created=created,
        )

        patched_step.additional_properties = d
        return patched_step

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
