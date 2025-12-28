from enum import Enum


class MediaStreamType(str, Enum):
    AUDIO = "Audio"
    DATA = "Data"
    EMBEDDEDIMAGE = "EmbeddedImage"
    LYRIC = "Lyric"
    SUBTITLE = "Subtitle"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
