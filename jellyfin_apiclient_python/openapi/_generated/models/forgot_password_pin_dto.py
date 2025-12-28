from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ForgotPasswordPinDto")


@_attrs_define
class ForgotPasswordPinDto:
    """Forgot Password Pin enter request body DTO.

    Attributes:
        pin (str): Gets or sets the entered pin to have the password reset.
    """

    pin: str

    def to_dict(self) -> dict[str, Any]:
        pin = self.pin

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Pin": pin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pin = d.pop("Pin")

        forgot_password_pin_dto = cls(
            pin=pin,
        )

        return forgot_password_pin_dto
