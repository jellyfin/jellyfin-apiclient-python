from enum import Enum


class TranscodeSeekInfo(str, Enum):
    AUTO = "Auto"
    BYTES = "Bytes"

    def __str__(self) -> str:
        return str(self.value)
