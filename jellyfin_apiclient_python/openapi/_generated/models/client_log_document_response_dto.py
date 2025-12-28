from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientLogDocumentResponseDto")


@_attrs_define
class ClientLogDocumentResponseDto:
    """Client log document response dto.

    Attributes:
        file_name (str | Unset): Gets the resulting filename.
    """

    file_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_name is not UNSET:
            field_dict["FileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("FileName", UNSET)

        client_log_document_response_dto = cls(
            file_name=file_name,
        )

        return client_log_document_response_dto
