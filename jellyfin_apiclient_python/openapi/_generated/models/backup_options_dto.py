from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupOptionsDto")


@_attrs_define
class BackupOptionsDto:
    """Defines the optional contents of the backup archive.

    Attributes:
        metadata (bool | Unset): Gets or sets a value indicating whether the archive contains the Metadata contents.
        trickplay (bool | Unset): Gets or sets a value indicating whether the archive contains the Trickplay contents.
        subtitles (bool | Unset): Gets or sets a value indicating whether the archive contains the Subtitle contents.
        database (bool | Unset): Gets or sets a value indicating whether the archive contains the Database contents.
    """

    metadata: bool | Unset = UNSET
    trickplay: bool | Unset = UNSET
    subtitles: bool | Unset = UNSET
    database: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata

        trickplay = self.trickplay

        subtitles = self.subtitles

        database = self.database

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if trickplay is not UNSET:
            field_dict["Trickplay"] = trickplay
        if subtitles is not UNSET:
            field_dict["Subtitles"] = subtitles
        if database is not UNSET:
            field_dict["Database"] = database

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metadata = d.pop("Metadata", UNSET)

        trickplay = d.pop("Trickplay", UNSET)

        subtitles = d.pop("Subtitles", UNSET)

        database = d.pop("Database", UNSET)

        backup_options_dto = cls(
            metadata=metadata,
            trickplay=trickplay,
            subtitles=subtitles,
            database=database,
        )

        return backup_options_dto
