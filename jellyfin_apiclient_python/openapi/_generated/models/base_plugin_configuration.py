from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BasePluginConfiguration")


@_attrs_define
class BasePluginConfiguration:
    """Class BasePluginConfiguration."""

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        base_plugin_configuration = cls()

        return base_plugin_configuration
