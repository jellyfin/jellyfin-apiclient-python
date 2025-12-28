from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.group_state_type import GroupStateType
from ..models.playback_request_type import PlaybackRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupStateUpdate")


@_attrs_define
class GroupStateUpdate:
    """Class GroupStateUpdate.

    Attributes:
        state (GroupStateType | Unset): Enum GroupState.
        reason (PlaybackRequestType | Unset): Enum PlaybackRequestType.
    """

    state: GroupStateType | Unset = UNSET
    reason: PlaybackRequestType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if state is not UNSET:
            field_dict["State"] = state
        if reason is not UNSET:
            field_dict["Reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("State", UNSET)
        state: GroupStateType | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GroupStateType(_state)

        _reason = d.pop("Reason", UNSET)
        reason: PlaybackRequestType | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PlaybackRequestType(_reason)

        group_state_update = cls(
            state=state,
            reason=reason,
        )

        return group_state_update
