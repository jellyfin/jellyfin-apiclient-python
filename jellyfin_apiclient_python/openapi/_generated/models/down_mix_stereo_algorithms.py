from enum import Enum


class DownMixStereoAlgorithms(str, Enum):
    AC4 = "Ac4"
    DAVE750 = "Dave750"
    NIGHTMODEDIALOGUE = "NightmodeDialogue"
    NONE = "None"
    RFC7845 = "Rfc7845"

    def __str__(self) -> str:
        return str(self.value)
