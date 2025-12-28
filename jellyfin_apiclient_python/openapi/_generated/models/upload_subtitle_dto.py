from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UploadSubtitleDto")


@_attrs_define
class UploadSubtitleDto:
    """Upload subtitles dto.

    Attributes:
        language (str): Gets or sets the subtitle language.
        format_ (str): Gets or sets the subtitle format.
        is_forced (bool): Gets or sets a value indicating whether the subtitle is forced.
        is_hearing_impaired (bool): Gets or sets a value indicating whether the subtitle is for hearing impaired.
        data (str): Gets or sets the subtitle data.
    """

    language: str
    format_: str
    is_forced: bool
    is_hearing_impaired: bool
    data: str

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        format_ = self.format_

        is_forced = self.is_forced

        is_hearing_impaired = self.is_hearing_impaired

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Language": language,
                "Format": format_,
                "IsForced": is_forced,
                "IsHearingImpaired": is_hearing_impaired,
                "Data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("Language")

        format_ = d.pop("Format")

        is_forced = d.pop("IsForced")

        is_hearing_impaired = d.pop("IsHearingImpaired")

        data = d.pop("Data")

        upload_subtitle_dto = cls(
            language=language,
            format_=format_,
            is_forced=is_forced,
            is_hearing_impaired=is_hearing_impaired,
            data=data,
        )

        return upload_subtitle_dto
