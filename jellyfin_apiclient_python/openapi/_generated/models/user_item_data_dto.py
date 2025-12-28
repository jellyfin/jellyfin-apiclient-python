from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserItemDataDto")


@_attrs_define
class UserItemDataDto:
    """Class UserItemDataDto.

    Attributes:
        rating (float | None | Unset): Gets or sets the rating.
        played_percentage (float | None | Unset): Gets or sets the played percentage.
        unplayed_item_count (int | None | Unset): Gets or sets the unplayed item count.
        playback_position_ticks (int | Unset): Gets or sets the playback position ticks.
        play_count (int | Unset): Gets or sets the play count.
        is_favorite (bool | Unset): Gets or sets a value indicating whether this instance is favorite.
        likes (bool | None | Unset): Gets or sets a value indicating whether this MediaBrowser.Model.Dto.UserItemDataDto
            is likes.
        last_played_date (datetime.datetime | None | Unset): Gets or sets the last played date.
        played (bool | Unset): Gets or sets a value indicating whether this MediaBrowser.Model.Dto.UserItemDataDto is
            played.
        key (str | Unset): Gets or sets the key.
        item_id (UUID | Unset): Gets or sets the item identifier.
    """

    rating: float | None | Unset = UNSET
    played_percentage: float | None | Unset = UNSET
    unplayed_item_count: int | None | Unset = UNSET
    playback_position_ticks: int | Unset = UNSET
    play_count: int | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    likes: bool | None | Unset = UNSET
    last_played_date: datetime.datetime | None | Unset = UNSET
    played: bool | Unset = UNSET
    key: str | Unset = UNSET
    item_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        played_percentage: float | None | Unset
        if isinstance(self.played_percentage, Unset):
            played_percentage = UNSET
        else:
            played_percentage = self.played_percentage

        unplayed_item_count: int | None | Unset
        if isinstance(self.unplayed_item_count, Unset):
            unplayed_item_count = UNSET
        else:
            unplayed_item_count = self.unplayed_item_count

        playback_position_ticks = self.playback_position_ticks

        play_count = self.play_count

        is_favorite = self.is_favorite

        likes: bool | None | Unset
        if isinstance(self.likes, Unset):
            likes = UNSET
        else:
            likes = self.likes

        last_played_date: None | str | Unset
        if isinstance(self.last_played_date, Unset):
            last_played_date = UNSET
        elif isinstance(self.last_played_date, datetime.datetime):
            last_played_date = self.last_played_date.isoformat()
        else:
            last_played_date = self.last_played_date

        played = self.played

        key = self.key

        item_id: str | Unset = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rating is not UNSET:
            field_dict["Rating"] = rating
        if played_percentage is not UNSET:
            field_dict["PlayedPercentage"] = played_percentage
        if unplayed_item_count is not UNSET:
            field_dict["UnplayedItemCount"] = unplayed_item_count
        if playback_position_ticks is not UNSET:
            field_dict["PlaybackPositionTicks"] = playback_position_ticks
        if play_count is not UNSET:
            field_dict["PlayCount"] = play_count
        if is_favorite is not UNSET:
            field_dict["IsFavorite"] = is_favorite
        if likes is not UNSET:
            field_dict["Likes"] = likes
        if last_played_date is not UNSET:
            field_dict["LastPlayedDate"] = last_played_date
        if played is not UNSET:
            field_dict["Played"] = played
        if key is not UNSET:
            field_dict["Key"] = key
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("Rating", UNSET))

        def _parse_played_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        played_percentage = _parse_played_percentage(d.pop("PlayedPercentage", UNSET))

        def _parse_unplayed_item_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unplayed_item_count = _parse_unplayed_item_count(
            d.pop("UnplayedItemCount", UNSET)
        )

        playback_position_ticks = d.pop("PlaybackPositionTicks", UNSET)

        play_count = d.pop("PlayCount", UNSET)

        is_favorite = d.pop("IsFavorite", UNSET)

        def _parse_likes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        likes = _parse_likes(d.pop("Likes", UNSET))

        def _parse_last_played_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_played_date_type_0 = isoparse(data)

                return last_played_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_played_date = _parse_last_played_date(d.pop("LastPlayedDate", UNSET))

        played = d.pop("Played", UNSET)

        key = d.pop("Key", UNSET)

        _item_id = d.pop("ItemId", UNSET)
        item_id: UUID | Unset
        if isinstance(_item_id, Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)

        user_item_data_dto = cls(
            rating=rating,
            played_percentage=played_percentage,
            unplayed_item_count=unplayed_item_count,
            playback_position_ticks=playback_position_ticks,
            play_count=play_count,
            is_favorite=is_favorite,
            likes=likes,
            last_played_date=last_played_date,
            played=played,
            key=key,
            item_id=item_id,
        )

        return user_item_data_dto
