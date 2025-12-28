from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..models.rating_type import RatingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteImageInfo")


@_attrs_define
class RemoteImageInfo:
    """Class RemoteImageInfo.

    Attributes:
        provider_name (None | str | Unset): Gets or sets the name of the provider.
        url (None | str | Unset): Gets or sets the URL.
        thumbnail_url (None | str | Unset): Gets or sets a url used for previewing a smaller version.
        height (int | None | Unset): Gets or sets the height.
        width (int | None | Unset): Gets or sets the width.
        community_rating (float | None | Unset): Gets or sets the community rating.
        vote_count (int | None | Unset): Gets or sets the vote count.
        language (None | str | Unset): Gets or sets the language.
        type_ (ImageType | Unset): Enum ImageType.
        rating_type (RatingType | Unset):
    """

    provider_name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    height: int | None | Unset = UNSET
    width: int | None | Unset = UNSET
    community_rating: float | None | Unset = UNSET
    vote_count: int | None | Unset = UNSET
    language: None | str | Unset = UNSET
    type_: ImageType | Unset = UNSET
    rating_type: RatingType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider_name: None | str | Unset
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        community_rating: float | None | Unset
        if isinstance(self.community_rating, Unset):
            community_rating = UNSET
        else:
            community_rating = self.community_rating

        vote_count: int | None | Unset
        if isinstance(self.vote_count, Unset):
            vote_count = UNSET
        else:
            vote_count = self.vote_count

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        rating_type: str | Unset = UNSET
        if not isinstance(self.rating_type, Unset):
            rating_type = self.rating_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if url is not UNSET:
            field_dict["Url"] = url
        if thumbnail_url is not UNSET:
            field_dict["ThumbnailUrl"] = thumbnail_url
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if vote_count is not UNSET:
            field_dict["VoteCount"] = vote_count
        if language is not UNSET:
            field_dict["Language"] = language
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if rating_type is not UNSET:
            field_dict["RatingType"] = rating_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_provider_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_name = _parse_provider_name(d.pop("ProviderName", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("Url", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("ThumbnailUrl", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_community_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        community_rating = _parse_community_rating(d.pop("CommunityRating", UNSET))

        def _parse_vote_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vote_count = _parse_vote_count(d.pop("VoteCount", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("Language", UNSET))

        _type_ = d.pop("Type", UNSET)
        type_: ImageType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ImageType(_type_)

        _rating_type = d.pop("RatingType", UNSET)
        rating_type: RatingType | Unset
        if isinstance(_rating_type, Unset):
            rating_type = UNSET
        else:
            rating_type = RatingType(_rating_type)

        remote_image_info = cls(
            provider_name=provider_name,
            url=url,
            thumbnail_url=thumbnail_url,
            height=height,
            width=width,
            community_rating=community_rating,
            vote_count=vote_count,
            language=language,
            type_=type_,
            rating_type=rating_type,
        )

        return remote_image_info
