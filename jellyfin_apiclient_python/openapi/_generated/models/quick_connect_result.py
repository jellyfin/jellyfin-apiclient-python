from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickConnectResult")


@_attrs_define
class QuickConnectResult:
    """Stores the state of an quick connect request.

    Attributes:
        authenticated (bool | Unset): Gets or sets a value indicating whether this request is authorized.
        secret (str | Unset): Gets the secret value used to uniquely identify this request. Can be used to retrieve
            authentication information.
        code (str | Unset): Gets the user facing code used so the user can quickly differentiate this request from
            others.
        device_id (str | Unset): Gets the requesting device id.
        device_name (str | Unset): Gets the requesting device name.
        app_name (str | Unset): Gets the requesting app name.
        app_version (str | Unset): Gets the requesting app version.
        date_added (datetime.datetime | Unset): Gets or sets the DateTime that this request was created.
    """

    authenticated: bool | Unset = UNSET
    secret: str | Unset = UNSET
    code: str | Unset = UNSET
    device_id: str | Unset = UNSET
    device_name: str | Unset = UNSET
    app_name: str | Unset = UNSET
    app_version: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        authenticated = self.authenticated

        secret = self.secret

        code = self.code

        device_id = self.device_id

        device_name = self.device_name

        app_name = self.app_name

        app_version = self.app_version

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["Authenticated"] = authenticated
        if secret is not UNSET:
            field_dict["Secret"] = secret
        if code is not UNSET:
            field_dict["Code"] = code
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if date_added is not UNSET:
            field_dict["DateAdded"] = date_added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authenticated = d.pop("Authenticated", UNSET)

        secret = d.pop("Secret", UNSET)

        code = d.pop("Code", UNSET)

        device_id = d.pop("DeviceId", UNSET)

        device_name = d.pop("DeviceName", UNSET)

        app_name = d.pop("AppName", UNSET)

        app_version = d.pop("AppVersion", UNSET)

        _date_added = d.pop("DateAdded", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        quick_connect_result = cls(
            authenticated=authenticated,
            secret=secret,
            code=code,
            device_id=device_id,
            device_name=device_name,
            app_name=app_name,
            app_version=app_version,
            date_added=date_added,
        )

        return quick_connect_result
