from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryOptionInfoDto")


@_attrs_define
class LibraryOptionInfoDto:
    """Library option info dto.

    Attributes:
        name (None | str | Unset): Gets or sets name.
        default_enabled (bool | Unset): Gets or sets a value indicating whether default enabled.
    """

    name: None | str | Unset = UNSET
    default_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        default_enabled = self.default_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if default_enabled is not UNSET:
            field_dict["DefaultEnabled"] = default_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        default_enabled = d.pop("DefaultEnabled", UNSET)

        library_option_info_dto = cls(
            name=name,
            default_enabled=default_enabled,
        )

        return library_option_info_dto
