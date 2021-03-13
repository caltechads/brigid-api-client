from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReleaseImport")


@attr.s(auto_attribs=True)
class ReleaseImport:
    """  """

    software_id: int
    version: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        software_id = self.software_id
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "software_id": software_id,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        software_id = d.pop("software_id")

        version = d.pop("version")

        release_import = cls(
            software_id=software_id,
            version=version,
        )

        release_import.additional_properties = d
        return release_import

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
