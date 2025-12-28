from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.plugin_status import PluginStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginInfo")


@_attrs_define
class PluginInfo:
    """This is a serializable stub class that is used by the api to provide information about installed plugins.

    Attributes:
        name (str | Unset): Gets or sets the name.
        version (str | Unset): Gets or sets the version.
        configuration_file_name (None | str | Unset): Gets or sets the name of the configuration file.
        description (str | Unset): Gets or sets the description.
        id (UUID | Unset): Gets or sets the unique id.
        can_uninstall (bool | Unset): Gets or sets a value indicating whether the plugin can be uninstalled.
        has_image (bool | Unset): Gets or sets a value indicating whether this plugin has a valid image.
        status (PluginStatus | Unset): Plugin load status.
    """

    name: str | Unset = UNSET
    version: str | Unset = UNSET
    configuration_file_name: None | str | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    can_uninstall: bool | Unset = UNSET
    has_image: bool | Unset = UNSET
    status: PluginStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        configuration_file_name: None | str | Unset
        if isinstance(self.configuration_file_name, Unset):
            configuration_file_name = UNSET
        else:
            configuration_file_name = self.configuration_file_name

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        can_uninstall = self.can_uninstall

        has_image = self.has_image

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version
        if configuration_file_name is not UNSET:
            field_dict["ConfigurationFileName"] = configuration_file_name
        if description is not UNSET:
            field_dict["Description"] = description
        if id is not UNSET:
            field_dict["Id"] = id
        if can_uninstall is not UNSET:
            field_dict["CanUninstall"] = can_uninstall
        if has_image is not UNSET:
            field_dict["HasImage"] = has_image
        if status is not UNSET:
            field_dict["Status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        version = d.pop("Version", UNSET)

        def _parse_configuration_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        configuration_file_name = _parse_configuration_file_name(
            d.pop("ConfigurationFileName", UNSET)
        )

        description = d.pop("Description", UNSET)

        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        can_uninstall = d.pop("CanUninstall", UNSET)

        has_image = d.pop("HasImage", UNSET)

        _status = d.pop("Status", UNSET)
        status: PluginStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PluginStatus(_status)

        plugin_info = cls(
            name=name,
            version=version,
            configuration_file_name=configuration_file_name,
            description=description,
            id=id,
            can_uninstall=can_uninstall,
            has_image=has_image,
            status=status,
        )

        return plugin_info
