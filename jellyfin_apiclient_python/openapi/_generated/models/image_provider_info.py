from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageProviderInfo")


@_attrs_define
class ImageProviderInfo:
    """Class ImageProviderInfo.

    Attributes:
        name (str | Unset): Gets the name.
        supported_images (list[ImageType] | Unset): Gets the supported image types.
    """

    name: str | Unset = UNSET
    supported_images: list[ImageType] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        supported_images: list[str] | Unset = UNSET
        if not isinstance(self.supported_images, Unset):
            supported_images = []
            for supported_images_item_data in self.supported_images:
                supported_images_item = supported_images_item_data.value
                supported_images.append(supported_images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if supported_images is not UNSET:
            field_dict["SupportedImages"] = supported_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        _supported_images = d.pop("SupportedImages", UNSET)
        supported_images: list[ImageType] | Unset = UNSET
        if _supported_images is not UNSET:
            supported_images = []
            for supported_images_item_data in _supported_images:
                supported_images_item = ImageType(supported_images_item_data)

                supported_images.append(supported_images_item)

        image_provider_info = cls(
            name=name,
            supported_images=supported_images,
        )

        return image_provider_info
