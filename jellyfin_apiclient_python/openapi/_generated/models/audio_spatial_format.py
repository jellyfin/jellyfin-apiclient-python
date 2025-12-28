from enum import Enum


class AudioSpatialFormat(str, Enum):
    DOLBYATMOS = "DolbyAtmos"
    DTSX = "DTSX"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
