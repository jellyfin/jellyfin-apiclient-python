from enum import Enum


class PlaystateCommand(str, Enum):
    FASTFORWARD = "FastForward"
    NEXTTRACK = "NextTrack"
    PAUSE = "Pause"
    PLAYPAUSE = "PlayPause"
    PREVIOUSTRACK = "PreviousTrack"
    REWIND = "Rewind"
    SEEK = "Seek"
    STOP = "Stop"
    UNPAUSE = "Unpause"

    def __str__(self) -> str:
        return str(self.value)
