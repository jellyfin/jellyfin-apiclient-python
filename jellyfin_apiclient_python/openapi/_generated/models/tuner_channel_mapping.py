from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TunerChannelMapping")


@_attrs_define
class TunerChannelMapping:
    """
    Attributes:
        name (None | str | Unset):
        provider_channel_name (None | str | Unset):
        provider_channel_id (None | str | Unset):
        id (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    provider_channel_name: None | str | Unset = UNSET
    provider_channel_id: None | str | Unset = UNSET
    id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        provider_channel_name: None | str | Unset
        if isinstance(self.provider_channel_name, Unset):
            provider_channel_name = UNSET
        else:
            provider_channel_name = self.provider_channel_name

        provider_channel_id: None | str | Unset
        if isinstance(self.provider_channel_id, Unset):
            provider_channel_id = UNSET
        else:
            provider_channel_id = self.provider_channel_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if provider_channel_name is not UNSET:
            field_dict["ProviderChannelName"] = provider_channel_name
        if provider_channel_id is not UNSET:
            field_dict["ProviderChannelId"] = provider_channel_id
        if id is not UNSET:
            field_dict["Id"] = id

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

        def _parse_provider_channel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_channel_name = _parse_provider_channel_name(
            d.pop("ProviderChannelName", UNSET)
        )

        def _parse_provider_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_channel_id = _parse_provider_channel_id(
            d.pop("ProviderChannelId", UNSET)
        )

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        tuner_channel_mapping = cls(
            name=name,
            provider_channel_name=provider_channel_name,
            provider_channel_id=provider_channel_id,
            id=id,
        )

        return tuner_channel_mapping
