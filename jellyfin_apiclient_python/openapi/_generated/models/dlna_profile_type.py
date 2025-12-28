from enum import Enum


class DlnaProfileType(str, Enum):
    AUDIO = "Audio"
    LYRIC = "Lyric"
    PHOTO = "Photo"
    SUBTITLE = "Subtitle"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
