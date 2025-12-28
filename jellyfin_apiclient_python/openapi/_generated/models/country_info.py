from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountryInfo")


@_attrs_define
class CountryInfo:
    """Class CountryInfo.

    Attributes:
        name (None | str | Unset): Gets or sets the name.
        display_name (None | str | Unset): Gets or sets the display name.
        two_letter_iso_region_name (None | str | Unset): Gets or sets the name of the two letter ISO region.
        three_letter_iso_region_name (None | str | Unset): Gets or sets the name of the three letter ISO region.
    """

    name: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    two_letter_iso_region_name: None | str | Unset = UNSET
    three_letter_iso_region_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        two_letter_iso_region_name: None | str | Unset
        if isinstance(self.two_letter_iso_region_name, Unset):
            two_letter_iso_region_name = UNSET
        else:
            two_letter_iso_region_name = self.two_letter_iso_region_name

        three_letter_iso_region_name: None | str | Unset
        if isinstance(self.three_letter_iso_region_name, Unset):
            three_letter_iso_region_name = UNSET
        else:
            three_letter_iso_region_name = self.three_letter_iso_region_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if two_letter_iso_region_name is not UNSET:
            field_dict["TwoLetterISORegionName"] = two_letter_iso_region_name
        if three_letter_iso_region_name is not UNSET:
            field_dict["ThreeLetterISORegionName"] = three_letter_iso_region_name

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

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("DisplayName", UNSET))

        def _parse_two_letter_iso_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        two_letter_iso_region_name = _parse_two_letter_iso_region_name(
            d.pop("TwoLetterISORegionName", UNSET)
        )

        def _parse_three_letter_iso_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        three_letter_iso_region_name = _parse_three_letter_iso_region_name(
            d.pop("ThreeLetterISORegionName", UNSET)
        )

        country_info = cls(
            name=name,
            display_name=display_name,
            two_letter_iso_region_name=two_letter_iso_region_name,
            three_letter_iso_region_name=three_letter_iso_region_name,
        )

        return country_info
