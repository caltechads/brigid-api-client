import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestResult")


@attr.s(auto_attribs=True)
class TestResult:
    """Dynamically removes fields from serializer.
    https://stackoverflow.com/questions/27935558/dynamically-exclude-or-include-a-field-in-django-rest-framework-serializer"""

    url: str
    id: int
    release: str
    results_url: str
    created: datetime.datetime
    passed: Union[Unset, Optional[bool]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        release = self.release
        results_url = self.results_url
        created = self.created.isoformat()

        passed = self.passed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "release": release,
                "results_url": results_url,
                "created": created,
            }
        )
        if passed is not UNSET:
            field_dict["passed"] = passed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        release = d.pop("release")

        results_url = d.pop("results_url")

        created = isoparse(d.pop("created"))

        passed = d.pop("passed", UNSET)

        test_result = cls(
            url=url,
            id=id,
            release=release,
            results_url=results_url,
            created=created,
            passed=passed,
        )

        test_result.additional_properties = d
        return test_result

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
