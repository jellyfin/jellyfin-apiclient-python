from enum import Enum


class MetadataRefreshMode(str, Enum):
    DEFAULT = "Default"
    FULLREFRESH = "FullRefresh"
    NONE = "None"
    VALIDATIONONLY = "ValidationOnly"

    def __str__(self) -> str:
        return str(self.value)
