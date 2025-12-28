from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderStorageDto")


@_attrs_define
class FolderStorageDto:
    """Contains information about a specific folder.

    Attributes:
        path (str | Unset): Gets the path of the folder in question.
        free_space (int | Unset): Gets the free space of the underlying storage device of the
            Jellyfin.Api.Models.SystemInfoDtos.FolderStorageDto.Path.
        used_space (int | Unset): Gets the used space of the underlying storage device of the
            Jellyfin.Api.Models.SystemInfoDtos.FolderStorageDto.Path.
        storage_type (None | str | Unset): Gets the kind of storage device of the
            Jellyfin.Api.Models.SystemInfoDtos.FolderStorageDto.Path.
        device_id (None | str | Unset): Gets the Device Identifier.
    """

    path: str | Unset = UNSET
    free_space: int | Unset = UNSET
    used_space: int | Unset = UNSET
    storage_type: None | str | Unset = UNSET
    device_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        free_space = self.free_space

        used_space = self.used_space

        storage_type: None | str | Unset
        if isinstance(self.storage_type, Unset):
            storage_type = UNSET
        else:
            storage_type = self.storage_type

        device_id: None | str | Unset
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if free_space is not UNSET:
            field_dict["FreeSpace"] = free_space
        if used_space is not UNSET:
            field_dict["UsedSpace"] = used_space
        if storage_type is not UNSET:
            field_dict["StorageType"] = storage_type
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("Path", UNSET)

        free_space = d.pop("FreeSpace", UNSET)

        used_space = d.pop("UsedSpace", UNSET)

        def _parse_storage_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_type = _parse_storage_type(d.pop("StorageType", UNSET))

        def _parse_device_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        folder_storage_dto = cls(
            path=path,
            free_space=free_space,
            used_space=used_space,
            storage_type=storage_type,
            device_id=device_id,
        )

        return folder_storage_dto
