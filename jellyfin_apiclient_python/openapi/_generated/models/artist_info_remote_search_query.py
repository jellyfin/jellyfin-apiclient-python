from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artist_info import ArtistInfo


T = TypeVar("T", bound="ArtistInfoRemoteSearchQuery")


@_attrs_define
class ArtistInfoRemoteSearchQuery:
    """
    Attributes:
        search_info (ArtistInfo | None | Unset):
        item_id (UUID | Unset):
        search_provider_name (None | str | Unset): Gets or sets the provider name to search within if set.
        include_disabled_providers (bool | Unset): Gets or sets a value indicating whether disabled providers should be
            included.
    """

    search_info: ArtistInfo | None | Unset = UNSET
    item_id: UUID | Unset = UNSET
    search_provider_name: None | str | Unset = UNSET
    include_disabled_providers: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.artist_info import ArtistInfo

        search_info: dict[str, Any] | None | Unset
        if isinstance(self.search_info, Unset):
            search_info = UNSET
        elif isinstance(self.search_info, ArtistInfo):
            search_info = self.search_info.to_dict()
        else:
            search_info = self.search_info

        item_id: str | Unset = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)

        search_provider_name: None | str | Unset
        if isinstance(self.search_provider_name, Unset):
            search_provider_name = UNSET
        else:
            search_provider_name = self.search_provider_name

        include_disabled_providers = self.include_disabled_providers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if search_info is not UNSET:
            field_dict["SearchInfo"] = search_info
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if search_provider_name is not UNSET:
            field_dict["SearchProviderName"] = search_provider_name
        if include_disabled_providers is not UNSET:
            field_dict["IncludeDisabledProviders"] = include_disabled_providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artist_info import ArtistInfo

        d = dict(src_dict)

        def _parse_search_info(data: object) -> ArtistInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_info_type_1 = ArtistInfo.from_dict(data)

                return search_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArtistInfo | None | Unset, data)

        search_info = _parse_search_info(d.pop("SearchInfo", UNSET))

        _item_id = d.pop("ItemId", UNSET)
        item_id: UUID | Unset
        if isinstance(_item_id, Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)

        def _parse_search_provider_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_provider_name = _parse_search_provider_name(
            d.pop("SearchProviderName", UNSET)
        )

        include_disabled_providers = d.pop("IncludeDisabledProviders", UNSET)

        artist_info_remote_search_query = cls(
            search_info=search_info,
            item_id=item_id,
            search_provider_name=search_provider_name,
            include_disabled_providers=include_disabled_providers,
        )

        return artist_info_remote_search_query
