from typing import Any, Dict, List, Optional, Union

import attr

from ..models.person_type import PersonType
from ..types import UNSET, Unset


@attr.s(auto_attribs=True)
class PaginatedPersonTypeList:
    """  """

    count: Union[Unset, int] = UNSET
    next: Union[Unset, Optional[str]] = UNSET
    previous: Union[Unset, Optional[str]] = UNSET
    results: Union[Unset, List[PersonType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        next = self.next
        previous = self.previous
        results: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if next is not UNSET:
            field_dict["next"] = next
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "PaginatedPersonTypeList":
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        next = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = PersonType.from_dict(results_item_data)

            results.append(results_item)

        paginated_person_type_list = PaginatedPersonTypeList(
            count=count,
            next=next,
            previous=previous,
            results=results,
        )

        paginated_person_type_list.additional_properties = d
        return paginated_person_type_list

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
