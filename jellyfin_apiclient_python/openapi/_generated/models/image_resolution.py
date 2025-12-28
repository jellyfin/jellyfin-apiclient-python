from enum import Enum


class ImageResolution(str, Enum):
    MATCHSOURCE = "MatchSource"
    P1080 = "P1080"
    P144 = "P144"
    P1440 = "P1440"
    P2160 = "P2160"
    P240 = "P240"
    P360 = "P360"
    P480 = "P480"
    P720 = "P720"

    def __str__(self) -> str:
        return str(self.value)
