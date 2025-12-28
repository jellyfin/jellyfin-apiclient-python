from enum import Enum


class LiveTvServiceStatus(str, Enum):
    OK = "Ok"
    UNAVAILABLE = "Unavailable"

    def __str__(self) -> str:
        return str(self.value)
