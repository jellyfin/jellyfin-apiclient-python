from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndPointInfo")


@_attrs_define
class EndPointInfo:
    """
    Attributes:
        is_local (bool | Unset):
        is_in_network (bool | Unset):
    """

    is_local: bool | Unset = UNSET
    is_in_network: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_local = self.is_local

        is_in_network = self.is_in_network

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_local is not UNSET:
            field_dict["IsLocal"] = is_local
        if is_in_network is not UNSET:
            field_dict["IsInNetwork"] = is_in_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_local = d.pop("IsLocal", UNSET)

        is_in_network = d.pop("IsInNetwork", UNSET)

        end_point_info = cls(
            is_local=is_local,
            is_in_network=is_in_network,
        )

        return end_point_info
