from enum import Enum


class GroupRepeatMode(str, Enum):
    REPEATALL = "RepeatAll"
    REPEATNONE = "RepeatNone"
    REPEATONE = "RepeatOne"

    def __str__(self) -> str:
        return str(self.value)
