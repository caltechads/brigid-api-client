import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="PipelineInvocation")


@attr.s(auto_attribs=True)
class PipelineInvocation:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    arn: str
    release: str
    pipeline: str
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        arn = self.arn
        release = self.release
        pipeline = self.pipeline
        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "arn": arn,
                "release": release,
                "pipeline": pipeline,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        arn = d.pop("arn")

        release = d.pop("release")

        pipeline = d.pop("pipeline")

        created = isoparse(d.pop("created"))

        pipeline_invocation = cls(
            url=url,
            id=id,
            arn=arn,
            release=release,
            pipeline=pipeline,
            created=created,
        )

        pipeline_invocation.additional_properties = d
        return pipeline_invocation

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
