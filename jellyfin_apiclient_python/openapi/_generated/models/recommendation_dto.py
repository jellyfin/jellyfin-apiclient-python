from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.recommendation_type import RecommendationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto


T = TypeVar("T", bound="RecommendationDto")


@_attrs_define
class RecommendationDto:
    """
    Attributes:
        items (list[BaseItemDto] | None | Unset):
        recommendation_type (RecommendationType | Unset):
        baseline_item_name (None | str | Unset):
        category_id (UUID | Unset):
    """

    items: list[BaseItemDto] | None | Unset = UNSET
    recommendation_type: RecommendationType | Unset = UNSET
    baseline_item_name: None | str | Unset = UNSET
    category_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        recommendation_type: str | Unset = UNSET
        if not isinstance(self.recommendation_type, Unset):
            recommendation_type = self.recommendation_type.value

        baseline_item_name: None | str | Unset
        if isinstance(self.baseline_item_name, Unset):
            baseline_item_name = UNSET
        else:
            baseline_item_name = self.baseline_item_name

        category_id: str | Unset = UNSET
        if not isinstance(self.category_id, Unset):
            category_id = str(self.category_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if recommendation_type is not UNSET:
            field_dict["RecommendationType"] = recommendation_type
        if baseline_item_name is not UNSET:
            field_dict["BaselineItemName"] = baseline_item_name
        if category_id is not UNSET:
            field_dict["CategoryId"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto

        d = dict(src_dict)

        def _parse_items(data: object) -> list[BaseItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = BaseItemDto.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BaseItemDto] | None | Unset, data)

        items = _parse_items(d.pop("Items", UNSET))

        _recommendation_type = d.pop("RecommendationType", UNSET)
        recommendation_type: RecommendationType | Unset
        if isinstance(_recommendation_type, Unset):
            recommendation_type = UNSET
        else:
            recommendation_type = RecommendationType(_recommendation_type)

        def _parse_baseline_item_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        baseline_item_name = _parse_baseline_item_name(d.pop("BaselineItemName", UNSET))

        _category_id = d.pop("CategoryId", UNSET)
        category_id: UUID | Unset
        if isinstance(_category_id, Unset):
            category_id = UNSET
        else:
            category_id = UUID(_category_id)

        recommendation_dto = cls(
            items=items,
            recommendation_type=recommendation_type,
            baseline_item_name=baseline_item_name,
            category_id=category_id,
        )

        return recommendation_dto
