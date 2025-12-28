from enum import Enum


class EncodingContext(str, Enum):
    STATIC = "Static"
    STREAMING = "Streaming"

    def __str__(self) -> str:
        return str(self.value)
