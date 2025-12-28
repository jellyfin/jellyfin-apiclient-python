from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.group_shuffle_mode import GroupShuffleMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetShuffleModeRequestDto")


@_attrs_define
class SetShuffleModeRequestDto:
    """Class SetShuffleModeRequestDto.

    Attributes:
        mode (GroupShuffleMode | Unset): Enum GroupShuffleMode.
    """

    mode: GroupShuffleMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("Mode", UNSET)
        mode: GroupShuffleMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupShuffleMode(_mode)

        set_shuffle_mode_request_dto = cls(
            mode=mode,
        )

        return set_shuffle_mode_request_dto
