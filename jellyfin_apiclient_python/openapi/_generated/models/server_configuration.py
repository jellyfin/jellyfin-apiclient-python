from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.image_resolution import ImageResolution
from ..models.image_saving_convention import ImageSavingConvention
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cast_receiver_application import CastReceiverApplication
    from ..models.metadata_options import MetadataOptions
    from ..models.name_value_pair import NameValuePair
    from ..models.path_substitution import PathSubstitution
    from ..models.repository_info import RepositoryInfo
    from ..models.trickplay_options import TrickplayOptions


T = TypeVar("T", bound="ServerConfiguration")


@_attrs_define
class ServerConfiguration:
    """Represents the server configuration.

    Attributes:
        log_file_retention_days (int | Unset): Gets or sets the number of days we should retain log files.
        is_startup_wizard_completed (bool | Unset): Gets or sets a value indicating whether this instance is first run.
        cache_path (None | str | Unset): Gets or sets the cache path.
        previous_version (None | str | Unset): Gets or sets the last known version that was ran using the configuration.
        previous_version_str (None | str | Unset): Gets or sets the stringified PreviousVersion to be stored/loaded,
            because System.Version itself isn't xml-serializable.
        enable_metrics (bool | Unset): Gets or sets a value indicating whether to enable prometheus metrics exporting.
        enable_normalized_item_by_name_ids (bool | Unset):
        is_port_authorized (bool | Unset): Gets or sets a value indicating whether this instance is port authorized.
        quick_connect_available (bool | Unset): Gets or sets a value indicating whether quick connect is available for
            use on this server.
        enable_case_sensitive_item_ids (bool | Unset): Gets or sets a value indicating whether [enable case-sensitive
            item ids].
        disable_live_tv_channel_user_data_name (bool | Unset):
        metadata_path (str | Unset): Gets or sets the metadata path.
        preferred_metadata_language (str | Unset): Gets or sets the preferred metadata language.
        metadata_country_code (str | Unset): Gets or sets the metadata country code.
        sort_replace_characters (list[str] | Unset): Gets or sets characters to be replaced with a ' ' in strings to
            create a sort name.
        sort_remove_characters (list[str] | Unset): Gets or sets characters to be removed from strings to create a sort
            name.
        sort_remove_words (list[str] | Unset): Gets or sets words to be removed from strings to create a sort name.
        min_resume_pct (int | Unset): Gets or sets the minimum percentage of an item that must be played in order for
            playstate to be updated.
        max_resume_pct (int | Unset): Gets or sets the maximum percentage of an item that can be played while still
            saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be
            marked watched.
        min_resume_duration_seconds (int | Unset): Gets or sets the minimum duration that an item must have in order to
            be eligible for playstate updates..
        min_audiobook_resume (int | Unset): Gets or sets the minimum minutes of a book that must be played in order for
            playstate to be updated.
        max_audiobook_resume (int | Unset): Gets or sets the remaining minutes of a book that can be played while still
            saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be
            marked watched.
        inactive_session_threshold (int | Unset): Gets or sets the threshold in minutes after a inactive session gets
            closed automatically.
            If set to 0 the check for inactive sessions gets disabled.
        library_monitor_delay (int | Unset): Gets or sets the delay in seconds that we will wait after a file system
            change to try and discover what has been added/removed
            Some delay is necessary with some items because their creation is not atomic.  It involves the creation of
            several
            different directories and files.
        library_update_duration (int | Unset): Gets or sets the duration in seconds that we will wait after a library
            updated event before executing the library changed notification.
        cache_size (int | Unset): Gets or sets the maximum amount of items to cache.
        image_saving_convention (ImageSavingConvention | Unset):
        metadata_options (list[MetadataOptions] | Unset):
        skip_deserialization_for_basic_types (bool | Unset):
        server_name (str | Unset):
        ui_culture (str | Unset):
        save_metadata_hidden (bool | Unset):
        content_types (list[NameValuePair] | Unset):
        remote_client_bitrate_limit (int | Unset):
        enable_folder_view (bool | Unset):
        enable_grouping_movies_into_collections (bool | Unset):
        enable_grouping_shows_into_collections (bool | Unset):
        display_specials_within_seasons (bool | Unset):
        codecs_used (list[str] | Unset):
        plugin_repositories (list[RepositoryInfo] | Unset):
        enable_external_content_in_suggestions (bool | Unset):
        image_extraction_timeout_ms (int | Unset):
        path_substitutions (list[PathSubstitution] | Unset):
        enable_slow_response_warning (bool | Unset): Gets or sets a value indicating whether slow server responses
            should be logged as a warning.
        slow_response_threshold_ms (int | Unset): Gets or sets the threshold for the slow response time warning in ms.
        cors_hosts (list[str] | Unset): Gets or sets the cors hosts.
        activity_log_retention_days (int | None | Unset): Gets or sets the number of days we should retain activity
            logs.
        library_scan_fanout_concurrency (int | Unset): Gets or sets the how the library scan fans out.
        library_metadata_refresh_concurrency (int | Unset): Gets or sets the how many metadata refreshes can run
            concurrently.
        allow_client_log_upload (bool | Unset): Gets or sets a value indicating whether clients should be allowed to
            upload logs.
        dummy_chapter_duration (int | Unset): Gets or sets the dummy chapter duration in seconds, use 0 (zero) or less
            to disable generation altogether.
        chapter_image_resolution (ImageResolution | Unset): Enum ImageResolution.
        parallel_image_encoding_limit (int | Unset): Gets or sets the limit for parallel image encoding.
        cast_receiver_applications (list[CastReceiverApplication] | Unset): Gets or sets the list of cast receiver
            applications.
        trickplay_options (TrickplayOptions | Unset): Class TrickplayOptions.
        enable_legacy_authorization (bool | Unset): Gets or sets a value indicating whether old authorization methods
            are allowed.
    """

    log_file_retention_days: int | Unset = UNSET
    is_startup_wizard_completed: bool | Unset = UNSET
    cache_path: None | str | Unset = UNSET
    previous_version: None | str | Unset = UNSET
    previous_version_str: None | str | Unset = UNSET
    enable_metrics: bool | Unset = UNSET
    enable_normalized_item_by_name_ids: bool | Unset = UNSET
    is_port_authorized: bool | Unset = UNSET
    quick_connect_available: bool | Unset = UNSET
    enable_case_sensitive_item_ids: bool | Unset = UNSET
    disable_live_tv_channel_user_data_name: bool | Unset = UNSET
    metadata_path: str | Unset = UNSET
    preferred_metadata_language: str | Unset = UNSET
    metadata_country_code: str | Unset = UNSET
    sort_replace_characters: list[str] | Unset = UNSET
    sort_remove_characters: list[str] | Unset = UNSET
    sort_remove_words: list[str] | Unset = UNSET
    min_resume_pct: int | Unset = UNSET
    max_resume_pct: int | Unset = UNSET
    min_resume_duration_seconds: int | Unset = UNSET
    min_audiobook_resume: int | Unset = UNSET
    max_audiobook_resume: int | Unset = UNSET
    inactive_session_threshold: int | Unset = UNSET
    library_monitor_delay: int | Unset = UNSET
    library_update_duration: int | Unset = UNSET
    cache_size: int | Unset = UNSET
    image_saving_convention: ImageSavingConvention | Unset = UNSET
    metadata_options: list[MetadataOptions] | Unset = UNSET
    skip_deserialization_for_basic_types: bool | Unset = UNSET
    server_name: str | Unset = UNSET
    ui_culture: str | Unset = UNSET
    save_metadata_hidden: bool | Unset = UNSET
    content_types: list[NameValuePair] | Unset = UNSET
    remote_client_bitrate_limit: int | Unset = UNSET
    enable_folder_view: bool | Unset = UNSET
    enable_grouping_movies_into_collections: bool | Unset = UNSET
    enable_grouping_shows_into_collections: bool | Unset = UNSET
    display_specials_within_seasons: bool | Unset = UNSET
    codecs_used: list[str] | Unset = UNSET
    plugin_repositories: list[RepositoryInfo] | Unset = UNSET
    enable_external_content_in_suggestions: bool | Unset = UNSET
    image_extraction_timeout_ms: int | Unset = UNSET
    path_substitutions: list[PathSubstitution] | Unset = UNSET
    enable_slow_response_warning: bool | Unset = UNSET
    slow_response_threshold_ms: int | Unset = UNSET
    cors_hosts: list[str] | Unset = UNSET
    activity_log_retention_days: int | None | Unset = UNSET
    library_scan_fanout_concurrency: int | Unset = UNSET
    library_metadata_refresh_concurrency: int | Unset = UNSET
    allow_client_log_upload: bool | Unset = UNSET
    dummy_chapter_duration: int | Unset = UNSET
    chapter_image_resolution: ImageResolution | Unset = UNSET
    parallel_image_encoding_limit: int | Unset = UNSET
    cast_receiver_applications: list[CastReceiverApplication] | Unset = UNSET
    trickplay_options: TrickplayOptions | Unset = UNSET
    enable_legacy_authorization: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        log_file_retention_days = self.log_file_retention_days

        is_startup_wizard_completed = self.is_startup_wizard_completed

        cache_path: None | str | Unset
        if isinstance(self.cache_path, Unset):
            cache_path = UNSET
        else:
            cache_path = self.cache_path

        previous_version: None | str | Unset
        if isinstance(self.previous_version, Unset):
            previous_version = UNSET
        else:
            previous_version = self.previous_version

        previous_version_str: None | str | Unset
        if isinstance(self.previous_version_str, Unset):
            previous_version_str = UNSET
        else:
            previous_version_str = self.previous_version_str

        enable_metrics = self.enable_metrics

        enable_normalized_item_by_name_ids = self.enable_normalized_item_by_name_ids

        is_port_authorized = self.is_port_authorized

        quick_connect_available = self.quick_connect_available

        enable_case_sensitive_item_ids = self.enable_case_sensitive_item_ids

        disable_live_tv_channel_user_data_name = (
            self.disable_live_tv_channel_user_data_name
        )

        metadata_path = self.metadata_path

        preferred_metadata_language = self.preferred_metadata_language

        metadata_country_code = self.metadata_country_code

        sort_replace_characters: list[str] | Unset = UNSET
        if not isinstance(self.sort_replace_characters, Unset):
            sort_replace_characters = self.sort_replace_characters

        sort_remove_characters: list[str] | Unset = UNSET
        if not isinstance(self.sort_remove_characters, Unset):
            sort_remove_characters = self.sort_remove_characters

        sort_remove_words: list[str] | Unset = UNSET
        if not isinstance(self.sort_remove_words, Unset):
            sort_remove_words = self.sort_remove_words

        min_resume_pct = self.min_resume_pct

        max_resume_pct = self.max_resume_pct

        min_resume_duration_seconds = self.min_resume_duration_seconds

        min_audiobook_resume = self.min_audiobook_resume

        max_audiobook_resume = self.max_audiobook_resume

        inactive_session_threshold = self.inactive_session_threshold

        library_monitor_delay = self.library_monitor_delay

        library_update_duration = self.library_update_duration

        cache_size = self.cache_size

        image_saving_convention: str | Unset = UNSET
        if not isinstance(self.image_saving_convention, Unset):
            image_saving_convention = self.image_saving_convention.value

        metadata_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metadata_options, Unset):
            metadata_options = []
            for metadata_options_item_data in self.metadata_options:
                metadata_options_item = metadata_options_item_data.to_dict()
                metadata_options.append(metadata_options_item)

        skip_deserialization_for_basic_types = self.skip_deserialization_for_basic_types

        server_name = self.server_name

        ui_culture = self.ui_culture

        save_metadata_hidden = self.save_metadata_hidden

        content_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_types, Unset):
            content_types = []
            for content_types_item_data in self.content_types:
                content_types_item = content_types_item_data.to_dict()
                content_types.append(content_types_item)

        remote_client_bitrate_limit = self.remote_client_bitrate_limit

        enable_folder_view = self.enable_folder_view

        enable_grouping_movies_into_collections = (
            self.enable_grouping_movies_into_collections
        )

        enable_grouping_shows_into_collections = (
            self.enable_grouping_shows_into_collections
        )

        display_specials_within_seasons = self.display_specials_within_seasons

        codecs_used: list[str] | Unset = UNSET
        if not isinstance(self.codecs_used, Unset):
            codecs_used = self.codecs_used

        plugin_repositories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.plugin_repositories, Unset):
            plugin_repositories = []
            for plugin_repositories_item_data in self.plugin_repositories:
                plugin_repositories_item = plugin_repositories_item_data.to_dict()
                plugin_repositories.append(plugin_repositories_item)

        enable_external_content_in_suggestions = (
            self.enable_external_content_in_suggestions
        )

        image_extraction_timeout_ms = self.image_extraction_timeout_ms

        path_substitutions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.path_substitutions, Unset):
            path_substitutions = []
            for path_substitutions_item_data in self.path_substitutions:
                path_substitutions_item = path_substitutions_item_data.to_dict()
                path_substitutions.append(path_substitutions_item)

        enable_slow_response_warning = self.enable_slow_response_warning

        slow_response_threshold_ms = self.slow_response_threshold_ms

        cors_hosts: list[str] | Unset = UNSET
        if not isinstance(self.cors_hosts, Unset):
            cors_hosts = self.cors_hosts

        activity_log_retention_days: int | None | Unset
        if isinstance(self.activity_log_retention_days, Unset):
            activity_log_retention_days = UNSET
        else:
            activity_log_retention_days = self.activity_log_retention_days

        library_scan_fanout_concurrency = self.library_scan_fanout_concurrency

        library_metadata_refresh_concurrency = self.library_metadata_refresh_concurrency

        allow_client_log_upload = self.allow_client_log_upload

        dummy_chapter_duration = self.dummy_chapter_duration

        chapter_image_resolution: str | Unset = UNSET
        if not isinstance(self.chapter_image_resolution, Unset):
            chapter_image_resolution = self.chapter_image_resolution.value

        parallel_image_encoding_limit = self.parallel_image_encoding_limit

        cast_receiver_applications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cast_receiver_applications, Unset):
            cast_receiver_applications = []
            for cast_receiver_applications_item_data in self.cast_receiver_applications:
                cast_receiver_applications_item = (
                    cast_receiver_applications_item_data.to_dict()
                )
                cast_receiver_applications.append(cast_receiver_applications_item)

        trickplay_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trickplay_options, Unset):
            trickplay_options = self.trickplay_options.to_dict()

        enable_legacy_authorization = self.enable_legacy_authorization

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if log_file_retention_days is not UNSET:
            field_dict["LogFileRetentionDays"] = log_file_retention_days
        if is_startup_wizard_completed is not UNSET:
            field_dict["IsStartupWizardCompleted"] = is_startup_wizard_completed
        if cache_path is not UNSET:
            field_dict["CachePath"] = cache_path
        if previous_version is not UNSET:
            field_dict["PreviousVersion"] = previous_version
        if previous_version_str is not UNSET:
            field_dict["PreviousVersionStr"] = previous_version_str
        if enable_metrics is not UNSET:
            field_dict["EnableMetrics"] = enable_metrics
        if enable_normalized_item_by_name_ids is not UNSET:
            field_dict["EnableNormalizedItemByNameIds"] = (
                enable_normalized_item_by_name_ids
            )
        if is_port_authorized is not UNSET:
            field_dict["IsPortAuthorized"] = is_port_authorized
        if quick_connect_available is not UNSET:
            field_dict["QuickConnectAvailable"] = quick_connect_available
        if enable_case_sensitive_item_ids is not UNSET:
            field_dict["EnableCaseSensitiveItemIds"] = enable_case_sensitive_item_ids
        if disable_live_tv_channel_user_data_name is not UNSET:
            field_dict["DisableLiveTvChannelUserDataName"] = (
                disable_live_tv_channel_user_data_name
            )
        if metadata_path is not UNSET:
            field_dict["MetadataPath"] = metadata_path
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if sort_replace_characters is not UNSET:
            field_dict["SortReplaceCharacters"] = sort_replace_characters
        if sort_remove_characters is not UNSET:
            field_dict["SortRemoveCharacters"] = sort_remove_characters
        if sort_remove_words is not UNSET:
            field_dict["SortRemoveWords"] = sort_remove_words
        if min_resume_pct is not UNSET:
            field_dict["MinResumePct"] = min_resume_pct
        if max_resume_pct is not UNSET:
            field_dict["MaxResumePct"] = max_resume_pct
        if min_resume_duration_seconds is not UNSET:
            field_dict["MinResumeDurationSeconds"] = min_resume_duration_seconds
        if min_audiobook_resume is not UNSET:
            field_dict["MinAudiobookResume"] = min_audiobook_resume
        if max_audiobook_resume is not UNSET:
            field_dict["MaxAudiobookResume"] = max_audiobook_resume
        if inactive_session_threshold is not UNSET:
            field_dict["InactiveSessionThreshold"] = inactive_session_threshold
        if library_monitor_delay is not UNSET:
            field_dict["LibraryMonitorDelay"] = library_monitor_delay
        if library_update_duration is not UNSET:
            field_dict["LibraryUpdateDuration"] = library_update_duration
        if cache_size is not UNSET:
            field_dict["CacheSize"] = cache_size
        if image_saving_convention is not UNSET:
            field_dict["ImageSavingConvention"] = image_saving_convention
        if metadata_options is not UNSET:
            field_dict["MetadataOptions"] = metadata_options
        if skip_deserialization_for_basic_types is not UNSET:
            field_dict["SkipDeserializationForBasicTypes"] = (
                skip_deserialization_for_basic_types
            )
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if ui_culture is not UNSET:
            field_dict["UICulture"] = ui_culture
        if save_metadata_hidden is not UNSET:
            field_dict["SaveMetadataHidden"] = save_metadata_hidden
        if content_types is not UNSET:
            field_dict["ContentTypes"] = content_types
        if remote_client_bitrate_limit is not UNSET:
            field_dict["RemoteClientBitrateLimit"] = remote_client_bitrate_limit
        if enable_folder_view is not UNSET:
            field_dict["EnableFolderView"] = enable_folder_view
        if enable_grouping_movies_into_collections is not UNSET:
            field_dict["EnableGroupingMoviesIntoCollections"] = (
                enable_grouping_movies_into_collections
            )
        if enable_grouping_shows_into_collections is not UNSET:
            field_dict["EnableGroupingShowsIntoCollections"] = (
                enable_grouping_shows_into_collections
            )
        if display_specials_within_seasons is not UNSET:
            field_dict["DisplaySpecialsWithinSeasons"] = display_specials_within_seasons
        if codecs_used is not UNSET:
            field_dict["CodecsUsed"] = codecs_used
        if plugin_repositories is not UNSET:
            field_dict["PluginRepositories"] = plugin_repositories
        if enable_external_content_in_suggestions is not UNSET:
            field_dict["EnableExternalContentInSuggestions"] = (
                enable_external_content_in_suggestions
            )
        if image_extraction_timeout_ms is not UNSET:
            field_dict["ImageExtractionTimeoutMs"] = image_extraction_timeout_ms
        if path_substitutions is not UNSET:
            field_dict["PathSubstitutions"] = path_substitutions
        if enable_slow_response_warning is not UNSET:
            field_dict["EnableSlowResponseWarning"] = enable_slow_response_warning
        if slow_response_threshold_ms is not UNSET:
            field_dict["SlowResponseThresholdMs"] = slow_response_threshold_ms
        if cors_hosts is not UNSET:
            field_dict["CorsHosts"] = cors_hosts
        if activity_log_retention_days is not UNSET:
            field_dict["ActivityLogRetentionDays"] = activity_log_retention_days
        if library_scan_fanout_concurrency is not UNSET:
            field_dict["LibraryScanFanoutConcurrency"] = library_scan_fanout_concurrency
        if library_metadata_refresh_concurrency is not UNSET:
            field_dict["LibraryMetadataRefreshConcurrency"] = (
                library_metadata_refresh_concurrency
            )
        if allow_client_log_upload is not UNSET:
            field_dict["AllowClientLogUpload"] = allow_client_log_upload
        if dummy_chapter_duration is not UNSET:
            field_dict["DummyChapterDuration"] = dummy_chapter_duration
        if chapter_image_resolution is not UNSET:
            field_dict["ChapterImageResolution"] = chapter_image_resolution
        if parallel_image_encoding_limit is not UNSET:
            field_dict["ParallelImageEncodingLimit"] = parallel_image_encoding_limit
        if cast_receiver_applications is not UNSET:
            field_dict["CastReceiverApplications"] = cast_receiver_applications
        if trickplay_options is not UNSET:
            field_dict["TrickplayOptions"] = trickplay_options
        if enable_legacy_authorization is not UNSET:
            field_dict["EnableLegacyAuthorization"] = enable_legacy_authorization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cast_receiver_application import CastReceiverApplication
        from ..models.metadata_options import MetadataOptions
        from ..models.name_value_pair import NameValuePair
        from ..models.path_substitution import PathSubstitution
        from ..models.repository_info import RepositoryInfo
        from ..models.trickplay_options import TrickplayOptions

        d = dict(src_dict)
        log_file_retention_days = d.pop("LogFileRetentionDays", UNSET)

        is_startup_wizard_completed = d.pop("IsStartupWizardCompleted", UNSET)

        def _parse_cache_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_path = _parse_cache_path(d.pop("CachePath", UNSET))

        def _parse_previous_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_version = _parse_previous_version(d.pop("PreviousVersion", UNSET))

        def _parse_previous_version_str(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_version_str = _parse_previous_version_str(
            d.pop("PreviousVersionStr", UNSET)
        )

        enable_metrics = d.pop("EnableMetrics", UNSET)

        enable_normalized_item_by_name_ids = d.pop(
            "EnableNormalizedItemByNameIds", UNSET
        )

        is_port_authorized = d.pop("IsPortAuthorized", UNSET)

        quick_connect_available = d.pop("QuickConnectAvailable", UNSET)

        enable_case_sensitive_item_ids = d.pop("EnableCaseSensitiveItemIds", UNSET)

        disable_live_tv_channel_user_data_name = d.pop(
            "DisableLiveTvChannelUserDataName", UNSET
        )

        metadata_path = d.pop("MetadataPath", UNSET)

        preferred_metadata_language = d.pop("PreferredMetadataLanguage", UNSET)

        metadata_country_code = d.pop("MetadataCountryCode", UNSET)

        sort_replace_characters = cast(list[str], d.pop("SortReplaceCharacters", UNSET))

        sort_remove_characters = cast(list[str], d.pop("SortRemoveCharacters", UNSET))

        sort_remove_words = cast(list[str], d.pop("SortRemoveWords", UNSET))

        min_resume_pct = d.pop("MinResumePct", UNSET)

        max_resume_pct = d.pop("MaxResumePct", UNSET)

        min_resume_duration_seconds = d.pop("MinResumeDurationSeconds", UNSET)

        min_audiobook_resume = d.pop("MinAudiobookResume", UNSET)

        max_audiobook_resume = d.pop("MaxAudiobookResume", UNSET)

        inactive_session_threshold = d.pop("InactiveSessionThreshold", UNSET)

        library_monitor_delay = d.pop("LibraryMonitorDelay", UNSET)

        library_update_duration = d.pop("LibraryUpdateDuration", UNSET)

        cache_size = d.pop("CacheSize", UNSET)

        _image_saving_convention = d.pop("ImageSavingConvention", UNSET)
        image_saving_convention: ImageSavingConvention | Unset
        if isinstance(_image_saving_convention, Unset):
            image_saving_convention = UNSET
        else:
            image_saving_convention = ImageSavingConvention(_image_saving_convention)

        _metadata_options = d.pop("MetadataOptions", UNSET)
        metadata_options: list[MetadataOptions] | Unset = UNSET
        if _metadata_options is not UNSET:
            metadata_options = []
            for metadata_options_item_data in _metadata_options:
                metadata_options_item = MetadataOptions.from_dict(
                    metadata_options_item_data
                )

                metadata_options.append(metadata_options_item)

        skip_deserialization_for_basic_types = d.pop(
            "SkipDeserializationForBasicTypes", UNSET
        )

        server_name = d.pop("ServerName", UNSET)

        ui_culture = d.pop("UICulture", UNSET)

        save_metadata_hidden = d.pop("SaveMetadataHidden", UNSET)

        _content_types = d.pop("ContentTypes", UNSET)
        content_types: list[NameValuePair] | Unset = UNSET
        if _content_types is not UNSET:
            content_types = []
            for content_types_item_data in _content_types:
                content_types_item = NameValuePair.from_dict(content_types_item_data)

                content_types.append(content_types_item)

        remote_client_bitrate_limit = d.pop("RemoteClientBitrateLimit", UNSET)

        enable_folder_view = d.pop("EnableFolderView", UNSET)

        enable_grouping_movies_into_collections = d.pop(
            "EnableGroupingMoviesIntoCollections", UNSET
        )

        enable_grouping_shows_into_collections = d.pop(
            "EnableGroupingShowsIntoCollections", UNSET
        )

        display_specials_within_seasons = d.pop("DisplaySpecialsWithinSeasons", UNSET)

        codecs_used = cast(list[str], d.pop("CodecsUsed", UNSET))

        _plugin_repositories = d.pop("PluginRepositories", UNSET)
        plugin_repositories: list[RepositoryInfo] | Unset = UNSET
        if _plugin_repositories is not UNSET:
            plugin_repositories = []
            for plugin_repositories_item_data in _plugin_repositories:
                plugin_repositories_item = RepositoryInfo.from_dict(
                    plugin_repositories_item_data
                )

                plugin_repositories.append(plugin_repositories_item)

        enable_external_content_in_suggestions = d.pop(
            "EnableExternalContentInSuggestions", UNSET
        )

        image_extraction_timeout_ms = d.pop("ImageExtractionTimeoutMs", UNSET)

        _path_substitutions = d.pop("PathSubstitutions", UNSET)
        path_substitutions: list[PathSubstitution] | Unset = UNSET
        if _path_substitutions is not UNSET:
            path_substitutions = []
            for path_substitutions_item_data in _path_substitutions:
                path_substitutions_item = PathSubstitution.from_dict(
                    path_substitutions_item_data
                )

                path_substitutions.append(path_substitutions_item)

        enable_slow_response_warning = d.pop("EnableSlowResponseWarning", UNSET)

        slow_response_threshold_ms = d.pop("SlowResponseThresholdMs", UNSET)

        cors_hosts = cast(list[str], d.pop("CorsHosts", UNSET))

        def _parse_activity_log_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        activity_log_retention_days = _parse_activity_log_retention_days(
            d.pop("ActivityLogRetentionDays", UNSET)
        )

        library_scan_fanout_concurrency = d.pop("LibraryScanFanoutConcurrency", UNSET)

        library_metadata_refresh_concurrency = d.pop(
            "LibraryMetadataRefreshConcurrency", UNSET
        )

        allow_client_log_upload = d.pop("AllowClientLogUpload", UNSET)

        dummy_chapter_duration = d.pop("DummyChapterDuration", UNSET)

        _chapter_image_resolution = d.pop("ChapterImageResolution", UNSET)
        chapter_image_resolution: ImageResolution | Unset
        if isinstance(_chapter_image_resolution, Unset):
            chapter_image_resolution = UNSET
        else:
            chapter_image_resolution = ImageResolution(_chapter_image_resolution)

        parallel_image_encoding_limit = d.pop("ParallelImageEncodingLimit", UNSET)

        _cast_receiver_applications = d.pop("CastReceiverApplications", UNSET)
        cast_receiver_applications: list[CastReceiverApplication] | Unset = UNSET
        if _cast_receiver_applications is not UNSET:
            cast_receiver_applications = []
            for cast_receiver_applications_item_data in _cast_receiver_applications:
                cast_receiver_applications_item = CastReceiverApplication.from_dict(
                    cast_receiver_applications_item_data
                )

                cast_receiver_applications.append(cast_receiver_applications_item)

        _trickplay_options = d.pop("TrickplayOptions", UNSET)
        trickplay_options: TrickplayOptions | Unset
        if isinstance(_trickplay_options, Unset):
            trickplay_options = UNSET
        else:
            trickplay_options = TrickplayOptions.from_dict(_trickplay_options)

        enable_legacy_authorization = d.pop("EnableLegacyAuthorization", UNSET)

        server_configuration = cls(
            log_file_retention_days=log_file_retention_days,
            is_startup_wizard_completed=is_startup_wizard_completed,
            cache_path=cache_path,
            previous_version=previous_version,
            previous_version_str=previous_version_str,
            enable_metrics=enable_metrics,
            enable_normalized_item_by_name_ids=enable_normalized_item_by_name_ids,
            is_port_authorized=is_port_authorized,
            quick_connect_available=quick_connect_available,
            enable_case_sensitive_item_ids=enable_case_sensitive_item_ids,
            disable_live_tv_channel_user_data_name=disable_live_tv_channel_user_data_name,
            metadata_path=metadata_path,
            preferred_metadata_language=preferred_metadata_language,
            metadata_country_code=metadata_country_code,
            sort_replace_characters=sort_replace_characters,
            sort_remove_characters=sort_remove_characters,
            sort_remove_words=sort_remove_words,
            min_resume_pct=min_resume_pct,
            max_resume_pct=max_resume_pct,
            min_resume_duration_seconds=min_resume_duration_seconds,
            min_audiobook_resume=min_audiobook_resume,
            max_audiobook_resume=max_audiobook_resume,
            inactive_session_threshold=inactive_session_threshold,
            library_monitor_delay=library_monitor_delay,
            library_update_duration=library_update_duration,
            cache_size=cache_size,
            image_saving_convention=image_saving_convention,
            metadata_options=metadata_options,
            skip_deserialization_for_basic_types=skip_deserialization_for_basic_types,
            server_name=server_name,
            ui_culture=ui_culture,
            save_metadata_hidden=save_metadata_hidden,
            content_types=content_types,
            remote_client_bitrate_limit=remote_client_bitrate_limit,
            enable_folder_view=enable_folder_view,
            enable_grouping_movies_into_collections=enable_grouping_movies_into_collections,
            enable_grouping_shows_into_collections=enable_grouping_shows_into_collections,
            display_specials_within_seasons=display_specials_within_seasons,
            codecs_used=codecs_used,
            plugin_repositories=plugin_repositories,
            enable_external_content_in_suggestions=enable_external_content_in_suggestions,
            image_extraction_timeout_ms=image_extraction_timeout_ms,
            path_substitutions=path_substitutions,
            enable_slow_response_warning=enable_slow_response_warning,
            slow_response_threshold_ms=slow_response_threshold_ms,
            cors_hosts=cors_hosts,
            activity_log_retention_days=activity_log_retention_days,
            library_scan_fanout_concurrency=library_scan_fanout_concurrency,
            library_metadata_refresh_concurrency=library_metadata_refresh_concurrency,
            allow_client_log_upload=allow_client_log_upload,
            dummy_chapter_duration=dummy_chapter_duration,
            chapter_image_resolution=chapter_image_resolution,
            parallel_image_encoding_limit=parallel_image_encoding_limit,
            cast_receiver_applications=cast_receiver_applications,
            trickplay_options=trickplay_options,
            enable_legacy_authorization=enable_legacy_authorization,
        )

        return server_configuration
