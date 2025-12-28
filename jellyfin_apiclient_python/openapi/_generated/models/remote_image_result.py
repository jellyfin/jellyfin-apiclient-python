from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_image_info import RemoteImageInfo


T = TypeVar("T", bound="RemoteImageResult")


@_attrs_define
class RemoteImageResult:
    """Class RemoteImageResult.

    Attributes:
        images (list[RemoteImageInfo] | None | Unset): Gets or sets the images.
        total_record_count (int | Unset): Gets or sets the total record count.
        providers (list[str] | None | Unset): Gets or sets the providers.
    """

    images: list[RemoteImageInfo] | None | Unset = UNSET
    total_record_count: int | Unset = UNSET
    providers: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        images: list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        total_record_count = self.total_record_count

        providers: list[str] | None | Unset
        if isinstance(self.providers, Unset):
            providers = UNSET
        elif isinstance(self.providers, list):
            providers = self.providers

        else:
            providers = self.providers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if images is not UNSET:
            field_dict["Images"] = images
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if providers is not UNSET:
            field_dict["Providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remote_image_info import RemoteImageInfo

        d = dict(src_dict)

        def _parse_images(data: object) -> list[RemoteImageInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = RemoteImageInfo.from_dict(
                        images_type_0_item_data
                    )

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RemoteImageInfo] | None | Unset, data)

        images = _parse_images(d.pop("Images", UNSET))

        total_record_count = d.pop("TotalRecordCount", UNSET)

        def _parse_providers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                providers_type_0 = cast(list[str], data)

                return providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        providers = _parse_providers(d.pop("Providers", UNSET))

        remote_image_result = cls(
            images=images,
            total_record_count=total_record_count,
            providers=providers,
        )

        return remote_image_result
