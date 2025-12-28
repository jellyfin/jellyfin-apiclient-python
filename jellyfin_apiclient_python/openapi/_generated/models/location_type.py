from enum import Enum


class LocationType(str, Enum):
    FILESYSTEM = "FileSystem"
    OFFLINE = "Offline"
    REMOTE = "Remote"
    VIRTUAL = "Virtual"

    def __str__(self) -> str:
        return str(self.value)
