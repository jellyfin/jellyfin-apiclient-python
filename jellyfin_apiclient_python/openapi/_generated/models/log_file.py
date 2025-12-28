from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogFile")


@_attrs_define
class LogFile:
    """
    Attributes:
        date_created (datetime.datetime | Unset): Gets or sets the date created.
        date_modified (datetime.datetime | Unset): Gets or sets the date modified.
        size (int | Unset): Gets or sets the size.
        name (str | Unset): Gets or sets the name.
    """

    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    size: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        size = self.size

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["DateModified"] = date_modified
        if size is not UNSET:
            field_dict["Size"] = size
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_created = d.pop("DateCreated", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_modified = d.pop("DateModified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        size = d.pop("Size", UNSET)

        name = d.pop("Name", UNSET)

        log_file = cls(
            date_created=date_created,
            date_modified=date_modified,
            size=size,
            name=name,
        )

        return log_file
