from enum import Enum


class TaskState(str, Enum):
    CANCELLING = "Cancelling"
    IDLE = "Idle"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
