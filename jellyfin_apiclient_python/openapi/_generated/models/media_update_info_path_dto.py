from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaUpdateInfoPathDto")


@_attrs_define
class MediaUpdateInfoPathDto:
    """The media update info path.

    Attributes:
        path (None | str | Unset): Gets or sets media path.
        update_type (None | str | Unset): Gets or sets media update type.
            Created, Modified, Deleted.
    """

    path: None | str | Unset = UNSET
    update_type: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        update_type: None | str | Unset
        if isinstance(self.update_type, Unset):
            update_type = UNSET
        else:
            update_type = self.update_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if update_type is not UNSET:
            field_dict["UpdateType"] = update_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_update_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        update_type = _parse_update_type(d.pop("UpdateType", UNSET))

        media_update_info_path_dto = cls(
            path=path,
            update_type=update_type,
        )

        return media_update_info_path_dto
