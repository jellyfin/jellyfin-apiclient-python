from enum import Enum


class GroupStateType(str, Enum):
    IDLE = "Idle"
    PAUSED = "Paused"
    PLAYING = "Playing"
    WAITING = "Waiting"

    def __str__(self) -> str:
        return str(self.value)
