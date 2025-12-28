from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticateUserByName")


@_attrs_define
class AuthenticateUserByName:
    """The authenticate user by name request body.

    Attributes:
        username (None | str | Unset): Gets or sets the username.
        pw (None | str | Unset): Gets or sets the plain text password.
    """

    username: None | str | Unset = UNSET
    pw: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        pw: None | str | Unset
        if isinstance(self.pw, Unset):
            pw = UNSET
        else:
            pw = self.pw

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["Username"] = username
        if pw is not UNSET:
            field_dict["Pw"] = pw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("Username", UNSET))

        def _parse_pw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pw = _parse_pw(d.pop("Pw", UNSET))

        authenticate_user_by_name = cls(
            username=username,
            pw=pw,
        )

        return authenticate_user_by_name
