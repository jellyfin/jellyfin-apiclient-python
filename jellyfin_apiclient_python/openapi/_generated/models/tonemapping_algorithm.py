from enum import Enum


class TonemappingAlgorithm(str, Enum):
    BT2390 = "bt2390"
    CLIP = "clip"
    GAMMA = "gamma"
    HABLE = "hable"
    LINEAR = "linear"
    MOBIUS = "mobius"
    NONE = "none"
    REINHARD = "reinhard"

    def __str__(self) -> str:
        return str(self.value)
