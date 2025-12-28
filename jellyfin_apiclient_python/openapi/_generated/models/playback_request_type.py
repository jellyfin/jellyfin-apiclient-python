from enum import Enum


class PlaybackRequestType(str, Enum):
    BUFFER = "Buffer"
    IGNOREWAIT = "IgnoreWait"
    MOVEPLAYLISTITEM = "MovePlaylistItem"
    NEXTITEM = "NextItem"
    PAUSE = "Pause"
    PING = "Ping"
    PLAY = "Play"
    PREVIOUSITEM = "PreviousItem"
    QUEUE = "Queue"
    READY = "Ready"
    REMOVEFROMPLAYLIST = "RemoveFromPlaylist"
    SEEK = "Seek"
    SETPLAYLISTITEM = "SetPlaylistItem"
    SETREPEATMODE = "SetRepeatMode"
    SETSHUFFLEMODE = "SetShuffleMode"
    STOP = "Stop"
    UNPAUSE = "Unpause"

    def __str__(self) -> str:
        return str(self.value)
