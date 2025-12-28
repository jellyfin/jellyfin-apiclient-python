from enum import Enum


class RecommendationType(str, Enum):
    HASACTORFROMRECENTLYPLAYED = "HasActorFromRecentlyPlayed"
    HASDIRECTORFROMRECENTLYPLAYED = "HasDirectorFromRecentlyPlayed"
    HASLIKEDACTOR = "HasLikedActor"
    HASLIKEDDIRECTOR = "HasLikedDirector"
    SIMILARTOLIKEDITEM = "SimilarToLikedItem"
    SIMILARTORECENTLYPLAYED = "SimilarToRecentlyPlayed"

    def __str__(self) -> str:
        return str(self.value)
