from enum import Enum


class MediaType(str, Enum):
    AUDIO = "Audio"
    BOOK = "Book"
    PHOTO = "Photo"
    UNKNOWN = "Unknown"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
