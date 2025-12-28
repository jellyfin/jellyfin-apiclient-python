from enum import Enum


class GroupQueueMode(str, Enum):
    QUEUE = "Queue"
    QUEUENEXT = "QueueNext"

    def __str__(self) -> str:
        return str(self.value)
