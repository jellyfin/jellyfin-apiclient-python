from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationInfo")


@_attrs_define
class AuthenticationInfo:
    """
    Attributes:
        id (int | Unset): Gets or sets the identifier.
        access_token (None | str | Unset): Gets or sets the access token.
        device_id (None | str | Unset): Gets or sets the device identifier.
        app_name (None | str | Unset): Gets or sets the name of the application.
        app_version (None | str | Unset): Gets or sets the application version.
        device_name (None | str | Unset): Gets or sets the name of the device.
        user_id (UUID | Unset): Gets or sets the user identifier.
        is_active (bool | Unset): Gets or sets a value indicating whether this instance is active.
        date_created (datetime.datetime | Unset): Gets or sets the date created.
        date_revoked (datetime.datetime | None | Unset): Gets or sets the date revoked.
        date_last_activity (datetime.datetime | Unset):
        user_name (None | str | Unset):
    """

    id: int | Unset = UNSET
    access_token: None | str | Unset = UNSET
    device_id: None | str | Unset = UNSET
    app_name: None | str | Unset = UNSET
    app_version: None | str | Unset = UNSET
    device_name: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_revoked: datetime.datetime | None | Unset = UNSET
    date_last_activity: datetime.datetime | Unset = UNSET
    user_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        device_id: None | str | Unset
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

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

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        is_active = self.is_active

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_revoked: None | str | Unset
        if isinstance(self.date_revoked, Unset):
            date_revoked = UNSET
        elif isinstance(self.date_revoked, datetime.datetime):
            date_revoked = self.date_revoked.isoformat()
        else:
            date_revoked = self.date_revoked

        date_last_activity: str | Unset = UNSET
        if not isinstance(self.date_last_activity, Unset):
            date_last_activity = self.date_last_activity.isoformat()

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_revoked is not UNSET:
            field_dict["DateRevoked"] = date_revoked
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_device_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

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

        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("DeviceName", UNSET))

        _user_id = d.pop("UserId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        is_active = d.pop("IsActive", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        def _parse_date_revoked(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_revoked_type_0 = isoparse(data)

                return date_revoked_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_revoked = _parse_date_revoked(d.pop("DateRevoked", UNSET))

        _date_last_activity = d.pop("DateLastActivity", UNSET)
        date_last_activity: datetime.datetime | Unset
        if isinstance(_date_last_activity, Unset):
            date_last_activity = UNSET
        else:
            date_last_activity = isoparse(_date_last_activity)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("UserName", UNSET))

        authentication_info = cls(
            id=id,
            access_token=access_token,
            device_id=device_id,
            app_name=app_name,
            app_version=app_version,
            device_name=device_name,
            user_id=user_id,
            is_active=is_active,
            date_created=date_created,
            date_revoked=date_revoked,
            date_last_activity=date_last_activity,
            user_name=user_name,
        )

        return authentication_info
