from enum import Enum


class PlaybackOrder(str, Enum):
    DEFAULT = "Default"
    SHUFFLE = "Shuffle"

    def __str__(self) -> str:
        return str(self.value)
