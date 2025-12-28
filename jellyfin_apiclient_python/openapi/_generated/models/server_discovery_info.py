from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerDiscoveryInfo")


@_attrs_define
class ServerDiscoveryInfo:
    """The server discovery info model.

    Attributes:
        address (str | Unset): Gets the address.
        id (str | Unset): Gets the server identifier.
        name (str | Unset): Gets the name.
        endpoint_address (None | str | Unset): Gets the endpoint address.
    """

    address: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    endpoint_address: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        id = self.id

        name = self.name

        endpoint_address: None | str | Unset
        if isinstance(self.endpoint_address, Unset):
            endpoint_address = UNSET
        else:
            endpoint_address = self.endpoint_address

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if endpoint_address is not UNSET:
            field_dict["EndpointAddress"] = endpoint_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("Address", UNSET)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        def _parse_endpoint_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint_address = _parse_endpoint_address(d.pop("EndpointAddress", UNSET))

        server_discovery_info = cls(
            address=address,
            id=id,
            name=name,
            endpoint_address=endpoint_address,
        )

        return server_discovery_info
