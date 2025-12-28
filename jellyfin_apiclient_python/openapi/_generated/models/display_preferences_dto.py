from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.scroll_direction import ScrollDirection
from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.display_preferences_dto_custom_prefs import (
        DisplayPreferencesDtoCustomPrefs,
    )


T = TypeVar("T", bound="DisplayPreferencesDto")


@_attrs_define
class DisplayPreferencesDto:
    """Defines the display preferences for any item that supports them (usually Folders).

    Attributes:
        id (None | str | Unset): Gets or sets the user id.
        view_type (None | str | Unset): Gets or sets the type of the view.
        sort_by (None | str | Unset): Gets or sets the sort by.
        index_by (None | str | Unset): Gets or sets the index by.
        remember_indexing (bool | Unset): Gets or sets a value indicating whether [remember indexing].
        primary_image_height (int | Unset): Gets or sets the height of the primary image.
        primary_image_width (int | Unset): Gets or sets the width of the primary image.
        custom_prefs (DisplayPreferencesDtoCustomPrefs | Unset): Gets or sets the custom prefs.
        scroll_direction (ScrollDirection | Unset): An enum representing the axis that should be scrolled.
        show_backdrop (bool | Unset): Gets or sets a value indicating whether to show backdrops on this item.
        remember_sorting (bool | Unset): Gets or sets a value indicating whether [remember sorting].
        sort_order (SortOrder | Unset): An enum representing the sorting order.
        show_sidebar (bool | Unset): Gets or sets a value indicating whether [show sidebar].
        client (None | str | Unset): Gets or sets the client.
    """

    id: None | str | Unset = UNSET
    view_type: None | str | Unset = UNSET
    sort_by: None | str | Unset = UNSET
    index_by: None | str | Unset = UNSET
    remember_indexing: bool | Unset = UNSET
    primary_image_height: int | Unset = UNSET
    primary_image_width: int | Unset = UNSET
    custom_prefs: DisplayPreferencesDtoCustomPrefs | Unset = UNSET
    scroll_direction: ScrollDirection | Unset = UNSET
    show_backdrop: bool | Unset = UNSET
    remember_sorting: bool | Unset = UNSET
    sort_order: SortOrder | Unset = UNSET
    show_sidebar: bool | Unset = UNSET
    client: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        view_type: None | str | Unset
        if isinstance(self.view_type, Unset):
            view_type = UNSET
        else:
            view_type = self.view_type

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = self.sort_by

        index_by: None | str | Unset
        if isinstance(self.index_by, Unset):
            index_by = UNSET
        else:
            index_by = self.index_by

        remember_indexing = self.remember_indexing

        primary_image_height = self.primary_image_height

        primary_image_width = self.primary_image_width

        custom_prefs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_prefs, Unset):
            custom_prefs = self.custom_prefs.to_dict()

        scroll_direction: str | Unset = UNSET
        if not isinstance(self.scroll_direction, Unset):
            scroll_direction = self.scroll_direction.value

        show_backdrop = self.show_backdrop

        remember_sorting = self.remember_sorting

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        show_sidebar = self.show_sidebar

        client: None | str | Unset
        if isinstance(self.client, Unset):
            client = UNSET
        else:
            client = self.client

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if view_type is not UNSET:
            field_dict["ViewType"] = view_type
        if sort_by is not UNSET:
            field_dict["SortBy"] = sort_by
        if index_by is not UNSET:
            field_dict["IndexBy"] = index_by
        if remember_indexing is not UNSET:
            field_dict["RememberIndexing"] = remember_indexing
        if primary_image_height is not UNSET:
            field_dict["PrimaryImageHeight"] = primary_image_height
        if primary_image_width is not UNSET:
            field_dict["PrimaryImageWidth"] = primary_image_width
        if custom_prefs is not UNSET:
            field_dict["CustomPrefs"] = custom_prefs
        if scroll_direction is not UNSET:
            field_dict["ScrollDirection"] = scroll_direction
        if show_backdrop is not UNSET:
            field_dict["ShowBackdrop"] = show_backdrop
        if remember_sorting is not UNSET:
            field_dict["RememberSorting"] = remember_sorting
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if show_sidebar is not UNSET:
            field_dict["ShowSidebar"] = show_sidebar
        if client is not UNSET:
            field_dict["Client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.display_preferences_dto_custom_prefs import (
            DisplayPreferencesDtoCustomPrefs,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_view_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_type = _parse_view_type(d.pop("ViewType", UNSET))

        def _parse_sort_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sort_by = _parse_sort_by(d.pop("SortBy", UNSET))

        def _parse_index_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        index_by = _parse_index_by(d.pop("IndexBy", UNSET))

        remember_indexing = d.pop("RememberIndexing", UNSET)

        primary_image_height = d.pop("PrimaryImageHeight", UNSET)

        primary_image_width = d.pop("PrimaryImageWidth", UNSET)

        _custom_prefs = d.pop("CustomPrefs", UNSET)
        custom_prefs: DisplayPreferencesDtoCustomPrefs | Unset
        if isinstance(_custom_prefs, Unset):
            custom_prefs = UNSET
        else:
            custom_prefs = DisplayPreferencesDtoCustomPrefs.from_dict(_custom_prefs)

        _scroll_direction = d.pop("ScrollDirection", UNSET)
        scroll_direction: ScrollDirection | Unset
        if isinstance(_scroll_direction, Unset):
            scroll_direction = UNSET
        else:
            scroll_direction = ScrollDirection(_scroll_direction)

        show_backdrop = d.pop("ShowBackdrop", UNSET)

        remember_sorting = d.pop("RememberSorting", UNSET)

        _sort_order = d.pop("SortOrder", UNSET)
        sort_order: SortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrder(_sort_order)

        show_sidebar = d.pop("ShowSidebar", UNSET)

        def _parse_client(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client = _parse_client(d.pop("Client", UNSET))

        display_preferences_dto = cls(
            id=id,
            view_type=view_type,
            sort_by=sort_by,
            index_by=index_by,
            remember_indexing=remember_indexing,
            primary_image_height=primary_image_height,
            primary_image_width=primary_image_width,
            custom_prefs=custom_prefs,
            scroll_direction=scroll_direction,
            show_backdrop=show_backdrop,
            remember_sorting=remember_sorting,
            sort_order=sort_order,
            show_sidebar=show_sidebar,
            client=client,
        )

        return display_preferences_dto
