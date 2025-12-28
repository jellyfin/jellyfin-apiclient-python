from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionUserInfo")


@_attrs_define
class SessionUserInfo:
    """Class SessionUserInfo.

    Attributes:
        user_id (UUID | Unset): Gets or sets the user identifier.
        user_name (None | str | Unset): Gets or sets the name of the user.
    """

    user_id: UUID | Unset = UNSET
    user_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_id = d.pop("UserId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("UserName", UNSET))

        session_user_info = cls(
            user_id=user_id,
            user_name=user_name,
        )

        return session_user_info
