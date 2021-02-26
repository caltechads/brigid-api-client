import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPipeline")


@attr.s(auto_attribs=True)
class PatchedPipeline:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    aws_account: Union[Unset, str] = UNSET
    application: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    pipeline_invocations: Union[Unset, List[str]] = UNSET
    steps: Union[Unset, List[str]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        aws_account = self.aws_account
        application = self.application
        name = self.name
        arn = self.arn
        pipeline_invocations: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.pipeline_invocations, Unset):
            pipeline_invocations = self.pipeline_invocations

        steps: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps

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
        if application is not UNSET:
            field_dict["application"] = application
        if name is not UNSET:
            field_dict["name"] = name
        if arn is not UNSET:
            field_dict["arn"] = arn
        if pipeline_invocations is not UNSET:
            field_dict["pipeline_invocations"] = pipeline_invocations
        if steps is not UNSET:
            field_dict["steps"] = steps
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        aws_account = d.pop("aws_account", UNSET)

        application = d.pop("application", UNSET)

        name = d.pop("name", UNSET)

        arn = d.pop("arn", UNSET)

        pipeline_invocations = cast(List[str], d.pop("pipeline_invocations", UNSET))

        steps = cast(List[str], d.pop("steps", UNSET))

        created: Union[Unset, datetime.datetime] = UNSET
        _created = d.pop("created", UNSET)
        if not isinstance(_created, Unset):
            created = isoparse(_created)

        patched_pipeline = cls(
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

        patched_pipeline.additional_properties = d
        return patched_pipeline

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
