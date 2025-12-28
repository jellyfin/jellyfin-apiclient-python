from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_capabilities_dto import ClientCapabilitiesDto


T = TypeVar("T", bound="DeviceInfoDto")


@_attrs_define
class DeviceInfoDto:
    """A DTO representing device information.

    Attributes:
        name (None | str | Unset): Gets or sets the name.
        custom_name (None | str | Unset): Gets or sets the custom name.
        access_token (None | str | Unset): Gets or sets the access token.
        id (None | str | Unset): Gets or sets the identifier.
        last_user_name (None | str | Unset): Gets or sets the last name of the user.
        app_name (None | str | Unset): Gets or sets the name of the application.
        app_version (None | str | Unset): Gets or sets the application version.
        last_user_id (None | Unset | UUID): Gets or sets the last user identifier.
        date_last_activity (datetime.datetime | None | Unset): Gets or sets the date last modified.
        capabilities (ClientCapabilitiesDto | Unset): Client capabilities dto.
        icon_url (None | str | Unset): Gets or sets the icon URL.
    """

    name: None | str | Unset = UNSET
    custom_name: None | str | Unset = UNSET
    access_token: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    last_user_name: None | str | Unset = UNSET
    app_name: None | str | Unset = UNSET
    app_version: None | str | Unset = UNSET
    last_user_id: None | Unset | UUID = UNSET
    date_last_activity: datetime.datetime | None | Unset = UNSET
    capabilities: ClientCapabilitiesDto | Unset = UNSET
    icon_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        custom_name: None | str | Unset
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last_user_name: None | str | Unset
        if isinstance(self.last_user_name, Unset):
            last_user_name = UNSET
        else:
            last_user_name = self.last_user_name

        app_name: None | str | Unset
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        app_version: None | str | Unset
        if isinstance(self.app_version, Unset):
            app_version = UNSET
        else:
            app_version = self.app_version

        last_user_id: None | str | Unset
        if isinstance(self.last_user_id, Unset):
            last_user_id = UNSET
        elif isinstance(self.last_user_id, UUID):
            last_user_id = str(self.last_user_id)
        else:
            last_user_id = self.last_user_id

        date_last_activity: None | str | Unset
        if isinstance(self.date_last_activity, Unset):
            date_last_activity = UNSET
        elif isinstance(self.date_last_activity, datetime.datetime):
            date_last_activity = self.date_last_activity.isoformat()
        else:
            date_last_activity = self.date_last_activity

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if id is not UNSET:
            field_dict["Id"] = id
        if last_user_name is not UNSET:
            field_dict["LastUserName"] = last_user_name
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if last_user_id is not UNSET:
            field_dict["LastUserId"] = last_user_id
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_capabilities_dto import ClientCapabilitiesDto

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_custom_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_name = _parse_custom_name(d.pop("CustomName", UNSET))

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_last_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_user_name = _parse_last_user_name(d.pop("LastUserName", UNSET))

        def _parse_app_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_name = _parse_app_name(d.pop("AppName", UNSET))

        def _parse_app_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_version = _parse_app_version(d.pop("AppVersion", UNSET))

        def _parse_last_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_user_id_type_0 = UUID(data)

                return last_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        last_user_id = _parse_last_user_id(d.pop("LastUserId", UNSET))

        def _parse_date_last_activity(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_last_activity_type_0 = isoparse(data)

                return date_last_activity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_last_activity = _parse_date_last_activity(d.pop("DateLastActivity", UNSET))

        _capabilities = d.pop("Capabilities", UNSET)
        capabilities: ClientCapabilitiesDto | Unset
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = ClientCapabilitiesDto.from_dict(_capabilities)

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("IconUrl", UNSET))

        device_info_dto = cls(
            name=name,
            custom_name=custom_name,
            access_token=access_token,
            id=id,
            last_user_name=last_user_name,
            app_name=app_name,
            app_version=app_version,
            last_user_id=last_user_id,
            date_last_activity=date_last_activity,
            capabilities=capabilities,
            icon_url=icon_url,
        )

        return device_info_dto
