from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrandingOptionsDto")


@_attrs_define
class BrandingOptionsDto:
    """The branding options DTO for API use.
    This DTO excludes SplashscreenLocation to prevent it from being updated via API.

        Attributes:
            login_disclaimer (None | str | Unset): Gets or sets the login disclaimer.
            custom_css (None | str | Unset): Gets or sets the custom CSS.
            splashscreen_enabled (bool | Unset): Gets or sets a value indicating whether to enable the splashscreen.
    """

    login_disclaimer: None | str | Unset = UNSET
    custom_css: None | str | Unset = UNSET
    splashscreen_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        login_disclaimer: None | str | Unset
        if isinstance(self.login_disclaimer, Unset):
            login_disclaimer = UNSET
        else:
            login_disclaimer = self.login_disclaimer

        custom_css: None | str | Unset
        if isinstance(self.custom_css, Unset):
            custom_css = UNSET
        else:
            custom_css = self.custom_css

        splashscreen_enabled = self.splashscreen_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if login_disclaimer is not UNSET:
            field_dict["LoginDisclaimer"] = login_disclaimer
        if custom_css is not UNSET:
            field_dict["CustomCss"] = custom_css
        if splashscreen_enabled is not UNSET:
            field_dict["SplashscreenEnabled"] = splashscreen_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_login_disclaimer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login_disclaimer = _parse_login_disclaimer(d.pop("LoginDisclaimer", UNSET))

        def _parse_custom_css(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_css = _parse_custom_css(d.pop("CustomCss", UNSET))

        splashscreen_enabled = d.pop("SplashscreenEnabled", UNSET)

        branding_options_dto = cls(
            login_disclaimer=login_disclaimer,
            custom_css=custom_css,
            splashscreen_enabled=splashscreen_enabled,
        )

        return branding_options_dto
