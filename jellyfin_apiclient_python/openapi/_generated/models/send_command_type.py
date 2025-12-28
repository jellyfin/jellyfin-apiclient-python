from enum import Enum


class SendCommandType(str, Enum):
    PAUSE = "Pause"
    SEEK = "Seek"
    STOP = "Stop"
    UNPAUSE = "Unpause"

    def __str__(self) -> str:
        return str(self.value)
