from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageOption")


@_attrs_define
class ImageOption:
    """
    Attributes:
        type_ (ImageType | Unset): Enum ImageType.
        limit (int | Unset): Gets or sets the limit.
        min_width (int | Unset): Gets or sets the minimum width.
    """

    type_: ImageType | Unset = UNSET
    limit: int | Unset = UNSET
    min_width: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        limit = self.limit

        min_width = self.min_width

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if min_width is not UNSET:
            field_dict["MinWidth"] = min_width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("Type", UNSET)
        type_: ImageType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ImageType(_type_)

        limit = d.pop("Limit", UNSET)

        min_width = d.pop("MinWidth", UNSET)

        image_option = cls(
            type_=type_,
            limit=limit,
            min_width=min_width,
        )

        return image_option
