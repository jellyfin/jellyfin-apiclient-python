from enum import Enum


class TransportStreamTimestamp(str, Enum):
    NONE = "None"
    VALID = "Valid"
    ZERO = "Zero"

    def __str__(self) -> str:
        return str(self.value)
