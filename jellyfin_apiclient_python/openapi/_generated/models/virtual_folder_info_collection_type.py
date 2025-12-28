from enum import Enum


class VirtualFolderInfoCollectionType(str, Enum):
    BOOKS = "books"
    BOXSETS = "boxsets"
    HOMEVIDEOS = "homevideos"
    MIXED = "mixed"
    MOVIES = "movies"
    MUSIC = "music"
    MUSICVIDEOS = "musicvideos"
    TVSHOWS = "tvshows"

    def __str__(self) -> str:
        return str(self.value)
