from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryInfo")


@_attrs_define
class RepositoryInfo:
    """Class RepositoryInfo.

    Attributes:
        name (None | str | Unset): Gets or sets the name.
        url (None | str | Unset): Gets or sets the URL.
        enabled (bool | Unset): Gets or sets a value indicating whether the repository is enabled.
    """

    name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if url is not UNSET:
            field_dict["Url"] = url
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("Url", UNSET))

        enabled = d.pop("Enabled", UNSET)

        repository_info = cls(
            name=name,
            url=url,
            enabled=enabled,
        )

        return repository_info
