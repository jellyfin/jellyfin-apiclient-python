from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IgnoreWaitRequestDto")


@_attrs_define
class IgnoreWaitRequestDto:
    """Class IgnoreWaitRequestDto.

    Attributes:
        ignore_wait (bool | Unset): Gets or sets a value indicating whether the client should be ignored.
    """

    ignore_wait: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ignore_wait = self.ignore_wait

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ignore_wait is not UNSET:
            field_dict["IgnoreWait"] = ignore_wait

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_wait = d.pop("IgnoreWait", UNSET)

        ignore_wait_request_dto = cls(
            ignore_wait=ignore_wait,
        )

        return ignore_wait_request_dto
