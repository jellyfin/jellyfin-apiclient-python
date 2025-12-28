from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartupConfigurationDto")


@_attrs_define
class StartupConfigurationDto:
    """The startup configuration DTO.

    Attributes:
        server_name (None | str | Unset): Gets or sets the server name.
        ui_culture (None | str | Unset): Gets or sets UI language culture.
        metadata_country_code (None | str | Unset): Gets or sets the metadata country code.
        preferred_metadata_language (None | str | Unset): Gets or sets the preferred language for the metadata.
    """

    server_name: None | str | Unset = UNSET
    ui_culture: None | str | Unset = UNSET
    metadata_country_code: None | str | Unset = UNSET
    preferred_metadata_language: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        ui_culture: None | str | Unset
        if isinstance(self.ui_culture, Unset):
            ui_culture = UNSET
        else:
            ui_culture = self.ui_culture

        metadata_country_code: None | str | Unset
        if isinstance(self.metadata_country_code, Unset):
            metadata_country_code = UNSET
        else:
            metadata_country_code = self.metadata_country_code

        preferred_metadata_language: None | str | Unset
        if isinstance(self.preferred_metadata_language, Unset):
            preferred_metadata_language = UNSET
        else:
            preferred_metadata_language = self.preferred_metadata_language

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if ui_culture is not UNSET:
            field_dict["UICulture"] = ui_culture
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("ServerName", UNSET))

        def _parse_ui_culture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_culture = _parse_ui_culture(d.pop("UICulture", UNSET))

        def _parse_metadata_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_country_code = _parse_metadata_country_code(
            d.pop("MetadataCountryCode", UNSET)
        )

        def _parse_preferred_metadata_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_metadata_language = _parse_preferred_metadata_language(
            d.pop("PreferredMetadataLanguage", UNSET)
        )

        startup_configuration_dto = cls(
            server_name=server_name,
            ui_culture=ui_culture,
            metadata_country_code=metadata_country_code,
            preferred_metadata_language=preferred_metadata_language,
        )

        return startup_configuration_dto
