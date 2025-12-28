from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_system_entry_type import FileSystemEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSystemEntryInfo")


@_attrs_define
class FileSystemEntryInfo:
    """Class FileSystemEntryInfo.

    Attributes:
        name (str | Unset): Gets the name.
        path (str | Unset): Gets the path.
        type_ (FileSystemEntryType | Unset): Enum FileSystemEntryType.
    """

    name: str | Unset = UNSET
    path: str | Unset = UNSET
    type_: FileSystemEntryType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if path is not UNSET:
            field_dict["Path"] = path
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        path = d.pop("Path", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: FileSystemEntryType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileSystemEntryType(_type_)

        file_system_entry_info = cls(
            name=name,
            path=path,
            type_=type_,
        )

        return file_system_entry_info
