from enum import Enum


class TonemappingMode(str, Enum):
    AUTO = "auto"
    ITP = "itp"
    LUM = "lum"
    MAX = "max"
    RGB = "rgb"

    def __str__(self) -> str:
        return str(self.value)
