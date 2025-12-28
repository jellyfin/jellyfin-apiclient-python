from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserPassword")


@_attrs_define
class UpdateUserPassword:
    """The update user password request body.

    Attributes:
        current_password (None | str | Unset): Gets or sets the current sha1-hashed password.
        current_pw (None | str | Unset): Gets or sets the current plain text password.
        new_pw (None | str | Unset): Gets or sets the new plain text password.
        reset_password (bool | Unset): Gets or sets a value indicating whether to reset the password.
    """

    current_password: None | str | Unset = UNSET
    current_pw: None | str | Unset = UNSET
    new_pw: None | str | Unset = UNSET
    reset_password: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_password: None | str | Unset
        if isinstance(self.current_password, Unset):
            current_password = UNSET
        else:
            current_password = self.current_password

        current_pw: None | str | Unset
        if isinstance(self.current_pw, Unset):
            current_pw = UNSET
        else:
            current_pw = self.current_pw

        new_pw: None | str | Unset
        if isinstance(self.new_pw, Unset):
            new_pw = UNSET
        else:
            new_pw = self.new_pw

        reset_password = self.reset_password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if current_password is not UNSET:
            field_dict["CurrentPassword"] = current_password
        if current_pw is not UNSET:
            field_dict["CurrentPw"] = current_pw
        if new_pw is not UNSET:
            field_dict["NewPw"] = new_pw
        if reset_password is not UNSET:
            field_dict["ResetPassword"] = reset_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_current_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_password = _parse_current_password(d.pop("CurrentPassword", UNSET))

        def _parse_current_pw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_pw = _parse_current_pw(d.pop("CurrentPw", UNSET))

        def _parse_new_pw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_pw = _parse_new_pw(d.pop("NewPw", UNSET))

        reset_password = d.pop("ResetPassword", UNSET)

        update_user_password = cls(
            current_password=current_password,
            current_pw=current_pw,
            new_pw=new_pw,
            reset_password=reset_password,
        )

        return update_user_password
