from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_item_data_dto import UserItemDataDto


T = TypeVar("T", bound="UserDataChangeInfo")


@_attrs_define
class UserDataChangeInfo:
    """Class UserDataChangeInfo.

    Attributes:
        user_id (UUID | Unset): Gets or sets the user id.
        user_data_list (list[UserItemDataDto] | Unset): Gets or sets the user data list.
    """

    user_id: UUID | Unset = UNSET
    user_data_list: list[UserItemDataDto] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        user_data_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_data_list, Unset):
            user_data_list = []
            for user_data_list_item_data in self.user_data_list:
                user_data_list_item = user_data_list_item_data.to_dict()
                user_data_list.append(user_data_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_data_list is not UNSET:
            field_dict["UserDataList"] = user_data_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_item_data_dto import UserItemDataDto

        d = dict(src_dict)
        _user_id = d.pop("UserId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        _user_data_list = d.pop("UserDataList", UNSET)
        user_data_list: list[UserItemDataDto] | Unset = UNSET
        if _user_data_list is not UNSET:
            user_data_list = []
            for user_data_list_item_data in _user_data_list:
                user_data_list_item = UserItemDataDto.from_dict(
                    user_data_list_item_data
                )

                user_data_list.append(user_data_list_item)

        user_data_change_info = cls(
            user_id=user_id,
            user_data_list=user_data_list,
        )

        return user_data_change_info
