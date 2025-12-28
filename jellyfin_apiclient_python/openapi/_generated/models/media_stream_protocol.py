from enum import Enum


class MediaStreamProtocol(str, Enum):
    HLS = "hls"
    HTTP = "http"

    def __str__(self) -> str:
        return str(self.value)
