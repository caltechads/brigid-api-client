import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Step")


@attr.s(auto_attribs=True)
class Step:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    step_type: str
    pipeline: str
    predecessor: str
    decendents: List[str]
    step_invocations: List[str]
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        step_type = self.step_type
        pipeline = self.pipeline
        predecessor = self.predecessor
        decendents = self.decendents

        step_invocations = self.step_invocations

        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "step_type": step_type,
                "pipeline": pipeline,
                "predecessor": predecessor,
                "decendents": decendents,
                "step_invocations": step_invocations,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        step_type = d.pop("step_type")

        pipeline = d.pop("pipeline")

        predecessor = d.pop("predecessor")

        decendents = cast(List[str], d.pop("decendents"))

        step_invocations = cast(List[str], d.pop("step_invocations"))

        created = isoparse(d.pop("created"))

        step = cls(
            url=url,
            id=id,
            step_type=step_type,
            pipeline=pipeline,
            predecessor=predecessor,
            decendents=decendents,
            step_invocations=step_invocations,
            created=created,
        )

        step.additional_properties = d
        return step

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
