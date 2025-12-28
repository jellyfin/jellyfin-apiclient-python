from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionInfo")


@_attrs_define
class VersionInfo:
    """Defines the MediaBrowser.Model.Updates.VersionInfo class.

    Attributes:
        version (str | Unset): Gets or sets the version.
        version_number (str | Unset): Gets the version as a System.Version.
        changelog (None | str | Unset): Gets or sets the changelog for this version.
        target_abi (None | str | Unset): Gets or sets the ABI that this version was built against.
        source_url (None | str | Unset): Gets or sets the source URL.
        checksum (None | str | Unset): Gets or sets a checksum for the binary.
        timestamp (None | str | Unset): Gets or sets a timestamp of when the binary was built.
        repository_name (str | Unset): Gets or sets the repository name.
        repository_url (str | Unset): Gets or sets the repository url.
    """

    version: str | Unset = UNSET
    version_number: str | Unset = UNSET
    changelog: None | str | Unset = UNSET
    target_abi: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    checksum: None | str | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    repository_name: str | Unset = UNSET
    repository_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        version_number = self.version_number

        changelog: None | str | Unset
        if isinstance(self.changelog, Unset):
            changelog = UNSET
        else:
            changelog = self.changelog

        target_abi: None | str | Unset
        if isinstance(self.target_abi, Unset):
            target_abi = UNSET
        else:
            target_abi = self.target_abi

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

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        repository_name = self.repository_name

        repository_url = self.repository_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if version_number is not UNSET:
            field_dict["VersionNumber"] = version_number
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if target_abi is not UNSET:
            field_dict["targetAbi"] = target_abi
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if repository_url is not UNSET:
            field_dict["repositoryUrl"] = repository_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        version_number = d.pop("VersionNumber", UNSET)

        def _parse_changelog(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        changelog = _parse_changelog(d.pop("changelog", UNSET))

        def _parse_target_abi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_abi = _parse_target_abi(d.pop("targetAbi", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("sourceUrl", UNSET))

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        repository_name = d.pop("repositoryName", UNSET)

        repository_url = d.pop("repositoryUrl", UNSET)

        version_info = cls(
            version=version,
            version_number=version_number,
            changelog=changelog,
            target_abi=target_abi,
            source_url=source_url,
            checksum=checksum,
            timestamp=timestamp,
            repository_name=repository_name,
            repository_url=repository_url,
        )

        return version_info
