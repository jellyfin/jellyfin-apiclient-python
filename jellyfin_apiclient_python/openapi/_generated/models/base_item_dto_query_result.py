from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto


T = TypeVar("T", bound="BaseItemDtoQueryResult")


@_attrs_define
class BaseItemDtoQueryResult:
    """Query result container.

    Attributes:
        items (list[BaseItemDto] | Unset): Gets or sets the items.
        total_record_count (int | Unset): Gets or sets the total number of records available.
        start_index (int | Unset): Gets or sets the index of the first record in Items.
    """

    items: list[BaseItemDto] | Unset = UNSET
    total_record_count: int | Unset = UNSET
    start_index: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        total_record_count = self.total_record_count

        start_index = self.start_index

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto

        d = dict(src_dict)
        _items = d.pop("Items", UNSET)
        items: list[BaseItemDto] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BaseItemDto.from_dict(items_item_data)

                items.append(items_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        base_item_dto_query_result = cls(
            items=items,
            total_record_count=total_record_count,
            start_index=start_index,
        )

        return base_item_dto_query_result
