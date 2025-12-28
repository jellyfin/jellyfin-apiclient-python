from enum import Enum


class MediaSourceType(str, Enum):
    DEFAULT = "Default"
    GROUPING = "Grouping"
    PLACEHOLDER = "Placeholder"

    def __str__(self) -> str:
        return str(self.value)
