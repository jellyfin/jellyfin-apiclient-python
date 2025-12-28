from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LyricLineCue")


@_attrs_define
class LyricLineCue:
    """LyricLineCue model, holds information about the timing of words within a LyricLine.

    Attributes:
        position (int | Unset): Gets the start character index of the cue.
        end_position (int | Unset): Gets the end character index of the cue.
        start (int | Unset): Gets the timestamp the lyric is synced to in ticks.
        end (int | None | Unset): Gets the end timestamp the lyric is synced to in ticks.
    """

    position: int | Unset = UNSET
    end_position: int | Unset = UNSET
    start: int | Unset = UNSET
    end: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        end_position = self.end_position

        start = self.start

        end: int | None | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        else:
            end = self.end

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if position is not UNSET:
            field_dict["Position"] = position
        if end_position is not UNSET:
            field_dict["EndPosition"] = end_position
        if start is not UNSET:
            field_dict["Start"] = start
        if end is not UNSET:
            field_dict["End"] = end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("Position", UNSET)

        end_position = d.pop("EndPosition", UNSET)

        start = d.pop("Start", UNSET)

        def _parse_end(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end = _parse_end(d.pop("End", UNSET))

        lyric_line_cue = cls(
            position=position,
            end_position=end_position,
            start=start,
            end=end,
        )

        return lyric_line_cue
