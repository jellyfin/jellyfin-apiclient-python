from enum import Enum


class DeinterlaceMethod(str, Enum):
    BWDIF = "bwdif"
    YADIF = "yadif"

    def __str__(self) -> str:
        return str(self.value)
