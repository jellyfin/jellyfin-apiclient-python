from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartupUserDto")


@_attrs_define
class StartupUserDto:
    """The startup user DTO.

    Attributes:
        name (None | str | Unset): Gets or sets the username.
        password (None | str | Unset): Gets or sets the user's password.
    """

    name: None | str | Unset = UNSET
    password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("Password", UNSET))

        startup_user_dto = cls(
            name=name,
            password=password,
        )

        return startup_user_dto
