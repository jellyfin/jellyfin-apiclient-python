from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_options import LibraryOptions


T = TypeVar("T", bound="UpdateLibraryOptionsDto")


@_attrs_define
class UpdateLibraryOptionsDto:
    """Update library options dto.

    Attributes:
        id (UUID | Unset): Gets or sets the library item id.
        library_options (LibraryOptions | None | Unset): Gets or sets library options.
    """

    id: UUID | Unset = UNSET
    library_options: LibraryOptions | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.library_options import LibraryOptions

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        library_options: dict[str, Any] | None | Unset
        if isinstance(self.library_options, Unset):
            library_options = UNSET
        elif isinstance(self.library_options, LibraryOptions):
            library_options = self.library_options.to_dict()
        else:
            library_options = self.library_options

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if library_options is not UNSET:
            field_dict["LibraryOptions"] = library_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_options import LibraryOptions

        d = dict(src_dict)
        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_library_options(data: object) -> LibraryOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                library_options_type_1 = LibraryOptions.from_dict(data)

                return library_options_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LibraryOptions | None | Unset, data)

        library_options = _parse_library_options(d.pop("LibraryOptions", UNSET))

        update_library_options_dto = cls(
            id=id,
            library_options=library_options,
        )

        return update_library_options_dto
