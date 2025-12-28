from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_info import PackageInfo


T = TypeVar("T", bound="InstallationInfo")


@_attrs_define
class InstallationInfo:
    """Class InstallationInfo.

    Attributes:
        guid (UUID | Unset): Gets or sets the Id.
        name (None | str | Unset): Gets or sets the name.
        version (None | str | Unset): Gets or sets the version.
        changelog (None | str | Unset): Gets or sets the changelog for this version.
        source_url (None | str | Unset): Gets or sets the source URL.
        checksum (None | str | Unset): Gets or sets a checksum for the binary.
        package_info (None | PackageInfo | Unset): Gets or sets package information for the installation.
    """

    guid: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    changelog: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    checksum: None | str | Unset = UNSET
    package_info: None | PackageInfo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.package_info import PackageInfo

        guid: str | Unset = UNSET
        if not isinstance(self.guid, Unset):
            guid = str(self.guid)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        changelog: None | str | Unset
        if isinstance(self.changelog, Unset):
            changelog = UNSET
        else:
            changelog = self.changelog

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        package_info: dict[str, Any] | None | Unset
        if isinstance(self.package_info, Unset):
            package_info = UNSET
        elif isinstance(self.package_info, PackageInfo):
            package_info = self.package_info.to_dict()
        else:
            package_info = self.package_info

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version
        if changelog is not UNSET:
            field_dict["Changelog"] = changelog
        if source_url is not UNSET:
            field_dict["SourceUrl"] = source_url
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if package_info is not UNSET:
            field_dict["PackageInfo"] = package_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_info import PackageInfo

        d = dict(src_dict)
        _guid = d.pop("Guid", UNSET)
        guid: UUID | Unset
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = UUID(_guid)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_changelog(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        changelog = _parse_changelog(d.pop("Changelog", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("SourceUrl", UNSET))

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("Checksum", UNSET))

        def _parse_package_info(data: object) -> None | PackageInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                package_info_type_1 = PackageInfo.from_dict(data)

                return package_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PackageInfo | Unset, data)

        package_info = _parse_package_info(d.pop("PackageInfo", UNSET))

        installation_info = cls(
            guid=guid,
            name=name,
            version=version,
            changelog=changelog,
            source_url=source_url,
            checksum=checksum,
            package_info=package_info,
        )

        return installation_info
