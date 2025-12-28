from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="QuickConnectDto")


@_attrs_define
class QuickConnectDto:
    """The quick connect request body.

    Attributes:
        secret (str): Gets or sets the quick connect secret.
    """

    secret: str

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("Secret")

        quick_connect_dto = cls(
            secret=secret,
        )

        return quick_connect_dto
