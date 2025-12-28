from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="JoinGroupRequestDto")


@_attrs_define
class JoinGroupRequestDto:
    """Class JoinGroupRequestDto.

    Attributes:
        group_id (UUID | Unset): Gets or sets the group identifier.
    """

    group_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id

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

        join_group_request_dto = cls(
            group_id=group_id,
        )

        return join_group_request_dto
