from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.group_state_type import GroupStateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupInfoDto")


@_attrs_define
class GroupInfoDto:
    """Class GroupInfoDto.

    Attributes:
        group_id (UUID | Unset): Gets the group identifier.
        group_name (str | Unset): Gets the group name.
        state (GroupStateType | Unset): Enum GroupState.
        participants (list[str] | Unset): Gets the participants.
        last_updated_at (datetime.datetime | Unset): Gets the date when this DTO has been created.
    """

    group_id: UUID | Unset = UNSET
    group_name: str | Unset = UNSET
    state: GroupStateType | Unset = UNSET
    participants: list[str] | Unset = UNSET
    last_updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        group_name = self.group_name

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        participants: list[str] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants

        last_updated_at: str | Unset = UNSET
        if not isinstance(self.last_updated_at, Unset):
            last_updated_at = self.last_updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name
        if state is not UNSET:
            field_dict["State"] = state
        if participants is not UNSET:
            field_dict["Participants"] = participants
        if last_updated_at is not UNSET:
            field_dict["LastUpdatedAt"] = last_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _group_id = d.pop("GroupId", UNSET)
        group_id: UUID | Unset
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

        group_name = d.pop("GroupName", UNSET)

        _state = d.pop("State", UNSET)
        state: GroupStateType | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GroupStateType(_state)

        participants = cast(list[str], d.pop("Participants", UNSET))

        _last_updated_at = d.pop("LastUpdatedAt", UNSET)
        last_updated_at: datetime.datetime | Unset
        if isinstance(_last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = isoparse(_last_updated_at)

        group_info_dto = cls(
            group_id=group_id,
            group_name=group_name,
            state=state,
            participants=participants,
            last_updated_at=last_updated_at,
        )

        return group_info_dto
