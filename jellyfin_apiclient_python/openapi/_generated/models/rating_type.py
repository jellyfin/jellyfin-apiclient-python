from enum import Enum


class RatingType(str, Enum):
    LIKES = "Likes"
    SCORE = "Score"

    def __str__(self) -> str:
        return str(self.value)
