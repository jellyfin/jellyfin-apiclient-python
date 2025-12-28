from enum import Enum


class UnratedItem(str, Enum):
    BOOK = "Book"
    CHANNELCONTENT = "ChannelContent"
    LIVETVCHANNEL = "LiveTvChannel"
    LIVETVPROGRAM = "LiveTvProgram"
    MOVIE = "Movie"
    MUSIC = "Music"
    OTHER = "Other"
    SERIES = "Series"
    TRAILER = "Trailer"

    def __str__(self) -> str:
        return str(self.value)
