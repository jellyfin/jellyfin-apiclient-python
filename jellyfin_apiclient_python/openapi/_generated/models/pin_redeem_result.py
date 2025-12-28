from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PinRedeemResult")


@_attrs_define
class PinRedeemResult:
    """
    Attributes:
        success (bool | Unset): Gets or sets a value indicating whether this MediaBrowser.Model.Users.PinRedeemResult is
            success.
        users_reset (list[str] | Unset): Gets or sets the users reset.
    """

    success: bool | Unset = UNSET
    users_reset: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        users_reset: list[str] | Unset = UNSET
        if not isinstance(self.users_reset, Unset):
            users_reset = self.users_reset

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success is not UNSET:
            field_dict["Success"] = success
        if users_reset is not UNSET:
            field_dict["UsersReset"] = users_reset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("Success", UNSET)

        users_reset = cast(list[str], d.pop("UsersReset", UNSET))

        pin_redeem_result = cls(
            success=success,
            users_reset=users_reset,
        )

        return pin_redeem_result
