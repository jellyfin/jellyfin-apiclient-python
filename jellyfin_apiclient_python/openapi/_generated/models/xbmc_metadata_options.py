from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="XbmcMetadataOptions")


@_attrs_define
class XbmcMetadataOptions:
    """
    Attributes:
        user_id (None | str | Unset):
        release_date_format (str | Unset):
        save_image_paths_in_nfo (bool | Unset):
        enable_path_substitution (bool | Unset):
        enable_extra_thumbs_duplication (bool | Unset):
    """

    user_id: None | str | Unset = UNSET
    release_date_format: str | Unset = UNSET
    save_image_paths_in_nfo: bool | Unset = UNSET
    enable_path_substitution: bool | Unset = UNSET
    enable_extra_thumbs_duplication: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        release_date_format = self.release_date_format

        save_image_paths_in_nfo = self.save_image_paths_in_nfo

        enable_path_substitution = self.enable_path_substitution

        enable_extra_thumbs_duplication = self.enable_extra_thumbs_duplication

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if release_date_format is not UNSET:
            field_dict["ReleaseDateFormat"] = release_date_format
        if save_image_paths_in_nfo is not UNSET:
            field_dict["SaveImagePathsInNfo"] = save_image_paths_in_nfo
        if enable_path_substitution is not UNSET:
            field_dict["EnablePathSubstitution"] = enable_path_substitution
        if enable_extra_thumbs_duplication is not UNSET:
            field_dict["EnableExtraThumbsDuplication"] = enable_extra_thumbs_duplication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        release_date_format = d.pop("ReleaseDateFormat", UNSET)

        save_image_paths_in_nfo = d.pop("SaveImagePathsInNfo", UNSET)

        enable_path_substitution = d.pop("EnablePathSubstitution", UNSET)

        enable_extra_thumbs_duplication = d.pop("EnableExtraThumbsDuplication", UNSET)

        xbmc_metadata_options = cls(
            user_id=user_id,
            release_date_format=release_date_format,
            save_image_paths_in_nfo=save_image_paths_in_nfo,
            enable_path_substitution=enable_path_substitution,
            enable_extra_thumbs_duplication=enable_extra_thumbs_duplication,
        )

        return xbmc_metadata_options
