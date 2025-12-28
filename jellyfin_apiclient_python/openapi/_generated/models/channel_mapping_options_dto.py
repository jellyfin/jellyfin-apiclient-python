from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_id_pair import NameIdPair
    from ..models.name_value_pair import NameValuePair
    from ..models.tuner_channel_mapping import TunerChannelMapping


T = TypeVar("T", bound="ChannelMappingOptionsDto")


@_attrs_define
class ChannelMappingOptionsDto:
    """Channel mapping options dto.

    Attributes:
        tuner_channels (list[TunerChannelMapping] | Unset): Gets or sets list of tuner channels.
        provider_channels (list[NameIdPair] | Unset): Gets or sets list of provider channels.
        mappings (list[NameValuePair] | Unset): Gets or sets list of mappings.
        provider_name (None | str | Unset): Gets or sets provider name.
    """

    tuner_channels: list[TunerChannelMapping] | Unset = UNSET
    provider_channels: list[NameIdPair] | Unset = UNSET
    mappings: list[NameValuePair] | Unset = UNSET
    provider_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tuner_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tuner_channels, Unset):
            tuner_channels = []
            for tuner_channels_item_data in self.tuner_channels:
                tuner_channels_item = tuner_channels_item_data.to_dict()
                tuner_channels.append(tuner_channels_item)

        provider_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.provider_channels, Unset):
            provider_channels = []
            for provider_channels_item_data in self.provider_channels:
                provider_channels_item = provider_channels_item_data.to_dict()
                provider_channels.append(provider_channels_item)

        mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        provider_name: None | str | Unset
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tuner_channels is not UNSET:
            field_dict["TunerChannels"] = tuner_channels
        if provider_channels is not UNSET:
            field_dict["ProviderChannels"] = provider_channels
        if mappings is not UNSET:
            field_dict["Mappings"] = mappings
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_id_pair import NameIdPair
        from ..models.name_value_pair import NameValuePair
        from ..models.tuner_channel_mapping import TunerChannelMapping

        d = dict(src_dict)
        _tuner_channels = d.pop("TunerChannels", UNSET)
        tuner_channels: list[TunerChannelMapping] | Unset = UNSET
        if _tuner_channels is not UNSET:
            tuner_channels = []
            for tuner_channels_item_data in _tuner_channels:
                tuner_channels_item = TunerChannelMapping.from_dict(
                    tuner_channels_item_data
                )

                tuner_channels.append(tuner_channels_item)

        _provider_channels = d.pop("ProviderChannels", UNSET)
        provider_channels: list[NameIdPair] | Unset = UNSET
        if _provider_channels is not UNSET:
            provider_channels = []
            for provider_channels_item_data in _provider_channels:
                provider_channels_item = NameIdPair.from_dict(
                    provider_channels_item_data
                )

                provider_channels.append(provider_channels_item)

        _mappings = d.pop("Mappings", UNSET)
        mappings: list[NameValuePair] | Unset = UNSET
        if _mappings is not UNSET:
            mappings = []
            for mappings_item_data in _mappings:
                mappings_item = NameValuePair.from_dict(mappings_item_data)

                mappings.append(mappings_item)

        def _parse_provider_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_name = _parse_provider_name(d.pop("ProviderName", UNSET))

        channel_mapping_options_dto = cls(
            tuner_channels=tuner_channels,
            provider_channels=provider_channels,
            mappings=mappings,
            provider_name=provider_name,
        )

        return channel_mapping_options_dto
