from enum import Enum


class KeepUntil(str, Enum):
    UNTILDATE = "UntilDate"
    UNTILDELETED = "UntilDeleted"
    UNTILSPACENEEDED = "UntilSpaceNeeded"
    UNTILWATCHED = "UntilWatched"

    def __str__(self) -> str:
        return str(self.value)
