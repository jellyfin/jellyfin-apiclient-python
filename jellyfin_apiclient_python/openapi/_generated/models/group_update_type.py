from enum import Enum


class GroupUpdateType(str, Enum):
    GROUPDOESNOTEXIST = "GroupDoesNotExist"
    GROUPJOINED = "GroupJoined"
    GROUPLEFT = "GroupLeft"
    LIBRARYACCESSDENIED = "LibraryAccessDenied"
    NOTINGROUP = "NotInGroup"
    PLAYQUEUE = "PlayQueue"
    STATEUPDATE = "StateUpdate"
    USERJOINED = "UserJoined"
    USERLEFT = "UserLeft"

    def __str__(self) -> str:
        return str(self.value)
