from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="StartupRemoteAccessDto")


@_attrs_define
class StartupRemoteAccessDto:
    """Startup remote access dto.

    Attributes:
        enable_remote_access (bool): Gets or sets a value indicating whether enable remote access.
        enable_automatic_port_mapping (bool): Gets or sets a value indicating whether enable automatic port mapping.
    """

    enable_remote_access: bool
    enable_automatic_port_mapping: bool

    def to_dict(self) -> dict[str, Any]:
        enable_remote_access = self.enable_remote_access

        enable_automatic_port_mapping = self.enable_automatic_port_mapping

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "EnableRemoteAccess": enable_remote_access,
                "EnableAutomaticPortMapping": enable_automatic_port_mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_remote_access = d.pop("EnableRemoteAccess")

        enable_automatic_port_mapping = d.pop("EnableAutomaticPortMapping")

        startup_remote_access_dto = cls(
            enable_remote_access=enable_remote_access,
            enable_automatic_port_mapping=enable_automatic_port_mapping,
        )

        return startup_remote_access_dto
