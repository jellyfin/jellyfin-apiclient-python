from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_configuration import UserConfiguration
    from ..models.user_policy import UserPolicy


T = TypeVar("T", bound="UserDto")


@_attrs_define
class UserDto:
    """Class UserDto.

    Attributes:
        name (None | str | Unset): Gets or sets the name.
        server_id (None | str | Unset): Gets or sets the server identifier.
        server_name (None | str | Unset): Gets or sets the name of the server.
            This is not used by the server and is for client-side usage only.
        id (UUID | Unset): Gets or sets the id.
        primary_image_tag (None | str | Unset): Gets or sets the primary image tag.
        has_password (bool | Unset): Gets or sets a value indicating whether this instance has password.
        has_configured_password (bool | Unset): Gets or sets a value indicating whether this instance has configured
            password.
        has_configured_easy_password (bool | Unset): Gets or sets a value indicating whether this instance has
            configured easy password.
        enable_auto_login (bool | None | Unset): Gets or sets whether async login is enabled or not.
        last_login_date (datetime.datetime | None | Unset): Gets or sets the last login date.
        last_activity_date (datetime.datetime | None | Unset): Gets or sets the last activity date.
        configuration (None | Unset | UserConfiguration): Gets or sets the configuration.
        policy (None | Unset | UserPolicy): Gets or sets the policy.
        primary_image_aspect_ratio (float | None | Unset): Gets or sets the primary image aspect ratio.
    """

    name: None | str | Unset = UNSET
    server_id: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    primary_image_tag: None | str | Unset = UNSET
    has_password: bool | Unset = UNSET
    has_configured_password: bool | Unset = UNSET
    has_configured_easy_password: bool | Unset = UNSET
    enable_auto_login: bool | None | Unset = UNSET
    last_login_date: datetime.datetime | None | Unset = UNSET
    last_activity_date: datetime.datetime | None | Unset = UNSET
    configuration: None | Unset | UserConfiguration = UNSET
    policy: None | Unset | UserPolicy = UNSET
    primary_image_aspect_ratio: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_configuration import UserConfiguration
        from ..models.user_policy import UserPolicy

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        server_id: None | str | Unset
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        primary_image_tag: None | str | Unset
        if isinstance(self.primary_image_tag, Unset):
            primary_image_tag = UNSET
        else:
            primary_image_tag = self.primary_image_tag

        has_password = self.has_password

        has_configured_password = self.has_configured_password

        has_configured_easy_password = self.has_configured_easy_password

        enable_auto_login: bool | None | Unset
        if isinstance(self.enable_auto_login, Unset):
            enable_auto_login = UNSET
        else:
            enable_auto_login = self.enable_auto_login

        last_login_date: None | str | Unset
        if isinstance(self.last_login_date, Unset):
            last_login_date = UNSET
        elif isinstance(self.last_login_date, datetime.datetime):
            last_login_date = self.last_login_date.isoformat()
        else:
            last_login_date = self.last_login_date

        last_activity_date: None | str | Unset
        if isinstance(self.last_activity_date, Unset):
            last_activity_date = UNSET
        elif isinstance(self.last_activity_date, datetime.datetime):
            last_activity_date = self.last_activity_date.isoformat()
        else:
            last_activity_date = self.last_activity_date

        configuration: dict[str, Any] | None | Unset
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, UserConfiguration):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        policy: dict[str, Any] | None | Unset
        if isinstance(self.policy, Unset):
            policy = UNSET
        elif isinstance(self.policy, UserPolicy):
            policy = self.policy.to_dict()
        else:
            policy = self.policy

        primary_image_aspect_ratio: float | None | Unset
        if isinstance(self.primary_image_aspect_ratio, Unset):
            primary_image_aspect_ratio = UNSET
        else:
            primary_image_aspect_ratio = self.primary_image_aspect_ratio

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if id is not UNSET:
            field_dict["Id"] = id
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if has_password is not UNSET:
            field_dict["HasPassword"] = has_password
        if has_configured_password is not UNSET:
            field_dict["HasConfiguredPassword"] = has_configured_password
        if has_configured_easy_password is not UNSET:
            field_dict["HasConfiguredEasyPassword"] = has_configured_easy_password
        if enable_auto_login is not UNSET:
            field_dict["EnableAutoLogin"] = enable_auto_login
        if last_login_date is not UNSET:
            field_dict["LastLoginDate"] = last_login_date
        if last_activity_date is not UNSET:
            field_dict["LastActivityDate"] = last_activity_date
        if configuration is not UNSET:
            field_dict["Configuration"] = configuration
        if policy is not UNSET:
            field_dict["Policy"] = policy
        if primary_image_aspect_ratio is not UNSET:
            field_dict["PrimaryImageAspectRatio"] = primary_image_aspect_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_configuration import UserConfiguration
        from ..models.user_policy import UserPolicy

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_id = _parse_server_id(d.pop("ServerId", UNSET))

        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("ServerName", UNSET))

        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_primary_image_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_image_tag = _parse_primary_image_tag(d.pop("PrimaryImageTag", UNSET))

        has_password = d.pop("HasPassword", UNSET)

        has_configured_password = d.pop("HasConfiguredPassword", UNSET)

        has_configured_easy_password = d.pop("HasConfiguredEasyPassword", UNSET)

        def _parse_enable_auto_login(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_auto_login = _parse_enable_auto_login(d.pop("EnableAutoLogin", UNSET))

        def _parse_last_login_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_date_type_0 = isoparse(data)

                return last_login_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login_date = _parse_last_login_date(d.pop("LastLoginDate", UNSET))

        def _parse_last_activity_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_date_type_0 = isoparse(data)

                return last_activity_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_date = _parse_last_activity_date(d.pop("LastActivityDate", UNSET))

        def _parse_configuration(data: object) -> None | Unset | UserConfiguration:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_1 = UserConfiguration.from_dict(data)

                return configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserConfiguration, data)

        configuration = _parse_configuration(d.pop("Configuration", UNSET))

        def _parse_policy(data: object) -> None | Unset | UserPolicy:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_type_1 = UserPolicy.from_dict(data)

                return policy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserPolicy, data)

        policy = _parse_policy(d.pop("Policy", UNSET))

        def _parse_primary_image_aspect_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        primary_image_aspect_ratio = _parse_primary_image_aspect_ratio(
            d.pop("PrimaryImageAspectRatio", UNSET)
        )

        user_dto = cls(
            name=name,
            server_id=server_id,
            server_name=server_name,
            id=id,
            primary_image_tag=primary_image_tag,
            has_password=has_password,
            has_configured_password=has_configured_password,
            has_configured_easy_password=has_configured_easy_password,
            enable_auto_login=enable_auto_login,
            last_login_date=last_login_date,
            last_activity_date=last_activity_date,
            configuration=configuration,
            policy=policy,
            primary_image_aspect_ratio=primary_image_aspect_ratio,
        )

        return user_dto
