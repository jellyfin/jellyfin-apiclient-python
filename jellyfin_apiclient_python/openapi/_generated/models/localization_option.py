from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizationOption")


@_attrs_define
class LocalizationOption:
    """
    Attributes:
        name (None | str | Unset):
        value (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value

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

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("Value", UNSET))

        localization_option = cls(
            name=name,
            value=value,
        )

        return localization_option
