from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteSubtitleInfo")


@_attrs_define
class RemoteSubtitleInfo:
    """
    Attributes:
        three_letter_iso_language_name (None | str | Unset):
        id (None | str | Unset):
        provider_name (None | str | Unset):
        name (None | str | Unset):
        format_ (None | str | Unset):
        author (None | str | Unset):
        comment (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        community_rating (float | None | Unset):
        frame_rate (float | None | Unset):
        download_count (int | None | Unset):
        is_hash_match (bool | None | Unset):
        ai_translated (bool | None | Unset):
        machine_translated (bool | None | Unset):
        forced (bool | None | Unset):
        hearing_impaired (bool | None | Unset):
    """

    three_letter_iso_language_name: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    provider_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    author: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    community_rating: float | None | Unset = UNSET
    frame_rate: float | None | Unset = UNSET
    download_count: int | None | Unset = UNSET
    is_hash_match: bool | None | Unset = UNSET
    ai_translated: bool | None | Unset = UNSET
    machine_translated: bool | None | Unset = UNSET
    forced: bool | None | Unset = UNSET
    hearing_impaired: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        three_letter_iso_language_name: None | str | Unset
        if isinstance(self.three_letter_iso_language_name, Unset):
            three_letter_iso_language_name = UNSET
        else:
            three_letter_iso_language_name = self.three_letter_iso_language_name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        provider_name: None | str | Unset
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        community_rating: float | None | Unset
        if isinstance(self.community_rating, Unset):
            community_rating = UNSET
        else:
            community_rating = self.community_rating

        frame_rate: float | None | Unset
        if isinstance(self.frame_rate, Unset):
            frame_rate = UNSET
        else:
            frame_rate = self.frame_rate

        download_count: int | None | Unset
        if isinstance(self.download_count, Unset):
            download_count = UNSET
        else:
            download_count = self.download_count

        is_hash_match: bool | None | Unset
        if isinstance(self.is_hash_match, Unset):
            is_hash_match = UNSET
        else:
            is_hash_match = self.is_hash_match

        ai_translated: bool | None | Unset
        if isinstance(self.ai_translated, Unset):
            ai_translated = UNSET
        else:
            ai_translated = self.ai_translated

        machine_translated: bool | None | Unset
        if isinstance(self.machine_translated, Unset):
            machine_translated = UNSET
        else:
            machine_translated = self.machine_translated

        forced: bool | None | Unset
        if isinstance(self.forced, Unset):
            forced = UNSET
        else:
            forced = self.forced

        hearing_impaired: bool | None | Unset
        if isinstance(self.hearing_impaired, Unset):
            hearing_impaired = UNSET
        else:
            hearing_impaired = self.hearing_impaired

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if three_letter_iso_language_name is not UNSET:
            field_dict["ThreeLetterISOLanguageName"] = three_letter_iso_language_name
        if id is not UNSET:
            field_dict["Id"] = id
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if name is not UNSET:
            field_dict["Name"] = name
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if author is not UNSET:
            field_dict["Author"] = author
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if frame_rate is not UNSET:
            field_dict["FrameRate"] = frame_rate
        if download_count is not UNSET:
            field_dict["DownloadCount"] = download_count
        if is_hash_match is not UNSET:
            field_dict["IsHashMatch"] = is_hash_match
        if ai_translated is not UNSET:
            field_dict["AiTranslated"] = ai_translated
        if machine_translated is not UNSET:
            field_dict["MachineTranslated"] = machine_translated
        if forced is not UNSET:
            field_dict["Forced"] = forced
        if hearing_impaired is not UNSET:
            field_dict["HearingImpaired"] = hearing_impaired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_three_letter_iso_language_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        three_letter_iso_language_name = _parse_three_letter_iso_language_name(
            d.pop("ThreeLetterISOLanguageName", UNSET)
        )

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_provider_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_name = _parse_provider_name(d.pop("ProviderName", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("Format", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("Author", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("Comment", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = isoparse(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("DateCreated", UNSET))

        def _parse_community_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        community_rating = _parse_community_rating(d.pop("CommunityRating", UNSET))

        def _parse_frame_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        frame_rate = _parse_frame_rate(d.pop("FrameRate", UNSET))

        def _parse_download_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        download_count = _parse_download_count(d.pop("DownloadCount", UNSET))

        def _parse_is_hash_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_hash_match = _parse_is_hash_match(d.pop("IsHashMatch", UNSET))

        def _parse_ai_translated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ai_translated = _parse_ai_translated(d.pop("AiTranslated", UNSET))

        def _parse_machine_translated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        machine_translated = _parse_machine_translated(
            d.pop("MachineTranslated", UNSET)
        )

        def _parse_forced(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        forced = _parse_forced(d.pop("Forced", UNSET))

        def _parse_hearing_impaired(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hearing_impaired = _parse_hearing_impaired(d.pop("HearingImpaired", UNSET))

        remote_subtitle_info = cls(
            three_letter_iso_language_name=three_letter_iso_language_name,
            id=id,
            provider_name=provider_name,
            name=name,
            format_=format_,
            author=author,
            comment=comment,
            date_created=date_created,
            community_rating=community_rating,
            frame_rate=frame_rate,
            download_count=download_count,
            is_hash_match=is_hash_match,
            ai_translated=ai_translated,
            machine_translated=machine_translated,
            forced=forced,
            hearing_impaired=hearing_impaired,
        )

        return remote_subtitle_info
