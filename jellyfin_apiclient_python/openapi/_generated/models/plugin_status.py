from enum import Enum


class PluginStatus(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    DISABLED = "Disabled"
    MALFUNCTIONED = "Malfunctioned"
    NOTSUPPORTED = "NotSupported"
    RESTART = "Restart"
    SUPERCEDED = "Superceded"
    SUPERSEDED = "Superseded"

    def __str__(self) -> str:
        return str(self.value)
