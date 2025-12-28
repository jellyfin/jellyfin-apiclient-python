from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.session_message_type import SessionMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refresh_progress_message_data_type_0 import (
        RefreshProgressMessageDataType0,
    )


T = TypeVar("T", bound="RefreshProgressMessage")


@_attrs_define
class RefreshProgressMessage:
    """Refresh progress message.

    Attributes:
        data (None | RefreshProgressMessageDataType0 | Unset): Gets or sets the data.
        message_id (UUID | Unset): Gets or sets the message id.
        message_type (SessionMessageType | Unset): The different kinds of messages that are used in the WebSocket api.
            Default: SessionMessageType.REFRESHPROGRESS.
    """

    data: None | RefreshProgressMessageDataType0 | Unset = UNSET
    message_id: UUID | Unset = UNSET
    message_type: SessionMessageType | Unset = SessionMessageType.REFRESHPROGRESS

    def to_dict(self) -> dict[str, Any]:
        from ..models.refresh_progress_message_data_type_0 import (
            RefreshProgressMessageDataType0,
        )

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, RefreshProgressMessageDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

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
        from ..models.refresh_progress_message_data_type_0 import (
            RefreshProgressMessageDataType0,
        )

        d = dict(src_dict)

        def _parse_data(data: object) -> None | RefreshProgressMessageDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = RefreshProgressMessageDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RefreshProgressMessageDataType0 | Unset, data)

        data = _parse_data(d.pop("Data", UNSET))

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

        refresh_progress_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return refresh_progress_message
