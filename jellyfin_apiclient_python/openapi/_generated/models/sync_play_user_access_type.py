from enum import Enum


class SyncPlayUserAccessType(str, Enum):
    CREATEANDJOINGROUPS = "CreateAndJoinGroups"
    JOINGROUPS = "JoinGroups"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
