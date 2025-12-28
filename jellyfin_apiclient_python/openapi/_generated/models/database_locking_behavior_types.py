from enum import Enum


class DatabaseLockingBehaviorTypes(str, Enum):
    NOLOCK = "NoLock"
    OPTIMISTIC = "Optimistic"
    PESSIMISTIC = "Pessimistic"

    def __str__(self) -> str:
        return str(self.value)
