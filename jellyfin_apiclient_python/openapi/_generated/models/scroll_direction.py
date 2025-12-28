from enum import Enum


class ScrollDirection(str, Enum):
    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"

    def __str__(self) -> str:
        return str(self.value)
