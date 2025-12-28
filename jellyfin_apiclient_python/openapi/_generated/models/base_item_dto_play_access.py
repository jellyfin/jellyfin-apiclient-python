from enum import Enum


class BaseItemDtoPlayAccess(str, Enum):
    FULL = "Full"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
