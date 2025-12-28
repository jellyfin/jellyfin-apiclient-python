from enum import Enum


class MediaSourceInfoVideo3DFormat(str, Enum):
    FULLSIDEBYSIDE = "FullSideBySide"
    FULLTOPANDBOTTOM = "FullTopAndBottom"
    HALFSIDEBYSIDE = "HalfSideBySide"
    HALFTOPANDBOTTOM = "HalfTopAndBottom"
    MVC = "MVC"

    def __str__(self) -> str:
        return str(self.value)
