from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewGroupRequestDto")


@_attrs_define
class NewGroupRequestDto:
    """Class NewGroupRequestDto.

    Attributes:
        group_name (str | Unset): Gets or sets the group name.
    """

    group_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_name = self.group_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_name = d.pop("GroupName", UNSET)

        new_group_request_dto = cls(
            group_name=group_name,
        )

        return new_group_request_dto
