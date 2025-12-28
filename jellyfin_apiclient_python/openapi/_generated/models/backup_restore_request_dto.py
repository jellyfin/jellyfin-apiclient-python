from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupRestoreRequestDto")


@_attrs_define
class BackupRestoreRequestDto:
    """Defines properties used to start a restore process.

    Attributes:
        archive_file_name (str | Unset): Gets or Sets the name of the backup archive to restore from. Must be present in
            MediaBrowser.Common.Configuration.IApplicationPaths.BackupPath.
    """

    archive_file_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        archive_file_name = self.archive_file_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if archive_file_name is not UNSET:
            field_dict["ArchiveFileName"] = archive_file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archive_file_name = d.pop("ArchiveFileName", UNSET)

        backup_restore_request_dto = cls(
            archive_file_name=archive_file_name,
        )

        return backup_restore_request_dto
