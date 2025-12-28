from enum import Enum


class ChannelItemSortField(str, Enum):
    COMMUNITYPLAYCOUNT = "CommunityPlayCount"
    COMMUNITYRATING = "CommunityRating"
    DATECREATED = "DateCreated"
    NAME = "Name"
    PLAYCOUNT = "PlayCount"
    PREMIEREDATE = "PremiereDate"
    RUNTIME = "Runtime"

    def __str__(self) -> str:
        return str(self.value)
