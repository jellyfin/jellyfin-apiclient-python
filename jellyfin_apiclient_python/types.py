from dataclasses import dataclass
from typing import List, Optional, Dict, Type, TypeVar, Generic
from uuid import UUID

from jellyfin_apiclient_python.constants import MediaType, ImageType, ItemType
from jellyfin_apiclient_python.util import api_parse_constructor

# Generics

T = TypeVar('T')

@dataclass
class ListResponse(Generic[T]):
    """Wrapper for API responses that list things."""
    items: Optional[List[T]] = None
    total_record_count: Optional[int] = None
    start_index: Optional[int] = None

    def __init__(self, data: Optional[Dict] = None, list_type: Optional[Type[T]] = None):
        api_parse_constructor(self, data, {'items': list_type})

@dataclass
class MediaUserData:
    """Contains information about a users playlist play state."""

    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    unplayed_item_count: Optional[int] = None
    playback_position_ticks: Optional[int] = None
    play_count: Optional[int] = None
    is_favorite: Optional[bool] = None
    played: Optional[bool] = None
    key: Optional[str] = None
    item_id: Optional[str] = None

@dataclass
class URLMap:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    name: Optional[str] = None
    url: Optional[str] = None


@dataclass
class ItemIdMap:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    name: Optional[str] = None
    id: Optional[UUID] = None

@dataclass
class Person:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    name: Optional[str] = None
    id: Optional[UUID] = None
    role: Optional[str] = None
    type: Optional[str] = None
    primary_image_tag: Optional[str] = None
    image_blur_hashes: Optional[Dict[ImageType, Dict[str, str]]] = None

@dataclass
class MediaStream:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    codec: Optional[str] = None
    codec_tag: Optional[str] = None
    language: Optional[str] = None
    color_range: Optional[str] = None
    color_space: Optional[str] = None
    color_transfer: Optional[str] = None
    color_primaries: Optional[str] = None
    dv_version_major: Optional[int] = None
    dv_version_minor: Optional[int] = None
    dv_profile: Optional[int] = None
    dv_level: Optional[int] = None
    rpu_present_flag: Optional[int] = None
    el_present_flag: Optional[int] = None
    bl_present_flag: Optional[int] = None
    dv_bl_signal_compatibility_id: Optional[int] = None
    rotation: Optional[int] = None
    comment: Optional[str] = None
    time_base: Optional[str] = None
    codec_time_base: Optional[str] = None
    title: Optional[str] = None
    video_range: Optional[str] = None
    video_range_type: Optional[str] = None
    video_do_vi_title: Optional[str] = None
    audio_spatial_format: Optional[str] = None
    localized_undefined: Optional[str] = None
    localized_default: Optional[str] = None
    localized_forced: Optional[str] = None
    localized_external: Optional[str] = None
    localized_hearing_impaired: Optional[str] = None
    display_title: Optional[str] = None
    nal_length_size: Optional[str] = None
    is_interlaced: Optional[bool] = None
    is_avc: Optional[bool] = None
    channel_layout: Optional[str] = None
    bit_rate: Optional[int] = None
    bit_depth: Optional[int] = None
    ref_frames: Optional[int] = None
    packet_length: Optional[int] = None
    channels: Optional[int] = None
    sample_rate: Optional[int] = None
    is_default: Optional[bool] = None
    is_forced: Optional[bool] = None
    is_hearing_impaired: Optional[bool] = None
    height: Optional[int] = None
    width: Optional[int] = None
    average_frame_rate: Optional[int] = None
    real_frame_rate: Optional[int] = None
    reference_frame_rate: Optional[int] = None
    profile: Optional[str] = None
    type: Optional[MediaType] = None
    aspect_ratio: Optional[str] = None
    index: Optional[int] = None
    score: Optional[int] = None
    is_external: Optional[bool] = None
    delivery_method: Optional[str] = None
    delivery_url: Optional[str] = None
    is_external_url: Optional[bool] = None
    is_text_subtitle_stream: Optional[bool] = None
    supports_external_stream: Optional[bool] = None
    path: Optional[str] = None
    pixel_format: Optional[str] = None
    level: Optional[int] = None
    is_anamorphic: Optional[bool] = None

@dataclass
class Chapter:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    start_position_ticks: Optional[int] = None
    name: Optional[str] = None
    image_path: Optional[str] = None
    image_date_modified: Optional[str] = None
    image_tag: Optional[str] = None

@dataclass
class MediaAttachment:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data)

    codec: Optional[str] = None
    codec_tag: Optional[str] = None
    comment: Optional[str] = None
    index: Optional[int] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    delivery_url: Optional[str] = None


@dataclass
class MediaSource:
    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data, {
            'media_streams': MediaStream,
            'media_attachments': MediaAttachment,
        })

    protocol: Optional[str] = None
    id: Optional[UUID] = None
    path: Optional[str] = None
    encoder_path: Optional[str] = None
    encoder_protocol: Optional[str] = None
    type: Optional[MediaType] = None
    container: Optional[str] = None
    size: Optional[int] = None
    name: Optional[str] = None
    is_remote: Optional[bool] = None
    etag: Optional[str] = None
    run_time_ticks: Optional[int] = None
    read_at_native_framerate: Optional[bool] = None
    ignore_dts: Optional[bool] = None
    ignore_index: Optional[bool] = None
    gen_pts_input: Optional[bool] = None
    supports_transcoding: Optional[bool] = None
    supports_direct_stream: Optional[bool] = None
    supports_direct_play: Optional[bool] = None
    is_infinite_stream: Optional[bool] = None
    use_most_compatible_transcoding_profile: Optional[bool] = None
    requires_opening: Optional[bool] = None
    open_token: Optional[str] = None
    requires_closing: Optional[bool] = None
    live_stream_id: Optional[str] = None
    buffer_ms: Optional[int] = None
    requires_looping: Optional[bool] = None
    supports_probing: Optional[bool] = None
    video_type: Optional[str] = None
    iso_type: Optional[str] = None
    video_3_dformat: Optional[str] = None
    media_streams: Optional[List[MediaStream]] = None
    media_attachments: Optional[List[MediaAttachment]] = None
    formats: Optional[List[str]] = None
    bitrate: Optional[int] = None
    fallback_max_streaming_bitrate: Optional[int] = None
    timestamp: Optional[str] = None
    required_http_headers: Optional[Dict] = None  # Not further specified
    transcoding_url: Optional[str] = None
    transcoding_sub_protocol: Optional[str] = None
    transcoding_container: Optional[str] = None
    analyze_duration_ms: Optional[int] = None
    default_audio_stream_index: Optional[int] = None
    default_subtitle_stream_index: Optional[int] = None
    has_segments: Optional[bool] = None


@dataclass
class MediaItemData:
    """
    Holds information about a playlist.
    References:
        BaseItemDto from the APIDoc
    """

    def __init__(self, data: Optional[Dict] = None):
        api_parse_constructor(self, data, {
            'external_urls': URLMap,
            'remote_trailers': URLMap,
            'studios': ItemIdMap,
            'genre_items': ItemIdMap,
            'user_data': MediaUserData,
            'artist_items': ItemIdMap,
            'album_artists': ItemIdMap,
            'people': Person,
            'media_streams': MediaStream,
            'chapters': Chapter,
            'media_sources': MediaSource
        })

    name: Optional[str] = None
    original_title: Optional[str] = None
    server_id: Optional[UUID] = None
    id: Optional[UUID] = None
    etag: Optional[str] = None
    source_type: Optional[str] = None
    playlist_item_id: Optional[str] = None
    date_created: Optional[str] = None
    date_last_media_added: Optional[str] = None
    extra_type: Optional[str] = None
    airs_before_season_number: Optional[int] = None
    airs_after_season_number: Optional[int] = None
    airs_before_episode_number: Optional[int] = None
    can_delete: Optional[bool] = None
    can_download: Optional[bool] = None
    has_lyrics: Optional[bool] = None
    has_subtitles: Optional[bool] = None
    preferred_metadata_language: Optional[str] = None
    preferred_metadata_country_code: Optional[str] = None
    container: Optional[str] = None
    sort_name: Optional[str] = None
    forced_sort_name: Optional[str] = None
    video_3_dformat: Optional[str] = None
    premiere_date: Optional[str] = None
    external_urls: Optional[List[URLMap]] = None
    media_sources: Optional[List[MediaSource]] = None
    critic_rating: Optional[int] = None
    production_locations: Optional[List[str]] = None
    path: Optional[str] = None
    enable_media_source_display: Optional[bool] = None
    official_rating: Optional[str] = None
    custom_rating: Optional[str] = None
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    overview: Optional[str] = None
    taglines: Optional[List[str]] = None
    genres: Optional[List[str]] = None
    community_rating: Optional[int] = None
    cumulative_run_time_ticks: Optional[int] = None
    run_time_ticks: Optional[str] = None
    play_access: Optional[str] = None
    aspect_ratio: Optional[str] = None
    production_year: Optional[int] = None
    is_place_holder: Optional[bool] = None
    number: Optional[str] = None # The api doc says so. I don't know why a number is of type string
    channel_number: Optional[str] = None  # same here!!!
    index_number: Optional[int] = None  # and now an int ?!?
    index_number_end: Optional[int] = None
    parent_index_number: Optional[int] = None
    remote_trailers: Optional[List[URLMap]] = None
    provider_ids: Optional[Dict] = None  # This is not properly documented in the APIDoc
    is_hd: Optional[bool] = None
    is_folder: Optional[bool] = None
    parent_id: Optional[UUID] = None
    type: Optional[ItemType] = None
    people: Optional[List[Person]] = None
    studios: Optional[List[ItemIdMap]] = None
    genre_items: Optional[List[ItemIdMap]] = None
    parent_logo_item_id: Optional[UUID] = None
    parent_backdrop_item_id: Optional[UUID] = None
    parent_backdrop_image_tags: Optional[List[str]] = None
    local_trailer_count: Optional[int] = None
    user_data: Optional[MediaUserData] = None
    recursive_item_count: Optional[int] = None
    child_count: Optional[int] = None
    series_name: Optional[str] = None
    series_id: Optional[UUID] = None
    season_id: Optional[UUID] = None
    special_feature_count: Optional[int] = None
    display_preferences_id: Optional[str] = None
    status: Optional[str] = None
    air_time: Optional[str] = None
    air_days: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    primary_image_aspect_ratio: Optional[str] = None
    artists: Optional[List[str]] = None
    artist_items: Optional[List[ItemIdMap]] = None
    album: Optional[str] = None
    collection_type: Optional[str] = None  # maybe define enum
    display_order: Optional[str] = None
    album_id: Optional[UUID] = None
    album_primary_image_tag: Optional[str] = None
    series_primary_image_tag: Optional[str] = None
    album_artist: Optional[str] = None
    album_artists: Optional[List[ItemIdMap]] = None
    season_name: Optional[str] = None
    media_streams: Optional[List[MediaStream]] = None
    video_type: Optional[str] = None
    part_count: Optional[int] = None
    media_source_count: Optional[int] = None
    image_tags: Optional[Dict[ImageType, str]] = None
    backdrop_image_tags: Optional[List[str]] = None
    screenshot_image_tags: Optional[List[str]] = None
    parent_logo_image_tag: Optional[str] = None
    parent_art_item_id: Optional[UUID] = None
    parent_art_image_tag: Optional[str] = None
    series_thumb_image_tag: Optional[str] = None
    image_blur_hashes: Optional[Dict[ImageType, Dict[str, str]]] = None
    series_studio: Optional[str] = None
    parent_thumb_item_id: Optional[UUID] = None
    parent_thumb_image_tag: Optional[str] = None
    parent_primary_image_item_id: Optional[UUID] = None
    parent_primary_image_tag: Optional[str] = None
    chapters: Optional[List[Chapter]] = None
    trickplay: Optional[Dict] = None # better specify the type - The documentation is not that precise
    location_type: Optional[str] = None
    iso_type: Optional[str] = None
    media_type: Optional[MediaType] = None
    end_date: Optional[str] = None
    locked_fields: Optional[List[str]] = None
    trailer_count: Optional[int] = None
    movie_count: Optional[int] = None
    series_count: Optional[int] = None
    program_count: Optional[int] = None
    episode_count: Optional[int] = None
    song_count: Optional[int] = None
    album_count: Optional[int] = None
    artist_count: Optional[int] = None
    music_video_count: Optional[int] = None
    lock_data: Optional[bool] = None
    width: Optional[int] = None
    height: Optional[int] = None
    camera_make: Optional[str] = None
    camera_model: Optional[str] = None
    software: Optional[str] = None
    exposure_time: Optional[int] = None
    focal_length: Optional[int] = None
    image_orientation: Optional[str] = None
    aperture: Optional[int] = None
    shutter_speed: Optional[int] = None
    latitude: Optional[int] = None
    longitude: Optional[int] = None
    altitude: Optional[int] = None
    iso_speed_rating: Optional[int] = None
    series_timer_id: Optional[str] = None
    program_id: Optional[str] = None
    channel_primary_image_tag: Optional[str] = None
    start_date: Optional[str] = None
    completion_percentage: Optional[int] = None
    is_repeat: Optional[bool] = None
    episode_title: Optional[str] = None
    channel_type: Optional[str] = None
    audio: Optional[str] = None
    is_movie: Optional[bool] = None
    is_sports: Optional[bool] = None
    is_series: Optional[bool] = None
    is_live: Optional[bool] = None
    is_news: Optional[bool] = None
    is_kids: Optional[bool] = None
    is_premiere: Optional[bool] = None
    timer_id: Optional[str] = None
    normalization_gain: Optional[int] = None
    current_program: Optional[Dict] = None # The type isn't specified in the API