"""Contains all the data models used in inputs/outputs"""

from .access_schedule import AccessSchedule
from .activity_log_entry import ActivityLogEntry
from .activity_log_entry_message import ActivityLogEntryMessage
from .activity_log_entry_query_result import ActivityLogEntryQueryResult
from .activity_log_entry_start_message import ActivityLogEntryStartMessage
from .activity_log_entry_stop_message import ActivityLogEntryStopMessage
from .add_virtual_folder_dto import AddVirtualFolderDto
from .album_info import AlbumInfo
from .album_info_artist_provider_ids import AlbumInfoArtistProviderIds
from .album_info_provider_ids_type_0 import AlbumInfoProviderIdsType0
from .album_info_remote_search_query import AlbumInfoRemoteSearchQuery
from .all_theme_media_result import AllThemeMediaResult
from .artist_info import ArtistInfo
from .artist_info_provider_ids_type_0 import ArtistInfoProviderIdsType0
from .artist_info_remote_search_query import ArtistInfoRemoteSearchQuery
from .audio_spatial_format import AudioSpatialFormat
from .authenticate_user_by_name import AuthenticateUserByName
from .authentication_info import AuthenticationInfo
from .authentication_info_query_result import AuthenticationInfoQueryResult
from .authentication_result import AuthenticationResult
from .backup_manifest_dto import BackupManifestDto
from .backup_options_dto import BackupOptionsDto
from .backup_restore_request_dto import BackupRestoreRequestDto
from .base_item_dto import BaseItemDto
from .base_item_dto_audio import BaseItemDtoAudio
from .base_item_dto_channel_type import BaseItemDtoChannelType
from .base_item_dto_collection_type import BaseItemDtoCollectionType
from .base_item_dto_extra_type import BaseItemDtoExtraType
from .base_item_dto_image_blur_hashes_type_0 import BaseItemDtoImageBlurHashesType0
from .base_item_dto_image_blur_hashes_type_0_art import (
    BaseItemDtoImageBlurHashesType0Art,
)
from .base_item_dto_image_blur_hashes_type_0_backdrop import (
    BaseItemDtoImageBlurHashesType0Backdrop,
)
from .base_item_dto_image_blur_hashes_type_0_banner import (
    BaseItemDtoImageBlurHashesType0Banner,
)
from .base_item_dto_image_blur_hashes_type_0_box import (
    BaseItemDtoImageBlurHashesType0Box,
)
from .base_item_dto_image_blur_hashes_type_0_box_rear import (
    BaseItemDtoImageBlurHashesType0BoxRear,
)
from .base_item_dto_image_blur_hashes_type_0_chapter import (
    BaseItemDtoImageBlurHashesType0Chapter,
)
from .base_item_dto_image_blur_hashes_type_0_disc import (
    BaseItemDtoImageBlurHashesType0Disc,
)
from .base_item_dto_image_blur_hashes_type_0_logo import (
    BaseItemDtoImageBlurHashesType0Logo,
)
from .base_item_dto_image_blur_hashes_type_0_menu import (
    BaseItemDtoImageBlurHashesType0Menu,
)
from .base_item_dto_image_blur_hashes_type_0_primary import (
    BaseItemDtoImageBlurHashesType0Primary,
)
from .base_item_dto_image_blur_hashes_type_0_profile import (
    BaseItemDtoImageBlurHashesType0Profile,
)
from .base_item_dto_image_blur_hashes_type_0_screenshot import (
    BaseItemDtoImageBlurHashesType0Screenshot,
)
from .base_item_dto_image_blur_hashes_type_0_thumb import (
    BaseItemDtoImageBlurHashesType0Thumb,
)
from .base_item_dto_image_orientation import BaseItemDtoImageOrientation
from .base_item_dto_image_tags_type_0 import BaseItemDtoImageTagsType0
from .base_item_dto_iso_type import BaseItemDtoIsoType
from .base_item_dto_location_type import BaseItemDtoLocationType
from .base_item_dto_play_access import BaseItemDtoPlayAccess
from .base_item_dto_provider_ids_type_0 import BaseItemDtoProviderIdsType0
from .base_item_dto_query_result import BaseItemDtoQueryResult
from .base_item_dto_trickplay_type_0 import BaseItemDtoTrickplayType0
from .base_item_dto_trickplay_type_0_additional_property import (
    BaseItemDtoTrickplayType0AdditionalProperty,
)
from .base_item_dto_video_3d_format import BaseItemDtoVideo3DFormat
from .base_item_dto_video_type import BaseItemDtoVideoType
from .base_item_kind import BaseItemKind
from .base_item_person import BaseItemPerson
from .base_item_person_image_blur_hashes_type_0 import (
    BaseItemPersonImageBlurHashesType0,
)
from .base_item_person_image_blur_hashes_type_0_art import (
    BaseItemPersonImageBlurHashesType0Art,
)
from .base_item_person_image_blur_hashes_type_0_backdrop import (
    BaseItemPersonImageBlurHashesType0Backdrop,
)
from .base_item_person_image_blur_hashes_type_0_banner import (
    BaseItemPersonImageBlurHashesType0Banner,
)
from .base_item_person_image_blur_hashes_type_0_box import (
    BaseItemPersonImageBlurHashesType0Box,
)
from .base_item_person_image_blur_hashes_type_0_box_rear import (
    BaseItemPersonImageBlurHashesType0BoxRear,
)
from .base_item_person_image_blur_hashes_type_0_chapter import (
    BaseItemPersonImageBlurHashesType0Chapter,
)
from .base_item_person_image_blur_hashes_type_0_disc import (
    BaseItemPersonImageBlurHashesType0Disc,
)
from .base_item_person_image_blur_hashes_type_0_logo import (
    BaseItemPersonImageBlurHashesType0Logo,
)
from .base_item_person_image_blur_hashes_type_0_menu import (
    BaseItemPersonImageBlurHashesType0Menu,
)
from .base_item_person_image_blur_hashes_type_0_primary import (
    BaseItemPersonImageBlurHashesType0Primary,
)
from .base_item_person_image_blur_hashes_type_0_profile import (
    BaseItemPersonImageBlurHashesType0Profile,
)
from .base_item_person_image_blur_hashes_type_0_screenshot import (
    BaseItemPersonImageBlurHashesType0Screenshot,
)
from .base_item_person_image_blur_hashes_type_0_thumb import (
    BaseItemPersonImageBlurHashesType0Thumb,
)
from .base_plugin_configuration import BasePluginConfiguration
from .book_info import BookInfo
from .book_info_provider_ids_type_0 import BookInfoProviderIdsType0
from .book_info_remote_search_query import BookInfoRemoteSearchQuery
from .box_set_info import BoxSetInfo
from .box_set_info_provider_ids_type_0 import BoxSetInfoProviderIdsType0
from .box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery
from .branding_options_dto import BrandingOptionsDto
from .buffer_request_dto import BufferRequestDto
from .cast_receiver_application import CastReceiverApplication
from .channel_features import ChannelFeatures
from .channel_item_sort_field import ChannelItemSortField
from .channel_mapping_options_dto import ChannelMappingOptionsDto
from .channel_media_content_type import ChannelMediaContentType
from .channel_media_type import ChannelMediaType
from .channel_type import ChannelType
from .chapter_info import ChapterInfo
from .client_capabilities_dto import ClientCapabilitiesDto
from .client_log_document_response_dto import ClientLogDocumentResponseDto
from .codec_profile import CodecProfile
from .codec_type import CodecType
from .collection_creation_result import CollectionCreationResult
from .collection_type import CollectionType
from .collection_type_options import CollectionTypeOptions
from .config_image_types import ConfigImageTypes
from .configuration_page_info import ConfigurationPageInfo
from .container_profile import ContainerProfile
from .country_info import CountryInfo
from .create_playlist_dto import CreatePlaylistDto
from .create_playlist_dto_media_type import CreatePlaylistDtoMediaType
from .create_user_by_name import CreateUserByName
from .culture_dto import CultureDto
from .custom_database_option import CustomDatabaseOption
from .custom_database_options import CustomDatabaseOptions
from .database_configuration_options import DatabaseConfigurationOptions
from .database_locking_behavior_types import DatabaseLockingBehaviorTypes
from .day_of_week import DayOfWeek
from .day_pattern import DayPattern
from .default_directory_browser_info_dto import DefaultDirectoryBrowserInfoDto
from .deinterlace_method import DeinterlaceMethod
from .device_info_dto import DeviceInfoDto
from .device_info_dto_query_result import DeviceInfoDtoQueryResult
from .device_options_dto import DeviceOptionsDto
from .device_profile import DeviceProfile
from .direct_play_profile import DirectPlayProfile
from .display_preferences_dto import DisplayPreferencesDto
from .display_preferences_dto_custom_prefs import DisplayPreferencesDtoCustomPrefs
from .dlna_profile_type import DlnaProfileType
from .down_mix_stereo_algorithms import DownMixStereoAlgorithms
from .dynamic_day_of_week import DynamicDayOfWeek
from .embedded_subtitle_options import EmbeddedSubtitleOptions
from .encoder_preset import EncoderPreset
from .encoding_context import EncodingContext
from .encoding_options import EncodingOptions
from .encoding_options_encoder_preset import EncodingOptionsEncoderPreset
from .end_point_info import EndPointInfo
from .external_id_info import ExternalIdInfo
from .external_id_info_type import ExternalIdInfoType
from .external_id_media_type import ExternalIdMediaType
from .external_url import ExternalUrl
from .extra_type import ExtraType
from .file_system_entry_info import FileSystemEntryInfo
from .file_system_entry_type import FileSystemEntryType
from .folder_storage_dto import FolderStorageDto
from .font_file import FontFile
from .force_keep_alive_message import ForceKeepAliveMessage
from .forgot_password_action import ForgotPasswordAction
from .forgot_password_dto import ForgotPasswordDto
from .forgot_password_pin_dto import ForgotPasswordPinDto
from .forgot_password_result import ForgotPasswordResult
from .general_command import GeneralCommand
from .general_command_arguments import GeneralCommandArguments
from .general_command_message import GeneralCommandMessage
from .general_command_type import GeneralCommandType
from .get_audio_stream_by_container_stream_options import (
    GetAudioStreamByContainerStreamOptions,
)
from .get_audio_stream_stream_options import GetAudioStreamStreamOptions
from .get_hls_audio_segment_stream_options import GetHlsAudioSegmentStreamOptions
from .get_hls_video_segment_stream_options import GetHlsVideoSegmentStreamOptions
from .get_live_hls_stream_stream_options import GetLiveHlsStreamStreamOptions
from .get_master_hls_audio_playlist_stream_options import (
    GetMasterHlsAudioPlaylistStreamOptions,
)
from .get_master_hls_video_playlist_stream_options import (
    GetMasterHlsVideoPlaylistStreamOptions,
)
from .get_programs_dto import GetProgramsDto
from .get_variant_hls_audio_playlist_stream_options import (
    GetVariantHlsAudioPlaylistStreamOptions,
)
from .get_variant_hls_video_playlist_stream_options import (
    GetVariantHlsVideoPlaylistStreamOptions,
)
from .get_video_stream_by_container_stream_options import (
    GetVideoStreamByContainerStreamOptions,
)
from .get_video_stream_stream_options import GetVideoStreamStreamOptions
from .group_info_dto import GroupInfoDto
from .group_queue_mode import GroupQueueMode
from .group_repeat_mode import GroupRepeatMode
from .group_shuffle_mode import GroupShuffleMode
from .group_state_type import GroupStateType
from .group_state_update import GroupStateUpdate
from .group_update_type import GroupUpdateType
from .guide_info import GuideInfo
from .hardware_acceleration_type import HardwareAccelerationType
from .head_audio_stream_by_container_stream_options import (
    HeadAudioStreamByContainerStreamOptions,
)
from .head_audio_stream_stream_options import HeadAudioStreamStreamOptions
from .head_master_hls_audio_playlist_stream_options import (
    HeadMasterHlsAudioPlaylistStreamOptions,
)
from .head_master_hls_video_playlist_stream_options import (
    HeadMasterHlsVideoPlaylistStreamOptions,
)
from .head_video_stream_by_container_stream_options import (
    HeadVideoStreamByContainerStreamOptions,
)
from .head_video_stream_stream_options import HeadVideoStreamStreamOptions
from .i_plugin import IPlugin
from .ignore_wait_request_dto import IgnoreWaitRequestDto
from .image_format import ImageFormat
from .image_info import ImageInfo
from .image_option import ImageOption
from .image_orientation import ImageOrientation
from .image_provider_info import ImageProviderInfo
from .image_resolution import ImageResolution
from .image_saving_convention import ImageSavingConvention
from .image_type import ImageType
from .inbound_keep_alive_message import InboundKeepAliveMessage
from .installation_info import InstallationInfo
from .iso_type import IsoType
from .item_counts import ItemCounts
from .item_fields import ItemFields
from .item_filter import ItemFilter
from .item_sort_by import ItemSortBy
from .join_group_request_dto import JoinGroupRequestDto
from .keep_until import KeepUntil
from .library_changed_message import LibraryChangedMessage
from .library_option_info_dto import LibraryOptionInfoDto
from .library_options import LibraryOptions
from .library_options_result_dto import LibraryOptionsResultDto
from .library_storage_dto import LibraryStorageDto
from .library_type_options_dto import LibraryTypeOptionsDto
from .library_update_info import LibraryUpdateInfo
from .listings_provider_info import ListingsProviderInfo
from .live_stream_response import LiveStreamResponse
from .live_tv_info import LiveTvInfo
from .live_tv_options import LiveTvOptions
from .live_tv_service_info import LiveTvServiceInfo
from .live_tv_service_status import LiveTvServiceStatus
from .localization_option import LocalizationOption
from .location_type import LocationType
from .log_file import LogFile
from .log_level import LogLevel
from .lyric_dto import LyricDto
from .lyric_line import LyricLine
from .lyric_line_cue import LyricLineCue
from .lyric_metadata import LyricMetadata
from .media_attachment import MediaAttachment
from .media_path_dto import MediaPathDto
from .media_path_info import MediaPathInfo
from .media_protocol import MediaProtocol
from .media_segment_dto import MediaSegmentDto
from .media_segment_dto_query_result import MediaSegmentDtoQueryResult
from .media_segment_type import MediaSegmentType
from .media_source_info import MediaSourceInfo
from .media_source_info_encoder_protocol import MediaSourceInfoEncoderProtocol
from .media_source_info_iso_type import MediaSourceInfoIsoType
from .media_source_info_required_http_headers_type_0 import (
    MediaSourceInfoRequiredHttpHeadersType0,
)
from .media_source_info_timestamp import MediaSourceInfoTimestamp
from .media_source_info_video_3d_format import MediaSourceInfoVideo3DFormat
from .media_source_info_video_type import MediaSourceInfoVideoType
from .media_source_type import MediaSourceType
from .media_stream import MediaStream
from .media_stream_delivery_method import MediaStreamDeliveryMethod
from .media_stream_protocol import MediaStreamProtocol
from .media_stream_type import MediaStreamType
from .media_type import MediaType
from .media_update_info_dto import MediaUpdateInfoDto
from .media_update_info_path_dto import MediaUpdateInfoPathDto
from .media_url import MediaUrl
from .message_command import MessageCommand
from .metadata_configuration import MetadataConfiguration
from .metadata_editor_info import MetadataEditorInfo
from .metadata_editor_info_content_type import MetadataEditorInfoContentType
from .metadata_field import MetadataField
from .metadata_options import MetadataOptions
from .metadata_refresh_mode import MetadataRefreshMode
from .move_playlist_item_request_dto import MovePlaylistItemRequestDto
from .movie_info import MovieInfo
from .movie_info_provider_ids_type_0 import MovieInfoProviderIdsType0
from .movie_info_remote_search_query import MovieInfoRemoteSearchQuery
from .music_video_info import MusicVideoInfo
from .music_video_info_provider_ids_type_0 import MusicVideoInfoProviderIdsType0
from .music_video_info_remote_search_query import MusicVideoInfoRemoteSearchQuery
from .name_guid_pair import NameGuidPair
from .name_id_pair import NameIdPair
from .name_value_pair import NameValuePair
from .network_configuration import NetworkConfiguration
from .new_group_request_dto import NewGroupRequestDto
from .next_item_request_dto import NextItemRequestDto
from .open_live_stream_dto import OpenLiveStreamDto
from .outbound_keep_alive_message import OutboundKeepAliveMessage
from .package_info import PackageInfo
from .parental_rating import ParentalRating
from .parental_rating_score import ParentalRatingScore
from .path_substitution import PathSubstitution
from .person_kind import PersonKind
from .person_lookup_info import PersonLookupInfo
from .person_lookup_info_provider_ids_type_0 import PersonLookupInfoProviderIdsType0
from .person_lookup_info_remote_search_query import PersonLookupInfoRemoteSearchQuery
from .pin_redeem_result import PinRedeemResult
from .ping_request_dto import PingRequestDto
from .play_access import PlayAccess
from .play_command import PlayCommand
from .play_message import PlayMessage
from .play_method import PlayMethod
from .play_queue_update import PlayQueueUpdate
from .play_queue_update_reason import PlayQueueUpdateReason
from .play_request import PlayRequest
from .play_request_dto import PlayRequestDto
from .playback_error_code import PlaybackErrorCode
from .playback_info_dto import PlaybackInfoDto
from .playback_info_response import PlaybackInfoResponse
from .playback_info_response_error_code import PlaybackInfoResponseErrorCode
from .playback_order import PlaybackOrder
from .playback_progress_info import PlaybackProgressInfo
from .playback_request_type import PlaybackRequestType
from .playback_start_info import PlaybackStartInfo
from .playback_stop_info import PlaybackStopInfo
from .player_state_info import PlayerStateInfo
from .player_state_info_play_method import PlayerStateInfoPlayMethod
from .playlist_creation_result import PlaylistCreationResult
from .playlist_dto import PlaylistDto
from .playlist_user_permissions import PlaylistUserPermissions
from .playstate_command import PlaystateCommand
from .playstate_message import PlaystateMessage
from .playstate_request import PlaystateRequest
from .plugin_info import PluginInfo
from .plugin_installation_cancelled_message import PluginInstallationCancelledMessage
from .plugin_installation_completed_message import PluginInstallationCompletedMessage
from .plugin_installation_failed_message import PluginInstallationFailedMessage
from .plugin_installing_message import PluginInstallingMessage
from .plugin_status import PluginStatus
from .plugin_uninstalled_message import PluginUninstalledMessage
from .previous_item_request_dto import PreviousItemRequestDto
from .problem_details import ProblemDetails
from .process_priority_class import ProcessPriorityClass
from .profile_condition import ProfileCondition
from .profile_condition_type import ProfileConditionType
from .profile_condition_value import ProfileConditionValue
from .program_audio import ProgramAudio
from .public_system_info import PublicSystemInfo
from .query_filters import QueryFilters
from .query_filters_legacy import QueryFiltersLegacy
from .queue_item import QueueItem
from .queue_request_dto import QueueRequestDto
from .quick_connect_dto import QuickConnectDto
from .quick_connect_result import QuickConnectResult
from .rating_type import RatingType
from .ready_request_dto import ReadyRequestDto
from .recommendation_dto import RecommendationDto
from .recommendation_type import RecommendationType
from .recording_status import RecordingStatus
from .refresh_progress_message import RefreshProgressMessage
from .refresh_progress_message_data_type_0 import RefreshProgressMessageDataType0
from .remote_image_info import RemoteImageInfo
from .remote_image_result import RemoteImageResult
from .remote_lyric_info_dto import RemoteLyricInfoDto
from .remote_search_result import RemoteSearchResult
from .remote_search_result_provider_ids_type_0 import RemoteSearchResultProviderIdsType0
from .remote_subtitle_info import RemoteSubtitleInfo
from .remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto
from .repeat_mode import RepeatMode
from .repository_info import RepositoryInfo
from .restart_required_message import RestartRequiredMessage
from .scheduled_task_ended_message import ScheduledTaskEndedMessage
from .scheduled_tasks_info_message import ScheduledTasksInfoMessage
from .scheduled_tasks_info_start_message import ScheduledTasksInfoStartMessage
from .scheduled_tasks_info_stop_message import ScheduledTasksInfoStopMessage
from .scroll_direction import ScrollDirection
from .search_hint import SearchHint
from .search_hint_result import SearchHintResult
from .seek_request_dto import SeekRequestDto
from .send_command import SendCommand
from .send_command_type import SendCommandType
from .series_info import SeriesInfo
from .series_info_provider_ids_type_0 import SeriesInfoProviderIdsType0
from .series_info_remote_search_query import SeriesInfoRemoteSearchQuery
from .series_status import SeriesStatus
from .series_timer_cancelled_message import SeriesTimerCancelledMessage
from .series_timer_created_message import SeriesTimerCreatedMessage
from .series_timer_info_dto import SeriesTimerInfoDto
from .series_timer_info_dto_day_pattern import SeriesTimerInfoDtoDayPattern
from .series_timer_info_dto_image_tags_type_0 import SeriesTimerInfoDtoImageTagsType0
from .series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from .server_configuration import ServerConfiguration
from .server_discovery_info import ServerDiscoveryInfo
from .server_restarting_message import ServerRestartingMessage
from .server_shutting_down_message import ServerShuttingDownMessage
from .session_info_dto import SessionInfoDto
from .session_message_type import SessionMessageType
from .session_user_info import SessionUserInfo
from .sessions_message import SessionsMessage
from .sessions_start_message import SessionsStartMessage
from .sessions_stop_message import SessionsStopMessage
from .set_channel_mapping_dto import SetChannelMappingDto
from .set_playlist_item_request_dto import SetPlaylistItemRequestDto
from .set_repeat_mode_request_dto import SetRepeatModeRequestDto
from .set_shuffle_mode_request_dto import SetShuffleModeRequestDto
from .song_info import SongInfo
from .song_info_provider_ids_type_0 import SongInfoProviderIdsType0
from .sort_order import SortOrder
from .special_view_option_dto import SpecialViewOptionDto
from .startup_configuration_dto import StartupConfigurationDto
from .startup_remote_access_dto import StartupRemoteAccessDto
from .startup_user_dto import StartupUserDto
from .subtitle_delivery_method import SubtitleDeliveryMethod
from .subtitle_options import SubtitleOptions
from .subtitle_playback_mode import SubtitlePlaybackMode
from .subtitle_profile import SubtitleProfile
from .sync_play_command_message import SyncPlayCommandMessage
from .sync_play_group_does_not_exist_update import SyncPlayGroupDoesNotExistUpdate
from .sync_play_group_joined_update import SyncPlayGroupJoinedUpdate
from .sync_play_group_left_update import SyncPlayGroupLeftUpdate
from .sync_play_group_update_message import SyncPlayGroupUpdateMessage
from .sync_play_library_access_denied_update import SyncPlayLibraryAccessDeniedUpdate
from .sync_play_not_in_group_update import SyncPlayNotInGroupUpdate
from .sync_play_play_queue_update import SyncPlayPlayQueueUpdate
from .sync_play_queue_item import SyncPlayQueueItem
from .sync_play_state_update import SyncPlayStateUpdate
from .sync_play_user_access_type import SyncPlayUserAccessType
from .sync_play_user_joined_update import SyncPlayUserJoinedUpdate
from .sync_play_user_left_update import SyncPlayUserLeftUpdate
from .system_info import SystemInfo
from .system_storage_dto import SystemStorageDto
from .task_completion_status import TaskCompletionStatus
from .task_info import TaskInfo
from .task_result import TaskResult
from .task_state import TaskState
from .task_trigger_info import TaskTriggerInfo
from .task_trigger_info_day_of_week import TaskTriggerInfoDayOfWeek
from .task_trigger_info_type import TaskTriggerInfoType
from .theme_media_result import ThemeMediaResult
from .timer_cancelled_message import TimerCancelledMessage
from .timer_created_message import TimerCreatedMessage
from .timer_event_info import TimerEventInfo
from .timer_info_dto import TimerInfoDto
from .timer_info_dto_query_result import TimerInfoDtoQueryResult
from .tonemapping_algorithm import TonemappingAlgorithm
from .tonemapping_mode import TonemappingMode
from .tonemapping_range import TonemappingRange
from .trailer_info import TrailerInfo
from .trailer_info_provider_ids_type_0 import TrailerInfoProviderIdsType0
from .trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery
from .transcode_reason import TranscodeReason
from .transcode_seek_info import TranscodeSeekInfo
from .transcoding_info import TranscodingInfo
from .transcoding_info_hardware_acceleration_type import (
    TranscodingInfoHardwareAccelerationType,
)
from .transcoding_info_transcode_reasons import TranscodingInfoTranscodeReasons
from .transcoding_profile import TranscodingProfile
from .transport_stream_timestamp import TransportStreamTimestamp
from .trickplay_info_dto import TrickplayInfoDto
from .trickplay_options import TrickplayOptions
from .trickplay_scan_behavior import TrickplayScanBehavior
from .tuner_channel_mapping import TunerChannelMapping
from .tuner_host_info import TunerHostInfo
from .type_options import TypeOptions
from .unrated_item import UnratedItem
from .update_library_options_dto import UpdateLibraryOptionsDto
from .update_media_path_request_dto import UpdateMediaPathRequestDto
from .update_playlist_dto import UpdatePlaylistDto
from .update_playlist_user_dto import UpdatePlaylistUserDto
from .update_user_item_data_dto import UpdateUserItemDataDto
from .update_user_password import UpdateUserPassword
from .upload_subtitle_dto import UploadSubtitleDto
from .user_configuration import UserConfiguration
from .user_data_change_info import UserDataChangeInfo
from .user_data_changed_message import UserDataChangedMessage
from .user_deleted_message import UserDeletedMessage
from .user_dto import UserDto
from .user_item_data_dto import UserItemDataDto
from .user_policy import UserPolicy
from .user_updated_message import UserUpdatedMessage
from .utc_time_response import UtcTimeResponse
from .validate_path_dto import ValidatePathDto
from .version_info import VersionInfo
from .video_3d_format import Video3DFormat
from .video_range import VideoRange
from .video_range_type import VideoRangeType
from .video_type import VideoType
from .virtual_folder_info import VirtualFolderInfo
from .virtual_folder_info_collection_type import VirtualFolderInfoCollectionType
from .xbmc_metadata_options import XbmcMetadataOptions

__all__ = (
    "AccessSchedule",
    "ActivityLogEntry",
    "ActivityLogEntryMessage",
    "ActivityLogEntryQueryResult",
    "ActivityLogEntryStartMessage",
    "ActivityLogEntryStopMessage",
    "AddVirtualFolderDto",
    "AlbumInfo",
    "AlbumInfoArtistProviderIds",
    "AlbumInfoProviderIdsType0",
    "AlbumInfoRemoteSearchQuery",
    "AllThemeMediaResult",
    "ArtistInfo",
    "ArtistInfoProviderIdsType0",
    "ArtistInfoRemoteSearchQuery",
    "AudioSpatialFormat",
    "AuthenticateUserByName",
    "AuthenticationInfo",
    "AuthenticationInfoQueryResult",
    "AuthenticationResult",
    "BackupManifestDto",
    "BackupOptionsDto",
    "BackupRestoreRequestDto",
    "BaseItemDto",
    "BaseItemDtoAudio",
    "BaseItemDtoChannelType",
    "BaseItemDtoCollectionType",
    "BaseItemDtoExtraType",
    "BaseItemDtoImageBlurHashesType0",
    "BaseItemDtoImageBlurHashesType0Art",
    "BaseItemDtoImageBlurHashesType0Backdrop",
    "BaseItemDtoImageBlurHashesType0Banner",
    "BaseItemDtoImageBlurHashesType0Box",
    "BaseItemDtoImageBlurHashesType0BoxRear",
    "BaseItemDtoImageBlurHashesType0Chapter",
    "BaseItemDtoImageBlurHashesType0Disc",
    "BaseItemDtoImageBlurHashesType0Logo",
    "BaseItemDtoImageBlurHashesType0Menu",
    "BaseItemDtoImageBlurHashesType0Primary",
    "BaseItemDtoImageBlurHashesType0Profile",
    "BaseItemDtoImageBlurHashesType0Screenshot",
    "BaseItemDtoImageBlurHashesType0Thumb",
    "BaseItemDtoImageOrientation",
    "BaseItemDtoImageTagsType0",
    "BaseItemDtoIsoType",
    "BaseItemDtoLocationType",
    "BaseItemDtoPlayAccess",
    "BaseItemDtoProviderIdsType0",
    "BaseItemDtoQueryResult",
    "BaseItemDtoTrickplayType0",
    "BaseItemDtoTrickplayType0AdditionalProperty",
    "BaseItemDtoVideo3DFormat",
    "BaseItemDtoVideoType",
    "BaseItemKind",
    "BaseItemPerson",
    "BaseItemPersonImageBlurHashesType0",
    "BaseItemPersonImageBlurHashesType0Art",
    "BaseItemPersonImageBlurHashesType0Backdrop",
    "BaseItemPersonImageBlurHashesType0Banner",
    "BaseItemPersonImageBlurHashesType0Box",
    "BaseItemPersonImageBlurHashesType0BoxRear",
    "BaseItemPersonImageBlurHashesType0Chapter",
    "BaseItemPersonImageBlurHashesType0Disc",
    "BaseItemPersonImageBlurHashesType0Logo",
    "BaseItemPersonImageBlurHashesType0Menu",
    "BaseItemPersonImageBlurHashesType0Primary",
    "BaseItemPersonImageBlurHashesType0Profile",
    "BaseItemPersonImageBlurHashesType0Screenshot",
    "BaseItemPersonImageBlurHashesType0Thumb",
    "BasePluginConfiguration",
    "BookInfo",
    "BookInfoProviderIdsType0",
    "BookInfoRemoteSearchQuery",
    "BoxSetInfo",
    "BoxSetInfoProviderIdsType0",
    "BoxSetInfoRemoteSearchQuery",
    "BrandingOptionsDto",
    "BufferRequestDto",
    "CastReceiverApplication",
    "ChannelFeatures",
    "ChannelItemSortField",
    "ChannelMappingOptionsDto",
    "ChannelMediaContentType",
    "ChannelMediaType",
    "ChannelType",
    "ChapterInfo",
    "ClientCapabilitiesDto",
    "ClientLogDocumentResponseDto",
    "CodecProfile",
    "CodecType",
    "CollectionCreationResult",
    "CollectionType",
    "CollectionTypeOptions",
    "ConfigImageTypes",
    "ConfigurationPageInfo",
    "ContainerProfile",
    "CountryInfo",
    "CreatePlaylistDto",
    "CreatePlaylistDtoMediaType",
    "CreateUserByName",
    "CultureDto",
    "CustomDatabaseOption",
    "CustomDatabaseOptions",
    "DatabaseConfigurationOptions",
    "DatabaseLockingBehaviorTypes",
    "DayOfWeek",
    "DayPattern",
    "DefaultDirectoryBrowserInfoDto",
    "DeinterlaceMethod",
    "DeviceInfoDto",
    "DeviceInfoDtoQueryResult",
    "DeviceOptionsDto",
    "DeviceProfile",
    "DirectPlayProfile",
    "DisplayPreferencesDto",
    "DisplayPreferencesDtoCustomPrefs",
    "DlnaProfileType",
    "DownMixStereoAlgorithms",
    "DynamicDayOfWeek",
    "EmbeddedSubtitleOptions",
    "EncoderPreset",
    "EncodingContext",
    "EncodingOptions",
    "EncodingOptionsEncoderPreset",
    "EndPointInfo",
    "ExternalIdInfo",
    "ExternalIdInfoType",
    "ExternalIdMediaType",
    "ExternalUrl",
    "ExtraType",
    "FileSystemEntryInfo",
    "FileSystemEntryType",
    "FolderStorageDto",
    "FontFile",
    "ForceKeepAliveMessage",
    "ForgotPasswordAction",
    "ForgotPasswordDto",
    "ForgotPasswordPinDto",
    "ForgotPasswordResult",
    "GeneralCommand",
    "GeneralCommandArguments",
    "GeneralCommandMessage",
    "GeneralCommandType",
    "GetAudioStreamByContainerStreamOptions",
    "GetAudioStreamStreamOptions",
    "GetHlsAudioSegmentStreamOptions",
    "GetHlsVideoSegmentStreamOptions",
    "GetLiveHlsStreamStreamOptions",
    "GetMasterHlsAudioPlaylistStreamOptions",
    "GetMasterHlsVideoPlaylistStreamOptions",
    "GetProgramsDto",
    "GetVariantHlsAudioPlaylistStreamOptions",
    "GetVariantHlsVideoPlaylistStreamOptions",
    "GetVideoStreamByContainerStreamOptions",
    "GetVideoStreamStreamOptions",
    "GroupInfoDto",
    "GroupQueueMode",
    "GroupRepeatMode",
    "GroupShuffleMode",
    "GroupStateType",
    "GroupStateUpdate",
    "GroupUpdateType",
    "GuideInfo",
    "HardwareAccelerationType",
    "HeadAudioStreamByContainerStreamOptions",
    "HeadAudioStreamStreamOptions",
    "HeadMasterHlsAudioPlaylistStreamOptions",
    "HeadMasterHlsVideoPlaylistStreamOptions",
    "HeadVideoStreamByContainerStreamOptions",
    "HeadVideoStreamStreamOptions",
    "IgnoreWaitRequestDto",
    "ImageFormat",
    "ImageInfo",
    "ImageOption",
    "ImageOrientation",
    "ImageProviderInfo",
    "ImageResolution",
    "ImageSavingConvention",
    "ImageType",
    "InboundKeepAliveMessage",
    "InstallationInfo",
    "IPlugin",
    "IsoType",
    "ItemCounts",
    "ItemFields",
    "ItemFilter",
    "ItemSortBy",
    "JoinGroupRequestDto",
    "KeepUntil",
    "LibraryChangedMessage",
    "LibraryOptionInfoDto",
    "LibraryOptions",
    "LibraryOptionsResultDto",
    "LibraryStorageDto",
    "LibraryTypeOptionsDto",
    "LibraryUpdateInfo",
    "ListingsProviderInfo",
    "LiveStreamResponse",
    "LiveTvInfo",
    "LiveTvOptions",
    "LiveTvServiceInfo",
    "LiveTvServiceStatus",
    "LocalizationOption",
    "LocationType",
    "LogFile",
    "LogLevel",
    "LyricDto",
    "LyricLine",
    "LyricLineCue",
    "LyricMetadata",
    "MediaAttachment",
    "MediaPathDto",
    "MediaPathInfo",
    "MediaProtocol",
    "MediaSegmentDto",
    "MediaSegmentDtoQueryResult",
    "MediaSegmentType",
    "MediaSourceInfo",
    "MediaSourceInfoEncoderProtocol",
    "MediaSourceInfoIsoType",
    "MediaSourceInfoRequiredHttpHeadersType0",
    "MediaSourceInfoTimestamp",
    "MediaSourceInfoVideo3DFormat",
    "MediaSourceInfoVideoType",
    "MediaSourceType",
    "MediaStream",
    "MediaStreamDeliveryMethod",
    "MediaStreamProtocol",
    "MediaStreamType",
    "MediaType",
    "MediaUpdateInfoDto",
    "MediaUpdateInfoPathDto",
    "MediaUrl",
    "MessageCommand",
    "MetadataConfiguration",
    "MetadataEditorInfo",
    "MetadataEditorInfoContentType",
    "MetadataField",
    "MetadataOptions",
    "MetadataRefreshMode",
    "MovePlaylistItemRequestDto",
    "MovieInfo",
    "MovieInfoProviderIdsType0",
    "MovieInfoRemoteSearchQuery",
    "MusicVideoInfo",
    "MusicVideoInfoProviderIdsType0",
    "MusicVideoInfoRemoteSearchQuery",
    "NameGuidPair",
    "NameIdPair",
    "NameValuePair",
    "NetworkConfiguration",
    "NewGroupRequestDto",
    "NextItemRequestDto",
    "OpenLiveStreamDto",
    "OutboundKeepAliveMessage",
    "PackageInfo",
    "ParentalRating",
    "ParentalRatingScore",
    "PathSubstitution",
    "PersonKind",
    "PersonLookupInfo",
    "PersonLookupInfoProviderIdsType0",
    "PersonLookupInfoRemoteSearchQuery",
    "PingRequestDto",
    "PinRedeemResult",
    "PlayAccess",
    "PlaybackErrorCode",
    "PlaybackInfoDto",
    "PlaybackInfoResponse",
    "PlaybackInfoResponseErrorCode",
    "PlaybackOrder",
    "PlaybackProgressInfo",
    "PlaybackRequestType",
    "PlaybackStartInfo",
    "PlaybackStopInfo",
    "PlayCommand",
    "PlayerStateInfo",
    "PlayerStateInfoPlayMethod",
    "PlaylistCreationResult",
    "PlaylistDto",
    "PlaylistUserPermissions",
    "PlayMessage",
    "PlayMethod",
    "PlayQueueUpdate",
    "PlayQueueUpdateReason",
    "PlayRequest",
    "PlayRequestDto",
    "PlaystateCommand",
    "PlaystateMessage",
    "PlaystateRequest",
    "PluginInfo",
    "PluginInstallationCancelledMessage",
    "PluginInstallationCompletedMessage",
    "PluginInstallationFailedMessage",
    "PluginInstallingMessage",
    "PluginStatus",
    "PluginUninstalledMessage",
    "PreviousItemRequestDto",
    "ProblemDetails",
    "ProcessPriorityClass",
    "ProfileCondition",
    "ProfileConditionType",
    "ProfileConditionValue",
    "ProgramAudio",
    "PublicSystemInfo",
    "QueryFilters",
    "QueryFiltersLegacy",
    "QueueItem",
    "QueueRequestDto",
    "QuickConnectDto",
    "QuickConnectResult",
    "RatingType",
    "ReadyRequestDto",
    "RecommendationDto",
    "RecommendationType",
    "RecordingStatus",
    "RefreshProgressMessage",
    "RefreshProgressMessageDataType0",
    "RemoteImageInfo",
    "RemoteImageResult",
    "RemoteLyricInfoDto",
    "RemoteSearchResult",
    "RemoteSearchResultProviderIdsType0",
    "RemoteSubtitleInfo",
    "RemoveFromPlaylistRequestDto",
    "RepeatMode",
    "RepositoryInfo",
    "RestartRequiredMessage",
    "ScheduledTaskEndedMessage",
    "ScheduledTasksInfoMessage",
    "ScheduledTasksInfoStartMessage",
    "ScheduledTasksInfoStopMessage",
    "ScrollDirection",
    "SearchHint",
    "SearchHintResult",
    "SeekRequestDto",
    "SendCommand",
    "SendCommandType",
    "SeriesInfo",
    "SeriesInfoProviderIdsType0",
    "SeriesInfoRemoteSearchQuery",
    "SeriesStatus",
    "SeriesTimerCancelledMessage",
    "SeriesTimerCreatedMessage",
    "SeriesTimerInfoDto",
    "SeriesTimerInfoDtoDayPattern",
    "SeriesTimerInfoDtoImageTagsType0",
    "SeriesTimerInfoDtoQueryResult",
    "ServerConfiguration",
    "ServerDiscoveryInfo",
    "ServerRestartingMessage",
    "ServerShuttingDownMessage",
    "SessionInfoDto",
    "SessionMessageType",
    "SessionsMessage",
    "SessionsStartMessage",
    "SessionsStopMessage",
    "SessionUserInfo",
    "SetChannelMappingDto",
    "SetPlaylistItemRequestDto",
    "SetRepeatModeRequestDto",
    "SetShuffleModeRequestDto",
    "SongInfo",
    "SongInfoProviderIdsType0",
    "SortOrder",
    "SpecialViewOptionDto",
    "StartupConfigurationDto",
    "StartupRemoteAccessDto",
    "StartupUserDto",
    "SubtitleDeliveryMethod",
    "SubtitleOptions",
    "SubtitlePlaybackMode",
    "SubtitleProfile",
    "SyncPlayCommandMessage",
    "SyncPlayGroupDoesNotExistUpdate",
    "SyncPlayGroupJoinedUpdate",
    "SyncPlayGroupLeftUpdate",
    "SyncPlayGroupUpdateMessage",
    "SyncPlayLibraryAccessDeniedUpdate",
    "SyncPlayNotInGroupUpdate",
    "SyncPlayPlayQueueUpdate",
    "SyncPlayQueueItem",
    "SyncPlayStateUpdate",
    "SyncPlayUserAccessType",
    "SyncPlayUserJoinedUpdate",
    "SyncPlayUserLeftUpdate",
    "SystemInfo",
    "SystemStorageDto",
    "TaskCompletionStatus",
    "TaskInfo",
    "TaskResult",
    "TaskState",
    "TaskTriggerInfo",
    "TaskTriggerInfoDayOfWeek",
    "TaskTriggerInfoType",
    "ThemeMediaResult",
    "TimerCancelledMessage",
    "TimerCreatedMessage",
    "TimerEventInfo",
    "TimerInfoDto",
    "TimerInfoDtoQueryResult",
    "TonemappingAlgorithm",
    "TonemappingMode",
    "TonemappingRange",
    "TrailerInfo",
    "TrailerInfoProviderIdsType0",
    "TrailerInfoRemoteSearchQuery",
    "TranscodeReason",
    "TranscodeSeekInfo",
    "TranscodingInfo",
    "TranscodingInfoHardwareAccelerationType",
    "TranscodingInfoTranscodeReasons",
    "TranscodingProfile",
    "TransportStreamTimestamp",
    "TrickplayInfoDto",
    "TrickplayOptions",
    "TrickplayScanBehavior",
    "TunerChannelMapping",
    "TunerHostInfo",
    "TypeOptions",
    "UnratedItem",
    "UpdateLibraryOptionsDto",
    "UpdateMediaPathRequestDto",
    "UpdatePlaylistDto",
    "UpdatePlaylistUserDto",
    "UpdateUserItemDataDto",
    "UpdateUserPassword",
    "UploadSubtitleDto",
    "UserConfiguration",
    "UserDataChangedMessage",
    "UserDataChangeInfo",
    "UserDeletedMessage",
    "UserDto",
    "UserItemDataDto",
    "UserPolicy",
    "UserUpdatedMessage",
    "UtcTimeResponse",
    "ValidatePathDto",
    "VersionInfo",
    "Video3DFormat",
    "VideoRange",
    "VideoRangeType",
    "VideoType",
    "VirtualFolderInfo",
    "VirtualFolderInfoCollectionType",
    "XbmcMetadataOptions",
)
