from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.metadata_editor_info_content_type import MetadataEditorInfoContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country_info import CountryInfo
    from ..models.culture_dto import CultureDto
    from ..models.external_id_info import ExternalIdInfo
    from ..models.name_value_pair import NameValuePair
    from ..models.parental_rating import ParentalRating


T = TypeVar("T", bound="MetadataEditorInfo")


@_attrs_define
class MetadataEditorInfo:
    """A class representing metadata editor information.

    Attributes:
        parental_rating_options (list[ParentalRating] | Unset): Gets or sets the parental rating options.
        countries (list[CountryInfo] | Unset): Gets or sets the countries.
        cultures (list[CultureDto] | Unset): Gets or sets the cultures.
        external_id_infos (list[ExternalIdInfo] | Unset): Gets or sets the external id infos.
        content_type (MetadataEditorInfoContentType | Unset): Gets or sets the content type.
        content_type_options (list[NameValuePair] | Unset): Gets or sets the content type options.
    """

    parental_rating_options: list[ParentalRating] | Unset = UNSET
    countries: list[CountryInfo] | Unset = UNSET
    cultures: list[CultureDto] | Unset = UNSET
    external_id_infos: list[ExternalIdInfo] | Unset = UNSET
    content_type: MetadataEditorInfoContentType | Unset = UNSET
    content_type_options: list[NameValuePair] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        parental_rating_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parental_rating_options, Unset):
            parental_rating_options = []
            for parental_rating_options_item_data in self.parental_rating_options:
                parental_rating_options_item = (
                    parental_rating_options_item_data.to_dict()
                )
                parental_rating_options.append(parental_rating_options_item)

        countries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = []
            for countries_item_data in self.countries:
                countries_item = countries_item_data.to_dict()
                countries.append(countries_item)

        cultures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cultures, Unset):
            cultures = []
            for cultures_item_data in self.cultures:
                cultures_item = cultures_item_data.to_dict()
                cultures.append(cultures_item)

        external_id_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_id_infos, Unset):
            external_id_infos = []
            for external_id_infos_item_data in self.external_id_infos:
                external_id_infos_item = external_id_infos_item_data.to_dict()
                external_id_infos.append(external_id_infos_item)

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        content_type_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_type_options, Unset):
            content_type_options = []
            for content_type_options_item_data in self.content_type_options:
                content_type_options_item = content_type_options_item_data.to_dict()
                content_type_options.append(content_type_options_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if parental_rating_options is not UNSET:
            field_dict["ParentalRatingOptions"] = parental_rating_options
        if countries is not UNSET:
            field_dict["Countries"] = countries
        if cultures is not UNSET:
            field_dict["Cultures"] = cultures
        if external_id_infos is not UNSET:
            field_dict["ExternalIdInfos"] = external_id_infos
        if content_type is not UNSET:
            field_dict["ContentType"] = content_type
        if content_type_options is not UNSET:
            field_dict["ContentTypeOptions"] = content_type_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.country_info import CountryInfo
        from ..models.culture_dto import CultureDto
        from ..models.external_id_info import ExternalIdInfo
        from ..models.name_value_pair import NameValuePair
        from ..models.parental_rating import ParentalRating

        d = dict(src_dict)
        _parental_rating_options = d.pop("ParentalRatingOptions", UNSET)
        parental_rating_options: list[ParentalRating] | Unset = UNSET
        if _parental_rating_options is not UNSET:
            parental_rating_options = []
            for parental_rating_options_item_data in _parental_rating_options:
                parental_rating_options_item = ParentalRating.from_dict(
                    parental_rating_options_item_data
                )

                parental_rating_options.append(parental_rating_options_item)

        _countries = d.pop("Countries", UNSET)
        countries: list[CountryInfo] | Unset = UNSET
        if _countries is not UNSET:
            countries = []
            for countries_item_data in _countries:
                countries_item = CountryInfo.from_dict(countries_item_data)

                countries.append(countries_item)

        _cultures = d.pop("Cultures", UNSET)
        cultures: list[CultureDto] | Unset = UNSET
        if _cultures is not UNSET:
            cultures = []
            for cultures_item_data in _cultures:
                cultures_item = CultureDto.from_dict(cultures_item_data)

                cultures.append(cultures_item)

        _external_id_infos = d.pop("ExternalIdInfos", UNSET)
        external_id_infos: list[ExternalIdInfo] | Unset = UNSET
        if _external_id_infos is not UNSET:
            external_id_infos = []
            for external_id_infos_item_data in _external_id_infos:
                external_id_infos_item = ExternalIdInfo.from_dict(
                    external_id_infos_item_data
                )

                external_id_infos.append(external_id_infos_item)

        _content_type = d.pop("ContentType", UNSET)
        content_type: MetadataEditorInfoContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = MetadataEditorInfoContentType(_content_type)

        _content_type_options = d.pop("ContentTypeOptions", UNSET)
        content_type_options: list[NameValuePair] | Unset = UNSET
        if _content_type_options is not UNSET:
            content_type_options = []
            for content_type_options_item_data in _content_type_options:
                content_type_options_item = NameValuePair.from_dict(
                    content_type_options_item_data
                )

                content_type_options.append(content_type_options_item)

        metadata_editor_info = cls(
            parental_rating_options=parental_rating_options,
            countries=countries,
            cultures=cultures,
            external_id_infos=external_id_infos,
            content_type=content_type,
            content_type_options=content_type_options,
        )

        return metadata_editor_info
