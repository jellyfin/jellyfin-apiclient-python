from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.subtitle_delivery_method import SubtitleDeliveryMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubtitleProfile")


@_attrs_define
class SubtitleProfile:
    """A class for subtitle profile information.

    Attributes:
        format_ (None | str | Unset): Gets or sets the format.
        method (SubtitleDeliveryMethod | Unset): Delivery method to use during playback of a specific subtitle format.
        didl_mode (None | str | Unset): Gets or sets the DIDL mode.
        language (None | str | Unset): Gets or sets the language.
        container (None | str | Unset): Gets or sets the container.
    """

    format_: None | str | Unset = UNSET
    method: SubtitleDeliveryMethod | Unset = UNSET
    didl_mode: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    container: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        didl_mode: None | str | Unset
        if isinstance(self.didl_mode, Unset):
            didl_mode = UNSET
        else:
            didl_mode = self.didl_mode

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        container: None | str | Unset
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if method is not UNSET:
            field_dict["Method"] = method
        if didl_mode is not UNSET:
            field_dict["DidlMode"] = didl_mode
        if language is not UNSET:
            field_dict["Language"] = language
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("Format", UNSET))

        _method = d.pop("Method", UNSET)
        method: SubtitleDeliveryMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = SubtitleDeliveryMethod(_method)

        def _parse_didl_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        didl_mode = _parse_didl_mode(d.pop("DidlMode", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("Language", UNSET))

        def _parse_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container = _parse_container(d.pop("Container", UNSET))

        subtitle_profile = cls(
            format_=format_,
            method=method,
            didl_mode=didl_mode,
            language=language,
            container=container,
        )

        return subtitle_profile
