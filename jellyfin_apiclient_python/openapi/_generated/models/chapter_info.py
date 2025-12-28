from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChapterInfo")


@_attrs_define
class ChapterInfo:
    """Class ChapterInfo.

    Attributes:
        start_position_ticks (int | Unset): Gets or sets the start position ticks.
        name (None | str | Unset): Gets or sets the name.
        image_path (None | str | Unset): Gets or sets the image path.
        image_date_modified (datetime.datetime | Unset):
        image_tag (None | str | Unset):
    """

    start_position_ticks: int | Unset = UNSET
    name: None | str | Unset = UNSET
    image_path: None | str | Unset = UNSET
    image_date_modified: datetime.datetime | Unset = UNSET
    image_tag: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_position_ticks = self.start_position_ticks

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        image_path: None | str | Unset
        if isinstance(self.image_path, Unset):
            image_path = UNSET
        else:
            image_path = self.image_path

        image_date_modified: str | Unset = UNSET
        if not isinstance(self.image_date_modified, Unset):
            image_date_modified = self.image_date_modified.isoformat()

        image_tag: None | str | Unset
        if isinstance(self.image_tag, Unset):
            image_tag = UNSET
        else:
            image_tag = self.image_tag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if name is not UNSET:
            field_dict["Name"] = name
        if image_path is not UNSET:
            field_dict["ImagePath"] = image_path
        if image_date_modified is not UNSET:
            field_dict["ImageDateModified"] = image_date_modified
        if image_tag is not UNSET:
            field_dict["ImageTag"] = image_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_image_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_path = _parse_image_path(d.pop("ImagePath", UNSET))

        _image_date_modified = d.pop("ImageDateModified", UNSET)
        image_date_modified: datetime.datetime | Unset
        if isinstance(_image_date_modified, Unset):
            image_date_modified = UNSET
        else:
            image_date_modified = isoparse(_image_date_modified)

        def _parse_image_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_tag = _parse_image_tag(d.pop("ImageTag", UNSET))

        chapter_info = cls(
            start_position_ticks=start_position_ticks,
            name=name,
            image_path=image_path,
            image_date_modified=image_date_modified,
            image_tag=image_tag,
        )

        return chapter_info
