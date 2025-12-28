from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryUpdateInfo")


@_attrs_define
class LibraryUpdateInfo:
    """Class LibraryUpdateInfo.

    Attributes:
        folders_added_to (list[str] | Unset): Gets or sets the folders added to.
        folders_removed_from (list[str] | Unset): Gets or sets the folders removed from.
        items_added (list[str] | Unset): Gets or sets the items added.
        items_removed (list[str] | Unset): Gets or sets the items removed.
        items_updated (list[str] | Unset): Gets or sets the items updated.
        collection_folders (list[str] | Unset):
        is_empty (bool | Unset):
    """

    folders_added_to: list[str] | Unset = UNSET
    folders_removed_from: list[str] | Unset = UNSET
    items_added: list[str] | Unset = UNSET
    items_removed: list[str] | Unset = UNSET
    items_updated: list[str] | Unset = UNSET
    collection_folders: list[str] | Unset = UNSET
    is_empty: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        folders_added_to: list[str] | Unset = UNSET
        if not isinstance(self.folders_added_to, Unset):
            folders_added_to = self.folders_added_to

        folders_removed_from: list[str] | Unset = UNSET
        if not isinstance(self.folders_removed_from, Unset):
            folders_removed_from = self.folders_removed_from

        items_added: list[str] | Unset = UNSET
        if not isinstance(self.items_added, Unset):
            items_added = self.items_added

        items_removed: list[str] | Unset = UNSET
        if not isinstance(self.items_removed, Unset):
            items_removed = self.items_removed

        items_updated: list[str] | Unset = UNSET
        if not isinstance(self.items_updated, Unset):
            items_updated = self.items_updated

        collection_folders: list[str] | Unset = UNSET
        if not isinstance(self.collection_folders, Unset):
            collection_folders = self.collection_folders

        is_empty = self.is_empty

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if folders_added_to is not UNSET:
            field_dict["FoldersAddedTo"] = folders_added_to
        if folders_removed_from is not UNSET:
            field_dict["FoldersRemovedFrom"] = folders_removed_from
        if items_added is not UNSET:
            field_dict["ItemsAdded"] = items_added
        if items_removed is not UNSET:
            field_dict["ItemsRemoved"] = items_removed
        if items_updated is not UNSET:
            field_dict["ItemsUpdated"] = items_updated
        if collection_folders is not UNSET:
            field_dict["CollectionFolders"] = collection_folders
        if is_empty is not UNSET:
            field_dict["IsEmpty"] = is_empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folders_added_to = cast(list[str], d.pop("FoldersAddedTo", UNSET))

        folders_removed_from = cast(list[str], d.pop("FoldersRemovedFrom", UNSET))

        items_added = cast(list[str], d.pop("ItemsAdded", UNSET))

        items_removed = cast(list[str], d.pop("ItemsRemoved", UNSET))

        items_updated = cast(list[str], d.pop("ItemsUpdated", UNSET))

        collection_folders = cast(list[str], d.pop("CollectionFolders", UNSET))

        is_empty = d.pop("IsEmpty", UNSET)

        library_update_info = cls(
            folders_added_to=folders_added_to,
            folders_removed_from=folders_removed_from,
            items_added=items_added,
            items_removed=items_removed,
            items_updated=items_updated,
            collection_folders=collection_folders,
            is_empty=is_empty,
        )

        return library_update_info
