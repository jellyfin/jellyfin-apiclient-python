from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_hint import SearchHint


T = TypeVar("T", bound="SearchHintResult")


@_attrs_define
class SearchHintResult:
    """Class SearchHintResult.

    Attributes:
        search_hints (list[SearchHint] | Unset): Gets the search hints.
        total_record_count (int | Unset): Gets the total record count.
    """

    search_hints: list[SearchHint] | Unset = UNSET
    total_record_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        search_hints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.search_hints, Unset):
            search_hints = []
            for search_hints_item_data in self.search_hints:
                search_hints_item = search_hints_item_data.to_dict()
                search_hints.append(search_hints_item)

        total_record_count = self.total_record_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if search_hints is not UNSET:
            field_dict["SearchHints"] = search_hints
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_hint import SearchHint

        d = dict(src_dict)
        _search_hints = d.pop("SearchHints", UNSET)
        search_hints: list[SearchHint] | Unset = UNSET
        if _search_hints is not UNSET:
            search_hints = []
            for search_hints_item_data in _search_hints:
                search_hints_item = SearchHint.from_dict(search_hints_item_data)

                search_hints.append(search_hints_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        search_hint_result = cls(
            search_hints=search_hints,
            total_record_count=total_record_count,
        )

        return search_hint_result
