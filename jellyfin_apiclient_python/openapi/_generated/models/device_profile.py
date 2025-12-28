from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codec_profile import CodecProfile
    from ..models.container_profile import ContainerProfile
    from ..models.direct_play_profile import DirectPlayProfile
    from ..models.subtitle_profile import SubtitleProfile
    from ..models.transcoding_profile import TranscodingProfile


T = TypeVar("T", bound="DeviceProfile")


@_attrs_define
class DeviceProfile:
    """A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device
    is able to play.
    <br />
    Specifically, it defines the supported <see
    cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
    <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec
    profiles and levels)
    the device is able to direct play (without transcoding or remuxing),
    as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
    transcode to</see> in case it isn't.

        Attributes:
            name (None | str | Unset): Gets or sets the name of this device profile. User profiles must have a unique name.
            id (None | Unset | UUID): Gets or sets the unique internal identifier.
            max_streaming_bitrate (int | None | Unset): Gets or sets the maximum allowed bitrate for all streamed content.
            max_static_bitrate (int | None | Unset): Gets or sets the maximum allowed bitrate for statically streamed
                content (= direct played files).
            music_streaming_transcoding_bitrate (int | None | Unset): Gets or sets the maximum allowed bitrate for
                transcoded music streams.
            max_static_music_bitrate (int | None | Unset): Gets or sets the maximum allowed bitrate for statically streamed
                (= direct played) music files.
            direct_play_profiles (list[DirectPlayProfile] | Unset): Gets or sets the direct play profiles.
            transcoding_profiles (list[TranscodingProfile] | Unset): Gets or sets the transcoding profiles.
            container_profiles (list[ContainerProfile] | Unset): Gets or sets the container profiles. Failing to meet these
                optional conditions causes transcoding to occur.
            codec_profiles (list[CodecProfile] | Unset): Gets or sets the codec profiles.
            subtitle_profiles (list[SubtitleProfile] | Unset): Gets or sets the subtitle profiles.
    """

    name: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    max_streaming_bitrate: int | None | Unset = UNSET
    max_static_bitrate: int | None | Unset = UNSET
    music_streaming_transcoding_bitrate: int | None | Unset = UNSET
    max_static_music_bitrate: int | None | Unset = UNSET
    direct_play_profiles: list[DirectPlayProfile] | Unset = UNSET
    transcoding_profiles: list[TranscodingProfile] | Unset = UNSET
    container_profiles: list[ContainerProfile] | Unset = UNSET
    codec_profiles: list[CodecProfile] | Unset = UNSET
    subtitle_profiles: list[SubtitleProfile] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        max_streaming_bitrate: int | None | Unset
        if isinstance(self.max_streaming_bitrate, Unset):
            max_streaming_bitrate = UNSET
        else:
            max_streaming_bitrate = self.max_streaming_bitrate

        max_static_bitrate: int | None | Unset
        if isinstance(self.max_static_bitrate, Unset):
            max_static_bitrate = UNSET
        else:
            max_static_bitrate = self.max_static_bitrate

        music_streaming_transcoding_bitrate: int | None | Unset
        if isinstance(self.music_streaming_transcoding_bitrate, Unset):
            music_streaming_transcoding_bitrate = UNSET
        else:
            music_streaming_transcoding_bitrate = (
                self.music_streaming_transcoding_bitrate
            )

        max_static_music_bitrate: int | None | Unset
        if isinstance(self.max_static_music_bitrate, Unset):
            max_static_music_bitrate = UNSET
        else:
            max_static_music_bitrate = self.max_static_music_bitrate

        direct_play_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.direct_play_profiles, Unset):
            direct_play_profiles = []
            for direct_play_profiles_item_data in self.direct_play_profiles:
                direct_play_profiles_item = direct_play_profiles_item_data.to_dict()
                direct_play_profiles.append(direct_play_profiles_item)

        transcoding_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transcoding_profiles, Unset):
            transcoding_profiles = []
            for transcoding_profiles_item_data in self.transcoding_profiles:
                transcoding_profiles_item = transcoding_profiles_item_data.to_dict()
                transcoding_profiles.append(transcoding_profiles_item)

        container_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.container_profiles, Unset):
            container_profiles = []
            for container_profiles_item_data in self.container_profiles:
                container_profiles_item = container_profiles_item_data.to_dict()
                container_profiles.append(container_profiles_item)

        codec_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.codec_profiles, Unset):
            codec_profiles = []
            for codec_profiles_item_data in self.codec_profiles:
                codec_profiles_item = codec_profiles_item_data.to_dict()
                codec_profiles.append(codec_profiles_item)

        subtitle_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subtitle_profiles, Unset):
            subtitle_profiles = []
            for subtitle_profiles_item_data in self.subtitle_profiles:
                subtitle_profiles_item = subtitle_profiles_item_data.to_dict()
                subtitle_profiles.append(subtitle_profiles_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if max_streaming_bitrate is not UNSET:
            field_dict["MaxStreamingBitrate"] = max_streaming_bitrate
        if max_static_bitrate is not UNSET:
            field_dict["MaxStaticBitrate"] = max_static_bitrate
        if music_streaming_transcoding_bitrate is not UNSET:
            field_dict["MusicStreamingTranscodingBitrate"] = (
                music_streaming_transcoding_bitrate
            )
        if max_static_music_bitrate is not UNSET:
            field_dict["MaxStaticMusicBitrate"] = max_static_music_bitrate
        if direct_play_profiles is not UNSET:
            field_dict["DirectPlayProfiles"] = direct_play_profiles
        if transcoding_profiles is not UNSET:
            field_dict["TranscodingProfiles"] = transcoding_profiles
        if container_profiles is not UNSET:
            field_dict["ContainerProfiles"] = container_profiles
        if codec_profiles is not UNSET:
            field_dict["CodecProfiles"] = codec_profiles
        if subtitle_profiles is not UNSET:
            field_dict["SubtitleProfiles"] = subtitle_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.codec_profile import CodecProfile
        from ..models.container_profile import ContainerProfile
        from ..models.direct_play_profile import DirectPlayProfile
        from ..models.subtitle_profile import SubtitleProfile
        from ..models.transcoding_profile import TranscodingProfile

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_max_streaming_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_streaming_bitrate = _parse_max_streaming_bitrate(
            d.pop("MaxStreamingBitrate", UNSET)
        )

        def _parse_max_static_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_static_bitrate = _parse_max_static_bitrate(d.pop("MaxStaticBitrate", UNSET))

        def _parse_music_streaming_transcoding_bitrate(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        music_streaming_transcoding_bitrate = (
            _parse_music_streaming_transcoding_bitrate(
                d.pop("MusicStreamingTranscodingBitrate", UNSET)
            )
        )

        def _parse_max_static_music_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_static_music_bitrate = _parse_max_static_music_bitrate(
            d.pop("MaxStaticMusicBitrate", UNSET)
        )

        _direct_play_profiles = d.pop("DirectPlayProfiles", UNSET)
        direct_play_profiles: list[DirectPlayProfile] | Unset = UNSET
        if _direct_play_profiles is not UNSET:
            direct_play_profiles = []
            for direct_play_profiles_item_data in _direct_play_profiles:
                direct_play_profiles_item = DirectPlayProfile.from_dict(
                    direct_play_profiles_item_data
                )

                direct_play_profiles.append(direct_play_profiles_item)

        _transcoding_profiles = d.pop("TranscodingProfiles", UNSET)
        transcoding_profiles: list[TranscodingProfile] | Unset = UNSET
        if _transcoding_profiles is not UNSET:
            transcoding_profiles = []
            for transcoding_profiles_item_data in _transcoding_profiles:
                transcoding_profiles_item = TranscodingProfile.from_dict(
                    transcoding_profiles_item_data
                )

                transcoding_profiles.append(transcoding_profiles_item)

        _container_profiles = d.pop("ContainerProfiles", UNSET)
        container_profiles: list[ContainerProfile] | Unset = UNSET
        if _container_profiles is not UNSET:
            container_profiles = []
            for container_profiles_item_data in _container_profiles:
                container_profiles_item = ContainerProfile.from_dict(
                    container_profiles_item_data
                )

                container_profiles.append(container_profiles_item)

        _codec_profiles = d.pop("CodecProfiles", UNSET)
        codec_profiles: list[CodecProfile] | Unset = UNSET
        if _codec_profiles is not UNSET:
            codec_profiles = []
            for codec_profiles_item_data in _codec_profiles:
                codec_profiles_item = CodecProfile.from_dict(codec_profiles_item_data)

                codec_profiles.append(codec_profiles_item)

        _subtitle_profiles = d.pop("SubtitleProfiles", UNSET)
        subtitle_profiles: list[SubtitleProfile] | Unset = UNSET
        if _subtitle_profiles is not UNSET:
            subtitle_profiles = []
            for subtitle_profiles_item_data in _subtitle_profiles:
                subtitle_profiles_item = SubtitleProfile.from_dict(
                    subtitle_profiles_item_data
                )

                subtitle_profiles.append(subtitle_profiles_item)

        device_profile = cls(
            name=name,
            id=id,
            max_streaming_bitrate=max_streaming_bitrate,
            max_static_bitrate=max_static_bitrate,
            music_streaming_transcoding_bitrate=music_streaming_transcoding_bitrate,
            max_static_music_bitrate=max_static_music_bitrate,
            direct_play_profiles=direct_play_profiles,
            transcoding_profiles=transcoding_profiles,
            container_profiles=container_profiles,
            codec_profiles=codec_profiles,
            subtitle_profiles=subtitle_profiles,
        )

        return device_profile
