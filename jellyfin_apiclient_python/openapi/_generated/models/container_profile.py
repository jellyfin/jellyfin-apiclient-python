from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="ContainerProfile")


@_attrs_define
class ContainerProfile:
    """Defines the MediaBrowser.Model.Dlna.ContainerProfile.

    Attributes:
        type_ (DlnaProfileType | Unset):
        conditions (list[ProfileCondition] | Unset): Gets or sets the list of MediaBrowser.Model.Dlna.ProfileCondition
            which this container will be applied to.
        container (None | str | Unset): Gets or sets the container(s) which this container must meet.
        sub_container (None | str | Unset): Gets or sets the sub container(s) which this container must meet.
    """

    type_: DlnaProfileType | Unset = UNSET
    conditions: list[ProfileCondition] | Unset = UNSET
    container: None | str | Unset = UNSET
    sub_container: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        container: None | str | Unset
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        sub_container: None | str | Unset
        if isinstance(self.sub_container, Unset):
            sub_container = UNSET
        else:
            sub_container = self.sub_container

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if container is not UNSET:
            field_dict["Container"] = container
        if sub_container is not UNSET:
            field_dict["SubContainer"] = sub_container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = dict(src_dict)
        _type_ = d.pop("Type", UNSET)
        type_: DlnaProfileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DlnaProfileType(_type_)

        _conditions = d.pop("Conditions", UNSET)
        conditions: list[ProfileCondition] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ProfileCondition.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        def _parse_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_sub_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_container = _parse_sub_container(d.pop("SubContainer", UNSET))

        container_profile = cls(
            type_=type_,
            conditions=conditions,
            container=container,
            sub_container=sub_container,
        )

        return container_profile
