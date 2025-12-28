from enum import Enum


class LogLevel(str, Enum):
    CRITICAL = "Critical"
    DEBUG = "Debug"
    ERROR = "Error"
    INFORMATION = "Information"
    NONE = "None"
    TRACE = "Trace"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
