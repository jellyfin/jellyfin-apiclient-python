from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceOptionsDto")


@_attrs_define
class DeviceOptionsDto:
    """A dto representing custom options for a device.

    Attributes:
        id (int | Unset): Gets or sets the id.
        device_id (None | str | Unset): Gets or sets the device id.
        custom_name (None | str | Unset): Gets or sets the custom name.
    """

    id: int | Unset = UNSET
    device_id: None | str | Unset = UNSET
    custom_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        device_id: None | str | Unset
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        custom_name: None | str | Unset
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        def _parse_device_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        def _parse_custom_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_name = _parse_custom_name(d.pop("CustomName", UNSET))

        device_options_dto = cls(
            id=id,
            device_id=device_id,
            custom_name=custom_name,
        )

        return device_options_dto
