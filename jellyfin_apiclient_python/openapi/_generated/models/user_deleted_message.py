from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.session_message_type import SessionMessageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDeletedMessage")


@_attrs_define
class UserDeletedMessage:
    """User deleted message.

    Attributes:
        data (UUID | Unset): Gets or sets the data.
        message_id (UUID | Unset): Gets or sets the message id.
        message_type (SessionMessageType | Unset): The different kinds of messages that are used in the WebSocket api.
            Default: SessionMessageType.USERDELETED.
    """

    data: UUID | Unset = UNSET
    message_id: UUID | Unset = UNSET
    message_type: SessionMessageType | Unset = SessionMessageType.USERDELETED

    def to_dict(self) -> dict[str, Any]:
        data: str | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = str(self.data)

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        message_type: str | Unset = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["Data"] = data
        if message_id is not UNSET:
            field_dict["MessageId"] = message_id
        if message_type is not UNSET:
            field_dict["MessageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _data = d.pop("Data", UNSET)
        data: UUID | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UUID(_data)

        _message_id = d.pop("MessageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id, Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)

        _message_type = d.pop("MessageType", UNSET)
        message_type: SessionMessageType | Unset
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        user_deleted_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return user_deleted_message
