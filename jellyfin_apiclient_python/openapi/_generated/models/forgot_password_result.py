from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.forgot_password_action import ForgotPasswordAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForgotPasswordResult")


@_attrs_define
class ForgotPasswordResult:
    """
    Attributes:
        action (ForgotPasswordAction | Unset):
        pin_file (None | str | Unset): Gets or sets the pin file.
        pin_expiration_date (datetime.datetime | None | Unset): Gets or sets the pin expiration date.
    """

    action: ForgotPasswordAction | Unset = UNSET
    pin_file: None | str | Unset = UNSET
    pin_expiration_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        pin_file: None | str | Unset
        if isinstance(self.pin_file, Unset):
            pin_file = UNSET
        else:
            pin_file = self.pin_file

        pin_expiration_date: None | str | Unset
        if isinstance(self.pin_expiration_date, Unset):
            pin_expiration_date = UNSET
        elif isinstance(self.pin_expiration_date, datetime.datetime):
            pin_expiration_date = self.pin_expiration_date.isoformat()
        else:
            pin_expiration_date = self.pin_expiration_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if action is not UNSET:
            field_dict["Action"] = action
        if pin_file is not UNSET:
            field_dict["PinFile"] = pin_file
        if pin_expiration_date is not UNSET:
            field_dict["PinExpirationDate"] = pin_expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("Action", UNSET)
        action: ForgotPasswordAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ForgotPasswordAction(_action)

        def _parse_pin_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pin_file = _parse_pin_file(d.pop("PinFile", UNSET))

        def _parse_pin_expiration_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pin_expiration_date_type_0 = isoparse(data)

                return pin_expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pin_expiration_date = _parse_pin_expiration_date(
            d.pop("PinExpirationDate", UNSET)
        )

        forgot_password_result = cls(
            action=action,
            pin_file=pin_file,
            pin_expiration_date=pin_expiration_date,
        )

        return forgot_password_result
