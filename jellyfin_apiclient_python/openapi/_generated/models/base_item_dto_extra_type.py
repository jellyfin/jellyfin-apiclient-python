from enum import Enum


class BaseItemDtoExtraType(str, Enum):
    BEHINDTHESCENES = "BehindTheScenes"
    CLIP = "Clip"
    DELETEDSCENE = "DeletedScene"
    FEATURETTE = "Featurette"
    INTERVIEW = "Interview"
    SAMPLE = "Sample"
    SCENE = "Scene"
    SHORT = "Short"
    THEMESONG = "ThemeSong"
    THEMEVIDEO = "ThemeVideo"
    TRAILER = "Trailer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
