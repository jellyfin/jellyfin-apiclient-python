from enum import Enum


class MediaSourceInfoEncoderProtocol(str, Enum):
    FILE = "File"
    FTP = "Ftp"
    HTTP = "Http"
    RTMP = "Rtmp"
    RTP = "Rtp"
    RTSP = "Rtsp"
    UDP = "Udp"

    def __str__(self) -> str:
        return str(self.value)
