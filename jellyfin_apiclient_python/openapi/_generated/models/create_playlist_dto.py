from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.create_playlist_dto_media_type import CreatePlaylistDtoMediaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="CreatePlaylistDto")


@_attrs_define
class CreatePlaylistDto:
    """Create new playlist dto.

    Attributes:
        name (str | Unset): Gets or sets the name of the new playlist.
        ids (list[UUID] | Unset): Gets or sets item ids to add to the playlist.
        user_id (None | Unset | UUID): Gets or sets the user id.
        media_type (CreatePlaylistDtoMediaType | Unset): Gets or sets the media type.
        users (list[PlaylistUserPermissions] | Unset): Gets or sets the playlist users.
        is_public (bool | Unset): Gets or sets a value indicating whether the playlist is public.
    """

    name: str | Unset = UNSET
    ids: list[UUID] | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    media_type: CreatePlaylistDtoMediaType | Unset = UNSET
    users: list[PlaylistUserPermissions] | Unset = UNSET
    is_public: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = str(ids_item_data)
                ids.append(ids_item)

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        media_type: str | Unset = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        is_public = self.is_public

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if users is not UNSET:
            field_dict["Users"] = users
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        _ids = d.pop("Ids", UNSET)
        ids: list[UUID] | Unset = UNSET
        if _ids is not UNSET:
            ids = []
            for ids_item_data in _ids:
                ids_item = UUID(ids_item_data)

                ids.append(ids_item)

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        _media_type = d.pop("MediaType", UNSET)
        media_type: CreatePlaylistDtoMediaType | Unset
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = CreatePlaylistDtoMediaType(_media_type)

        _users = d.pop("Users", UNSET)
        users: list[PlaylistUserPermissions] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = PlaylistUserPermissions.from_dict(users_item_data)

                users.append(users_item)

        is_public = d.pop("IsPublic", UNSET)

        create_playlist_dto = cls(
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
            users=users,
            is_public=is_public,
        )

        return create_playlist_dto
