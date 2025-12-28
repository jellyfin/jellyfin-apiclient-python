from enum import Enum


class RecordingStatus(str, Enum):
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    CONFLICTEDNOTOK = "ConflictedNotOk"
    CONFLICTEDOK = "ConflictedOk"
    ERROR = "Error"
    INPROGRESS = "InProgress"
    NEW = "New"

    def __str__(self) -> str:
        return str(self.value)
