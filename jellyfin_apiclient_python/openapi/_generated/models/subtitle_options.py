from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubtitleOptions")


@_attrs_define
class SubtitleOptions:
    """
    Attributes:
        skip_if_embedded_subtitles_present (bool | Unset):
        skip_if_audio_track_matches (bool | Unset):
        download_languages (list[str] | None | Unset):
        download_movie_subtitles (bool | Unset):
        download_episode_subtitles (bool | Unset):
        open_subtitles_username (None | str | Unset):
        open_subtitles_password_hash (None | str | Unset):
        is_open_subtitle_vip_account (bool | Unset):
        require_perfect_match (bool | Unset):
    """

    skip_if_embedded_subtitles_present: bool | Unset = UNSET
    skip_if_audio_track_matches: bool | Unset = UNSET
    download_languages: list[str] | None | Unset = UNSET
    download_movie_subtitles: bool | Unset = UNSET
    download_episode_subtitles: bool | Unset = UNSET
    open_subtitles_username: None | str | Unset = UNSET
    open_subtitles_password_hash: None | str | Unset = UNSET
    is_open_subtitle_vip_account: bool | Unset = UNSET
    require_perfect_match: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        skip_if_embedded_subtitles_present = self.skip_if_embedded_subtitles_present

        skip_if_audio_track_matches = self.skip_if_audio_track_matches

        download_languages: list[str] | None | Unset
        if isinstance(self.download_languages, Unset):
            download_languages = UNSET
        elif isinstance(self.download_languages, list):
            download_languages = self.download_languages

        else:
            download_languages = self.download_languages

        download_movie_subtitles = self.download_movie_subtitles

        download_episode_subtitles = self.download_episode_subtitles

        open_subtitles_username: None | str | Unset
        if isinstance(self.open_subtitles_username, Unset):
            open_subtitles_username = UNSET
        else:
            open_subtitles_username = self.open_subtitles_username

        open_subtitles_password_hash: None | str | Unset
        if isinstance(self.open_subtitles_password_hash, Unset):
            open_subtitles_password_hash = UNSET
        else:
            open_subtitles_password_hash = self.open_subtitles_password_hash

        is_open_subtitle_vip_account = self.is_open_subtitle_vip_account

        require_perfect_match = self.require_perfect_match

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if skip_if_embedded_subtitles_present is not UNSET:
            field_dict["SkipIfEmbeddedSubtitlesPresent"] = (
                skip_if_embedded_subtitles_present
            )
        if skip_if_audio_track_matches is not UNSET:
            field_dict["SkipIfAudioTrackMatches"] = skip_if_audio_track_matches
        if download_languages is not UNSET:
            field_dict["DownloadLanguages"] = download_languages
        if download_movie_subtitles is not UNSET:
            field_dict["DownloadMovieSubtitles"] = download_movie_subtitles
        if download_episode_subtitles is not UNSET:
            field_dict["DownloadEpisodeSubtitles"] = download_episode_subtitles
        if open_subtitles_username is not UNSET:
            field_dict["OpenSubtitlesUsername"] = open_subtitles_username
        if open_subtitles_password_hash is not UNSET:
            field_dict["OpenSubtitlesPasswordHash"] = open_subtitles_password_hash
        if is_open_subtitle_vip_account is not UNSET:
            field_dict["IsOpenSubtitleVipAccount"] = is_open_subtitle_vip_account
        if require_perfect_match is not UNSET:
            field_dict["RequirePerfectMatch"] = require_perfect_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skip_if_embedded_subtitles_present = d.pop(
            "SkipIfEmbeddedSubtitlesPresent", UNSET
        )

        skip_if_audio_track_matches = d.pop("SkipIfAudioTrackMatches", UNSET)

        def _parse_download_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                download_languages_type_0 = cast(list[str], data)

                return download_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        download_languages = _parse_download_languages(
            d.pop("DownloadLanguages", UNSET)
        )

        download_movie_subtitles = d.pop("DownloadMovieSubtitles", UNSET)

        download_episode_subtitles = d.pop("DownloadEpisodeSubtitles", UNSET)

        def _parse_open_subtitles_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_subtitles_username = _parse_open_subtitles_username(
            d.pop("OpenSubtitlesUsername", UNSET)
        )

        def _parse_open_subtitles_password_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_subtitles_password_hash = _parse_open_subtitles_password_hash(
            d.pop("OpenSubtitlesPasswordHash", UNSET)
        )

        is_open_subtitle_vip_account = d.pop("IsOpenSubtitleVipAccount", UNSET)

        require_perfect_match = d.pop("RequirePerfectMatch", UNSET)

        subtitle_options = cls(
            skip_if_embedded_subtitles_present=skip_if_embedded_subtitles_present,
            skip_if_audio_track_matches=skip_if_audio_track_matches,
            download_languages=download_languages,
            download_movie_subtitles=download_movie_subtitles,
            download_episode_subtitles=download_episode_subtitles,
            open_subtitles_username=open_subtitles_username,
            open_subtitles_password_hash=open_subtitles_password_hash,
            is_open_subtitle_vip_account=is_open_subtitle_vip_account,
            require_perfect_match=require_perfect_match,
        )

        return subtitle_options
