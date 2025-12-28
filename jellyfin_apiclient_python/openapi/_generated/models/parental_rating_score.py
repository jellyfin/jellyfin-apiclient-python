from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParentalRatingScore")


@_attrs_define
class ParentalRatingScore:
    """A class representing an parental rating score.

    Attributes:
        score (int | Unset): Gets or sets the score.
        sub_score (int | None | Unset): Gets or sets the sub score.
    """

    score: int | Unset = UNSET
    sub_score: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        sub_score: int | None | Unset
        if isinstance(self.sub_score, Unset):
            sub_score = UNSET
        else:
            sub_score = self.sub_score

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if sub_score is not UNSET:
            field_dict["subScore"] = sub_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score", UNSET)

        def _parse_sub_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sub_score = _parse_sub_score(d.pop("subScore", UNSET))

        parental_rating_score = cls(
            score=score,
            sub_score=sub_score,
        )

        return parental_rating_score
