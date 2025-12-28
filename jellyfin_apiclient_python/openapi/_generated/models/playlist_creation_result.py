from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaylistCreationResult")


@_attrs_define
class PlaylistCreationResult:
    """
    Attributes:
        id (str | Unset):
    """

    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        playlist_creation_result = cls(
            id=id,
        )

        return playlist_creation_result
