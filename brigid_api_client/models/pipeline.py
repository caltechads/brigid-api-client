import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Pipeline")


@attr.s(auto_attribs=True)
class Pipeline:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    aws_account: str
    application: str
    name: str
    arn: str
    pipeline_invocations: List[str]
    steps: List[str]
    created: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        aws_account = self.aws_account
        application = self.application
        name = self.name
        arn = self.arn
        pipeline_invocations = self.pipeline_invocations

        steps = self.steps

        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "aws_account": aws_account,
                "application": application,
                "name": name,
                "arn": arn,
                "pipeline_invocations": pipeline_invocations,
                "steps": steps,
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

        application = d.pop("application")

        name = d.pop("name")

        arn = d.pop("arn")

        pipeline_invocations = cast(List[str], d.pop("pipeline_invocations"))

        steps = cast(List[str], d.pop("steps"))

        created = isoparse(d.pop("created"))

        pipeline = cls(
            url=url,
            id=id,
            aws_account=aws_account,
            application=application,
            name=name,
            arn=arn,
            pipeline_invocations=pipeline_invocations,
            steps=steps,
            created=created,
        )

        pipeline.additional_properties = d
        return pipeline

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
