from enum import Enum


class GroupShuffleMode(str, Enum):
    SHUFFLE = "Shuffle"
    SORTED = "Sorted"

    def __str__(self) -> str:
        return str(self.value)
