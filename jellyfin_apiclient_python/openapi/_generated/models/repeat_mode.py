from enum import Enum


class RepeatMode(str, Enum):
    REPEATALL = "RepeatAll"
    REPEATNONE = "RepeatNone"
    REPEATONE = "RepeatOne"

    def __str__(self) -> str:
        return str(self.value)
