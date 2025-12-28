from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_info_dto import SessionInfoDto
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="AuthenticationResult")


@_attrs_define
class AuthenticationResult:
    """A class representing an authentication result.

    Attributes:
        user (None | Unset | UserDto): Class UserDto.
        session_info (None | SessionInfoDto | Unset): Session info DTO.
        access_token (None | str | Unset): Gets or sets the access token.
        server_id (None | str | Unset): Gets or sets the server id.
    """

    user: None | Unset | UserDto = UNSET
    session_info: None | SessionInfoDto | Unset = UNSET
    access_token: None | str | Unset = UNSET
    server_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_info_dto import SessionInfoDto
        from ..models.user_dto import UserDto

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UserDto):
            user = self.user.to_dict()
        else:
            user = self.user

        session_info: dict[str, Any] | None | Unset
        if isinstance(self.session_info, Unset):
            session_info = UNSET
        elif isinstance(self.session_info, SessionInfoDto):
            session_info = self.session_info.to_dict()
        else:
            session_info = self.session_info

        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        server_id: None | str | Unset
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["User"] = user
        if session_info is not UNSET:
            field_dict["SessionInfo"] = session_info
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_info_dto import SessionInfoDto
        from ..models.user_dto import UserDto

        d = dict(src_dict)

        def _parse_user(data: object) -> None | Unset | UserDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = UserDto.from_dict(data)

                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserDto, data)

        user = _parse_user(d.pop("User", UNSET))

        def _parse_session_info(data: object) -> None | SessionInfoDto | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_info_type_1 = SessionInfoDto.from_dict(data)

                return session_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionInfoDto | Unset, data)

        session_info = _parse_session_info(d.pop("SessionInfo", UNSET))

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_id = _parse_server_id(d.pop("ServerId", UNSET))

        authentication_result = cls(
            user=user,
            session_info=session_info,
            access_token=access_token,
            server_id=server_id,
        )

        return authentication_result
