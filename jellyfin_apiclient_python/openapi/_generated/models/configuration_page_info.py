from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationPageInfo")


@_attrs_define
class ConfigurationPageInfo:
    """The configuration page info.

    Attributes:
        name (str | Unset): Gets or sets the name.
        enable_in_main_menu (bool | Unset): Gets or sets a value indicating whether the configurations page is enabled
            in the main menu.
        menu_section (None | str | Unset): Gets or sets the menu section.
        menu_icon (None | str | Unset): Gets or sets the menu icon.
        display_name (None | str | Unset): Gets or sets the display name.
        plugin_id (None | Unset | UUID): Gets or sets the plugin id.
    """

    name: str | Unset = UNSET
    enable_in_main_menu: bool | Unset = UNSET
    menu_section: None | str | Unset = UNSET
    menu_icon: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    plugin_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable_in_main_menu = self.enable_in_main_menu

        menu_section: None | str | Unset
        if isinstance(self.menu_section, Unset):
            menu_section = UNSET
        else:
            menu_section = self.menu_section

        menu_icon: None | str | Unset
        if isinstance(self.menu_icon, Unset):
            menu_icon = UNSET
        else:
            menu_icon = self.menu_icon

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        plugin_id: None | str | Unset
        if isinstance(self.plugin_id, Unset):
            plugin_id = UNSET
        elif isinstance(self.plugin_id, UUID):
            plugin_id = str(self.plugin_id)
        else:
            plugin_id = self.plugin_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if enable_in_main_menu is not UNSET:
            field_dict["EnableInMainMenu"] = enable_in_main_menu
        if menu_section is not UNSET:
            field_dict["MenuSection"] = menu_section
        if menu_icon is not UNSET:
            field_dict["MenuIcon"] = menu_icon
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if plugin_id is not UNSET:
            field_dict["PluginId"] = plugin_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        enable_in_main_menu = d.pop("EnableInMainMenu", UNSET)

        def _parse_menu_section(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        menu_section = _parse_menu_section(d.pop("MenuSection", UNSET))

        def _parse_menu_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        menu_icon = _parse_menu_icon(d.pop("MenuIcon", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("DisplayName", UNSET))

        def _parse_plugin_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plugin_id_type_0 = UUID(data)

                return plugin_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        plugin_id = _parse_plugin_id(d.pop("PluginId", UNSET))

        configuration_page_info = cls(
            name=name,
            enable_in_main_menu=enable_in_main_menu,
            menu_section=menu_section,
            menu_icon=menu_icon,
            display_name=display_name,
            plugin_id=plugin_id,
        )

        return configuration_page_info
