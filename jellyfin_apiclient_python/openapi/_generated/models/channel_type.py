from enum import Enum


class ChannelType(str, Enum):
    RADIO = "Radio"
    TV = "TV"

    def __str__(self) -> str:
        return str(self.value)
