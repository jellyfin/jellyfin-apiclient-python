from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.session_message_type import SessionMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_play_group_does_not_exist_update import (
        SyncPlayGroupDoesNotExistUpdate,
    )
    from ..models.sync_play_group_joined_update import SyncPlayGroupJoinedUpdate
    from ..models.sync_play_group_left_update import SyncPlayGroupLeftUpdate
    from ..models.sync_play_library_access_denied_update import (
        SyncPlayLibraryAccessDeniedUpdate,
    )
    from ..models.sync_play_not_in_group_update import SyncPlayNotInGroupUpdate
    from ..models.sync_play_play_queue_update import SyncPlayPlayQueueUpdate
    from ..models.sync_play_state_update import SyncPlayStateUpdate
    from ..models.sync_play_user_joined_update import SyncPlayUserJoinedUpdate
    from ..models.sync_play_user_left_update import SyncPlayUserLeftUpdate


T = TypeVar("T", bound="SyncPlayGroupUpdateMessage")


@_attrs_define
class SyncPlayGroupUpdateMessage:
    """Untyped sync play command.

    Attributes:
        data (SyncPlayGroupDoesNotExistUpdate | SyncPlayGroupJoinedUpdate | SyncPlayGroupLeftUpdate |
            SyncPlayLibraryAccessDeniedUpdate | SyncPlayNotInGroupUpdate | SyncPlayPlayQueueUpdate | SyncPlayStateUpdate |
            SyncPlayUserJoinedUpdate | SyncPlayUserLeftUpdate | Unset): Represents the list of possible group update types
        message_id (UUID | Unset): Gets or sets the message id.
        message_type (SessionMessageType | Unset): The different kinds of messages that are used in the WebSocket api.
            Default: SessionMessageType.SYNCPLAYGROUPUPDATE.
    """

    data: (
        SyncPlayGroupDoesNotExistUpdate
        | SyncPlayGroupJoinedUpdate
        | SyncPlayGroupLeftUpdate
        | SyncPlayLibraryAccessDeniedUpdate
        | SyncPlayNotInGroupUpdate
        | SyncPlayPlayQueueUpdate
        | SyncPlayStateUpdate
        | SyncPlayUserJoinedUpdate
        | SyncPlayUserLeftUpdate
        | Unset
    ) = UNSET
    message_id: UUID | Unset = UNSET
    message_type: SessionMessageType | Unset = SessionMessageType.SYNCPLAYGROUPUPDATE

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_play_group_does_not_exist_update import (
            SyncPlayGroupDoesNotExistUpdate,
        )
        from ..models.sync_play_group_joined_update import SyncPlayGroupJoinedUpdate
        from ..models.sync_play_group_left_update import SyncPlayGroupLeftUpdate
        from ..models.sync_play_library_access_denied_update import (
            SyncPlayLibraryAccessDeniedUpdate,
        )
        from ..models.sync_play_not_in_group_update import SyncPlayNotInGroupUpdate
        from ..models.sync_play_play_queue_update import SyncPlayPlayQueueUpdate
        from ..models.sync_play_state_update import SyncPlayStateUpdate
        from ..models.sync_play_user_joined_update import SyncPlayUserJoinedUpdate

        data: dict[str, Any] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, SyncPlayGroupDoesNotExistUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayGroupJoinedUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayGroupLeftUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayLibraryAccessDeniedUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayNotInGroupUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayPlayQueueUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayStateUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, SyncPlayUserJoinedUpdate):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

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
        from ..models.sync_play_group_does_not_exist_update import (
            SyncPlayGroupDoesNotExistUpdate,
        )
        from ..models.sync_play_group_joined_update import SyncPlayGroupJoinedUpdate
        from ..models.sync_play_group_left_update import SyncPlayGroupLeftUpdate
        from ..models.sync_play_library_access_denied_update import (
            SyncPlayLibraryAccessDeniedUpdate,
        )
        from ..models.sync_play_not_in_group_update import SyncPlayNotInGroupUpdate
        from ..models.sync_play_play_queue_update import SyncPlayPlayQueueUpdate
        from ..models.sync_play_state_update import SyncPlayStateUpdate
        from ..models.sync_play_user_joined_update import SyncPlayUserJoinedUpdate
        from ..models.sync_play_user_left_update import SyncPlayUserLeftUpdate

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> (
            SyncPlayGroupDoesNotExistUpdate
            | SyncPlayGroupJoinedUpdate
            | SyncPlayGroupLeftUpdate
            | SyncPlayLibraryAccessDeniedUpdate
            | SyncPlayNotInGroupUpdate
            | SyncPlayPlayQueueUpdate
            | SyncPlayStateUpdate
            | SyncPlayUserJoinedUpdate
            | SyncPlayUserLeftUpdate
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_0 = (
                    SyncPlayGroupDoesNotExistUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_1 = (
                    SyncPlayGroupJoinedUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_2 = (
                    SyncPlayGroupLeftUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_3 = (
                    SyncPlayLibraryAccessDeniedUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_4 = (
                    SyncPlayNotInGroupUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_5 = (
                    SyncPlayPlayQueueUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_6 = SyncPlayStateUpdate.from_dict(
                    data
                )

                return componentsschemas_group_update_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_7 = (
                    SyncPlayUserJoinedUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_group_update_type_8 = SyncPlayUserLeftUpdate.from_dict(
                data
            )

            return componentsschemas_group_update_type_8

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

        sync_play_group_update_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return sync_play_group_update_message
