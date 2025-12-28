from enum import Enum


class PersonKind(str, Enum):
    ACTOR = "Actor"
    ALBUMARTIST = "AlbumArtist"
    ARRANGER = "Arranger"
    ARTIST = "Artist"
    AUTHOR = "Author"
    COLORIST = "Colorist"
    COMPOSER = "Composer"
    CONDUCTOR = "Conductor"
    COVERARTIST = "CoverArtist"
    CREATOR = "Creator"
    DIRECTOR = "Director"
    EDITOR = "Editor"
    ENGINEER = "Engineer"
    GUESTSTAR = "GuestStar"
    ILLUSTRATOR = "Illustrator"
    INKER = "Inker"
    LETTERER = "Letterer"
    LYRICIST = "Lyricist"
    MIXER = "Mixer"
    PENCILLER = "Penciller"
    PRODUCER = "Producer"
    REMIXER = "Remixer"
    TRANSLATOR = "Translator"
    UNKNOWN = "Unknown"
    WRITER = "Writer"

    def __str__(self) -> str:
        return str(self.value)
