from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_option import ImageOption
    from ..models.library_option_info_dto import LibraryOptionInfoDto


T = TypeVar("T", bound="LibraryTypeOptionsDto")


@_attrs_define
class LibraryTypeOptionsDto:
    """Library type options dto.

    Attributes:
        type_ (None | str | Unset): Gets or sets the type.
        metadata_fetchers (list[LibraryOptionInfoDto] | Unset): Gets or sets the metadata fetchers.
        image_fetchers (list[LibraryOptionInfoDto] | Unset): Gets or sets the image fetchers.
        supported_image_types (list[ImageType] | Unset): Gets or sets the supported image types.
        default_image_options (list[ImageOption] | Unset): Gets or sets the default image options.
    """

    type_: None | str | Unset = UNSET
    metadata_fetchers: list[LibraryOptionInfoDto] | Unset = UNSET
    image_fetchers: list[LibraryOptionInfoDto] | Unset = UNSET
    supported_image_types: list[ImageType] | Unset = UNSET
    default_image_options: list[ImageOption] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        metadata_fetchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metadata_fetchers, Unset):
            metadata_fetchers = []
            for metadata_fetchers_item_data in self.metadata_fetchers:
                metadata_fetchers_item = metadata_fetchers_item_data.to_dict()
                metadata_fetchers.append(metadata_fetchers_item)

        image_fetchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.image_fetchers, Unset):
            image_fetchers = []
            for image_fetchers_item_data in self.image_fetchers:
                image_fetchers_item = image_fetchers_item_data.to_dict()
                image_fetchers.append(image_fetchers_item)

        supported_image_types: list[str] | Unset = UNSET
        if not isinstance(self.supported_image_types, Unset):
            supported_image_types = []
            for supported_image_types_item_data in self.supported_image_types:
                supported_image_types_item = supported_image_types_item_data.value
                supported_image_types.append(supported_image_types_item)

        default_image_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_image_options, Unset):
            default_image_options = []
            for default_image_options_item_data in self.default_image_options:
                default_image_options_item = default_image_options_item_data.to_dict()
                default_image_options.append(default_image_options_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if metadata_fetchers is not UNSET:
            field_dict["MetadataFetchers"] = metadata_fetchers
        if image_fetchers is not UNSET:
            field_dict["ImageFetchers"] = image_fetchers
        if supported_image_types is not UNSET:
            field_dict["SupportedImageTypes"] = supported_image_types
        if default_image_options is not UNSET:
            field_dict["DefaultImageOptions"] = default_image_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_option import ImageOption
        from ..models.library_option_info_dto import LibraryOptionInfoDto

        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        _metadata_fetchers = d.pop("MetadataFetchers", UNSET)
        metadata_fetchers: list[LibraryOptionInfoDto] | Unset = UNSET
        if _metadata_fetchers is not UNSET:
            metadata_fetchers = []
            for metadata_fetchers_item_data in _metadata_fetchers:
                metadata_fetchers_item = LibraryOptionInfoDto.from_dict(
                    metadata_fetchers_item_data
                )

                metadata_fetchers.append(metadata_fetchers_item)

        _image_fetchers = d.pop("ImageFetchers", UNSET)
        image_fetchers: list[LibraryOptionInfoDto] | Unset = UNSET
        if _image_fetchers is not UNSET:
            image_fetchers = []
            for image_fetchers_item_data in _image_fetchers:
                image_fetchers_item = LibraryOptionInfoDto.from_dict(
                    image_fetchers_item_data
                )

                image_fetchers.append(image_fetchers_item)

        _supported_image_types = d.pop("SupportedImageTypes", UNSET)
        supported_image_types: list[ImageType] | Unset = UNSET
        if _supported_image_types is not UNSET:
            supported_image_types = []
            for supported_image_types_item_data in _supported_image_types:
                supported_image_types_item = ImageType(supported_image_types_item_data)

                supported_image_types.append(supported_image_types_item)

        _default_image_options = d.pop("DefaultImageOptions", UNSET)
        default_image_options: list[ImageOption] | Unset = UNSET
        if _default_image_options is not UNSET:
            default_image_options = []
            for default_image_options_item_data in _default_image_options:
                default_image_options_item = ImageOption.from_dict(
                    default_image_options_item_data
                )

                default_image_options.append(default_image_options_item)

        library_type_options_dto = cls(
            type_=type_,
            metadata_fetchers=metadata_fetchers,
            image_fetchers=image_fetchers,
            supported_image_types=supported_image_types,
            default_image_options=default_image_options,
        )

        return library_type_options_dto
