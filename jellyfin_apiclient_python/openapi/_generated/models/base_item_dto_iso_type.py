from enum import Enum


class BaseItemDtoIsoType(str, Enum):
    BLURAY = "BluRay"
    DVD = "Dvd"

    def __str__(self) -> str:
        return str(self.value)
