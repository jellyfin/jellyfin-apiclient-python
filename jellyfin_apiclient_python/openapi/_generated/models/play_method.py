from enum import Enum


class PlayMethod(str, Enum):
    DIRECTPLAY = "DirectPlay"
    DIRECTSTREAM = "DirectStream"
    TRANSCODE = "Transcode"

    def __str__(self) -> str:
        return str(self.value)
