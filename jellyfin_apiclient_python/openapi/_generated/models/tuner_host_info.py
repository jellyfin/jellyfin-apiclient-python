from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TunerHostInfo")


@_attrs_define
class TunerHostInfo:
    """
    Attributes:
        id (None | str | Unset):
        url (None | str | Unset):
        type_ (None | str | Unset):
        device_id (None | str | Unset):
        friendly_name (None | str | Unset):
        import_favorites_only (bool | Unset):
        allow_hw_transcoding (bool | Unset):
        allow_fmp_4_transcoding_container (bool | Unset):
        allow_stream_sharing (bool | Unset):
        fallback_max_streaming_bitrate (int | Unset):
        enable_stream_looping (bool | Unset):
        source (None | str | Unset):
        tuner_count (int | Unset):
        user_agent (None | str | Unset):
        ignore_dts (bool | Unset):
        read_at_native_framerate (bool | Unset):
    """

    id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    device_id: None | str | Unset = UNSET
    friendly_name: None | str | Unset = UNSET
    import_favorites_only: bool | Unset = UNSET
    allow_hw_transcoding: bool | Unset = UNSET
    allow_fmp_4_transcoding_container: bool | Unset = UNSET
    allow_stream_sharing: bool | Unset = UNSET
    fallback_max_streaming_bitrate: int | Unset = UNSET
    enable_stream_looping: bool | Unset = UNSET
    source: None | str | Unset = UNSET
    tuner_count: int | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    ignore_dts: bool | Unset = UNSET
    read_at_native_framerate: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        device_id: None | str | Unset
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        friendly_name: None | str | Unset
        if isinstance(self.friendly_name, Unset):
            friendly_name = UNSET
        else:
            friendly_name = self.friendly_name

        import_favorites_only = self.import_favorites_only

        allow_hw_transcoding = self.allow_hw_transcoding

        allow_fmp_4_transcoding_container = self.allow_fmp_4_transcoding_container

        allow_stream_sharing = self.allow_stream_sharing

        fallback_max_streaming_bitrate = self.fallback_max_streaming_bitrate

        enable_stream_looping = self.enable_stream_looping

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        tuner_count = self.tuner_count

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        ignore_dts = self.ignore_dts

        read_at_native_framerate = self.read_at_native_framerate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if url is not UNSET:
            field_dict["Url"] = url
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if friendly_name is not UNSET:
            field_dict["FriendlyName"] = friendly_name
        if import_favorites_only is not UNSET:
            field_dict["ImportFavoritesOnly"] = import_favorites_only
        if allow_hw_transcoding is not UNSET:
            field_dict["AllowHWTranscoding"] = allow_hw_transcoding
        if allow_fmp_4_transcoding_container is not UNSET:
            field_dict["AllowFmp4TranscodingContainer"] = (
                allow_fmp_4_transcoding_container
            )
        if allow_stream_sharing is not UNSET:
            field_dict["AllowStreamSharing"] = allow_stream_sharing
        if fallback_max_streaming_bitrate is not UNSET:
            field_dict["FallbackMaxStreamingBitrate"] = fallback_max_streaming_bitrate
        if enable_stream_looping is not UNSET:
            field_dict["EnableStreamLooping"] = enable_stream_looping
        if source is not UNSET:
            field_dict["Source"] = source
        if tuner_count is not UNSET:
            field_dict["TunerCount"] = tuner_count
        if user_agent is not UNSET:
            field_dict["UserAgent"] = user_agent
        if ignore_dts is not UNSET:
            field_dict["IgnoreDts"] = ignore_dts
        if read_at_native_framerate is not UNSET:
            field_dict["ReadAtNativeFramerate"] = read_at_native_framerate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("Url", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_device_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        def _parse_friendly_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        friendly_name = _parse_friendly_name(d.pop("FriendlyName", UNSET))

        import_favorites_only = d.pop("ImportFavoritesOnly", UNSET)

        allow_hw_transcoding = d.pop("AllowHWTranscoding", UNSET)

        allow_fmp_4_transcoding_container = d.pop(
            "AllowFmp4TranscodingContainer", UNSET
        )

        allow_stream_sharing = d.pop("AllowStreamSharing", UNSET)

        fallback_max_streaming_bitrate = d.pop("FallbackMaxStreamingBitrate", UNSET)

        enable_stream_looping = d.pop("EnableStreamLooping", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("Source", UNSET))

        tuner_count = d.pop("TunerCount", UNSET)

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("UserAgent", UNSET))

        ignore_dts = d.pop("IgnoreDts", UNSET)

        read_at_native_framerate = d.pop("ReadAtNativeFramerate", UNSET)

        tuner_host_info = cls(
            id=id,
            url=url,
            type_=type_,
            device_id=device_id,
            friendly_name=friendly_name,
            import_favorites_only=import_favorites_only,
            allow_hw_transcoding=allow_hw_transcoding,
            allow_fmp_4_transcoding_container=allow_fmp_4_transcoding_container,
            allow_stream_sharing=allow_stream_sharing,
            fallback_max_streaming_bitrate=fallback_max_streaming_bitrate,
            enable_stream_looping=enable_stream_looping,
            source=source,
            tuner_count=tuner_count,
            user_agent=user_agent,
            ignore_dts=ignore_dts,
            read_at_native_framerate=read_at_native_framerate,
        )

        return tuner_host_info
