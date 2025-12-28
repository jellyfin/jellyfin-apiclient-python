from enum import Enum


class ChannelMediaType(str, Enum):
    AUDIO = "Audio"
    PHOTO = "Photo"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
