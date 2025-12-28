from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.task_completion_status import TaskCompletionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskResult")


@_attrs_define
class TaskResult:
    """Class TaskExecutionInfo.

    Attributes:
        start_time_utc (datetime.datetime | Unset): Gets or sets the start time UTC.
        end_time_utc (datetime.datetime | Unset): Gets or sets the end time UTC.
        status (TaskCompletionStatus | Unset): Enum TaskCompletionStatus.
        name (None | str | Unset): Gets or sets the name.
        key (None | str | Unset): Gets or sets the key.
        id (None | str | Unset): Gets or sets the id.
        error_message (None | str | Unset): Gets or sets the error message.
        long_error_message (None | str | Unset): Gets or sets the long error message.
    """

    start_time_utc: datetime.datetime | Unset = UNSET
    end_time_utc: datetime.datetime | Unset = UNSET
    status: TaskCompletionStatus | Unset = UNSET
    name: None | str | Unset = UNSET
    key: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    long_error_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_time_utc: str | Unset = UNSET
        if not isinstance(self.start_time_utc, Unset):
            start_time_utc = self.start_time_utc.isoformat()

        end_time_utc: str | Unset = UNSET
        if not isinstance(self.end_time_utc, Unset):
            end_time_utc = self.end_time_utc.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        long_error_message: None | str | Unset
        if isinstance(self.long_error_message, Unset):
            long_error_message = UNSET
        else:
            long_error_message = self.long_error_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_time_utc is not UNSET:
            field_dict["StartTimeUtc"] = start_time_utc
        if end_time_utc is not UNSET:
            field_dict["EndTimeUtc"] = end_time_utc
        if status is not UNSET:
            field_dict["Status"] = status
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if id is not UNSET:
            field_dict["Id"] = id
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if long_error_message is not UNSET:
            field_dict["LongErrorMessage"] = long_error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_time_utc = d.pop("StartTimeUtc", UNSET)
        start_time_utc: datetime.datetime | Unset
        if isinstance(_start_time_utc, Unset):
            start_time_utc = UNSET
        else:
            start_time_utc = isoparse(_start_time_utc)

        _end_time_utc = d.pop("EndTimeUtc", UNSET)
        end_time_utc: datetime.datetime | Unset
        if isinstance(_end_time_utc, Unset):
            end_time_utc = UNSET
        else:
            end_time_utc = isoparse(_end_time_utc)

        _status = d.pop("Status", UNSET)
        status: TaskCompletionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskCompletionStatus(_status)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("Key", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("ErrorMessage", UNSET))

        def _parse_long_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_error_message = _parse_long_error_message(d.pop("LongErrorMessage", UNSET))

        task_result = cls(
            start_time_utc=start_time_utc,
            end_time_utc=end_time_utc,
            status=status,
            name=name,
            key=key,
            id=id,
            error_message=error_message,
            long_error_message=long_error_message,
        )

        return task_result
