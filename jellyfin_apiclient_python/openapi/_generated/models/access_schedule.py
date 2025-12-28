from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.dynamic_day_of_week import DynamicDayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessSchedule")


@_attrs_define
class AccessSchedule:
    """An entity representing a user's access schedule.

    Attributes:
        id (int | Unset): Gets the id of this instance.
        user_id (UUID | Unset): Gets the id of the associated user.
        day_of_week (DynamicDayOfWeek | Unset): An enum that represents a day of the week, weekdays, weekends, or all
            days.
        start_hour (float | Unset): Gets or sets the start hour.
        end_hour (float | Unset): Gets or sets the end hour.
    """

    id: int | Unset = UNSET
    user_id: UUID | Unset = UNSET
    day_of_week: DynamicDayOfWeek | Unset = UNSET
    start_hour: float | Unset = UNSET
    end_hour: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        start_hour = self.start_hour

        end_hour = self.end_hour

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if start_hour is not UNSET:
            field_dict["StartHour"] = start_hour
        if end_hour is not UNSET:
            field_dict["EndHour"] = end_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        _user_id = d.pop("UserId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        _day_of_week = d.pop("DayOfWeek", UNSET)
        day_of_week: DynamicDayOfWeek | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DynamicDayOfWeek(_day_of_week)

        start_hour = d.pop("StartHour", UNSET)

        end_hour = d.pop("EndHour", UNSET)

        access_schedule = cls(
            id=id,
            user_id=user_id,
            day_of_week=day_of_week,
            start_hour=start_hour,
            end_hour=end_hour,
        )

        return access_schedule
