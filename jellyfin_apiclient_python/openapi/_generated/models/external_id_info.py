from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.external_id_info_type import ExternalIdInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalIdInfo")


@_attrs_define
class ExternalIdInfo:
    """Represents the external id information for serialization to the client.

    Attributes:
        name (str | Unset): Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz, etc).
        key (str | Unset): Gets or sets the unique key for this id. This key should be unique across all providers.
        type_ (ExternalIdInfoType | Unset): Gets or sets the specific media type for this id. This is used to
            distinguish between the different
            external id types for providers with multiple ids.
            A null value indicates there is no specific media type associated with the external id, or this is the
            default id for the external provider so there is no need to specify a type.
    """

    name: str | Unset = UNSET
    key: str | Unset = UNSET
    type_: ExternalIdInfoType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        key = self.key

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        key = d.pop("Key", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: ExternalIdInfoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ExternalIdInfoType(_type_)

        external_id_info = cls(
            name=name,
            key=key,
            type_=type_,
        )

        return external_id_info
