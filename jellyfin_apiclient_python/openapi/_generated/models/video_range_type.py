from enum import Enum


class VideoRangeType(str, Enum):
    DOVI = "DOVI"
    DOVIINVALID = "DOVIInvalid"
    DOVIWITHEL = "DOVIWithEL"
    DOVIWITHELHDR10PLUS = "DOVIWithELHDR10Plus"
    DOVIWITHHDR10 = "DOVIWithHDR10"
    DOVIWITHHDR10PLUS = "DOVIWithHDR10Plus"
    DOVIWITHHLG = "DOVIWithHLG"
    DOVIWITHSDR = "DOVIWithSDR"
    HDR10 = "HDR10"
    HDR10PLUS = "HDR10Plus"
    HLG = "HLG"
    SDR = "SDR"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
