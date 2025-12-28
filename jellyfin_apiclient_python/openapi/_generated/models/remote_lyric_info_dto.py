from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lyric_dto import LyricDto


T = TypeVar("T", bound="RemoteLyricInfoDto")


@_attrs_define
class RemoteLyricInfoDto:
    """The remote lyric info dto.

    Attributes:
        id (str | Unset): Gets or sets the id for the lyric.
        provider_name (str | Unset): Gets the provider name.
        lyrics (LyricDto | Unset): LyricResponse model.
    """

    id: str | Unset = UNSET
    provider_name: str | Unset = UNSET
    lyrics: LyricDto | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_name = self.provider_name

        lyrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lyrics, Unset):
            lyrics = self.lyrics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if lyrics is not UNSET:
            field_dict["Lyrics"] = lyrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lyric_dto import LyricDto

        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        provider_name = d.pop("ProviderName", UNSET)

        _lyrics = d.pop("Lyrics", UNSET)
        lyrics: LyricDto | Unset
        if isinstance(_lyrics, Unset):
            lyrics = UNSET
        else:
            lyrics = LyricDto.from_dict(_lyrics)

        remote_lyric_info_dto = cls(
            id=id,
            provider_name=provider_name,
            lyrics=lyrics,
        )

        return remote_lyric_info_dto
