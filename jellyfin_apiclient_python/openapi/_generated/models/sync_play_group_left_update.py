from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.group_update_type import GroupUpdateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncPlayGroupLeftUpdate")


@_attrs_define
class SyncPlayGroupLeftUpdate:
    """
    Attributes:
        group_id (UUID | Unset): Gets the group identifier.
        data (str | Unset): Gets the update data.
        type_ (GroupUpdateType | Unset): Enum GroupUpdateType. Default: GroupUpdateType.GROUPLEFT.
    """

    group_id: UUID | Unset = UNSET
    data: str | Unset = UNSET
    type_: GroupUpdateType | Unset = GroupUpdateType.GROUPLEFT

    def to_dict(self) -> dict[str, Any]:
        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        data = self.data

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if data is not UNSET:
            field_dict["Data"] = data
        if type_ is not UNSET:
            field_dict["Type"] = type_

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

        data = d.pop("Data", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: GroupUpdateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GroupUpdateType(_type_)

        sync_play_group_left_update = cls(
            group_id=group_id,
            data=data,
            type_=type_,
        )

        return sync_play_group_left_update
