from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cast_receiver_application import CastReceiverApplication
    from ..models.installation_info import InstallationInfo


T = TypeVar("T", bound="SystemInfo")


@_attrs_define
class SystemInfo:
    """Class SystemInfo.

    Attributes:
        local_address (None | str | Unset): Gets or sets the local address.
        server_name (None | str | Unset): Gets or sets the name of the server.
        version (None | str | Unset): Gets or sets the server version.
        product_name (None | str | Unset): Gets or sets the product name. This is the AssemblyProduct name.
        operating_system (None | str | Unset): Gets or sets the operating system.
        id (None | str | Unset): Gets or sets the id.
        startup_wizard_completed (bool | None | Unset): Gets or sets a value indicating whether the startup wizard is
            completed.
        operating_system_display_name (None | str | Unset): Gets or sets the display name of the operating system.
        package_name (None | str | Unset): Gets or sets the package name.
        has_pending_restart (bool | Unset): Gets or sets a value indicating whether this instance has pending restart.
        is_shutting_down (bool | Unset):
        supports_library_monitor (bool | Unset): Gets or sets a value indicating whether [supports library monitor].
        web_socket_port_number (int | Unset): Gets or sets the web socket port number.
        completed_installations (list[InstallationInfo] | None | Unset): Gets or sets the completed installations.
        can_self_restart (bool | Unset): Gets or sets a value indicating whether this instance can self restart.
            Default: True.
        can_launch_web_browser (bool | Unset):  Default: False.
        program_data_path (None | str | Unset): Gets or sets the program data path.
        web_path (None | str | Unset): Gets or sets the web UI resources path.
        items_by_name_path (None | str | Unset): Gets or sets the items by name path.
        cache_path (None | str | Unset): Gets or sets the cache path.
        log_path (None | str | Unset): Gets or sets the log path.
        internal_metadata_path (None | str | Unset): Gets or sets the internal metadata path.
        transcoding_temp_path (None | str | Unset): Gets or sets the transcode path.
        cast_receiver_applications (list[CastReceiverApplication] | None | Unset): Gets or sets the list of cast
            receiver applications.
        has_update_available (bool | Unset): Gets or sets a value indicating whether this instance has update available.
            Default: False.
        encoder_location (None | str | Unset):  Default: 'System'.
        system_architecture (None | str | Unset):  Default: 'X64'.
    """

    local_address: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    operating_system: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    startup_wizard_completed: bool | None | Unset = UNSET
    operating_system_display_name: None | str | Unset = UNSET
    package_name: None | str | Unset = UNSET
    has_pending_restart: bool | Unset = UNSET
    is_shutting_down: bool | Unset = UNSET
    supports_library_monitor: bool | Unset = UNSET
    web_socket_port_number: int | Unset = UNSET
    completed_installations: list[InstallationInfo] | None | Unset = UNSET
    can_self_restart: bool | Unset = True
    can_launch_web_browser: bool | Unset = False
    program_data_path: None | str | Unset = UNSET
    web_path: None | str | Unset = UNSET
    items_by_name_path: None | str | Unset = UNSET
    cache_path: None | str | Unset = UNSET
    log_path: None | str | Unset = UNSET
    internal_metadata_path: None | str | Unset = UNSET
    transcoding_temp_path: None | str | Unset = UNSET
    cast_receiver_applications: list[CastReceiverApplication] | None | Unset = UNSET
    has_update_available: bool | Unset = False
    encoder_location: None | str | Unset = "System"
    system_architecture: None | str | Unset = "X64"

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

        operating_system_display_name: None | str | Unset
        if isinstance(self.operating_system_display_name, Unset):
            operating_system_display_name = UNSET
        else:
            operating_system_display_name = self.operating_system_display_name

        package_name: None | str | Unset
        if isinstance(self.package_name, Unset):
            package_name = UNSET
        else:
            package_name = self.package_name

        has_pending_restart = self.has_pending_restart

        is_shutting_down = self.is_shutting_down

        supports_library_monitor = self.supports_library_monitor

        web_socket_port_number = self.web_socket_port_number

        completed_installations: list[dict[str, Any]] | None | Unset
        if isinstance(self.completed_installations, Unset):
            completed_installations = UNSET
        elif isinstance(self.completed_installations, list):
            completed_installations = []
            for (
                completed_installations_type_0_item_data
            ) in self.completed_installations:
                completed_installations_type_0_item = (
                    completed_installations_type_0_item_data.to_dict()
                )
                completed_installations.append(completed_installations_type_0_item)

        else:
            completed_installations = self.completed_installations

        can_self_restart = self.can_self_restart

        can_launch_web_browser = self.can_launch_web_browser

        program_data_path: None | str | Unset
        if isinstance(self.program_data_path, Unset):
            program_data_path = UNSET
        else:
            program_data_path = self.program_data_path

        web_path: None | str | Unset
        if isinstance(self.web_path, Unset):
            web_path = UNSET
        else:
            web_path = self.web_path

        items_by_name_path: None | str | Unset
        if isinstance(self.items_by_name_path, Unset):
            items_by_name_path = UNSET
        else:
            items_by_name_path = self.items_by_name_path

        cache_path: None | str | Unset
        if isinstance(self.cache_path, Unset):
            cache_path = UNSET
        else:
            cache_path = self.cache_path

        log_path: None | str | Unset
        if isinstance(self.log_path, Unset):
            log_path = UNSET
        else:
            log_path = self.log_path

        internal_metadata_path: None | str | Unset
        if isinstance(self.internal_metadata_path, Unset):
            internal_metadata_path = UNSET
        else:
            internal_metadata_path = self.internal_metadata_path

        transcoding_temp_path: None | str | Unset
        if isinstance(self.transcoding_temp_path, Unset):
            transcoding_temp_path = UNSET
        else:
            transcoding_temp_path = self.transcoding_temp_path

        cast_receiver_applications: list[dict[str, Any]] | None | Unset
        if isinstance(self.cast_receiver_applications, Unset):
            cast_receiver_applications = UNSET
        elif isinstance(self.cast_receiver_applications, list):
            cast_receiver_applications = []
            for (
                cast_receiver_applications_type_0_item_data
            ) in self.cast_receiver_applications:
                cast_receiver_applications_type_0_item = (
                    cast_receiver_applications_type_0_item_data.to_dict()
                )
                cast_receiver_applications.append(
                    cast_receiver_applications_type_0_item
                )

        else:
            cast_receiver_applications = self.cast_receiver_applications

        has_update_available = self.has_update_available

        encoder_location: None | str | Unset
        if isinstance(self.encoder_location, Unset):
            encoder_location = UNSET
        else:
            encoder_location = self.encoder_location

        system_architecture: None | str | Unset
        if isinstance(self.system_architecture, Unset):
            system_architecture = UNSET
        else:
            system_architecture = self.system_architecture

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
        if operating_system_display_name is not UNSET:
            field_dict["OperatingSystemDisplayName"] = operating_system_display_name
        if package_name is not UNSET:
            field_dict["PackageName"] = package_name
        if has_pending_restart is not UNSET:
            field_dict["HasPendingRestart"] = has_pending_restart
        if is_shutting_down is not UNSET:
            field_dict["IsShuttingDown"] = is_shutting_down
        if supports_library_monitor is not UNSET:
            field_dict["SupportsLibraryMonitor"] = supports_library_monitor
        if web_socket_port_number is not UNSET:
            field_dict["WebSocketPortNumber"] = web_socket_port_number
        if completed_installations is not UNSET:
            field_dict["CompletedInstallations"] = completed_installations
        if can_self_restart is not UNSET:
            field_dict["CanSelfRestart"] = can_self_restart
        if can_launch_web_browser is not UNSET:
            field_dict["CanLaunchWebBrowser"] = can_launch_web_browser
        if program_data_path is not UNSET:
            field_dict["ProgramDataPath"] = program_data_path
        if web_path is not UNSET:
            field_dict["WebPath"] = web_path
        if items_by_name_path is not UNSET:
            field_dict["ItemsByNamePath"] = items_by_name_path
        if cache_path is not UNSET:
            field_dict["CachePath"] = cache_path
        if log_path is not UNSET:
            field_dict["LogPath"] = log_path
        if internal_metadata_path is not UNSET:
            field_dict["InternalMetadataPath"] = internal_metadata_path
        if transcoding_temp_path is not UNSET:
            field_dict["TranscodingTempPath"] = transcoding_temp_path
        if cast_receiver_applications is not UNSET:
            field_dict["CastReceiverApplications"] = cast_receiver_applications
        if has_update_available is not UNSET:
            field_dict["HasUpdateAvailable"] = has_update_available
        if encoder_location is not UNSET:
            field_dict["EncoderLocation"] = encoder_location
        if system_architecture is not UNSET:
            field_dict["SystemArchitecture"] = system_architecture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cast_receiver_application import CastReceiverApplication
        from ..models.installation_info import InstallationInfo

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

        def _parse_operating_system_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_system_display_name = _parse_operating_system_display_name(
            d.pop("OperatingSystemDisplayName", UNSET)
        )

        def _parse_package_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_name = _parse_package_name(d.pop("PackageName", UNSET))

        has_pending_restart = d.pop("HasPendingRestart", UNSET)

        is_shutting_down = d.pop("IsShuttingDown", UNSET)

        supports_library_monitor = d.pop("SupportsLibraryMonitor", UNSET)

        web_socket_port_number = d.pop("WebSocketPortNumber", UNSET)

        def _parse_completed_installations(
            data: object,
        ) -> list[InstallationInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                completed_installations_type_0 = []
                _completed_installations_type_0 = data
                for (
                    completed_installations_type_0_item_data
                ) in _completed_installations_type_0:
                    completed_installations_type_0_item = InstallationInfo.from_dict(
                        completed_installations_type_0_item_data
                    )

                    completed_installations_type_0.append(
                        completed_installations_type_0_item
                    )

                return completed_installations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstallationInfo] | None | Unset, data)

        completed_installations = _parse_completed_installations(
            d.pop("CompletedInstallations", UNSET)
        )

        can_self_restart = d.pop("CanSelfRestart", UNSET)

        can_launch_web_browser = d.pop("CanLaunchWebBrowser", UNSET)

        def _parse_program_data_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_data_path = _parse_program_data_path(d.pop("ProgramDataPath", UNSET))

        def _parse_web_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        web_path = _parse_web_path(d.pop("WebPath", UNSET))

        def _parse_items_by_name_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        items_by_name_path = _parse_items_by_name_path(d.pop("ItemsByNamePath", UNSET))

        def _parse_cache_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_path = _parse_cache_path(d.pop("CachePath", UNSET))

        def _parse_log_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        log_path = _parse_log_path(d.pop("LogPath", UNSET))

        def _parse_internal_metadata_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_metadata_path = _parse_internal_metadata_path(
            d.pop("InternalMetadataPath", UNSET)
        )

        def _parse_transcoding_temp_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcoding_temp_path = _parse_transcoding_temp_path(
            d.pop("TranscodingTempPath", UNSET)
        )

        def _parse_cast_receiver_applications(
            data: object,
        ) -> list[CastReceiverApplication] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cast_receiver_applications_type_0 = []
                _cast_receiver_applications_type_0 = data
                for (
                    cast_receiver_applications_type_0_item_data
                ) in _cast_receiver_applications_type_0:
                    cast_receiver_applications_type_0_item = (
                        CastReceiverApplication.from_dict(
                            cast_receiver_applications_type_0_item_data
                        )
                    )

                    cast_receiver_applications_type_0.append(
                        cast_receiver_applications_type_0_item
                    )

                return cast_receiver_applications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CastReceiverApplication] | None | Unset, data)

        cast_receiver_applications = _parse_cast_receiver_applications(
            d.pop("CastReceiverApplications", UNSET)
        )

        has_update_available = d.pop("HasUpdateAvailable", UNSET)

        def _parse_encoder_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encoder_location = _parse_encoder_location(d.pop("EncoderLocation", UNSET))

        def _parse_system_architecture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_architecture = _parse_system_architecture(
            d.pop("SystemArchitecture", UNSET)
        )

        system_info = cls(
            local_address=local_address,
            server_name=server_name,
            version=version,
            product_name=product_name,
            operating_system=operating_system,
            id=id,
            startup_wizard_completed=startup_wizard_completed,
            operating_system_display_name=operating_system_display_name,
            package_name=package_name,
            has_pending_restart=has_pending_restart,
            is_shutting_down=is_shutting_down,
            supports_library_monitor=supports_library_monitor,
            web_socket_port_number=web_socket_port_number,
            completed_installations=completed_installations,
            can_self_restart=can_self_restart,
            can_launch_web_browser=can_launch_web_browser,
            program_data_path=program_data_path,
            web_path=web_path,
            items_by_name_path=items_by_name_path,
            cache_path=cache_path,
            log_path=log_path,
            internal_metadata_path=internal_metadata_path,
            transcoding_temp_path=transcoding_temp_path,
            cast_receiver_applications=cast_receiver_applications,
            has_update_available=has_update_available,
            encoder_location=encoder_location,
            system_architecture=system_architecture,
        )

        return system_info
