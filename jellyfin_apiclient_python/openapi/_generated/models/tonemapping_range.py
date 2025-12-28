from enum import Enum


class TonemappingRange(str, Enum):
    AUTO = "auto"
    PC = "pc"
    TV = "tv"

    def __str__(self) -> str:
        return str(self.value)
