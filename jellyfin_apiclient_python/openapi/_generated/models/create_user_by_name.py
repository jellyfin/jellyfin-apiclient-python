from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserByName")


@_attrs_define
class CreateUserByName:
    """The create user by name request body.

    Attributes:
        name (str): Gets or sets the username.
        password (None | str | Unset): Gets or sets the password.
    """

    name: str
    password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Name": name,
            }
        )
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name")

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("Password", UNSET))

        create_user_by_name = cls(
            name=name,
            password=password,
        )

        return create_user_by_name
