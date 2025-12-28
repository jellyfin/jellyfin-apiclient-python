from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.process_priority_class import ProcessPriorityClass
from ..models.trickplay_scan_behavior import TrickplayScanBehavior
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrickplayOptions")


@_attrs_define
class TrickplayOptions:
    """Class TrickplayOptions.

    Attributes:
        enable_hw_acceleration (bool | Unset): Gets or sets a value indicating whether or not to use HW acceleration.
        enable_hw_encoding (bool | Unset): Gets or sets a value indicating whether or not to use HW accelerated MJPEG
            encoding.
        enable_key_frame_only_extraction (bool | Unset): Gets or sets a value indicating whether to only extract key
            frames.
            Significantly faster, but is not compatible with all decoders and/or video files.
        scan_behavior (TrickplayScanBehavior | Unset): Enum TrickplayScanBehavior.
        process_priority (ProcessPriorityClass | Unset):
        interval (int | Unset): Gets or sets the interval, in ms, between each new trickplay image.
        width_resolutions (list[int] | Unset): Gets or sets the target width resolutions, in px, to generates preview
            images for.
        tile_width (int | Unset): Gets or sets number of tile images to allow in X dimension.
        tile_height (int | Unset): Gets or sets number of tile images to allow in Y dimension.
        qscale (int | Unset): Gets or sets the ffmpeg output quality level.
        jpeg_quality (int | Unset): Gets or sets the jpeg quality to use for image tiles.
        process_threads (int | Unset): Gets or sets the number of threads to be used by ffmpeg.
    """

    enable_hw_acceleration: bool | Unset = UNSET
    enable_hw_encoding: bool | Unset = UNSET
    enable_key_frame_only_extraction: bool | Unset = UNSET
    scan_behavior: TrickplayScanBehavior | Unset = UNSET
    process_priority: ProcessPriorityClass | Unset = UNSET
    interval: int | Unset = UNSET
    width_resolutions: list[int] | Unset = UNSET
    tile_width: int | Unset = UNSET
    tile_height: int | Unset = UNSET
    qscale: int | Unset = UNSET
    jpeg_quality: int | Unset = UNSET
    process_threads: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enable_hw_acceleration = self.enable_hw_acceleration

        enable_hw_encoding = self.enable_hw_encoding

        enable_key_frame_only_extraction = self.enable_key_frame_only_extraction

        scan_behavior: str | Unset = UNSET
        if not isinstance(self.scan_behavior, Unset):
            scan_behavior = self.scan_behavior.value

        process_priority: str | Unset = UNSET
        if not isinstance(self.process_priority, Unset):
            process_priority = self.process_priority.value

        interval = self.interval

        width_resolutions: list[int] | Unset = UNSET
        if not isinstance(self.width_resolutions, Unset):
            width_resolutions = self.width_resolutions

        tile_width = self.tile_width

        tile_height = self.tile_height

        qscale = self.qscale

        jpeg_quality = self.jpeg_quality

        process_threads = self.process_threads

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enable_hw_acceleration is not UNSET:
            field_dict["EnableHwAcceleration"] = enable_hw_acceleration
        if enable_hw_encoding is not UNSET:
            field_dict["EnableHwEncoding"] = enable_hw_encoding
        if enable_key_frame_only_extraction is not UNSET:
            field_dict["EnableKeyFrameOnlyExtraction"] = (
                enable_key_frame_only_extraction
            )
        if scan_behavior is not UNSET:
            field_dict["ScanBehavior"] = scan_behavior
        if process_priority is not UNSET:
            field_dict["ProcessPriority"] = process_priority
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if width_resolutions is not UNSET:
            field_dict["WidthResolutions"] = width_resolutions
        if tile_width is not UNSET:
            field_dict["TileWidth"] = tile_width
        if tile_height is not UNSET:
            field_dict["TileHeight"] = tile_height
        if qscale is not UNSET:
            field_dict["Qscale"] = qscale
        if jpeg_quality is not UNSET:
            field_dict["JpegQuality"] = jpeg_quality
        if process_threads is not UNSET:
            field_dict["ProcessThreads"] = process_threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_hw_acceleration = d.pop("EnableHwAcceleration", UNSET)

        enable_hw_encoding = d.pop("EnableHwEncoding", UNSET)

        enable_key_frame_only_extraction = d.pop("EnableKeyFrameOnlyExtraction", UNSET)

        _scan_behavior = d.pop("ScanBehavior", UNSET)
        scan_behavior: TrickplayScanBehavior | Unset
        if isinstance(_scan_behavior, Unset):
            scan_behavior = UNSET
        else:
            scan_behavior = TrickplayScanBehavior(_scan_behavior)

        _process_priority = d.pop("ProcessPriority", UNSET)
        process_priority: ProcessPriorityClass | Unset
        if isinstance(_process_priority, Unset):
            process_priority = UNSET
        else:
            process_priority = ProcessPriorityClass(_process_priority)

        interval = d.pop("Interval", UNSET)

        width_resolutions = cast(list[int], d.pop("WidthResolutions", UNSET))

        tile_width = d.pop("TileWidth", UNSET)

        tile_height = d.pop("TileHeight", UNSET)

        qscale = d.pop("Qscale", UNSET)

        jpeg_quality = d.pop("JpegQuality", UNSET)

        process_threads = d.pop("ProcessThreads", UNSET)

        trickplay_options = cls(
            enable_hw_acceleration=enable_hw_acceleration,
            enable_hw_encoding=enable_hw_encoding,
            enable_key_frame_only_extraction=enable_key_frame_only_extraction,
            scan_behavior=scan_behavior,
            process_priority=process_priority,
            interval=interval,
            width_resolutions=width_resolutions,
            tile_width=tile_width,
            tile_height=tile_height,
            qscale=qscale,
            jpeg_quality=jpeg_quality,
            process_threads=process_threads,
        )

        return trickplay_options
