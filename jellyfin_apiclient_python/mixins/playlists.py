"""Holds functions for playlist API functionality."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Dict
from uuid import UUID

from ..constants import MediaType, HTTPAction, ItemFields, ImageType
from ..types import ListResponse, MediaItemData

if TYPE_CHECKING:
    from ..api import API

@dataclass
class PlaylistUserPermissions:
    """Holds permission data for a playlist on per-user-basis."""
    def __init__(self, user_id: UUID, can_edit: bool = False):
        self.user_id = user_id
        self.can_edit = can_edit

    user_id: UUID | None = None
    can_edit: bool = False

    def __dict__(self):
        return {
            'UserId': self.user_id,
            'CanEdit': self.can_edit,
        }

class PlaylistMixin:
    def playlists_list_all(self: 'API') -> ListResponse[MediaItemData]:
        """
        Retrieve a list of all playlists.
        Returns:
            All Playlists on the plex instance.
        """
        params = {
            'IncludeItemTypes': 'Playlist',  # Retrieve only playlists
            'Recursive': 'true',  # Include nested playlists
        }

        return ListResponse[MediaItemData](self.items(params=params), MediaItemData)

    def playlist_create(self: 'API', name: str, ids: List[UUID], user_id: Optional[UUID],
                        media_type: Optional[MediaType] = None,
                        users: Optional[List[PlaylistUserPermissions]] = None,
                        is_public: Optional[bool] = None) -> UUID:
        """
        Creates a new playlist with the specified name
        Args:
            name: Name of the playlist
            ids: ids of the items to add to the playlist
            user_id: id of the owner
            media_type: type of media for the playlist
            users: permissions for other users.
            is_public: if the playlist is public

        Returns:
            200: Created, returns the id of the newly created playlist.

        Raises:
            401: Unauthorized
            403: Forbidden

        References:
            .. [CreatePlaylist] https://api.jellyfin.org/#tag/Playlists/operation/CreatePlaylist
        """
        json_data = {
            'Name': name,
            'IDs': ids,
            **({'UserID': user_id} if user_id else {}),
            **({'MediaType': media_type} if media_type else {}),
            **({'Users': [user.__dict__() for user in users]} if users else {}),
            **({'IsPublic': is_public} if is_public is not None else {}),
        }
        return UUID(self.playlists(HTTPAction.POST, json_data=json_data).get('Id'))

    def playlist_delete(self: 'API', playlist_id: UUID) -> None:
        """
        Deletes the playlist with the provided id.
        Args:
            playlist_id: Playlist id to delete.

        Returns:
            None on success.

        Raises:
            unknown

        References:
            No documentation found...

        """
        return self.items(f"/{playlist_id}", HTTPAction.DELETE.value)

    def playlist_update(self: 'API', playlist_id = UUID, name: Optional[str] = None,
                        ids: Optional[List[UUID]] = None,
                        users: Optional[List[PlaylistUserPermissions]] = None,
                        is_public: Optional[bool] = None) -> None:
        """
        Updates the provided parts of the playlist. When updating the items all (old and new items) must be provided. Omitted items won't be updated.
        Args:
            playlist_id: Id of the playlist to modify
            name: New name of the playlist
            ids: list of the items in the playlist
            users: updated permissions for other users.
            is_public: updates weather the paylist is public.

        Returns:
            None on success

        Raises:
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        Todo:
            - Verify assumption on replacement.

        References:
            .. [UpdatePlaylist] https://api.jellyfin.org/#tag/Playlists/operation/UpdatePlaylist
        """
        json_data = {
            **({'Name': name} if name is not None else {}),
            **({'IDs': ids} if ids is not None else {}),
            **({'Users': [user.__dict__() for user in users]} if users is not None else {
                'Users': []}),
            **({'IsPublic': is_public} if is_public is not None else {})
        }

        return self.playlists(HTTPAction.POST, path=f"{playlist_id}", json_data=json_data if json_data != {} else None)


    def playlist_get(self: 'API', playlist_id: UUID):
        """
        Returns information about the specified playlist.
        Args:
            playlist_id: The if of the playlist to retrieve.

        Returns:
            200: The playlist. todo
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [GetPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/GetPlaylist
        """
        return self.playlists(HTTPAction.GET, path=f"{playlist_id}")

    def playlist_add_item(self: 'API', playlist_id: UUID, user_id: UUID, ids: List[UUID]) -> Dict:
        """
        Adds new items to the playlist.
        Args:
            playlist_id: The playlist to modify
            user_id: user id which triggers the modification - todo: check if this is true
            ids: elements to add.

        Returns:
            204: Playlist updated.
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [AddItemToPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/AddItemToPlaylist
        """
        json_data = {
            'Ids': ids,
            'UserID': user_id,
        }
        return self.playlists(HTTPAction.POST, path=f"{playlist_id}/Items", json_data=json_data)

    def playlist_remove_item(self: 'API', playlist_id: UUID, ids: List[UUID]) -> Dict:
        """
        Removes items from the playlist.
        Args:
            playlist_id: The playlist to modify
            ids: elements to remove

        Returns:
            204: Playlist updated.
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [RemoveItemFromPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/RemoveItemFromPlaylist
        """
        json_data = {
            'EntryIds': ids  # yes. This does not match the others. Check the doc :(
        }
        return self.playlists(HTTPAction.DELETE, path=f"{playlist_id}/Items", json_data=json_data)

    def playlist_get_items(
            self: 'API', playlist_id: UUID,
            user_id: Optional[UUID] = None, start_index: Optional[int] = None,
            limit: Optional[int] = None,
            fields: Optional[List[ItemFields]] = None,
            enable_images: Optional[bool] = None,
            enable_user_data: Optional[bool] = None,
            image_type_limit: Optional[int] = None,
            enable_image_types: Optional[List[ImageType]] = None
    ) -> ListResponse[MediaItemData]:
        """
        Returns the items in the specified playlist.
        Args:
            playlist_id: id of the playlist to retrieve information for.
            user_id: id of the user that executes the operation. todo: really?
            start_index: The index of the first item to be returned. For pagination with limit.
            limit: Maximum number of elements to return.
            fields: Which fields are to included.
            enable_images: If to include image data.
            enable_user_data: If to include user data.
            image_type_limit: maximum number of images to return per image type.
            enable_image_types: The image types to include in the output.

        Returns:
            200: Playlist Data
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [GetPlaylistItems] https://api.jellyfin.org/#tag/Playlists/operation/GetPlaylistItems
        """
        json_data = {
            'UserId': str(user_id),
            **({'StartIndex': str(start_index)} if start_index is not None else {}),
            **({'Limit': str(limit)} if limit is not None else {}),
            **({'Fields': str([str(field) for field in fields])} if fields is not None else {}),
            **({'EnableImages': str(enable_images)} if enable_images is not None else {}),
            **({'EnableUserData': str(enable_user_data)} if enable_user_data is not None else {}),
            **({'ImageTypeLimit': str(image_type_limit)} if image_type_limit is not None else {}),
            **({'EnableImageTypes': str([str(img_type) for img_type in
                                         enable_image_types])} if enable_image_types is not None else {})
        }

        return ListResponse[MediaItemData](self.playlists(HTTPAction.GET, path=f"{playlist_id}/Items", json_data=json_data), MediaItemData)


    def playlist_move_item(self: 'API', playlist_id: UUID, item_id: UUID, new_index: int):
        """
        Moves the item in the playlist to the specified index.
        Args:
            playlist_id: The playlist to modify
            item_id: The item to move
            new_index: The new index of the item

        Returns:
            204: Item moved
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [MoveItem] https://api.jellyfin.org/#tag/Playlists/operation/MoveItem
        """
        return self.playlists(HTTPAction.POST, path=f"{playlist_id}/Items/{item_id}/Move/{new_index}")


    def playlist_get_user_permissions(self: 'API', playlist_id: UUID) -> List[PlaylistUserPermissions]:
        """
        Returns information on the users permission to the playlist.
        Args:
            playlist_id: The playlist to retrieve information for.

        Returns:
            A list of permissions for users.
            200: User permuissions
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [GetPlaylistUsers] https://api.jellyfin.org/#tag/Playlists/operation/GetPlaylistUsers
        """
        return self.playlists(HTTPAction.GET, path=f"{playlist_id}/Users")

    def playlist_get_single_user_permission(self: 'API', playlist_id: UUID, user_id: UUID) -> PlaylistUserPermissions:
        """
        Returns the permissions for a single user.
        Args:
            playlist_id: The playlist to retrieve information for.
            user_id: The id of the user to retrieve information for.

        Returns:
            The permissions for a single user.
            200: User permissions
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [GetPlaylistUser] https://api.jellyfin.org/#tag/Playlists/operation/GetPlaylistUser
        """
        return self.playlists(HTTPAction.GET, path=f"{playlist_id}/Users/{user_id}")

    def playlist_update_user_permission(self: 'API', playlist_id: UUID, user_id: UUID, can_edit: bool) -> None:
        """
        Updates the permissions for a single user.
        Args:
            playlist_id: The playlist to update
            user_id: The user to update
            can_edit: Updates if the user can edit or not

        Returns:
            None on success

        Raises:
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [UpdatePlaylistUser] https://api.jellyfin.org/#tag/Playlists/operation/UpdatePlaylistUser
        """
        json_data = {
            'CanEdit': can_edit
        }
        return self.playlists(HTTPAction.POST, path=f"{playlist_id}/Users/{user_id}", json_data=json_data)

    def playlist_remove_user_permission(self: 'API', playlist_id: UUID, user_id: UUID):
        """
        Removes the permission for a single user.
        Args:
            playlist_id: The playlist to update
            user_id: The user to update

        Returns:
            None on success

        Raises:
            401: Unauthorized
            403: Forbidden
            404: Playlist not found

        References:
            .. [RemoveUserFromPlaylist] https://api.jellyfin.org/#tag/Playlists/operation/RemoveUserFromPlaylist
        """

