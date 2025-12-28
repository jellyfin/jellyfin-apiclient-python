from enum import Enum


class PlayQueueUpdateReason(str, Enum):
    MOVEITEM = "MoveItem"
    NEWPLAYLIST = "NewPlaylist"
    NEXTITEM = "NextItem"
    PREVIOUSITEM = "PreviousItem"
    QUEUE = "Queue"
    QUEUENEXT = "QueueNext"
    REMOVEITEMS = "RemoveItems"
    REPEATMODE = "RepeatMode"
    SETCURRENTITEM = "SetCurrentItem"
    SHUFFLEMODE = "ShuffleMode"

    def __str__(self) -> str:
        return str(self.value)
