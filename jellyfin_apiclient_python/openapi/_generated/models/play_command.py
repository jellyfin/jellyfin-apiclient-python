from enum import Enum


class PlayCommand(str, Enum):
    PLAYINSTANTMIX = "PlayInstantMix"
    PLAYLAST = "PlayLast"
    PLAYNEXT = "PlayNext"
    PLAYNOW = "PlayNow"
    PLAYSHUFFLE = "PlayShuffle"

    def __str__(self) -> str:
        return str(self.value)
