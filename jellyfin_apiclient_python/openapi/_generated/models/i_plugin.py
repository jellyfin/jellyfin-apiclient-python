from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPlugin")


@_attrs_define
class IPlugin:
    """Defines the MediaBrowser.Common.Plugins.IPlugin.

    Attributes:
        name (None | str | Unset): Gets the name of the plugin.
        description (None | str | Unset): Gets the Description.
        id (UUID | Unset): Gets the unique id.
        version (None | str | Unset): Gets the plugin version.
        assembly_file_path (None | str | Unset): Gets the path to the assembly file.
        can_uninstall (bool | Unset): Gets a value indicating whether the plugin can be uninstalled.
        data_folder_path (None | str | Unset): Gets the full path to the data folder, where the plugin can store any
            miscellaneous files needed.
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    version: None | str | Unset = UNSET
    assembly_file_path: None | str | Unset = UNSET
    can_uninstall: bool | Unset = UNSET
    data_folder_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        assembly_file_path: None | str | Unset
        if isinstance(self.assembly_file_path, Unset):
            assembly_file_path = UNSET
        else:
            assembly_file_path = self.assembly_file_path

        can_uninstall = self.can_uninstall

        data_folder_path: None | str | Unset
        if isinstance(self.data_folder_path, Unset):
            data_folder_path = UNSET
        else:
            data_folder_path = self.data_folder_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if id is not UNSET:
            field_dict["Id"] = id
        if version is not UNSET:
            field_dict["Version"] = version
        if assembly_file_path is not UNSET:
            field_dict["AssemblyFilePath"] = assembly_file_path
        if can_uninstall is not UNSET:
            field_dict["CanUninstall"] = can_uninstall
        if data_folder_path is not UNSET:
            field_dict["DataFolderPath"] = data_folder_path

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("Description", UNSET))

        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_assembly_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assembly_file_path = _parse_assembly_file_path(d.pop("AssemblyFilePath", UNSET))

        can_uninstall = d.pop("CanUninstall", UNSET)

        def _parse_data_folder_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_folder_path = _parse_data_folder_path(d.pop("DataFolderPath", UNSET))

        i_plugin = cls(
            name=name,
            description=description,
            id=id,
            version=version,
            assembly_file_path=assembly_file_path,
            can_uninstall=can_uninstall,
            data_folder_path=data_folder_path,
        )

        return i_plugin
