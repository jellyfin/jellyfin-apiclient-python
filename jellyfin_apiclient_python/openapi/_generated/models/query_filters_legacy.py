from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryFiltersLegacy")


@_attrs_define
class QueryFiltersLegacy:
    """
    Attributes:
        genres (list[str] | None | Unset):
        tags (list[str] | None | Unset):
        official_ratings (list[str] | None | Unset):
        years (list[int] | None | Unset):
    """

    genres: list[str] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    official_ratings: list[str] | None | Unset = UNSET
    years: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        genres: list[str] | None | Unset
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        official_ratings: list[str] | None | Unset
        if isinstance(self.official_ratings, Unset):
            official_ratings = UNSET
        elif isinstance(self.official_ratings, list):
            official_ratings = self.official_ratings

        else:
            official_ratings = self.official_ratings

        years: list[int] | None | Unset
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(self.years, list):
            years = self.years

        else:
            years = self.years

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if official_ratings is not UNSET:
            field_dict["OfficialRatings"] = official_ratings
        if years is not UNSET:
            field_dict["Years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_genres(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(list[str], data)

                return genres_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        genres = _parse_genres(d.pop("Genres", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("Tags", UNSET))

        def _parse_official_ratings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                official_ratings_type_0 = cast(list[str], data)

                return official_ratings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        official_ratings = _parse_official_ratings(d.pop("OfficialRatings", UNSET))

        def _parse_years(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                years_type_0 = cast(list[int], data)

                return years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        years = _parse_years(d.pop("Years", UNSET))

        query_filters_legacy = cls(
            genres=genres,
            tags=tags,
            official_ratings=official_ratings,
            years=years,
        )

        return query_filters_legacy
