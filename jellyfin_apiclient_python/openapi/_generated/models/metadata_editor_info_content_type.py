from enum import Enum


class MetadataEditorInfoContentType(str, Enum):
    BOOKS = "books"
    BOXSETS = "boxsets"
    FOLDERS = "folders"
    HOMEVIDEOS = "homevideos"
    LIVETV = "livetv"
    MOVIES = "movies"
    MUSIC = "music"
    MUSICVIDEOS = "musicvideos"
    PHOTOS = "photos"
    PLAYLISTS = "playlists"
    TRAILERS = "trailers"
    TVSHOWS = "tvshows"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
