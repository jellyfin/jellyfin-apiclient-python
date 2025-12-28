from enum import Enum


class ImageFormat(str, Enum):
    BMP = "Bmp"
    GIF = "Gif"
    JPG = "Jpg"
    PNG = "Png"
    SVG = "Svg"
    WEBP = "Webp"

    def __str__(self) -> str:
        return str(self.value)
