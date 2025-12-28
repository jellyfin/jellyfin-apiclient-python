from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetChannelMappingDto")


@_attrs_define
class SetChannelMappingDto:
    """Set channel mapping dto.

    Attributes:
        provider_id (str): Gets or sets the provider id.
        tuner_channel_id (str): Gets or sets the tuner channel id.
        provider_channel_id (str): Gets or sets the provider channel id.
    """

    provider_id: str
    tuner_channel_id: str
    provider_channel_id: str

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        tuner_channel_id = self.tuner_channel_id

        provider_channel_id = self.provider_channel_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ProviderId": provider_id,
                "TunerChannelId": tuner_channel_id,
                "ProviderChannelId": provider_channel_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("ProviderId")

        tuner_channel_id = d.pop("TunerChannelId")

        provider_channel_id = d.pop("ProviderChannelId")

        set_channel_mapping_dto = cls(
            provider_id=provider_id,
            tuner_channel_id=tuner_channel_id,
            provider_channel_id=provider_channel_id,
        )

        return set_channel_mapping_dto
