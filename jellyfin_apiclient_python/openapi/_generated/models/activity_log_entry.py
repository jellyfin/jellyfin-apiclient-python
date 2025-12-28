from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.log_level import LogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityLogEntry")


@_attrs_define
class ActivityLogEntry:
    """An activity log entry.

    Attributes:
        id (int | Unset): Gets or sets the identifier.
        name (str | Unset): Gets or sets the name.
        overview (None | str | Unset): Gets or sets the overview.
        short_overview (None | str | Unset): Gets or sets the short overview.
        type_ (str | Unset): Gets or sets the type.
        item_id (None | str | Unset): Gets or sets the item identifier.
        date (datetime.datetime | Unset): Gets or sets the date.
        user_id (UUID | Unset): Gets or sets the user identifier.
        user_primary_image_tag (None | str | Unset): Gets or sets the user primary image tag.
        severity (LogLevel | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    overview: None | str | Unset = UNSET
    short_overview: None | str | Unset = UNSET
    type_: str | Unset = UNSET
    item_id: None | str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    user_id: UUID | Unset = UNSET
    user_primary_image_tag: None | str | Unset = UNSET
    severity: LogLevel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        overview: None | str | Unset
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        short_overview: None | str | Unset
        if isinstance(self.short_overview, Unset):
            short_overview = UNSET
        else:
            short_overview = self.short_overview

        type_ = self.type_

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        user_primary_image_tag: None | str | Unset
        if isinstance(self.user_primary_image_tag, Unset):
            user_primary_image_tag = UNSET
        else:
            user_primary_image_tag = self.user_primary_image_tag

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if short_overview is not UNSET:
            field_dict["ShortOverview"] = short_overview
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if date is not UNSET:
            field_dict["Date"] = date
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_primary_image_tag is not UNSET:
            field_dict["UserPrimaryImageTag"] = user_primary_image_tag
        if severity is not UNSET:
            field_dict["Severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        def _parse_overview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overview = _parse_overview(d.pop("Overview", UNSET))

        def _parse_short_overview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_overview = _parse_short_overview(d.pop("ShortOverview", UNSET))

        type_ = d.pop("Type", UNSET)

        def _parse_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_id = _parse_item_id(d.pop("ItemId", UNSET))

        _date = d.pop("Date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _user_id = d.pop("UserId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        def _parse_user_primary_image_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_primary_image_tag = _parse_user_primary_image_tag(
            d.pop("UserPrimaryImageTag", UNSET)
        )

        _severity = d.pop("Severity", UNSET)
        severity: LogLevel | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = LogLevel(_severity)

        activity_log_entry = cls(
            id=id,
            name=name,
            overview=overview,
            short_overview=short_overview,
            type_=type_,
            item_id=item_id,
            date=date,
            user_id=user_id,
            user_primary_image_tag=user_primary_image_tag,
            severity=severity,
        )

        return activity_log_entry
