from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CultureDto")


@_attrs_define
class CultureDto:
    """Class CultureDto.

    Attributes:
        name (str | Unset): Gets the name.
        display_name (str | Unset): Gets the display name.
        two_letter_iso_language_name (str | Unset): Gets the name of the two letter ISO language.
        three_letter_iso_language_name (None | str | Unset): Gets the name of the three letter ISO language.
        three_letter_iso_language_names (list[str] | Unset):
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    two_letter_iso_language_name: str | Unset = UNSET
    three_letter_iso_language_name: None | str | Unset = UNSET
    three_letter_iso_language_names: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        two_letter_iso_language_name = self.two_letter_iso_language_name

        three_letter_iso_language_name: None | str | Unset
        if isinstance(self.three_letter_iso_language_name, Unset):
            three_letter_iso_language_name = UNSET
        else:
            three_letter_iso_language_name = self.three_letter_iso_language_name

        three_letter_iso_language_names: list[str] | Unset = UNSET
        if not isinstance(self.three_letter_iso_language_names, Unset):
            three_letter_iso_language_names = self.three_letter_iso_language_names

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if two_letter_iso_language_name is not UNSET:
            field_dict["TwoLetterISOLanguageName"] = two_letter_iso_language_name
        if three_letter_iso_language_name is not UNSET:
            field_dict["ThreeLetterISOLanguageName"] = three_letter_iso_language_name
        if three_letter_iso_language_names is not UNSET:
            field_dict["ThreeLetterISOLanguageNames"] = three_letter_iso_language_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        two_letter_iso_language_name = d.pop("TwoLetterISOLanguageName", UNSET)

        def _parse_three_letter_iso_language_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        three_letter_iso_language_name = _parse_three_letter_iso_language_name(
            d.pop("ThreeLetterISOLanguageName", UNSET)
        )

        three_letter_iso_language_names = cast(
            list[str], d.pop("ThreeLetterISOLanguageNames", UNSET)
        )

        culture_dto = cls(
            name=name,
            display_name=display_name,
            two_letter_iso_language_name=two_letter_iso_language_name,
            three_letter_iso_language_name=three_letter_iso_language_name,
            three_letter_iso_language_names=three_letter_iso_language_names,
        )

        return culture_dto
