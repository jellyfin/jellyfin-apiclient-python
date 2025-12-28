from enum import Enum


class ItemFilter(str, Enum):
    DISLIKES = "Dislikes"
    ISFAVORITE = "IsFavorite"
    ISFAVORITEORLIKES = "IsFavoriteOrLikes"
    ISFOLDER = "IsFolder"
    ISNOTFOLDER = "IsNotFolder"
    ISPLAYED = "IsPlayed"
    ISRESUMABLE = "IsResumable"
    ISUNPLAYED = "IsUnplayed"
    LIKES = "Likes"

    def __str__(self) -> str:
        return str(self.value)
