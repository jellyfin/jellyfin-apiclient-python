from enum import Enum


class ChannelMediaContentType(str, Enum):
    CLIP = "Clip"
    EPISODE = "Episode"
    MOVIE = "Movie"
    MOVIEEXTRA = "MovieExtra"
    PODCAST = "Podcast"
    SONG = "Song"
    TRAILER = "Trailer"
    TVEXTRA = "TvExtra"

    def __str__(self) -> str:
        return str(self.value)
