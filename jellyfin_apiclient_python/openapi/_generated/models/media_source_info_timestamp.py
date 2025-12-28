from enum import Enum


class MediaSourceInfoTimestamp(str, Enum):
    NONE = "None"
    VALID = "Valid"
    ZERO = "Zero"

    def __str__(self) -> str:
        return str(self.value)
