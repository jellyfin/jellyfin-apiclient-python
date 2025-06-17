from enum import Enum

# from enum import StrEnum


class StrEnum(str, Enum):
    """
    Minimal string enum that works with Python 3.6+
    """
    def __str__(self):
        return self.value

    @classmethod
    def _missing_(cls, value):
        # Allow case-insensitive lookups
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        return None


class ItemType(StrEnum):
    AGGREGATE_FOLDER = "AggregateFolder"
    AUDIO = "Audio"
    AUDIO_BOOK = "AudioBook"
    BASE_PLUGIN_FOLDER = "BasePluginFolder"
    BOOK = "Book"
    BOX_SET = "BoxSet"
    CHANNEL = "Channel"
    CHANNEL_FOLDER_ITEM = "ChannelFolderItem"
    COLLECTION_FOLDER = "CollectionFolder"
    EPISODE = "Episode"
    FOLDER = "Folder"
    GENRE = "Genre"
    MANUAL_PLAYLISTS_FOLDER = "ManualPlaylistsFolder"
    MOVIE = "Movie"
    LIVE_TV_CHANNEL = "LiveTvChannel"
    LIVE_TV_PROGRAM = "LiveTvProgram"
    MUSIC_ALBUM = "MusicAlbum"
    MUSIC_ARTIST = "MusicArtist"
    MUSIC_GENRE = "MusicGenre"
    MUSIC_VIDEO = "MusicVideo"
    PERSON = "Person"
    PHOTO = "Photo"
    PHOTO_ALBUM = "PhotoAlbum"
    PLAYLIST = "Playlist"
    PLAYLISTS_FOLDER = "PlaylistsFolder"
    PROGRAM = "Program"
    RECORDING = "Recording"
    SEASON = "Season"
    SERIES = "Series"
    STUDIO = "Studio"
    TRAILER = "Trailer"
    TV_CHANNEL = "TvChannel"
    TV_PROGRAM = "TvProgram"
    USER_ROOT_FOLDER = "UserRootFolder"
    USER_VIEW = "UserView"
    VIDEO = "Video"
    YEAR = "Year"


class ImageType(StrEnum):
    PRIMARY = "Primary"
    ART = "Art"
    BACKDROP = "Backdrop"
    BANNER = "Banner"
    LOGO = "Logo"
    THUMB = "Thumb"
    DISC = "Disc"
    BOX = "Box"
    SCREENSHOT = "Screenshot"
    MENU = "Menu"
    CHAPTER = "Chapter"
    BOXREAR = "BoxRear"
    PROFILE = "Profile"
