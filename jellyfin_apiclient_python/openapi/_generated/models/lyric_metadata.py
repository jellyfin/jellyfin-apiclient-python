from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LyricMetadata")


@_attrs_define
class LyricMetadata:
    """LyricMetadata model.

    Attributes:
        artist (None | str | Unset): Gets or sets the song artist.
        album (None | str | Unset): Gets or sets the album this song is on.
        title (None | str | Unset): Gets or sets the title of the song.
        author (None | str | Unset): Gets or sets the author of the lyric data.
        length (int | None | Unset): Gets or sets the length of the song in ticks.
        by (None | str | Unset): Gets or sets who the LRC file was created by.
        offset (int | None | Unset): Gets or sets the lyric offset compared to audio in ticks.
        creator (None | str | Unset): Gets or sets the software used to create the LRC file.
        version (None | str | Unset): Gets or sets the version of the creator used.
        is_synced (bool | None | Unset): Gets or sets a value indicating whether this lyric is synced.
    """

    artist: None | str | Unset = UNSET
    album: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    author: None | str | Unset = UNSET
    length: int | None | Unset = UNSET
    by: None | str | Unset = UNSET
    offset: int | None | Unset = UNSET
    creator: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    is_synced: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        artist: None | str | Unset
        if isinstance(self.artist, Unset):
            artist = UNSET
        else:
            artist = self.artist

        album: None | str | Unset
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        length: int | None | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        by: None | str | Unset
        if isinstance(self.by, Unset):
            by = UNSET
        else:
            by = self.by

        offset: int | None | Unset
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        creator: None | str | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        else:
            creator = self.creator

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        is_synced: bool | None | Unset
        if isinstance(self.is_synced, Unset):
            is_synced = UNSET
        else:
            is_synced = self.is_synced

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if artist is not UNSET:
            field_dict["Artist"] = artist
        if album is not UNSET:
            field_dict["Album"] = album
        if title is not UNSET:
            field_dict["Title"] = title
        if author is not UNSET:
            field_dict["Author"] = author
        if length is not UNSET:
            field_dict["Length"] = length
        if by is not UNSET:
            field_dict["By"] = by
        if offset is not UNSET:
            field_dict["Offset"] = offset
        if creator is not UNSET:
            field_dict["Creator"] = creator
        if version is not UNSET:
            field_dict["Version"] = version
        if is_synced is not UNSET:
            field_dict["IsSynced"] = is_synced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_artist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        artist = _parse_artist(d.pop("Artist", UNSET))

        def _parse_album(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        album = _parse_album(d.pop("Album", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("Title", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("Author", UNSET))

        def _parse_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length = _parse_length(d.pop("Length", UNSET))

        def _parse_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        by = _parse_by(d.pop("By", UNSET))

        def _parse_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        offset = _parse_offset(d.pop("Offset", UNSET))

        def _parse_creator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creator = _parse_creator(d.pop("Creator", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_is_synced(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_synced = _parse_is_synced(d.pop("IsSynced", UNSET))

        lyric_metadata = cls(
            artist=artist,
            album=album,
            title=title,
            author=author,
            length=length,
            by=by,
            offset=offset,
            creator=creator,
            version=version,
            is_synced=is_synced,
        )

        return lyric_metadata
