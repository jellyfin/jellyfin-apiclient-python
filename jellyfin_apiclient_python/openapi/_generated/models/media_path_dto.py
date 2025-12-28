from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_path_info import MediaPathInfo


T = TypeVar("T", bound="MediaPathDto")


@_attrs_define
class MediaPathDto:
    """Media Path dto.

    Attributes:
        name (str): Gets or sets the name of the library.
        path (None | str | Unset): Gets or sets the path to add.
        path_info (MediaPathInfo | None | Unset): Gets or sets the path info.
    """

    name: str
    path: None | str | Unset = UNSET
    path_info: MediaPathInfo | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_path_info import MediaPathInfo

        name = self.name

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        path_info: dict[str, Any] | None | Unset
        if isinstance(self.path_info, Unset):
            path_info = UNSET
        elif isinstance(self.path_info, MediaPathInfo):
            path_info = self.path_info.to_dict()
        else:
            path_info = self.path_info

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Name": name,
            }
        )
        if path is not UNSET:
            field_dict["Path"] = path
        if path_info is not UNSET:
            field_dict["PathInfo"] = path_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_path_info import MediaPathInfo

        d = dict(src_dict)
        name = d.pop("Name")

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_path_info(data: object) -> MediaPathInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                path_info_type_1 = MediaPathInfo.from_dict(data)

                return path_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MediaPathInfo | None | Unset, data)

        path_info = _parse_path_info(d.pop("PathInfo", UNSET))

        media_path_dto = cls(
            name=name,
            path=path,
            path_info=path_info,
        )

        return media_path_dto
