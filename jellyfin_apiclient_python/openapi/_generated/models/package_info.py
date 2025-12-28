from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.version_info import VersionInfo


T = TypeVar("T", bound="PackageInfo")


@_attrs_define
class PackageInfo:
    """Class PackageInfo.

    Attributes:
        name (str | Unset): Gets or sets the name.
        description (str | Unset): Gets or sets a long description of the plugin containing features or helpful
            explanations.
        overview (str | Unset): Gets or sets a short overview of what the plugin does.
        owner (str | Unset): Gets or sets the owner.
        category (str | Unset): Gets or sets the category.
        guid (UUID | Unset): Gets or sets the guid of the assembly associated with this plugin.
            This is used to identify the proper item for automatic updates.
        versions (list[VersionInfo] | Unset): Gets or sets the versions.
        image_url (None | str | Unset): Gets or sets the image url for the package.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    overview: str | Unset = UNSET
    owner: str | Unset = UNSET
    category: str | Unset = UNSET
    guid: UUID | Unset = UNSET
    versions: list[VersionInfo] | Unset = UNSET
    image_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        overview = self.overview

        owner = self.owner

        category = self.category

        guid: str | Unset = UNSET
        if not isinstance(self.guid, Unset):
            guid = str(self.guid)

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if overview is not UNSET:
            field_dict["overview"] = overview
        if owner is not UNSET:
            field_dict["owner"] = owner
        if category is not UNSET:
            field_dict["category"] = category
        if guid is not UNSET:
            field_dict["guid"] = guid
        if versions is not UNSET:
            field_dict["versions"] = versions
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.version_info import VersionInfo

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        overview = d.pop("overview", UNSET)

        owner = d.pop("owner", UNSET)

        category = d.pop("category", UNSET)

        _guid = d.pop("guid", UNSET)
        guid: UUID | Unset
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = UUID(_guid)

        _versions = d.pop("versions", UNSET)
        versions: list[VersionInfo] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = VersionInfo.from_dict(versions_item_data)

                versions.append(versions_item)

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))

        package_info = cls(
            name=name,
            description=description,
            overview=overview,
            owner=owner,
            category=category,
            guid=guid,
            versions=versions,
            image_url=image_url,
        )

        return package_info
