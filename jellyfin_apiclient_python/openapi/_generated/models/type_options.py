from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_option import ImageOption


T = TypeVar("T", bound="TypeOptions")


@_attrs_define
class TypeOptions:
    """
    Attributes:
        type_ (None | str | Unset):
        metadata_fetchers (list[str] | None | Unset):
        metadata_fetcher_order (list[str] | None | Unset):
        image_fetchers (list[str] | None | Unset):
        image_fetcher_order (list[str] | None | Unset):
        image_options (list[ImageOption] | None | Unset):
    """

    type_: None | str | Unset = UNSET
    metadata_fetchers: list[str] | None | Unset = UNSET
    metadata_fetcher_order: list[str] | None | Unset = UNSET
    image_fetchers: list[str] | None | Unset = UNSET
    image_fetcher_order: list[str] | None | Unset = UNSET
    image_options: list[ImageOption] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        metadata_fetchers: list[str] | None | Unset
        if isinstance(self.metadata_fetchers, Unset):
            metadata_fetchers = UNSET
        elif isinstance(self.metadata_fetchers, list):
            metadata_fetchers = self.metadata_fetchers

        else:
            metadata_fetchers = self.metadata_fetchers

        metadata_fetcher_order: list[str] | None | Unset
        if isinstance(self.metadata_fetcher_order, Unset):
            metadata_fetcher_order = UNSET
        elif isinstance(self.metadata_fetcher_order, list):
            metadata_fetcher_order = self.metadata_fetcher_order

        else:
            metadata_fetcher_order = self.metadata_fetcher_order

        image_fetchers: list[str] | None | Unset
        if isinstance(self.image_fetchers, Unset):
            image_fetchers = UNSET
        elif isinstance(self.image_fetchers, list):
            image_fetchers = self.image_fetchers

        else:
            image_fetchers = self.image_fetchers

        image_fetcher_order: list[str] | None | Unset
        if isinstance(self.image_fetcher_order, Unset):
            image_fetcher_order = UNSET
        elif isinstance(self.image_fetcher_order, list):
            image_fetcher_order = self.image_fetcher_order

        else:
            image_fetcher_order = self.image_fetcher_order

        image_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.image_options, Unset):
            image_options = UNSET
        elif isinstance(self.image_options, list):
            image_options = []
            for image_options_type_0_item_data in self.image_options:
                image_options_type_0_item = image_options_type_0_item_data.to_dict()
                image_options.append(image_options_type_0_item)

        else:
            image_options = self.image_options

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if metadata_fetchers is not UNSET:
            field_dict["MetadataFetchers"] = metadata_fetchers
        if metadata_fetcher_order is not UNSET:
            field_dict["MetadataFetcherOrder"] = metadata_fetcher_order
        if image_fetchers is not UNSET:
            field_dict["ImageFetchers"] = image_fetchers
        if image_fetcher_order is not UNSET:
            field_dict["ImageFetcherOrder"] = image_fetcher_order
        if image_options is not UNSET:
            field_dict["ImageOptions"] = image_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_option import ImageOption

        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_metadata_fetchers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_fetchers_type_0 = cast(list[str], data)

                return metadata_fetchers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        metadata_fetchers = _parse_metadata_fetchers(d.pop("MetadataFetchers", UNSET))

        def _parse_metadata_fetcher_order(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_fetcher_order_type_0 = cast(list[str], data)

                return metadata_fetcher_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        metadata_fetcher_order = _parse_metadata_fetcher_order(
            d.pop("MetadataFetcherOrder", UNSET)
        )

        def _parse_image_fetchers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_fetchers_type_0 = cast(list[str], data)

                return image_fetchers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_fetchers = _parse_image_fetchers(d.pop("ImageFetchers", UNSET))

        def _parse_image_fetcher_order(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_fetcher_order_type_0 = cast(list[str], data)

                return image_fetcher_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_fetcher_order = _parse_image_fetcher_order(
            d.pop("ImageFetcherOrder", UNSET)
        )

        def _parse_image_options(data: object) -> list[ImageOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_options_type_0 = []
                _image_options_type_0 = data
                for image_options_type_0_item_data in _image_options_type_0:
                    image_options_type_0_item = ImageOption.from_dict(
                        image_options_type_0_item_data
                    )

                    image_options_type_0.append(image_options_type_0_item)

                return image_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageOption] | None | Unset, data)

        image_options = _parse_image_options(d.pop("ImageOptions", UNSET))

        type_options = cls(
            type_=type_,
            metadata_fetchers=metadata_fetchers,
            metadata_fetcher_order=metadata_fetcher_order,
            image_fetchers=image_fetchers,
            image_fetcher_order=image_fetcher_order,
            image_options=image_options,
        )

        return type_options
