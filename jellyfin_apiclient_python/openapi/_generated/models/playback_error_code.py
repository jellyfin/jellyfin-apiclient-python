from enum import Enum


class PlaybackErrorCode(str, Enum):
    NOCOMPATIBLESTREAM = "NoCompatibleStream"
    NOTALLOWED = "NotAllowed"
    RATELIMITEXCEEDED = "RateLimitExceeded"

    def __str__(self) -> str:
        return str(self.value)
