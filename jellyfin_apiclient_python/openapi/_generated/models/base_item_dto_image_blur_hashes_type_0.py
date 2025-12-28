from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto_image_blur_hashes_type_0_art import (
        BaseItemDtoImageBlurHashesType0Art,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_backdrop import (
        BaseItemDtoImageBlurHashesType0Backdrop,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_banner import (
        BaseItemDtoImageBlurHashesType0Banner,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_box import (
        BaseItemDtoImageBlurHashesType0Box,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_box_rear import (
        BaseItemDtoImageBlurHashesType0BoxRear,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_chapter import (
        BaseItemDtoImageBlurHashesType0Chapter,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_disc import (
        BaseItemDtoImageBlurHashesType0Disc,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_logo import (
        BaseItemDtoImageBlurHashesType0Logo,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_menu import (
        BaseItemDtoImageBlurHashesType0Menu,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_primary import (
        BaseItemDtoImageBlurHashesType0Primary,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_profile import (
        BaseItemDtoImageBlurHashesType0Profile,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_screenshot import (
        BaseItemDtoImageBlurHashesType0Screenshot,
    )
    from ..models.base_item_dto_image_blur_hashes_type_0_thumb import (
        BaseItemDtoImageBlurHashesType0Thumb,
    )


T = TypeVar("T", bound="BaseItemDtoImageBlurHashesType0")


@_attrs_define
class BaseItemDtoImageBlurHashesType0:
    """Gets or sets the blurhashes for the image tags.
    Maps image type to dictionary mapping image tag to blurhash value.

        Attributes:
            primary (BaseItemDtoImageBlurHashesType0Primary | Unset):
            art (BaseItemDtoImageBlurHashesType0Art | Unset):
            backdrop (BaseItemDtoImageBlurHashesType0Backdrop | Unset):
            banner (BaseItemDtoImageBlurHashesType0Banner | Unset):
            logo (BaseItemDtoImageBlurHashesType0Logo | Unset):
            thumb (BaseItemDtoImageBlurHashesType0Thumb | Unset):
            disc (BaseItemDtoImageBlurHashesType0Disc | Unset):
            box (BaseItemDtoImageBlurHashesType0Box | Unset):
            screenshot (BaseItemDtoImageBlurHashesType0Screenshot | Unset):
            menu (BaseItemDtoImageBlurHashesType0Menu | Unset):
            chapter (BaseItemDtoImageBlurHashesType0Chapter | Unset):
            box_rear (BaseItemDtoImageBlurHashesType0BoxRear | Unset):
            profile (BaseItemDtoImageBlurHashesType0Profile | Unset):
    """

    primary: BaseItemDtoImageBlurHashesType0Primary | Unset = UNSET
    art: BaseItemDtoImageBlurHashesType0Art | Unset = UNSET
    backdrop: BaseItemDtoImageBlurHashesType0Backdrop | Unset = UNSET
    banner: BaseItemDtoImageBlurHashesType0Banner | Unset = UNSET
    logo: BaseItemDtoImageBlurHashesType0Logo | Unset = UNSET
    thumb: BaseItemDtoImageBlurHashesType0Thumb | Unset = UNSET
    disc: BaseItemDtoImageBlurHashesType0Disc | Unset = UNSET
    box: BaseItemDtoImageBlurHashesType0Box | Unset = UNSET
    screenshot: BaseItemDtoImageBlurHashesType0Screenshot | Unset = UNSET
    menu: BaseItemDtoImageBlurHashesType0Menu | Unset = UNSET
    chapter: BaseItemDtoImageBlurHashesType0Chapter | Unset = UNSET
    box_rear: BaseItemDtoImageBlurHashesType0BoxRear | Unset = UNSET
    profile: BaseItemDtoImageBlurHashesType0Profile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict()

        art: dict[str, Any] | Unset = UNSET
        if not isinstance(self.art, Unset):
            art = self.art.to_dict()

        backdrop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backdrop, Unset):
            backdrop = self.backdrop.to_dict()

        banner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.banner, Unset):
            banner = self.banner.to_dict()

        logo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        thumb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumb, Unset):
            thumb = self.thumb.to_dict()

        disc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disc, Unset):
            disc = self.disc.to_dict()

        box: dict[str, Any] | Unset = UNSET
        if not isinstance(self.box, Unset):
            box = self.box.to_dict()

        screenshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        menu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.menu, Unset):
            menu = self.menu.to_dict()

        chapter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chapter, Unset):
            chapter = self.chapter.to_dict()

        box_rear: dict[str, Any] | Unset = UNSET
        if not isinstance(self.box_rear, Unset):
            box_rear = self.box_rear.to_dict()

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["Primary"] = primary
        if art is not UNSET:
            field_dict["Art"] = art
        if backdrop is not UNSET:
            field_dict["Backdrop"] = backdrop
        if banner is not UNSET:
            field_dict["Banner"] = banner
        if logo is not UNSET:
            field_dict["Logo"] = logo
        if thumb is not UNSET:
            field_dict["Thumb"] = thumb
        if disc is not UNSET:
            field_dict["Disc"] = disc
        if box is not UNSET:
            field_dict["Box"] = box
        if screenshot is not UNSET:
            field_dict["Screenshot"] = screenshot
        if menu is not UNSET:
            field_dict["Menu"] = menu
        if chapter is not UNSET:
            field_dict["Chapter"] = chapter
        if box_rear is not UNSET:
            field_dict["BoxRear"] = box_rear
        if profile is not UNSET:
            field_dict["Profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_item_dto_image_blur_hashes_type_0_art import (
            BaseItemDtoImageBlurHashesType0Art,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_backdrop import (
            BaseItemDtoImageBlurHashesType0Backdrop,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_banner import (
            BaseItemDtoImageBlurHashesType0Banner,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_box import (
            BaseItemDtoImageBlurHashesType0Box,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_box_rear import (
            BaseItemDtoImageBlurHashesType0BoxRear,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_chapter import (
            BaseItemDtoImageBlurHashesType0Chapter,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_disc import (
            BaseItemDtoImageBlurHashesType0Disc,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_logo import (
            BaseItemDtoImageBlurHashesType0Logo,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_menu import (
            BaseItemDtoImageBlurHashesType0Menu,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_primary import (
            BaseItemDtoImageBlurHashesType0Primary,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_profile import (
            BaseItemDtoImageBlurHashesType0Profile,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_screenshot import (
            BaseItemDtoImageBlurHashesType0Screenshot,
        )
        from ..models.base_item_dto_image_blur_hashes_type_0_thumb import (
            BaseItemDtoImageBlurHashesType0Thumb,
        )

        d = dict(src_dict)
        _primary = d.pop("Primary", UNSET)
        primary: BaseItemDtoImageBlurHashesType0Primary | Unset
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = BaseItemDtoImageBlurHashesType0Primary.from_dict(_primary)

        _art = d.pop("Art", UNSET)
        art: BaseItemDtoImageBlurHashesType0Art | Unset
        if isinstance(_art, Unset):
            art = UNSET
        else:
            art = BaseItemDtoImageBlurHashesType0Art.from_dict(_art)

        _backdrop = d.pop("Backdrop", UNSET)
        backdrop: BaseItemDtoImageBlurHashesType0Backdrop | Unset
        if isinstance(_backdrop, Unset):
            backdrop = UNSET
        else:
            backdrop = BaseItemDtoImageBlurHashesType0Backdrop.from_dict(_backdrop)

        _banner = d.pop("Banner", UNSET)
        banner: BaseItemDtoImageBlurHashesType0Banner | Unset
        if isinstance(_banner, Unset):
            banner = UNSET
        else:
            banner = BaseItemDtoImageBlurHashesType0Banner.from_dict(_banner)

        _logo = d.pop("Logo", UNSET)
        logo: BaseItemDtoImageBlurHashesType0Logo | Unset
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = BaseItemDtoImageBlurHashesType0Logo.from_dict(_logo)

        _thumb = d.pop("Thumb", UNSET)
        thumb: BaseItemDtoImageBlurHashesType0Thumb | Unset
        if isinstance(_thumb, Unset):
            thumb = UNSET
        else:
            thumb = BaseItemDtoImageBlurHashesType0Thumb.from_dict(_thumb)

        _disc = d.pop("Disc", UNSET)
        disc: BaseItemDtoImageBlurHashesType0Disc | Unset
        if isinstance(_disc, Unset):
            disc = UNSET
        else:
            disc = BaseItemDtoImageBlurHashesType0Disc.from_dict(_disc)

        _box = d.pop("Box", UNSET)
        box: BaseItemDtoImageBlurHashesType0Box | Unset
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = BaseItemDtoImageBlurHashesType0Box.from_dict(_box)

        _screenshot = d.pop("Screenshot", UNSET)
        screenshot: BaseItemDtoImageBlurHashesType0Screenshot | Unset
        if isinstance(_screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = BaseItemDtoImageBlurHashesType0Screenshot.from_dict(
                _screenshot
            )

        _menu = d.pop("Menu", UNSET)
        menu: BaseItemDtoImageBlurHashesType0Menu | Unset
        if isinstance(_menu, Unset):
            menu = UNSET
        else:
            menu = BaseItemDtoImageBlurHashesType0Menu.from_dict(_menu)

        _chapter = d.pop("Chapter", UNSET)
        chapter: BaseItemDtoImageBlurHashesType0Chapter | Unset
        if isinstance(_chapter, Unset):
            chapter = UNSET
        else:
            chapter = BaseItemDtoImageBlurHashesType0Chapter.from_dict(_chapter)

        _box_rear = d.pop("BoxRear", UNSET)
        box_rear: BaseItemDtoImageBlurHashesType0BoxRear | Unset
        if isinstance(_box_rear, Unset):
            box_rear = UNSET
        else:
            box_rear = BaseItemDtoImageBlurHashesType0BoxRear.from_dict(_box_rear)

        _profile = d.pop("Profile", UNSET)
        profile: BaseItemDtoImageBlurHashesType0Profile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = BaseItemDtoImageBlurHashesType0Profile.from_dict(_profile)

        base_item_dto_image_blur_hashes_type_0 = cls(
            primary=primary,
            art=art,
            backdrop=backdrop,
            banner=banner,
            logo=logo,
            thumb=thumb,
            disc=disc,
            box=box,
            screenshot=screenshot,
            menu=menu,
            chapter=chapter,
            box_rear=box_rear,
            profile=profile,
        )

        base_item_dto_image_blur_hashes_type_0.additional_properties = d
        return base_item_dto_image_blur_hashes_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
