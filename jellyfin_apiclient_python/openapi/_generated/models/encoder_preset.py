from enum import Enum


class EncoderPreset(str, Enum):
    AUTO = "auto"
    FAST = "fast"
    FASTER = "faster"
    MEDIUM = "medium"
    PLACEBO = "placebo"
    SLOW = "slow"
    SLOWER = "slower"
    SUPERFAST = "superfast"
    ULTRAFAST = "ultrafast"
    VERYFAST = "veryfast"
    VERYSLOW = "veryslow"

    def __str__(self) -> str:
        return str(self.value)
