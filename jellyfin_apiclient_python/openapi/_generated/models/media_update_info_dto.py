from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_update_info_path_dto import MediaUpdateInfoPathDto


T = TypeVar("T", bound="MediaUpdateInfoDto")


@_attrs_define
class MediaUpdateInfoDto:
    """Media Update Info Dto.

    Attributes:
        updates (list[MediaUpdateInfoPathDto] | Unset): Gets or sets the list of updates.
    """

    updates: list[MediaUpdateInfoPathDto] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for updates_item_data in self.updates:
                updates_item = updates_item_data.to_dict()
                updates.append(updates_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if updates is not UNSET:
            field_dict["Updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_update_info_path_dto import MediaUpdateInfoPathDto

        d = dict(src_dict)
        _updates = d.pop("Updates", UNSET)
        updates: list[MediaUpdateInfoPathDto] | Unset = UNSET
        if _updates is not UNSET:
            updates = []
            for updates_item_data in _updates:
                updates_item = MediaUpdateInfoPathDto.from_dict(updates_item_data)

                updates.append(updates_item)

        media_update_info_dto = cls(
            updates=updates,
        )

        return media_update_info_dto
