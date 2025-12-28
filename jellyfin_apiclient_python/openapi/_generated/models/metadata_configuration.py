from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataConfiguration")


@_attrs_define
class MetadataConfiguration:
    """
    Attributes:
        use_file_creation_time_for_date_added (bool | Unset):
    """

    use_file_creation_time_for_date_added: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        use_file_creation_time_for_date_added = (
            self.use_file_creation_time_for_date_added
        )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if use_file_creation_time_for_date_added is not UNSET:
            field_dict["UseFileCreationTimeForDateAdded"] = (
                use_file_creation_time_for_date_added
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_file_creation_time_for_date_added = d.pop(
            "UseFileCreationTimeForDateAdded", UNSET
        )

        metadata_configuration = cls(
            use_file_creation_time_for_date_added=use_file_creation_time_for_date_added,
        )

        return metadata_configuration
