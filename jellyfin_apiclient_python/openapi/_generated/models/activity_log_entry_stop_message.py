from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.session_message_type import SessionMessageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityLogEntryStopMessage")


@_attrs_define
class ActivityLogEntryStopMessage:
    """Activity log entry stop message.

    Attributes:
        message_type (SessionMessageType | Unset): The different kinds of messages that are used in the WebSocket api.
            Default: SessionMessageType.ACTIVITYLOGENTRYSTOP.
    """

    message_type: SessionMessageType | Unset = SessionMessageType.ACTIVITYLOGENTRYSTOP

    def to_dict(self) -> dict[str, Any]:
        message_type: str | Unset = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message_type is not UNSET:
            field_dict["MessageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _message_type = d.pop("MessageType", UNSET)
        message_type: SessionMessageType | Unset
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        activity_log_entry_stop_message = cls(
            message_type=message_type,
        )

        return activity_log_entry_stop_message
