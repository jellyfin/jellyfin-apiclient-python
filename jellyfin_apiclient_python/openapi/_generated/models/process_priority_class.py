from enum import Enum


class ProcessPriorityClass(str, Enum):
    ABOVENORMAL = "AboveNormal"
    BELOWNORMAL = "BelowNormal"
    HIGH = "High"
    IDLE = "Idle"
    NORMAL = "Normal"
    REALTIME = "RealTime"

    def __str__(self) -> str:
        return str(self.value)
