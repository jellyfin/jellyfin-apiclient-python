from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.person_kind import PersonKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_person_image_blur_hashes_type_0 import (
        BaseItemPersonImageBlurHashesType0,
    )


T = TypeVar("T", bound="BaseItemPerson")


@_attrs_define
class BaseItemPerson:
    """This is used by the api to get information about a Person within a BaseItem.

    Attributes:
        name (None | str | Unset): Gets or sets the name.
        id (UUID | Unset): Gets or sets the identifier.
        role (None | str | Unset): Gets or sets the role.
        type_ (PersonKind | Unset): The person kind. Default: PersonKind.UNKNOWN.
        primary_image_tag (None | str | Unset): Gets or sets the primary image tag.
        image_blur_hashes (BaseItemPersonImageBlurHashesType0 | None | Unset): Gets or sets the primary image blurhash.
    """

    name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    role: None | str | Unset = UNSET
    type_: PersonKind | Unset = PersonKind.UNKNOWN
    primary_image_tag: None | str | Unset = UNSET
    image_blur_hashes: BaseItemPersonImageBlurHashesType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_item_person_image_blur_hashes_type_0 import (
            BaseItemPersonImageBlurHashesType0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        primary_image_tag: None | str | Unset
        if isinstance(self.primary_image_tag, Unset):
            primary_image_tag = UNSET
        else:
            primary_image_tag = self.primary_image_tag

        image_blur_hashes: dict[str, Any] | None | Unset
        if isinstance(self.image_blur_hashes, Unset):
            image_blur_hashes = UNSET
        elif isinstance(self.image_blur_hashes, BaseItemPersonImageBlurHashesType0):
            image_blur_hashes = self.image_blur_hashes.to_dict()
        else:
            image_blur_hashes = self.image_blur_hashes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if role is not UNSET:
            field_dict["Role"] = role
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if image_blur_hashes is not UNSET:
            field_dict["ImageBlurHashes"] = image_blur_hashes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_item_person_image_blur_hashes_type_0 import (
            BaseItemPersonImageBlurHashesType0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        _id = d.pop("Id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("Role", UNSET))

        _type_ = d.pop("Type", UNSET)
        type_: PersonKind | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PersonKind(_type_)

        def _parse_primary_image_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_image_tag = _parse_primary_image_tag(d.pop("PrimaryImageTag", UNSET))

        def _parse_image_blur_hashes(
            data: object,
        ) -> BaseItemPersonImageBlurHashesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_blur_hashes_type_0 = BaseItemPersonImageBlurHashesType0.from_dict(
                    data
                )

                return image_blur_hashes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseItemPersonImageBlurHashesType0 | None | Unset, data)

        image_blur_hashes = _parse_image_blur_hashes(d.pop("ImageBlurHashes", UNSET))

        base_item_person = cls(
            name=name,
            id=id,
            role=role,
            type_=type_,
            primary_image_tag=primary_image_tag,
            image_blur_hashes=image_blur_hashes,
        )

        return base_item_person
