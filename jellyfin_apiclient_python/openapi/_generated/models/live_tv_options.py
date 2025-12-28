from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_provider_info import ListingsProviderInfo
    from ..models.tuner_host_info import TunerHostInfo


T = TypeVar("T", bound="LiveTvOptions")


@_attrs_define
class LiveTvOptions:
    """
    Attributes:
        guide_days (int | None | Unset):
        recording_path (None | str | Unset):
        movie_recording_path (None | str | Unset):
        series_recording_path (None | str | Unset):
        enable_recording_subfolders (bool | Unset):
        enable_original_audio_with_encoded_recordings (bool | Unset):
        tuner_hosts (list[TunerHostInfo] | None | Unset):
        listing_providers (list[ListingsProviderInfo] | None | Unset):
        pre_padding_seconds (int | Unset):
        post_padding_seconds (int | Unset):
        media_locations_created (list[str] | None | Unset):
        recording_post_processor (None | str | Unset):
        recording_post_processor_arguments (None | str | Unset):
        save_recording_nfo (bool | Unset):
        save_recording_images (bool | Unset):
    """

    guide_days: int | None | Unset = UNSET
    recording_path: None | str | Unset = UNSET
    movie_recording_path: None | str | Unset = UNSET
    series_recording_path: None | str | Unset = UNSET
    enable_recording_subfolders: bool | Unset = UNSET
    enable_original_audio_with_encoded_recordings: bool | Unset = UNSET
    tuner_hosts: list[TunerHostInfo] | None | Unset = UNSET
    listing_providers: list[ListingsProviderInfo] | None | Unset = UNSET
    pre_padding_seconds: int | Unset = UNSET
    post_padding_seconds: int | Unset = UNSET
    media_locations_created: list[str] | None | Unset = UNSET
    recording_post_processor: None | str | Unset = UNSET
    recording_post_processor_arguments: None | str | Unset = UNSET
    save_recording_nfo: bool | Unset = UNSET
    save_recording_images: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        guide_days: int | None | Unset
        if isinstance(self.guide_days, Unset):
            guide_days = UNSET
        else:
            guide_days = self.guide_days

        recording_path: None | str | Unset
        if isinstance(self.recording_path, Unset):
            recording_path = UNSET
        else:
            recording_path = self.recording_path

        movie_recording_path: None | str | Unset
        if isinstance(self.movie_recording_path, Unset):
            movie_recording_path = UNSET
        else:
            movie_recording_path = self.movie_recording_path

        series_recording_path: None | str | Unset
        if isinstance(self.series_recording_path, Unset):
            series_recording_path = UNSET
        else:
            series_recording_path = self.series_recording_path

        enable_recording_subfolders = self.enable_recording_subfolders

        enable_original_audio_with_encoded_recordings = (
            self.enable_original_audio_with_encoded_recordings
        )

        tuner_hosts: list[dict[str, Any]] | None | Unset
        if isinstance(self.tuner_hosts, Unset):
            tuner_hosts = UNSET
        elif isinstance(self.tuner_hosts, list):
            tuner_hosts = []
            for tuner_hosts_type_0_item_data in self.tuner_hosts:
                tuner_hosts_type_0_item = tuner_hosts_type_0_item_data.to_dict()
                tuner_hosts.append(tuner_hosts_type_0_item)

        else:
            tuner_hosts = self.tuner_hosts

        listing_providers: list[dict[str, Any]] | None | Unset
        if isinstance(self.listing_providers, Unset):
            listing_providers = UNSET
        elif isinstance(self.listing_providers, list):
            listing_providers = []
            for listing_providers_type_0_item_data in self.listing_providers:
                listing_providers_type_0_item = (
                    listing_providers_type_0_item_data.to_dict()
                )
                listing_providers.append(listing_providers_type_0_item)

        else:
            listing_providers = self.listing_providers

        pre_padding_seconds = self.pre_padding_seconds

        post_padding_seconds = self.post_padding_seconds

        media_locations_created: list[str] | None | Unset
        if isinstance(self.media_locations_created, Unset):
            media_locations_created = UNSET
        elif isinstance(self.media_locations_created, list):
            media_locations_created = self.media_locations_created

        else:
            media_locations_created = self.media_locations_created

        recording_post_processor: None | str | Unset
        if isinstance(self.recording_post_processor, Unset):
            recording_post_processor = UNSET
        else:
            recording_post_processor = self.recording_post_processor

        recording_post_processor_arguments: None | str | Unset
        if isinstance(self.recording_post_processor_arguments, Unset):
            recording_post_processor_arguments = UNSET
        else:
            recording_post_processor_arguments = self.recording_post_processor_arguments

        save_recording_nfo = self.save_recording_nfo

        save_recording_images = self.save_recording_images

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if guide_days is not UNSET:
            field_dict["GuideDays"] = guide_days
        if recording_path is not UNSET:
            field_dict["RecordingPath"] = recording_path
        if movie_recording_path is not UNSET:
            field_dict["MovieRecordingPath"] = movie_recording_path
        if series_recording_path is not UNSET:
            field_dict["SeriesRecordingPath"] = series_recording_path
        if enable_recording_subfolders is not UNSET:
            field_dict["EnableRecordingSubfolders"] = enable_recording_subfolders
        if enable_original_audio_with_encoded_recordings is not UNSET:
            field_dict["EnableOriginalAudioWithEncodedRecordings"] = (
                enable_original_audio_with_encoded_recordings
            )
        if tuner_hosts is not UNSET:
            field_dict["TunerHosts"] = tuner_hosts
        if listing_providers is not UNSET:
            field_dict["ListingProviders"] = listing_providers
        if pre_padding_seconds is not UNSET:
            field_dict["PrePaddingSeconds"] = pre_padding_seconds
        if post_padding_seconds is not UNSET:
            field_dict["PostPaddingSeconds"] = post_padding_seconds
        if media_locations_created is not UNSET:
            field_dict["MediaLocationsCreated"] = media_locations_created
        if recording_post_processor is not UNSET:
            field_dict["RecordingPostProcessor"] = recording_post_processor
        if recording_post_processor_arguments is not UNSET:
            field_dict["RecordingPostProcessorArguments"] = (
                recording_post_processor_arguments
            )
        if save_recording_nfo is not UNSET:
            field_dict["SaveRecordingNFO"] = save_recording_nfo
        if save_recording_images is not UNSET:
            field_dict["SaveRecordingImages"] = save_recording_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listings_provider_info import ListingsProviderInfo
        from ..models.tuner_host_info import TunerHostInfo

        d = dict(src_dict)

        def _parse_guide_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guide_days = _parse_guide_days(d.pop("GuideDays", UNSET))

        def _parse_recording_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recording_path = _parse_recording_path(d.pop("RecordingPath", UNSET))

        def _parse_movie_recording_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        movie_recording_path = _parse_movie_recording_path(
            d.pop("MovieRecordingPath", UNSET)
        )

        def _parse_series_recording_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series_recording_path = _parse_series_recording_path(
            d.pop("SeriesRecordingPath", UNSET)
        )

        enable_recording_subfolders = d.pop("EnableRecordingSubfolders", UNSET)

        enable_original_audio_with_encoded_recordings = d.pop(
            "EnableOriginalAudioWithEncodedRecordings", UNSET
        )

        def _parse_tuner_hosts(data: object) -> list[TunerHostInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tuner_hosts_type_0 = []
                _tuner_hosts_type_0 = data
                for tuner_hosts_type_0_item_data in _tuner_hosts_type_0:
                    tuner_hosts_type_0_item = TunerHostInfo.from_dict(
                        tuner_hosts_type_0_item_data
                    )

                    tuner_hosts_type_0.append(tuner_hosts_type_0_item)

                return tuner_hosts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TunerHostInfo] | None | Unset, data)

        tuner_hosts = _parse_tuner_hosts(d.pop("TunerHosts", UNSET))

        def _parse_listing_providers(
            data: object,
        ) -> list[ListingsProviderInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                listing_providers_type_0 = []
                _listing_providers_type_0 = data
                for listing_providers_type_0_item_data in _listing_providers_type_0:
                    listing_providers_type_0_item = ListingsProviderInfo.from_dict(
                        listing_providers_type_0_item_data
                    )

                    listing_providers_type_0.append(listing_providers_type_0_item)

                return listing_providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListingsProviderInfo] | None | Unset, data)

        listing_providers = _parse_listing_providers(d.pop("ListingProviders", UNSET))

        pre_padding_seconds = d.pop("PrePaddingSeconds", UNSET)

        post_padding_seconds = d.pop("PostPaddingSeconds", UNSET)

        def _parse_media_locations_created(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_locations_created_type_0 = cast(list[str], data)

                return media_locations_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        media_locations_created = _parse_media_locations_created(
            d.pop("MediaLocationsCreated", UNSET)
        )

        def _parse_recording_post_processor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recording_post_processor = _parse_recording_post_processor(
            d.pop("RecordingPostProcessor", UNSET)
        )

        def _parse_recording_post_processor_arguments(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recording_post_processor_arguments = _parse_recording_post_processor_arguments(
            d.pop("RecordingPostProcessorArguments", UNSET)
        )

        save_recording_nfo = d.pop("SaveRecordingNFO", UNSET)

        save_recording_images = d.pop("SaveRecordingImages", UNSET)

        live_tv_options = cls(
            guide_days=guide_days,
            recording_path=recording_path,
            movie_recording_path=movie_recording_path,
            series_recording_path=series_recording_path,
            enable_recording_subfolders=enable_recording_subfolders,
            enable_original_audio_with_encoded_recordings=enable_original_audio_with_encoded_recordings,
            tuner_hosts=tuner_hosts,
            listing_providers=listing_providers,
            pre_padding_seconds=pre_padding_seconds,
            post_padding_seconds=post_padding_seconds,
            media_locations_created=media_locations_created,
            recording_post_processor=recording_post_processor,
            recording_post_processor_arguments=recording_post_processor_arguments,
            save_recording_nfo=save_recording_nfo,
            save_recording_images=save_recording_images,
        )

        return live_tv_options
