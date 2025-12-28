from enum import Enum


class CodecType(str, Enum):
    AUDIO = "Audio"
    VIDEO = "Video"
    VIDEOAUDIO = "VideoAudio"

    def __str__(self) -> str:
        return str(self.value)
