from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.profile_condition_type import ProfileConditionType
from ..models.profile_condition_value import ProfileConditionValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileCondition")


@_attrs_define
class ProfileCondition:
    """
    Attributes:
        condition (ProfileConditionType | Unset):
        property_ (ProfileConditionValue | Unset):
        value (None | str | Unset):
        is_required (bool | Unset):
    """

    condition: ProfileConditionType | Unset = UNSET
    property_: ProfileConditionValue | Unset = UNSET
    value: None | str | Unset = UNSET
    is_required: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        condition: str | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.value

        property_: str | Unset = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        is_required = self.is_required

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if property_ is not UNSET:
            field_dict["Property"] = property_
        if value is not UNSET:
            field_dict["Value"] = value
        if is_required is not UNSET:
            field_dict["IsRequired"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _condition = d.pop("Condition", UNSET)
        condition: ProfileConditionType | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = ProfileConditionType(_condition)

        _property_ = d.pop("Property", UNSET)
        property_: ProfileConditionValue | Unset
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = ProfileConditionValue(_property_)

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("Value", UNSET))

        is_required = d.pop("IsRequired", UNSET)

        profile_condition = cls(
            condition=condition,
            property_=property_,
            value=value,
            is_required=is_required,
        )

        return profile_condition
