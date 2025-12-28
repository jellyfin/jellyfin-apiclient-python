from enum import Enum


class EmbeddedSubtitleOptions(str, Enum):
    ALLOWALL = "AllowAll"
    ALLOWIMAGE = "AllowImage"
    ALLOWNONE = "AllowNone"
    ALLOWTEXT = "AllowText"

    def __str__(self) -> str:
        return str(self.value)
