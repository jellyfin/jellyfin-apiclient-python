from enum import Enum


class MetadataField(str, Enum):
    CAST = "Cast"
    GENRES = "Genres"
    NAME = "Name"
    OFFICIALRATING = "OfficialRating"
    OVERVIEW = "Overview"
    PRODUCTIONLOCATIONS = "ProductionLocations"
    RUNTIME = "Runtime"
    STUDIOS = "Studios"
    TAGS = "Tags"

    def __str__(self) -> str:
        return str(self.value)
