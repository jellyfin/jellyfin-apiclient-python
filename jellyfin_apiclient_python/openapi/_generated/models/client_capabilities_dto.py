from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.general_command_type import GeneralCommandType
from ..models.media_type import MediaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="ClientCapabilitiesDto")


@_attrs_define
class ClientCapabilitiesDto:
    """Client capabilities dto.

    Attributes:
        playable_media_types (list[MediaType] | Unset): Gets or sets the list of playable media types.
        supported_commands (list[GeneralCommandType] | Unset): Gets or sets the list of supported commands.
        supports_media_control (bool | Unset): Gets or sets a value indicating whether session supports media control.
        supports_persistent_identifier (bool | Unset): Gets or sets a value indicating whether session supports a
            persistent identifier.
        device_profile (DeviceProfile | None | Unset): Gets or sets the device profile.
        app_store_url (None | str | Unset): Gets or sets the app store url.
        icon_url (None | str | Unset): Gets or sets the icon url.
    """

    playable_media_types: list[MediaType] | Unset = UNSET
    supported_commands: list[GeneralCommandType] | Unset = UNSET
    supports_media_control: bool | Unset = UNSET
    supports_persistent_identifier: bool | Unset = UNSET
    device_profile: DeviceProfile | None | Unset = UNSET
    app_store_url: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.device_profile import DeviceProfile

        playable_media_types: list[str] | Unset = UNSET
        if not isinstance(self.playable_media_types, Unset):
            playable_media_types = []
            for playable_media_types_item_data in self.playable_media_types:
                playable_media_types_item = playable_media_types_item_data.value
                playable_media_types.append(playable_media_types_item)

        supported_commands: list[str] | Unset = UNSET
        if not isinstance(self.supported_commands, Unset):
            supported_commands = []
            for supported_commands_item_data in self.supported_commands:
                supported_commands_item = supported_commands_item_data.value
                supported_commands.append(supported_commands_item)

        supports_media_control = self.supports_media_control

        supports_persistent_identifier = self.supports_persistent_identifier

        device_profile: dict[str, Any] | None | Unset
        if isinstance(self.device_profile, Unset):
            device_profile = UNSET
        elif isinstance(self.device_profile, DeviceProfile):
            device_profile = self.device_profile.to_dict()
        else:
            device_profile = self.device_profile

        app_store_url: None | str | Unset
        if isinstance(self.app_store_url, Unset):
            app_store_url = UNSET
        else:
            app_store_url = self.app_store_url

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playable_media_types is not UNSET:
            field_dict["PlayableMediaTypes"] = playable_media_types
        if supported_commands is not UNSET:
            field_dict["SupportedCommands"] = supported_commands
        if supports_media_control is not UNSET:
            field_dict["SupportsMediaControl"] = supports_media_control
        if supports_persistent_identifier is not UNSET:
            field_dict["SupportsPersistentIdentifier"] = supports_persistent_identifier
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if app_store_url is not UNSET:
            field_dict["AppStoreUrl"] = app_store_url
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = dict(src_dict)
        _playable_media_types = d.pop("PlayableMediaTypes", UNSET)
        playable_media_types: list[MediaType] | Unset = UNSET
        if _playable_media_types is not UNSET:
            playable_media_types = []
            for playable_media_types_item_data in _playable_media_types:
                playable_media_types_item = MediaType(playable_media_types_item_data)

                playable_media_types.append(playable_media_types_item)

        _supported_commands = d.pop("SupportedCommands", UNSET)
        supported_commands: list[GeneralCommandType] | Unset = UNSET
        if _supported_commands is not UNSET:
            supported_commands = []
            for supported_commands_item_data in _supported_commands:
                supported_commands_item = GeneralCommandType(
                    supported_commands_item_data
                )

                supported_commands.append(supported_commands_item)

        supports_media_control = d.pop("SupportsMediaControl", UNSET)

        supports_persistent_identifier = d.pop("SupportsPersistentIdentifier", UNSET)

        def _parse_device_profile(data: object) -> DeviceProfile | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_profile_type_1 = DeviceProfile.from_dict(data)

                return device_profile_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeviceProfile | None | Unset, data)

        device_profile = _parse_device_profile(d.pop("DeviceProfile", UNSET))

        def _parse_app_store_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_store_url = _parse_app_store_url(d.pop("AppStoreUrl", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("IconUrl", UNSET))

        client_capabilities_dto = cls(
            playable_media_types=playable_media_types,
            supported_commands=supported_commands,
            supports_media_control=supports_media_control,
            supports_persistent_identifier=supports_persistent_identifier,
            device_profile=device_profile,
            app_store_url=app_store_url,
            icon_url=icon_url,
        )

        return client_capabilities_dto
