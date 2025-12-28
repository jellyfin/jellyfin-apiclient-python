from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaylistUserPermissions")


@_attrs_define
class PlaylistUserPermissions:
    """Class to hold data on user permissions for playlists.

    Attributes:
        user_id (UUID | Unset): Gets or sets the user id.
        can_edit (bool | Unset): Gets or sets a value indicating whether the user has edit permissions.
    """

    user_id: UUID | Unset = UNSET
    can_edit: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        can_edit = self.can_edit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit

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

        can_edit = d.pop("CanEdit", UNSET)

        playlist_user_permissions = cls(
            user_id=user_id,
            can_edit=can_edit,
        )

        return playlist_user_permissions
