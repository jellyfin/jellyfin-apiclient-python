from enum import Enum


class HardwareAccelerationType(str, Enum):
    AMF = "amf"
    NONE = "none"
    NVENC = "nvenc"
    QSV = "qsv"
    RKMPP = "rkmpp"
    V4L2M2M = "v4l2m2m"
    VAAPI = "vaapi"
    VIDEOTOOLBOX = "videotoolbox"

    def __str__(self) -> str:
        return str(self.value)
