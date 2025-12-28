from enum import Enum


class VideoRange(str, Enum):
    HDR = "HDR"
    SDR = "SDR"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
