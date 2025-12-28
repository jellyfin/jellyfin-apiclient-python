from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigImageTypes")


@_attrs_define
class ConfigImageTypes:
    """
    Attributes:
        backdrop_sizes (list[str] | None | Unset):
        base_url (None | str | Unset):
        logo_sizes (list[str] | None | Unset):
        poster_sizes (list[str] | None | Unset):
        profile_sizes (list[str] | None | Unset):
        secure_base_url (None | str | Unset):
        still_sizes (list[str] | None | Unset):
    """

    backdrop_sizes: list[str] | None | Unset = UNSET
    base_url: None | str | Unset = UNSET
    logo_sizes: list[str] | None | Unset = UNSET
    poster_sizes: list[str] | None | Unset = UNSET
    profile_sizes: list[str] | None | Unset = UNSET
    secure_base_url: None | str | Unset = UNSET
    still_sizes: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backdrop_sizes: list[str] | None | Unset
        if isinstance(self.backdrop_sizes, Unset):
            backdrop_sizes = UNSET
        elif isinstance(self.backdrop_sizes, list):
            backdrop_sizes = self.backdrop_sizes

        else:
            backdrop_sizes = self.backdrop_sizes

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        logo_sizes: list[str] | None | Unset
        if isinstance(self.logo_sizes, Unset):
            logo_sizes = UNSET
        elif isinstance(self.logo_sizes, list):
            logo_sizes = self.logo_sizes

        else:
            logo_sizes = self.logo_sizes

        poster_sizes: list[str] | None | Unset
        if isinstance(self.poster_sizes, Unset):
            poster_sizes = UNSET
        elif isinstance(self.poster_sizes, list):
            poster_sizes = self.poster_sizes

        else:
            poster_sizes = self.poster_sizes

        profile_sizes: list[str] | None | Unset
        if isinstance(self.profile_sizes, Unset):
            profile_sizes = UNSET
        elif isinstance(self.profile_sizes, list):
            profile_sizes = self.profile_sizes

        else:
            profile_sizes = self.profile_sizes

        secure_base_url: None | str | Unset
        if isinstance(self.secure_base_url, Unset):
            secure_base_url = UNSET
        else:
            secure_base_url = self.secure_base_url

        still_sizes: list[str] | None | Unset
        if isinstance(self.still_sizes, Unset):
            still_sizes = UNSET
        elif isinstance(self.still_sizes, list):
            still_sizes = self.still_sizes

        else:
            still_sizes = self.still_sizes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backdrop_sizes is not UNSET:
            field_dict["BackdropSizes"] = backdrop_sizes
        if base_url is not UNSET:
            field_dict["BaseUrl"] = base_url
        if logo_sizes is not UNSET:
            field_dict["LogoSizes"] = logo_sizes
        if poster_sizes is not UNSET:
            field_dict["PosterSizes"] = poster_sizes
        if profile_sizes is not UNSET:
            field_dict["ProfileSizes"] = profile_sizes
        if secure_base_url is not UNSET:
            field_dict["SecureBaseUrl"] = secure_base_url
        if still_sizes is not UNSET:
            field_dict["StillSizes"] = still_sizes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_backdrop_sizes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backdrop_sizes_type_0 = cast(list[str], data)

                return backdrop_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        backdrop_sizes = _parse_backdrop_sizes(d.pop("BackdropSizes", UNSET))

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("BaseUrl", UNSET))

        def _parse_logo_sizes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logo_sizes_type_0 = cast(list[str], data)

                return logo_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        logo_sizes = _parse_logo_sizes(d.pop("LogoSizes", UNSET))

        def _parse_poster_sizes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                poster_sizes_type_0 = cast(list[str], data)

                return poster_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        poster_sizes = _parse_poster_sizes(d.pop("PosterSizes", UNSET))

        def _parse_profile_sizes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                profile_sizes_type_0 = cast(list[str], data)

                return profile_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        profile_sizes = _parse_profile_sizes(d.pop("ProfileSizes", UNSET))

        def _parse_secure_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secure_base_url = _parse_secure_base_url(d.pop("SecureBaseUrl", UNSET))

        def _parse_still_sizes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                still_sizes_type_0 = cast(list[str], data)

                return still_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        still_sizes = _parse_still_sizes(d.pop("StillSizes", UNSET))

        config_image_types = cls(
            backdrop_sizes=backdrop_sizes,
            base_url=base_url,
            logo_sizes=logo_sizes,
            poster_sizes=poster_sizes,
            profile_sizes=profile_sizes,
            secure_base_url=secure_base_url,
            still_sizes=still_sizes,
        )

        return config_image_types
