from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.subtitle_playback_mode import SubtitlePlaybackMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserConfiguration")


@_attrs_define
class UserConfiguration:
    """Class UserConfiguration.

    Attributes:
        audio_language_preference (None | str | Unset): Gets or sets the audio language preference.
        play_default_audio_track (bool | Unset): Gets or sets a value indicating whether [play default audio track].
        subtitle_language_preference (None | str | Unset): Gets or sets the subtitle language preference.
        display_missing_episodes (bool | Unset):
        grouped_folders (list[UUID] | Unset):
        subtitle_mode (SubtitlePlaybackMode | Unset): An enum representing a subtitle playback mode.
        display_collections_view (bool | Unset):
        enable_local_password (bool | Unset):
        ordered_views (list[UUID] | Unset):
        latest_items_excludes (list[UUID] | Unset):
        my_media_excludes (list[UUID] | Unset):
        hide_played_in_latest (bool | Unset):
        remember_audio_selections (bool | Unset):
        remember_subtitle_selections (bool | Unset):
        enable_next_episode_auto_play (bool | Unset):
        cast_receiver_id (None | str | Unset): Gets or sets the id of the selected cast receiver.
    """

    audio_language_preference: None | str | Unset = UNSET
    play_default_audio_track: bool | Unset = UNSET
    subtitle_language_preference: None | str | Unset = UNSET
    display_missing_episodes: bool | Unset = UNSET
    grouped_folders: list[UUID] | Unset = UNSET
    subtitle_mode: SubtitlePlaybackMode | Unset = UNSET
    display_collections_view: bool | Unset = UNSET
    enable_local_password: bool | Unset = UNSET
    ordered_views: list[UUID] | Unset = UNSET
    latest_items_excludes: list[UUID] | Unset = UNSET
    my_media_excludes: list[UUID] | Unset = UNSET
    hide_played_in_latest: bool | Unset = UNSET
    remember_audio_selections: bool | Unset = UNSET
    remember_subtitle_selections: bool | Unset = UNSET
    enable_next_episode_auto_play: bool | Unset = UNSET
    cast_receiver_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_language_preference: None | str | Unset
        if isinstance(self.audio_language_preference, Unset):
            audio_language_preference = UNSET
        else:
            audio_language_preference = self.audio_language_preference

        play_default_audio_track = self.play_default_audio_track

        subtitle_language_preference: None | str | Unset
        if isinstance(self.subtitle_language_preference, Unset):
            subtitle_language_preference = UNSET
        else:
            subtitle_language_preference = self.subtitle_language_preference

        display_missing_episodes = self.display_missing_episodes

        grouped_folders: list[str] | Unset = UNSET
        if not isinstance(self.grouped_folders, Unset):
            grouped_folders = []
            for grouped_folders_item_data in self.grouped_folders:
                grouped_folders_item = str(grouped_folders_item_data)
                grouped_folders.append(grouped_folders_item)

        subtitle_mode: str | Unset = UNSET
        if not isinstance(self.subtitle_mode, Unset):
            subtitle_mode = self.subtitle_mode.value

        display_collections_view = self.display_collections_view

        enable_local_password = self.enable_local_password

        ordered_views: list[str] | Unset = UNSET
        if not isinstance(self.ordered_views, Unset):
            ordered_views = []
            for ordered_views_item_data in self.ordered_views:
                ordered_views_item = str(ordered_views_item_data)
                ordered_views.append(ordered_views_item)

        latest_items_excludes: list[str] | Unset = UNSET
        if not isinstance(self.latest_items_excludes, Unset):
            latest_items_excludes = []
            for latest_items_excludes_item_data in self.latest_items_excludes:
                latest_items_excludes_item = str(latest_items_excludes_item_data)
                latest_items_excludes.append(latest_items_excludes_item)

        my_media_excludes: list[str] | Unset = UNSET
        if not isinstance(self.my_media_excludes, Unset):
            my_media_excludes = []
            for my_media_excludes_item_data in self.my_media_excludes:
                my_media_excludes_item = str(my_media_excludes_item_data)
                my_media_excludes.append(my_media_excludes_item)

        hide_played_in_latest = self.hide_played_in_latest

        remember_audio_selections = self.remember_audio_selections

        remember_subtitle_selections = self.remember_subtitle_selections

        enable_next_episode_auto_play = self.enable_next_episode_auto_play

        cast_receiver_id: None | str | Unset
        if isinstance(self.cast_receiver_id, Unset):
            cast_receiver_id = UNSET
        else:
            cast_receiver_id = self.cast_receiver_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audio_language_preference is not UNSET:
            field_dict["AudioLanguagePreference"] = audio_language_preference
        if play_default_audio_track is not UNSET:
            field_dict["PlayDefaultAudioTrack"] = play_default_audio_track
        if subtitle_language_preference is not UNSET:
            field_dict["SubtitleLanguagePreference"] = subtitle_language_preference
        if display_missing_episodes is not UNSET:
            field_dict["DisplayMissingEpisodes"] = display_missing_episodes
        if grouped_folders is not UNSET:
            field_dict["GroupedFolders"] = grouped_folders
        if subtitle_mode is not UNSET:
            field_dict["SubtitleMode"] = subtitle_mode
        if display_collections_view is not UNSET:
            field_dict["DisplayCollectionsView"] = display_collections_view
        if enable_local_password is not UNSET:
            field_dict["EnableLocalPassword"] = enable_local_password
        if ordered_views is not UNSET:
            field_dict["OrderedViews"] = ordered_views
        if latest_items_excludes is not UNSET:
            field_dict["LatestItemsExcludes"] = latest_items_excludes
        if my_media_excludes is not UNSET:
            field_dict["MyMediaExcludes"] = my_media_excludes
        if hide_played_in_latest is not UNSET:
            field_dict["HidePlayedInLatest"] = hide_played_in_latest
        if remember_audio_selections is not UNSET:
            field_dict["RememberAudioSelections"] = remember_audio_selections
        if remember_subtitle_selections is not UNSET:
            field_dict["RememberSubtitleSelections"] = remember_subtitle_selections
        if enable_next_episode_auto_play is not UNSET:
            field_dict["EnableNextEpisodeAutoPlay"] = enable_next_episode_auto_play
        if cast_receiver_id is not UNSET:
            field_dict["CastReceiverId"] = cast_receiver_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_language_preference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audio_language_preference = _parse_audio_language_preference(
            d.pop("AudioLanguagePreference", UNSET)
        )

        play_default_audio_track = d.pop("PlayDefaultAudioTrack", UNSET)

        def _parse_subtitle_language_preference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle_language_preference = _parse_subtitle_language_preference(
            d.pop("SubtitleLanguagePreference", UNSET)
        )

        display_missing_episodes = d.pop("DisplayMissingEpisodes", UNSET)

        _grouped_folders = d.pop("GroupedFolders", UNSET)
        grouped_folders: list[UUID] | Unset = UNSET
        if _grouped_folders is not UNSET:
            grouped_folders = []
            for grouped_folders_item_data in _grouped_folders:
                grouped_folders_item = UUID(grouped_folders_item_data)

                grouped_folders.append(grouped_folders_item)

        _subtitle_mode = d.pop("SubtitleMode", UNSET)
        subtitle_mode: SubtitlePlaybackMode | Unset
        if isinstance(_subtitle_mode, Unset):
            subtitle_mode = UNSET
        else:
            subtitle_mode = SubtitlePlaybackMode(_subtitle_mode)

        display_collections_view = d.pop("DisplayCollectionsView", UNSET)

        enable_local_password = d.pop("EnableLocalPassword", UNSET)

        _ordered_views = d.pop("OrderedViews", UNSET)
        ordered_views: list[UUID] | Unset = UNSET
        if _ordered_views is not UNSET:
            ordered_views = []
            for ordered_views_item_data in _ordered_views:
                ordered_views_item = UUID(ordered_views_item_data)

                ordered_views.append(ordered_views_item)

        _latest_items_excludes = d.pop("LatestItemsExcludes", UNSET)
        latest_items_excludes: list[UUID] | Unset = UNSET
        if _latest_items_excludes is not UNSET:
            latest_items_excludes = []
            for latest_items_excludes_item_data in _latest_items_excludes:
                latest_items_excludes_item = UUID(latest_items_excludes_item_data)

                latest_items_excludes.append(latest_items_excludes_item)

        _my_media_excludes = d.pop("MyMediaExcludes", UNSET)
        my_media_excludes: list[UUID] | Unset = UNSET
        if _my_media_excludes is not UNSET:
            my_media_excludes = []
            for my_media_excludes_item_data in _my_media_excludes:
                my_media_excludes_item = UUID(my_media_excludes_item_data)

                my_media_excludes.append(my_media_excludes_item)

        hide_played_in_latest = d.pop("HidePlayedInLatest", UNSET)

        remember_audio_selections = d.pop("RememberAudioSelections", UNSET)

        remember_subtitle_selections = d.pop("RememberSubtitleSelections", UNSET)

        enable_next_episode_auto_play = d.pop("EnableNextEpisodeAutoPlay", UNSET)

        def _parse_cast_receiver_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cast_receiver_id = _parse_cast_receiver_id(d.pop("CastReceiverId", UNSET))

        user_configuration = cls(
            audio_language_preference=audio_language_preference,
            play_default_audio_track=play_default_audio_track,
            subtitle_language_preference=subtitle_language_preference,
            display_missing_episodes=display_missing_episodes,
            grouped_folders=grouped_folders,
            subtitle_mode=subtitle_mode,
            display_collections_view=display_collections_view,
            enable_local_password=enable_local_password,
            ordered_views=ordered_views,
            latest_items_excludes=latest_items_excludes,
            my_media_excludes=my_media_excludes,
            hide_played_in_latest=hide_played_in_latest,
            remember_audio_selections=remember_audio_selections,
            remember_subtitle_selections=remember_subtitle_selections,
            enable_next_episode_auto_play=enable_next_episode_auto_play,
            cast_receiver_id=cast_receiver_id,
        )

        return user_configuration
