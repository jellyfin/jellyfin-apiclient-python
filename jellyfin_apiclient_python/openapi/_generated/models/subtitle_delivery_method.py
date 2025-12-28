from enum import Enum


class SubtitleDeliveryMethod(str, Enum):
    DROP = "Drop"
    EMBED = "Embed"
    ENCODE = "Encode"
    EXTERNAL = "External"
    HLS = "Hls"

    def __str__(self) -> str:
        return str(self.value)
