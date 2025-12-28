from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="UpdatePlaylistDto")


@_attrs_define
class UpdatePlaylistDto:
    """Update existing playlist dto. Fields set to `null` will not be updated and keep their current values.

    Attributes:
        name (None | str | Unset): Gets or sets the name of the new playlist.
        ids (list[UUID] | None | Unset): Gets or sets item ids of the playlist.
        users (list[PlaylistUserPermissions] | None | Unset): Gets or sets the playlist users.
        is_public (bool | None | Unset): Gets or sets a value indicating whether the playlist is public.
    """

    name: None | str | Unset = UNSET
    ids: list[UUID] | None | Unset = UNSET
    users: list[PlaylistUserPermissions] | None | Unset = UNSET
    is_public: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ids: list[str] | None | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = []
            for ids_type_0_item_data in self.ids:
                ids_type_0_item = str(ids_type_0_item_data)
                ids.append(ids_type_0_item)

        else:
            ids = self.ids

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        is_public: bool | None | Unset
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if users is not UNSET:
            field_dict["Users"] = users
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = []
                _ids_type_0 = data
                for ids_type_0_item_data in _ids_type_0:
                    ids_type_0_item = UUID(ids_type_0_item_data)

                    ids_type_0.append(ids_type_0_item)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        ids = _parse_ids(d.pop("Ids", UNSET))

        def _parse_users(data: object) -> list[PlaylistUserPermissions] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = PlaylistUserPermissions.from_dict(
                        users_type_0_item_data
                    )

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlaylistUserPermissions] | None | Unset, data)

        users = _parse_users(d.pop("Users", UNSET))

        def _parse_is_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_public = _parse_is_public(d.pop("IsPublic", UNSET))

        update_playlist_dto = cls(
            name=name,
            ids=ids,
            users=users,
            is_public=is_public,
        )

        return update_playlist_dto
