from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicSystemInfo")


@_attrs_define
class PublicSystemInfo:
    """
    Attributes:
        local_address (None | str | Unset): Gets or sets the local address.
        server_name (None | str | Unset): Gets or sets the name of the server.
        version (None | str | Unset): Gets or sets the server version.
        product_name (None | str | Unset): Gets or sets the product name. This is the AssemblyProduct name.
        operating_system (None | str | Unset): Gets or sets the operating system.
        id (None | str | Unset): Gets or sets the id.
        startup_wizard_completed (bool | None | Unset): Gets or sets a value indicating whether the startup wizard is
            completed.
    """

    local_address: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    operating_system: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    startup_wizard_completed: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        local_address: None | str | Unset
        if isinstance(self.local_address, Unset):
            local_address = UNSET
        else:
            local_address = self.local_address

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        operating_system: None | str | Unset
        if isinstance(self.operating_system, Unset):
            operating_system = UNSET
        else:
            operating_system = self.operating_system

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        startup_wizard_completed: bool | None | Unset
        if isinstance(self.startup_wizard_completed, Unset):
            startup_wizard_completed = UNSET
        else:
            startup_wizard_completed = self.startup_wizard_completed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if local_address is not UNSET:
            field_dict["LocalAddress"] = local_address
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if version is not UNSET:
            field_dict["Version"] = version
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if operating_system is not UNSET:
            field_dict["OperatingSystem"] = operating_system
        if id is not UNSET:
            field_dict["Id"] = id
        if startup_wizard_completed is not UNSET:
            field_dict["StartupWizardCompleted"] = startup_wizard_completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_local_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_address = _parse_local_address(d.pop("LocalAddress", UNSET))

        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("ServerName", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("ProductName", UNSET))

        def _parse_operating_system(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_system = _parse_operating_system(d.pop("OperatingSystem", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_startup_wizard_completed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        startup_wizard_completed = _parse_startup_wizard_completed(
            d.pop("StartupWizardCompleted", UNSET)
        )

        public_system_info = cls(
            local_address=local_address,
            server_name=server_name,
            version=version,
            product_name=product_name,
            operating_system=operating_system,
            id=id,
            startup_wizard_completed=startup_wizard_completed,
        )

        return public_system_info
