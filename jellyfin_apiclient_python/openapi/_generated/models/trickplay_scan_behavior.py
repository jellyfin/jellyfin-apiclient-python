from enum import Enum


class TrickplayScanBehavior(str, Enum):
    BLOCKING = "Blocking"
    NONBLOCKING = "NonBlocking"

    def __str__(self) -> str:
        return str(self.value)
