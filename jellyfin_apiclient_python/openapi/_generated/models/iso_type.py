from enum import Enum


class IsoType(str, Enum):
    BLURAY = "BluRay"
    DVD = "Dvd"

    def __str__(self) -> str:
        return str(self.value)
