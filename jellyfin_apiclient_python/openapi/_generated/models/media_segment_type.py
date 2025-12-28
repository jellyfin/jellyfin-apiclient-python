from enum import Enum


class MediaSegmentType(str, Enum):
    COMMERCIAL = "Commercial"
    INTRO = "Intro"
    OUTRO = "Outro"
    PREVIEW = "Preview"
    RECAP = "Recap"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
