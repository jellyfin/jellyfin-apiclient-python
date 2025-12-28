from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="PlaylistDto")


@_attrs_define
class PlaylistDto:
    """DTO for playlists.

    Attributes:
        open_access (bool | Unset): Gets or sets a value indicating whether the playlist is publicly readable.
        shares (list[PlaylistUserPermissions] | Unset): Gets or sets the share permissions.
        item_ids (list[UUID] | Unset): Gets or sets the item ids.
    """

    open_access: bool | Unset = UNSET
    shares: list[PlaylistUserPermissions] | Unset = UNSET
    item_ids: list[UUID] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        open_access = self.open_access

        shares: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shares, Unset):
            shares = []
            for shares_item_data in self.shares:
                shares_item = shares_item_data.to_dict()
                shares.append(shares_item)

        item_ids: list[str] | Unset = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = []
            for item_ids_item_data in self.item_ids:
                item_ids_item = str(item_ids_item_data)
                item_ids.append(item_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if open_access is not UNSET:
            field_dict["OpenAccess"] = open_access
        if shares is not UNSET:
            field_dict["Shares"] = shares
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        d = dict(src_dict)
        open_access = d.pop("OpenAccess", UNSET)

        _shares = d.pop("Shares", UNSET)
        shares: list[PlaylistUserPermissions] | Unset = UNSET
        if _shares is not UNSET:
            shares = []
            for shares_item_data in _shares:
                shares_item = PlaylistUserPermissions.from_dict(shares_item_data)

                shares.append(shares_item)

        _item_ids = d.pop("ItemIds", UNSET)
        item_ids: list[UUID] | Unset = UNSET
        if _item_ids is not UNSET:
            item_ids = []
            for item_ids_item_data in _item_ids:
                item_ids_item = UUID(item_ids_item_data)

                item_ids.append(item_ids_item)

        playlist_dto = cls(
            open_access=open_access,
            shares=shares,
            item_ids=item_ids,
        )

        return playlist_dto
