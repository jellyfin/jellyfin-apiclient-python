from enum import Enum


class BaseItemDtoChannelType(str, Enum):
    RADIO = "Radio"
    TV = "TV"

    def __str__(self) -> str:
        return str(self.value)
