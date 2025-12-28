from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.group_queue_mode import GroupQueueMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueRequestDto")


@_attrs_define
class QueueRequestDto:
    """Class QueueRequestDto.

    Attributes:
        item_ids (list[UUID] | Unset): Gets or sets the items to enqueue.
        mode (GroupQueueMode | Unset): Enum GroupQueueMode.
    """

    item_ids: list[UUID] | Unset = UNSET
    mode: GroupQueueMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_ids: list[str] | Unset = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = []
            for item_ids_item_data in self.item_ids:
                item_ids_item = str(item_ids_item_data)
                item_ids.append(item_ids_item)

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _item_ids = d.pop("ItemIds", UNSET)
        item_ids: list[UUID] | Unset = UNSET
        if _item_ids is not UNSET:
            item_ids = []
            for item_ids_item_data in _item_ids:
                item_ids_item = UUID(item_ids_item_data)

                item_ids.append(item_ids_item)

        _mode = d.pop("Mode", UNSET)
        mode: GroupQueueMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupQueueMode(_mode)

        queue_request_dto = cls(
            item_ids=item_ids,
            mode=mode,
        )

        return queue_request_dto
