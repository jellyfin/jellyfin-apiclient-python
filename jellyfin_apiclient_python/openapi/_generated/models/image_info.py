from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageInfo")


@_attrs_define
class ImageInfo:
    """Class ImageInfo.

    Attributes:
        image_type (ImageType | Unset): Enum ImageType.
        image_index (int | None | Unset): Gets or sets the index of the image.
        image_tag (None | str | Unset): Gets or sets the image tag.
        path (None | str | Unset): Gets or sets the path.
        blur_hash (None | str | Unset): Gets or sets the blurhash.
        height (int | None | Unset): Gets or sets the height.
        width (int | None | Unset): Gets or sets the width.
        size (int | Unset): Gets or sets the size.
    """

    image_type: ImageType | Unset = UNSET
    image_index: int | None | Unset = UNSET
    image_tag: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    blur_hash: None | str | Unset = UNSET
    height: int | None | Unset = UNSET
    width: int | None | Unset = UNSET
    size: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        image_type: str | Unset = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        image_index: int | None | Unset
        if isinstance(self.image_index, Unset):
            image_index = UNSET
        else:
            image_index = self.image_index

        image_tag: None | str | Unset
        if isinstance(self.image_tag, Unset):
            image_tag = UNSET
        else:
            image_tag = self.image_tag

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        blur_hash: None | str | Unset
        if isinstance(self.blur_hash, Unset):
            blur_hash = UNSET
        else:
            blur_hash = self.blur_hash

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        size = self.size

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if image_type is not UNSET:
            field_dict["ImageType"] = image_type
        if image_index is not UNSET:
            field_dict["ImageIndex"] = image_index
        if image_tag is not UNSET:
            field_dict["ImageTag"] = image_tag
        if path is not UNSET:
            field_dict["Path"] = path
        if blur_hash is not UNSET:
            field_dict["BlurHash"] = blur_hash
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if size is not UNSET:
            field_dict["Size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _image_type = d.pop("ImageType", UNSET)
        image_type: ImageType | Unset
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = ImageType(_image_type)

        def _parse_image_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_index = _parse_image_index(d.pop("ImageIndex", UNSET))

        def _parse_image_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_tag = _parse_image_tag(d.pop("ImageTag", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_blur_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blur_hash = _parse_blur_hash(d.pop("BlurHash", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("Width", UNSET))

        size = d.pop("Size", UNSET)

        image_info = cls(
            image_type=image_type,
            image_index=image_index,
            image_tag=image_tag,
            path=path,
            blur_hash=blur_hash,
            height=height,
            width=width,
            size=size,
        )

        return image_info
