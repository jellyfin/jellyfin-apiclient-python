from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.embedded_subtitle_options import EmbeddedSubtitleOptions
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_path_info import MediaPathInfo
    from ..models.type_options import TypeOptions


T = TypeVar("T", bound="LibraryOptions")


@_attrs_define
class LibraryOptions:
    """
    Attributes:
        enabled (bool | Unset):
        enable_photos (bool | Unset):
        enable_realtime_monitor (bool | Unset):
        enable_lufs_scan (bool | Unset):
        enable_chapter_image_extraction (bool | Unset):
        extract_chapter_images_during_library_scan (bool | Unset):
        enable_trickplay_image_extraction (bool | Unset):
        extract_trickplay_images_during_library_scan (bool | Unset):
        path_infos (list[MediaPathInfo] | Unset):
        save_local_metadata (bool | Unset):
        enable_internet_providers (bool | Unset):
        enable_automatic_series_grouping (bool | Unset):
        enable_embedded_titles (bool | Unset):
        enable_embedded_extras_titles (bool | Unset):
        enable_embedded_episode_infos (bool | Unset):
        automatic_refresh_interval_days (int | Unset):
        preferred_metadata_language (None | str | Unset): Gets or sets the preferred metadata language.
        metadata_country_code (None | str | Unset): Gets or sets the metadata country code.
        season_zero_display_name (str | Unset):
        metadata_savers (list[str] | None | Unset):
        disabled_local_metadata_readers (list[str] | Unset):
        local_metadata_reader_order (list[str] | None | Unset):
        disabled_subtitle_fetchers (list[str] | Unset):
        subtitle_fetcher_order (list[str] | Unset):
        disabled_media_segment_providers (list[str] | Unset):
        media_segment_provider_order (list[str] | Unset):
        skip_subtitles_if_embedded_subtitles_present (bool | Unset):
        skip_subtitles_if_audio_track_matches (bool | Unset):
        subtitle_download_languages (list[str] | None | Unset):
        require_perfect_subtitle_match (bool | Unset):
        save_subtitles_with_media (bool | Unset):
        save_lyrics_with_media (bool | Unset):  Default: False.
        save_trickplay_with_media (bool | Unset):  Default: False.
        disabled_lyric_fetchers (list[str] | Unset):
        lyric_fetcher_order (list[str] | Unset):
        prefer_nonstandard_artists_tag (bool | Unset):  Default: False.
        use_custom_tag_delimiters (bool | Unset):  Default: False.
        custom_tag_delimiters (list[str] | Unset):
        delimiter_whitelist (list[str] | Unset):
        automatically_add_to_collection (bool | Unset):
        allow_embedded_subtitles (EmbeddedSubtitleOptions | Unset): An enum representing the options to disable embedded
            subs.
        type_options (list[TypeOptions] | Unset):
    """

    enabled: bool | Unset = UNSET
    enable_photos: bool | Unset = UNSET
    enable_realtime_monitor: bool | Unset = UNSET
    enable_lufs_scan: bool | Unset = UNSET
    enable_chapter_image_extraction: bool | Unset = UNSET
    extract_chapter_images_during_library_scan: bool | Unset = UNSET
    enable_trickplay_image_extraction: bool | Unset = UNSET
    extract_trickplay_images_during_library_scan: bool | Unset = UNSET
    path_infos: list[MediaPathInfo] | Unset = UNSET
    save_local_metadata: bool | Unset = UNSET
    enable_internet_providers: bool | Unset = UNSET
    enable_automatic_series_grouping: bool | Unset = UNSET
    enable_embedded_titles: bool | Unset = UNSET
    enable_embedded_extras_titles: bool | Unset = UNSET
    enable_embedded_episode_infos: bool | Unset = UNSET
    automatic_refresh_interval_days: int | Unset = UNSET
    preferred_metadata_language: None | str | Unset = UNSET
    metadata_country_code: None | str | Unset = UNSET
    season_zero_display_name: str | Unset = UNSET
    metadata_savers: list[str] | None | Unset = UNSET
    disabled_local_metadata_readers: list[str] | Unset = UNSET
    local_metadata_reader_order: list[str] | None | Unset = UNSET
    disabled_subtitle_fetchers: list[str] | Unset = UNSET
    subtitle_fetcher_order: list[str] | Unset = UNSET
    disabled_media_segment_providers: list[str] | Unset = UNSET
    media_segment_provider_order: list[str] | Unset = UNSET
    skip_subtitles_if_embedded_subtitles_present: bool | Unset = UNSET
    skip_subtitles_if_audio_track_matches: bool | Unset = UNSET
    subtitle_download_languages: list[str] | None | Unset = UNSET
    require_perfect_subtitle_match: bool | Unset = UNSET
    save_subtitles_with_media: bool | Unset = UNSET
    save_lyrics_with_media: bool | Unset = False
    save_trickplay_with_media: bool | Unset = False
    disabled_lyric_fetchers: list[str] | Unset = UNSET
    lyric_fetcher_order: list[str] | Unset = UNSET
    prefer_nonstandard_artists_tag: bool | Unset = False
    use_custom_tag_delimiters: bool | Unset = False
    custom_tag_delimiters: list[str] | Unset = UNSET
    delimiter_whitelist: list[str] | Unset = UNSET
    automatically_add_to_collection: bool | Unset = UNSET
    allow_embedded_subtitles: EmbeddedSubtitleOptions | Unset = UNSET
    type_options: list[TypeOptions] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        enable_photos = self.enable_photos

        enable_realtime_monitor = self.enable_realtime_monitor

        enable_lufs_scan = self.enable_lufs_scan

        enable_chapter_image_extraction = self.enable_chapter_image_extraction

        extract_chapter_images_during_library_scan = (
            self.extract_chapter_images_during_library_scan
        )

        enable_trickplay_image_extraction = self.enable_trickplay_image_extraction

        extract_trickplay_images_during_library_scan = (
            self.extract_trickplay_images_during_library_scan
        )

        path_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.path_infos, Unset):
            path_infos = []
            for path_infos_item_data in self.path_infos:
                path_infos_item = path_infos_item_data.to_dict()
                path_infos.append(path_infos_item)

        save_local_metadata = self.save_local_metadata

        enable_internet_providers = self.enable_internet_providers

        enable_automatic_series_grouping = self.enable_automatic_series_grouping

        enable_embedded_titles = self.enable_embedded_titles

        enable_embedded_extras_titles = self.enable_embedded_extras_titles

        enable_embedded_episode_infos = self.enable_embedded_episode_infos

        automatic_refresh_interval_days = self.automatic_refresh_interval_days

        preferred_metadata_language: None | str | Unset
        if isinstance(self.preferred_metadata_language, Unset):
            preferred_metadata_language = UNSET
        else:
            preferred_metadata_language = self.preferred_metadata_language

        metadata_country_code: None | str | Unset
        if isinstance(self.metadata_country_code, Unset):
            metadata_country_code = UNSET
        else:
            metadata_country_code = self.metadata_country_code

        season_zero_display_name = self.season_zero_display_name

        metadata_savers: list[str] | None | Unset
        if isinstance(self.metadata_savers, Unset):
            metadata_savers = UNSET
        elif isinstance(self.metadata_savers, list):
            metadata_savers = self.metadata_savers

        else:
            metadata_savers = self.metadata_savers

        disabled_local_metadata_readers: list[str] | Unset = UNSET
        if not isinstance(self.disabled_local_metadata_readers, Unset):
            disabled_local_metadata_readers = self.disabled_local_metadata_readers

        local_metadata_reader_order: list[str] | None | Unset
        if isinstance(self.local_metadata_reader_order, Unset):
            local_metadata_reader_order = UNSET
        elif isinstance(self.local_metadata_reader_order, list):
            local_metadata_reader_order = self.local_metadata_reader_order

        else:
            local_metadata_reader_order = self.local_metadata_reader_order

        disabled_subtitle_fetchers: list[str] | Unset = UNSET
        if not isinstance(self.disabled_subtitle_fetchers, Unset):
            disabled_subtitle_fetchers = self.disabled_subtitle_fetchers

        subtitle_fetcher_order: list[str] | Unset = UNSET
        if not isinstance(self.subtitle_fetcher_order, Unset):
            subtitle_fetcher_order = self.subtitle_fetcher_order

        disabled_media_segment_providers: list[str] | Unset = UNSET
        if not isinstance(self.disabled_media_segment_providers, Unset):
            disabled_media_segment_providers = self.disabled_media_segment_providers

        media_segment_provider_order: list[str] | Unset = UNSET
        if not isinstance(self.media_segment_provider_order, Unset):
            media_segment_provider_order = self.media_segment_provider_order

        skip_subtitles_if_embedded_subtitles_present = (
            self.skip_subtitles_if_embedded_subtitles_present
        )

        skip_subtitles_if_audio_track_matches = (
            self.skip_subtitles_if_audio_track_matches
        )

        subtitle_download_languages: list[str] | None | Unset
        if isinstance(self.subtitle_download_languages, Unset):
            subtitle_download_languages = UNSET
        elif isinstance(self.subtitle_download_languages, list):
            subtitle_download_languages = self.subtitle_download_languages

        else:
            subtitle_download_languages = self.subtitle_download_languages

        require_perfect_subtitle_match = self.require_perfect_subtitle_match

        save_subtitles_with_media = self.save_subtitles_with_media

        save_lyrics_with_media = self.save_lyrics_with_media

        save_trickplay_with_media = self.save_trickplay_with_media

        disabled_lyric_fetchers: list[str] | Unset = UNSET
        if not isinstance(self.disabled_lyric_fetchers, Unset):
            disabled_lyric_fetchers = self.disabled_lyric_fetchers

        lyric_fetcher_order: list[str] | Unset = UNSET
        if not isinstance(self.lyric_fetcher_order, Unset):
            lyric_fetcher_order = self.lyric_fetcher_order

        prefer_nonstandard_artists_tag = self.prefer_nonstandard_artists_tag

        use_custom_tag_delimiters = self.use_custom_tag_delimiters

        custom_tag_delimiters: list[str] | Unset = UNSET
        if not isinstance(self.custom_tag_delimiters, Unset):
            custom_tag_delimiters = self.custom_tag_delimiters

        delimiter_whitelist: list[str] | Unset = UNSET
        if not isinstance(self.delimiter_whitelist, Unset):
            delimiter_whitelist = self.delimiter_whitelist

        automatically_add_to_collection = self.automatically_add_to_collection

        allow_embedded_subtitles: str | Unset = UNSET
        if not isinstance(self.allow_embedded_subtitles, Unset):
            allow_embedded_subtitles = self.allow_embedded_subtitles.value

        type_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.type_options, Unset):
            type_options = []
            for type_options_item_data in self.type_options:
                type_options_item = type_options_item_data.to_dict()
                type_options.append(type_options_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if enable_photos is not UNSET:
            field_dict["EnablePhotos"] = enable_photos
        if enable_realtime_monitor is not UNSET:
            field_dict["EnableRealtimeMonitor"] = enable_realtime_monitor
        if enable_lufs_scan is not UNSET:
            field_dict["EnableLUFSScan"] = enable_lufs_scan
        if enable_chapter_image_extraction is not UNSET:
            field_dict["EnableChapterImageExtraction"] = enable_chapter_image_extraction
        if extract_chapter_images_during_library_scan is not UNSET:
            field_dict["ExtractChapterImagesDuringLibraryScan"] = (
                extract_chapter_images_during_library_scan
            )
        if enable_trickplay_image_extraction is not UNSET:
            field_dict["EnableTrickplayImageExtraction"] = (
                enable_trickplay_image_extraction
            )
        if extract_trickplay_images_during_library_scan is not UNSET:
            field_dict["ExtractTrickplayImagesDuringLibraryScan"] = (
                extract_trickplay_images_during_library_scan
            )
        if path_infos is not UNSET:
            field_dict["PathInfos"] = path_infos
        if save_local_metadata is not UNSET:
            field_dict["SaveLocalMetadata"] = save_local_metadata
        if enable_internet_providers is not UNSET:
            field_dict["EnableInternetProviders"] = enable_internet_providers
        if enable_automatic_series_grouping is not UNSET:
            field_dict["EnableAutomaticSeriesGrouping"] = (
                enable_automatic_series_grouping
            )
        if enable_embedded_titles is not UNSET:
            field_dict["EnableEmbeddedTitles"] = enable_embedded_titles
        if enable_embedded_extras_titles is not UNSET:
            field_dict["EnableEmbeddedExtrasTitles"] = enable_embedded_extras_titles
        if enable_embedded_episode_infos is not UNSET:
            field_dict["EnableEmbeddedEpisodeInfos"] = enable_embedded_episode_infos
        if automatic_refresh_interval_days is not UNSET:
            field_dict["AutomaticRefreshIntervalDays"] = automatic_refresh_interval_days
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if season_zero_display_name is not UNSET:
            field_dict["SeasonZeroDisplayName"] = season_zero_display_name
        if metadata_savers is not UNSET:
            field_dict["MetadataSavers"] = metadata_savers
        if disabled_local_metadata_readers is not UNSET:
            field_dict["DisabledLocalMetadataReaders"] = disabled_local_metadata_readers
        if local_metadata_reader_order is not UNSET:
            field_dict["LocalMetadataReaderOrder"] = local_metadata_reader_order
        if disabled_subtitle_fetchers is not UNSET:
            field_dict["DisabledSubtitleFetchers"] = disabled_subtitle_fetchers
        if subtitle_fetcher_order is not UNSET:
            field_dict["SubtitleFetcherOrder"] = subtitle_fetcher_order
        if disabled_media_segment_providers is not UNSET:
            field_dict["DisabledMediaSegmentProviders"] = (
                disabled_media_segment_providers
            )
        if media_segment_provider_order is not UNSET:
            field_dict["MediaSegmentProviderOrder"] = media_segment_provider_order
        if skip_subtitles_if_embedded_subtitles_present is not UNSET:
            field_dict["SkipSubtitlesIfEmbeddedSubtitlesPresent"] = (
                skip_subtitles_if_embedded_subtitles_present
            )
        if skip_subtitles_if_audio_track_matches is not UNSET:
            field_dict["SkipSubtitlesIfAudioTrackMatches"] = (
                skip_subtitles_if_audio_track_matches
            )
        if subtitle_download_languages is not UNSET:
            field_dict["SubtitleDownloadLanguages"] = subtitle_download_languages
        if require_perfect_subtitle_match is not UNSET:
            field_dict["RequirePerfectSubtitleMatch"] = require_perfect_subtitle_match
        if save_subtitles_with_media is not UNSET:
            field_dict["SaveSubtitlesWithMedia"] = save_subtitles_with_media
        if save_lyrics_with_media is not UNSET:
            field_dict["SaveLyricsWithMedia"] = save_lyrics_with_media
        if save_trickplay_with_media is not UNSET:
            field_dict["SaveTrickplayWithMedia"] = save_trickplay_with_media
        if disabled_lyric_fetchers is not UNSET:
            field_dict["DisabledLyricFetchers"] = disabled_lyric_fetchers
        if lyric_fetcher_order is not UNSET:
            field_dict["LyricFetcherOrder"] = lyric_fetcher_order
        if prefer_nonstandard_artists_tag is not UNSET:
            field_dict["PreferNonstandardArtistsTag"] = prefer_nonstandard_artists_tag
        if use_custom_tag_delimiters is not UNSET:
            field_dict["UseCustomTagDelimiters"] = use_custom_tag_delimiters
        if custom_tag_delimiters is not UNSET:
            field_dict["CustomTagDelimiters"] = custom_tag_delimiters
        if delimiter_whitelist is not UNSET:
            field_dict["DelimiterWhitelist"] = delimiter_whitelist
        if automatically_add_to_collection is not UNSET:
            field_dict["AutomaticallyAddToCollection"] = automatically_add_to_collection
        if allow_embedded_subtitles is not UNSET:
            field_dict["AllowEmbeddedSubtitles"] = allow_embedded_subtitles
        if type_options is not UNSET:
            field_dict["TypeOptions"] = type_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_path_info import MediaPathInfo
        from ..models.type_options import TypeOptions

        d = dict(src_dict)
        enabled = d.pop("Enabled", UNSET)

        enable_photos = d.pop("EnablePhotos", UNSET)

        enable_realtime_monitor = d.pop("EnableRealtimeMonitor", UNSET)

        enable_lufs_scan = d.pop("EnableLUFSScan", UNSET)

        enable_chapter_image_extraction = d.pop("EnableChapterImageExtraction", UNSET)

        extract_chapter_images_during_library_scan = d.pop(
            "ExtractChapterImagesDuringLibraryScan", UNSET
        )

        enable_trickplay_image_extraction = d.pop(
            "EnableTrickplayImageExtraction", UNSET
        )

        extract_trickplay_images_during_library_scan = d.pop(
            "ExtractTrickplayImagesDuringLibraryScan", UNSET
        )

        _path_infos = d.pop("PathInfos", UNSET)
        path_infos: list[MediaPathInfo] | Unset = UNSET
        if _path_infos is not UNSET:
            path_infos = []
            for path_infos_item_data in _path_infos:
                path_infos_item = MediaPathInfo.from_dict(path_infos_item_data)

                path_infos.append(path_infos_item)

        save_local_metadata = d.pop("SaveLocalMetadata", UNSET)

        enable_internet_providers = d.pop("EnableInternetProviders", UNSET)

        enable_automatic_series_grouping = d.pop("EnableAutomaticSeriesGrouping", UNSET)

        enable_embedded_titles = d.pop("EnableEmbeddedTitles", UNSET)

        enable_embedded_extras_titles = d.pop("EnableEmbeddedExtrasTitles", UNSET)

        enable_embedded_episode_infos = d.pop("EnableEmbeddedEpisodeInfos", UNSET)

        automatic_refresh_interval_days = d.pop("AutomaticRefreshIntervalDays", UNSET)

        def _parse_preferred_metadata_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_metadata_language = _parse_preferred_metadata_language(
            d.pop("PreferredMetadataLanguage", UNSET)
        )

        def _parse_metadata_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_country_code = _parse_metadata_country_code(
            d.pop("MetadataCountryCode", UNSET)
        )

        season_zero_display_name = d.pop("SeasonZeroDisplayName", UNSET)

        def _parse_metadata_savers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_savers_type_0 = cast(list[str], data)

                return metadata_savers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        metadata_savers = _parse_metadata_savers(d.pop("MetadataSavers", UNSET))

        disabled_local_metadata_readers = cast(
            list[str], d.pop("DisabledLocalMetadataReaders", UNSET)
        )

        def _parse_local_metadata_reader_order(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_metadata_reader_order_type_0 = cast(list[str], data)

                return local_metadata_reader_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        local_metadata_reader_order = _parse_local_metadata_reader_order(
            d.pop("LocalMetadataReaderOrder", UNSET)
        )

        disabled_subtitle_fetchers = cast(
            list[str], d.pop("DisabledSubtitleFetchers", UNSET)
        )

        subtitle_fetcher_order = cast(list[str], d.pop("SubtitleFetcherOrder", UNSET))

        disabled_media_segment_providers = cast(
            list[str], d.pop("DisabledMediaSegmentProviders", UNSET)
        )

        media_segment_provider_order = cast(
            list[str], d.pop("MediaSegmentProviderOrder", UNSET)
        )

        skip_subtitles_if_embedded_subtitles_present = d.pop(
            "SkipSubtitlesIfEmbeddedSubtitlesPresent", UNSET
        )

        skip_subtitles_if_audio_track_matches = d.pop(
            "SkipSubtitlesIfAudioTrackMatches", UNSET
        )

        def _parse_subtitle_download_languages(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtitle_download_languages_type_0 = cast(list[str], data)

                return subtitle_download_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        subtitle_download_languages = _parse_subtitle_download_languages(
            d.pop("SubtitleDownloadLanguages", UNSET)
        )

        require_perfect_subtitle_match = d.pop("RequirePerfectSubtitleMatch", UNSET)

        save_subtitles_with_media = d.pop("SaveSubtitlesWithMedia", UNSET)

        save_lyrics_with_media = d.pop("SaveLyricsWithMedia", UNSET)

        save_trickplay_with_media = d.pop("SaveTrickplayWithMedia", UNSET)

        disabled_lyric_fetchers = cast(list[str], d.pop("DisabledLyricFetchers", UNSET))

        lyric_fetcher_order = cast(list[str], d.pop("LyricFetcherOrder", UNSET))

        prefer_nonstandard_artists_tag = d.pop("PreferNonstandardArtistsTag", UNSET)

        use_custom_tag_delimiters = d.pop("UseCustomTagDelimiters", UNSET)

        custom_tag_delimiters = cast(list[str], d.pop("CustomTagDelimiters", UNSET))

        delimiter_whitelist = cast(list[str], d.pop("DelimiterWhitelist", UNSET))

        automatically_add_to_collection = d.pop("AutomaticallyAddToCollection", UNSET)

        _allow_embedded_subtitles = d.pop("AllowEmbeddedSubtitles", UNSET)
        allow_embedded_subtitles: EmbeddedSubtitleOptions | Unset
        if isinstance(_allow_embedded_subtitles, Unset):
            allow_embedded_subtitles = UNSET
        else:
            allow_embedded_subtitles = EmbeddedSubtitleOptions(
                _allow_embedded_subtitles
            )

        _type_options = d.pop("TypeOptions", UNSET)
        type_options: list[TypeOptions] | Unset = UNSET
        if _type_options is not UNSET:
            type_options = []
            for type_options_item_data in _type_options:
                type_options_item = TypeOptions.from_dict(type_options_item_data)

                type_options.append(type_options_item)

        library_options = cls(
            enabled=enabled,
            enable_photos=enable_photos,
            enable_realtime_monitor=enable_realtime_monitor,
            enable_lufs_scan=enable_lufs_scan,
            enable_chapter_image_extraction=enable_chapter_image_extraction,
            extract_chapter_images_during_library_scan=extract_chapter_images_during_library_scan,
            enable_trickplay_image_extraction=enable_trickplay_image_extraction,
            extract_trickplay_images_during_library_scan=extract_trickplay_images_during_library_scan,
            path_infos=path_infos,
            save_local_metadata=save_local_metadata,
            enable_internet_providers=enable_internet_providers,
            enable_automatic_series_grouping=enable_automatic_series_grouping,
            enable_embedded_titles=enable_embedded_titles,
            enable_embedded_extras_titles=enable_embedded_extras_titles,
            enable_embedded_episode_infos=enable_embedded_episode_infos,
            automatic_refresh_interval_days=automatic_refresh_interval_days,
            preferred_metadata_language=preferred_metadata_language,
            metadata_country_code=metadata_country_code,
            season_zero_display_name=season_zero_display_name,
            metadata_savers=metadata_savers,
            disabled_local_metadata_readers=disabled_local_metadata_readers,
            local_metadata_reader_order=local_metadata_reader_order,
            disabled_subtitle_fetchers=disabled_subtitle_fetchers,
            subtitle_fetcher_order=subtitle_fetcher_order,
            disabled_media_segment_providers=disabled_media_segment_providers,
            media_segment_provider_order=media_segment_provider_order,
            skip_subtitles_if_embedded_subtitles_present=skip_subtitles_if_embedded_subtitles_present,
            skip_subtitles_if_audio_track_matches=skip_subtitles_if_audio_track_matches,
            subtitle_download_languages=subtitle_download_languages,
            require_perfect_subtitle_match=require_perfect_subtitle_match,
            save_subtitles_with_media=save_subtitles_with_media,
            save_lyrics_with_media=save_lyrics_with_media,
            save_trickplay_with_media=save_trickplay_with_media,
            disabled_lyric_fetchers=disabled_lyric_fetchers,
            lyric_fetcher_order=lyric_fetcher_order,
            prefer_nonstandard_artists_tag=prefer_nonstandard_artists_tag,
            use_custom_tag_delimiters=use_custom_tag_delimiters,
            custom_tag_delimiters=custom_tag_delimiters,
            delimiter_whitelist=delimiter_whitelist,
            automatically_add_to_collection=automatically_add_to_collection,
            allow_embedded_subtitles=allow_embedded_subtitles,
            type_options=type_options,
        )

        return library_options
