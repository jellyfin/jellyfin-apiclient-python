from enum import Enum


class FileSystemEntryType(str, Enum):
    DIRECTORY = "Directory"
    FILE = "File"
    NETWORKCOMPUTER = "NetworkComputer"
    NETWORKSHARE = "NetworkShare"

    def __str__(self) -> str:
        return str(self.value)
