from enum import Enum


class SubtitlePlaybackMode(str, Enum):
    ALWAYS = "Always"
    DEFAULT = "Default"
    NONE = "None"
    ONLYFORCED = "OnlyForced"
    SMART = "Smart"

    def __str__(self) -> str:
        return str(self.value)
