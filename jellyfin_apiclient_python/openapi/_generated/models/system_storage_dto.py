from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_storage_dto import FolderStorageDto
    from ..models.library_storage_dto import LibraryStorageDto


T = TypeVar("T", bound="SystemStorageDto")


@_attrs_define
class SystemStorageDto:
    """Contains informations about the systems storage.

    Attributes:
        program_data_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        web_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        image_cache_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        cache_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        log_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        internal_metadata_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        transcoding_temp_folder (FolderStorageDto | Unset): Contains information about a specific folder.
        libraries (list[LibraryStorageDto] | Unset): Gets or sets the storage informations of all libraries.
    """

    program_data_folder: FolderStorageDto | Unset = UNSET
    web_folder: FolderStorageDto | Unset = UNSET
    image_cache_folder: FolderStorageDto | Unset = UNSET
    cache_folder: FolderStorageDto | Unset = UNSET
    log_folder: FolderStorageDto | Unset = UNSET
    internal_metadata_folder: FolderStorageDto | Unset = UNSET
    transcoding_temp_folder: FolderStorageDto | Unset = UNSET
    libraries: list[LibraryStorageDto] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        program_data_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.program_data_folder, Unset):
            program_data_folder = self.program_data_folder.to_dict()

        web_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.web_folder, Unset):
            web_folder = self.web_folder.to_dict()

        image_cache_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_cache_folder, Unset):
            image_cache_folder = self.image_cache_folder.to_dict()

        cache_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_folder, Unset):
            cache_folder = self.cache_folder.to_dict()

        log_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_folder, Unset):
            log_folder = self.log_folder.to_dict()

        internal_metadata_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internal_metadata_folder, Unset):
            internal_metadata_folder = self.internal_metadata_folder.to_dict()

        transcoding_temp_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transcoding_temp_folder, Unset):
            transcoding_temp_folder = self.transcoding_temp_folder.to_dict()

        libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()
                libraries.append(libraries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if program_data_folder is not UNSET:
            field_dict["ProgramDataFolder"] = program_data_folder
        if web_folder is not UNSET:
            field_dict["WebFolder"] = web_folder
        if image_cache_folder is not UNSET:
            field_dict["ImageCacheFolder"] = image_cache_folder
        if cache_folder is not UNSET:
            field_dict["CacheFolder"] = cache_folder
        if log_folder is not UNSET:
            field_dict["LogFolder"] = log_folder
        if internal_metadata_folder is not UNSET:
            field_dict["InternalMetadataFolder"] = internal_metadata_folder
        if transcoding_temp_folder is not UNSET:
            field_dict["TranscodingTempFolder"] = transcoding_temp_folder
        if libraries is not UNSET:
            field_dict["Libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_storage_dto import FolderStorageDto
        from ..models.library_storage_dto import LibraryStorageDto

        d = dict(src_dict)
        _program_data_folder = d.pop("ProgramDataFolder", UNSET)
        program_data_folder: FolderStorageDto | Unset
        if isinstance(_program_data_folder, Unset):
            program_data_folder = UNSET
        else:
            program_data_folder = FolderStorageDto.from_dict(_program_data_folder)

        _web_folder = d.pop("WebFolder", UNSET)
        web_folder: FolderStorageDto | Unset
        if isinstance(_web_folder, Unset):
            web_folder = UNSET
        else:
            web_folder = FolderStorageDto.from_dict(_web_folder)

        _image_cache_folder = d.pop("ImageCacheFolder", UNSET)
        image_cache_folder: FolderStorageDto | Unset
        if isinstance(_image_cache_folder, Unset):
            image_cache_folder = UNSET
        else:
            image_cache_folder = FolderStorageDto.from_dict(_image_cache_folder)

        _cache_folder = d.pop("CacheFolder", UNSET)
        cache_folder: FolderStorageDto | Unset
        if isinstance(_cache_folder, Unset):
            cache_folder = UNSET
        else:
            cache_folder = FolderStorageDto.from_dict(_cache_folder)

        _log_folder = d.pop("LogFolder", UNSET)
        log_folder: FolderStorageDto | Unset
        if isinstance(_log_folder, Unset):
            log_folder = UNSET
        else:
            log_folder = FolderStorageDto.from_dict(_log_folder)

        _internal_metadata_folder = d.pop("InternalMetadataFolder", UNSET)
        internal_metadata_folder: FolderStorageDto | Unset
        if isinstance(_internal_metadata_folder, Unset):
            internal_metadata_folder = UNSET
        else:
            internal_metadata_folder = FolderStorageDto.from_dict(
                _internal_metadata_folder
            )

        _transcoding_temp_folder = d.pop("TranscodingTempFolder", UNSET)
        transcoding_temp_folder: FolderStorageDto | Unset
        if isinstance(_transcoding_temp_folder, Unset):
            transcoding_temp_folder = UNSET
        else:
            transcoding_temp_folder = FolderStorageDto.from_dict(
                _transcoding_temp_folder
            )

        _libraries = d.pop("Libraries", UNSET)
        libraries: list[LibraryStorageDto] | Unset = UNSET
        if _libraries is not UNSET:
            libraries = []
            for libraries_item_data in _libraries:
                libraries_item = LibraryStorageDto.from_dict(libraries_item_data)

                libraries.append(libraries_item)

        system_storage_dto = cls(
            program_data_folder=program_data_folder,
            web_folder=web_folder,
            image_cache_folder=image_cache_folder,
            cache_folder=cache_folder,
            log_folder=log_folder,
            internal_metadata_folder=internal_metadata_folder,
            transcoding_temp_folder=transcoding_temp_folder,
            libraries=libraries,
        )

        return system_storage_dto
