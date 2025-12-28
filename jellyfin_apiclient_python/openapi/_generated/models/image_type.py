from enum import Enum


class ImageType(str, Enum):
    ART = "Art"
    BACKDROP = "Backdrop"
    BANNER = "Banner"
    BOX = "Box"
    BOXREAR = "BoxRear"
    CHAPTER = "Chapter"
    DISC = "Disc"
    LOGO = "Logo"
    MENU = "Menu"
    PRIMARY = "Primary"
    PROFILE = "Profile"
    SCREENSHOT = "Screenshot"
    THUMB = "Thumb"

    def __str__(self) -> str:
        return str(self.value)
