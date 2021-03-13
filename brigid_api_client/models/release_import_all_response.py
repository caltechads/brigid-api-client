from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.release_import_all_response_errors import ReleaseImportAllResponseErrors

T = TypeVar("T", bound="ReleaseImportAllResponse")


@attr.s(auto_attribs=True)
class ReleaseImportAllResponse:
    """  """

    status: None
    messages: str
    errors: ReleaseImportAllResponseErrors
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = None

        messages = self.messages
        errors = self.errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "messages": messages,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = None

        messages = d.pop("messages")

        errors = ReleaseImportAllResponseErrors.from_dict(d.pop("errors"))

        release_import_all_response = cls(
            status=status,
            messages=messages,
            errors=errors,
        )

        release_import_all_response.additional_properties = d
        return release_import_all_response

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
