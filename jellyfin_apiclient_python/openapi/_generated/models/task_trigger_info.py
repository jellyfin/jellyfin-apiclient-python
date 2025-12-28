from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.task_trigger_info_day_of_week import TaskTriggerInfoDayOfWeek
from ..models.task_trigger_info_type import TaskTriggerInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTriggerInfo")


@_attrs_define
class TaskTriggerInfo:
    """Class TaskTriggerInfo.

    Attributes:
        type_ (TaskTriggerInfoType | Unset): Enum TaskTriggerInfoType.
        time_of_day_ticks (int | None | Unset): Gets or sets the time of day.
        interval_ticks (int | None | Unset): Gets or sets the interval.
        day_of_week (TaskTriggerInfoDayOfWeek | Unset): Gets or sets the day of week.
        max_runtime_ticks (int | None | Unset): Gets or sets the maximum runtime ticks.
    """

    type_: TaskTriggerInfoType | Unset = UNSET
    time_of_day_ticks: int | None | Unset = UNSET
    interval_ticks: int | None | Unset = UNSET
    day_of_week: TaskTriggerInfoDayOfWeek | Unset = UNSET
    max_runtime_ticks: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        time_of_day_ticks: int | None | Unset
        if isinstance(self.time_of_day_ticks, Unset):
            time_of_day_ticks = UNSET
        else:
            time_of_day_ticks = self.time_of_day_ticks

        interval_ticks: int | None | Unset
        if isinstance(self.interval_ticks, Unset):
            interval_ticks = UNSET
        else:
            interval_ticks = self.interval_ticks

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        max_runtime_ticks: int | None | Unset
        if isinstance(self.max_runtime_ticks, Unset):
            max_runtime_ticks = UNSET
        else:
            max_runtime_ticks = self.max_runtime_ticks

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if time_of_day_ticks is not UNSET:
            field_dict["TimeOfDayTicks"] = time_of_day_ticks
        if interval_ticks is not UNSET:
            field_dict["IntervalTicks"] = interval_ticks
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if max_runtime_ticks is not UNSET:
            field_dict["MaxRuntimeTicks"] = max_runtime_ticks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("Type", UNSET)
        type_: TaskTriggerInfoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskTriggerInfoType(_type_)

        def _parse_time_of_day_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_of_day_ticks = _parse_time_of_day_ticks(d.pop("TimeOfDayTicks", UNSET))

        def _parse_interval_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interval_ticks = _parse_interval_ticks(d.pop("IntervalTicks", UNSET))

        _day_of_week = d.pop("DayOfWeek", UNSET)
        day_of_week: TaskTriggerInfoDayOfWeek | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = TaskTriggerInfoDayOfWeek(_day_of_week)

        def _parse_max_runtime_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_runtime_ticks = _parse_max_runtime_ticks(d.pop("MaxRuntimeTicks", UNSET))

        task_trigger_info = cls(
            type_=type_,
            time_of_day_ticks=time_of_day_ticks,
            interval_ticks=interval_ticks,
            day_of_week=day_of_week,
            max_runtime_ticks=max_runtime_ticks,
        )

        return task_trigger_info
