from enum import Enum


class MediaSourceInfoVideoType(str, Enum):
    BLURAY = "BluRay"
    DVD = "Dvd"
    ISO = "Iso"
    VIDEOFILE = "VideoFile"

    def __str__(self) -> str:
        return str(self.value)
