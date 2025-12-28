from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PathSubstitution")


@_attrs_define
class PathSubstitution:
    """Defines the MediaBrowser.Model.Configuration.PathSubstitution.

    Attributes:
        from_ (str | Unset): Gets or sets the value to substitute.
        to (str | Unset): Gets or sets the value to substitution with.
    """

    from_: str | Unset = UNSET
    to: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("From", UNSET)

        to = d.pop("To", UNSET)

        path_substitution = cls(
            from_=from_,
            to=to,
        )

        return path_substitution
