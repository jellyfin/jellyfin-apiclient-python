from enum import Enum


class SeriesStatus(str, Enum):
    CONTINUING = "Continuing"
    ENDED = "Ended"
    UNRELEASED = "Unreleased"

    def __str__(self) -> str:
        return str(self.value)
