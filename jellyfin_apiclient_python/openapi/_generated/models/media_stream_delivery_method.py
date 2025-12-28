from enum import Enum


class MediaStreamDeliveryMethod(str, Enum):
    DROP = "Drop"
    EMBED = "Embed"
    ENCODE = "Encode"
    EXTERNAL = "External"
    HLS = "Hls"

    def __str__(self) -> str:
        return str(self.value)
