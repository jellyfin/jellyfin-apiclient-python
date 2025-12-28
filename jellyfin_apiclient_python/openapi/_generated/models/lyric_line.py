from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lyric_line_cue import LyricLineCue


T = TypeVar("T", bound="LyricLine")


@_attrs_define
class LyricLine:
    """Lyric model.

    Attributes:
        text (str | Unset): Gets the text of this lyric line.
        start (int | None | Unset): Gets the start time in ticks.
        cues (list[LyricLineCue] | None | Unset): Gets the time-aligned cues for the song's lyrics.
    """

    text: str | Unset = UNSET
    start: int | None | Unset = UNSET
    cues: list[LyricLineCue] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        start: int | None | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        else:
            start = self.start

        cues: list[dict[str, Any]] | None | Unset
        if isinstance(self.cues, Unset):
            cues = UNSET
        elif isinstance(self.cues, list):
            cues = []
            for cues_type_0_item_data in self.cues:
                cues_type_0_item = cues_type_0_item_data.to_dict()
                cues.append(cues_type_0_item)

        else:
            cues = self.cues

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if text is not UNSET:
            field_dict["Text"] = text
        if start is not UNSET:
            field_dict["Start"] = start
        if cues is not UNSET:
            field_dict["Cues"] = cues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lyric_line_cue import LyricLineCue

        d = dict(src_dict)
        text = d.pop("Text", UNSET)

        def _parse_start(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start = _parse_start(d.pop("Start", UNSET))

        def _parse_cues(data: object) -> list[LyricLineCue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cues_type_0 = []
                _cues_type_0 = data
                for cues_type_0_item_data in _cues_type_0:
                    cues_type_0_item = LyricLineCue.from_dict(cues_type_0_item_data)

                    cues_type_0.append(cues_type_0_item)

                return cues_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LyricLineCue] | None | Unset, data)

        cues = _parse_cues(d.pop("Cues", UNSET))

        lyric_line = cls(
            text=text,
            start=start,
            cues=cues,
        )

        return lyric_line
