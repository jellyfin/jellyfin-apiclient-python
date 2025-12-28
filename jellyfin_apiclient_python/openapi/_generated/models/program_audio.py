from enum import Enum


class ProgramAudio(str, Enum):
    ATMOS = "Atmos"
    DOLBY = "Dolby"
    DOLBYDIGITAL = "DolbyDigital"
    MONO = "Mono"
    STEREO = "Stereo"
    THX = "Thx"

    def __str__(self) -> str:
        return str(self.value)
