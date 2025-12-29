Legacy API migration guide
==========================

This guide maps every public helper in ``jellyfin_apiclient_python.api.API``
to the equivalent call exposed by the OpenAPI-based convenience wrapper in
``jellyfin_apiclient_python.openapi.client``.  The rightmost column shows the
``Jellyfin`` helper you can call after creating and authenticating the wrapper
instance (``jf = Jellyfin(...).login()``).  Unless noted otherwise, calls return
the ``Response`` object from the generated client; append ``.parsed`` to access
model instances.

Authentication and utility
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``try_server``
     - ``GET /System/Info/Public``
     - ``jf.api.system.get_public_system_info()``
   * - ``login`` / ``validate_authentication_token``
     - ``POST /Users/AuthenticateByName`` then ``GET /System/Info``
     - ``jf.login(...)`` or ``jf.login_with_token(...)`` followed by ``jf.api.system.get_system_info()`` for token validation
   * - ``get_public_info`` / ``check_redirect``
     - ``GET /system/info/public``
     - ``jf.api.system.get_public_system_info()``
   * - ``get_default_headers`` / ``send_request``
     - custom request builder
     - handled automatically by ``Jellyfin``; call the generated endpoint directly
   * - ``validate_authentication_token``
     - ``GET /system/info`` with token
     - ``jf.api.system.get_system_info()`` (failures indicate an invalid token)
   * - ``utc_time``
     - ``GET /GetUTCTime``
     - ``jf.api.time_sync.get_utc_time()``

Sessions and playstate
----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``sessions`` / ``get_sessions`` / ``get_device``
     - ``GET /Sessions`` with filters
     - ``jf.api.session.get_sessions(...)``
   * - ``sessions(..., action="DELETE")``
     - ``DELETE /Sessions`` (terminate a session)
     - ``jf.api.session.report_session_ended(session_id=...)``
   * - ``command``
     - ``POST /Sessions/{sessionId}/Command``
     - ``jf.api.session.send_full_general_command(session_id=..., body=GeneralCommand(...))``
   * - ``remote`` / ``remote_pause`` / ``remote_playpause`` / ``remote_seek`` / ``remote_stop`` / ``remote_unpause``
     - ``POST /Sessions/{sessionId}/Playing`` or ``/Playing/{command}``
     - ``jf.api.session.play(session_id=..., play_command=..., item_ids=..., play_command_type=...)`` for play requests, or ``jf.api.session.send_playstate_command(session_id=..., command=PlaystateCommand.*, seek_position_ticks=...)`` for targeted playstate commands
   * - ``remote_play_media``
     - ``POST /Sessions/{sessionId}/Playing`` with ``playCommand`` + ``itemIds``
     - ``jf.api.session.play(session_id=..., play_command=..., item_ids=...)``
   * - ``remote_set_volume`` / ``remote_mute`` / ``remote_unmute``
     - ``POST /Sessions/{sessionId}/Command`` with a general command payload
     - ``jf.api.session.send_full_general_command(session_id=..., body=GeneralCommand(name="SetVolume"|"Mute"|"Unmute", ...))``
   * - ``sessions(..., action="POST"/"DELETE")`` / ``session_add_user``
     - ``POST/DELETE /Sessions/{sessionId}/Users/{userId}``
     - ``jf.api.session.add_user_to_session(...)`` or ``jf.api.session.remove_user_from_session(...)``
   * - ``post_session`` (generic passthrough)
     - ``POST /Sessions/{sessionId}/{handler}``
     - ``jf.api.session.send_general_command(session_id=..., command=..., data=...)`` or the matching ``send_*`` helper in ``jf.api.session``
   * - ``post_capabilities``
     - ``POST /Sessions/Capabilities/Full``
     - ``jf.api.session.post_full_capabilities(...)``
   * - ``session_playing``
     - ``POST /Sessions/Playing``
     - ``jf.api.playstate.report_playback_start(...)``
   * - ``session_progress``
     - ``POST /Sessions/Playing/Progress``
     - ``jf.api.playstate.report_playback_progress(...)``
   * - ``item_played``
     - ``POST/DELETE /PlayedItems/{itemId}``
     - ``jf.api.playstate.mark_played_item(...)`` or ``jf.api.playstate.mark_unplayed_item(...)``
   * - ``session_stop``
     - ``POST /Sessions/Playing/Stopped``
     - ``jf.api.playstate.report_playback_stopped(...)``
   * - ``get_now_playing``
     - ``GET /Sessions`` (client-side filter for ``PlayState``)
     - ``jf.api.session.get_sessions(controllable_by_user_id=...)`` then inspect ``parsed`` payload

User and authentication scoped helpers
--------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``get_users`` / ``get_public_users``
     - ``GET /Users`` / ``GET /Users/Public``
     - ``jf.api.user.get_users()`` / ``jf.api.user.get_public_users()``
   * - ``get_user``
     - ``GET /Users/{id}``
     - ``jf.api.user.get_user_by_id(user_id=...)`` (or ``jf.api.user.get_current_user()`` for the authenticated user)
   * - ``new_user`` / ``delete_user``
     - ``POST /Users/New`` / ``DELETE /Users/{id}``
     - ``jf.api.user.create_user_by_name(...)`` / ``jf.api.user.delete_user(user_id=...)``
   * - ``get_user_settings``
     - ``GET /DisplayPreferences/usersettings``
     - ``jf.api.display_preferences.get_display_preferences(display_preferences_id=..., user_id=..., client="emby")``
   * - ``get_views``
     - ``GET /Users/{UserId}/Views``
     - ``jf.api.user_views.get_user_views(user_id=...)``
   * - ``favorite``
     - ``POST/DELETE /FavoriteItems/{itemId}``
     - ``jf.api.user_library.mark_favorite_item(user_id=..., item_id=...)`` / ``jf.api.user_library.unmark_favorite_item(...)``
   * - ``get_userdata_for_item`` / ``update_userdata_for_item``
     - ``GET/POST /UserItems/{itemId}/UserData``
     - ``jf.api.items.get_item_user_data(item_id=..., user_id=...)`` / ``jf.api.items.update_item_user_data(...)``
   * - ``get_userdata_date_modified`` / ``get_date_modified``
     - ``GET /Users/{UserId}/Items`` with ``MinDateLastSaved`` filters
     - ``jf.api.items.get_items(user_id=..., min_date_last_saved=...)`` or ``min_date_last_saved_for_user=...``
   * - ``refresh_item``
     - ``POST /Items/{itemId}/Refresh``
     - ``jf.api.item_refresh.refresh_item(item_id=..., recursive=..., image_refresh_mode=..., metadata_refresh_mode=..., replace_all_images=..., replace_all_metadata=...)``

Library and item metadata
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 37 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``media_folders`` / ``get_media_folders``
     - ``GET /Library/MediaFolders`` or ``GET /Users/{UserId}/Items`` with ``IncludeItemTypes``
     - ``jf.api.library.get_media_folders()`` or ``jf.api.items.get_items(user_id=..., include_item_types=[...])``
   * - ``physical_paths`` / ``folder_contents``
     - ``GET /Library/PhysicalPaths`` / ``GET /Environment/DirectoryContents``
     - ``jf.api.library.get_physical_paths()`` / ``jf.api.environment.get_directory_contents(path=..., include_files=..., include_directories=...)``
   * - ``virtual_folders`` / ``add_media_library``
     - ``GET/POST/DELETE /Library/VirtualFolders``
     - ``jf.api.library_structure.get_virtual_folders()``, ``add_virtual_folder(...)``, or ``remove_virtual_folder(...)``
   * - ``refresh_library``
     - ``POST /Library/Refresh``
     - ``jf.api.library.refresh_library()``
   * - ``items`` / ``user_items`` / ``get_items``
     - ``GET /Items`` (with various filters)
     - ``jf.api.items.get_items(...)``
   * - ``get_item``
     - ``GET /Users/{UserId}/Items/{itemId}``
     - ``jf.api.user_library.get_item(user_id=..., item_id=...)``
   * - ``update_item``
     - ``POST /Items/{itemId}``
     - ``jf.api.item_update.update_item(item_id=..., body=...)``
   * - ``delete_item``
     - ``DELETE /Items/{itemId}``
     - ``jf.api.library.delete_item(item_id=...)``
   * - ``delete_collection``
     - ``DELETE`` (collection chosen via ``/Items`` search)
     - ``jf.api.library.delete_item(item_id=...)``
   * - ``get_images`` / ``artwork``
     - ``GET /Items/{itemId}/Images`` (or ``/Images/{type}``)
     - ``jf.api.image.get_item_image_infos(item_id=...)`` / ``jf.api.image.get_item_image(...)``
   * - ``download_url``
     - ``GET /Items/{itemId}/Download``
     - ``jf.api.library.get_download(item_id=...)``
   * - ``get_suggestion``
     - ``GET /Suggestions``
     - ``jf.api.suggestions.get_suggestions(user_id=..., type=..., limit=...)``
   * - ``get_recently_added``
     - ``GET /Users/{UserId}/Items/Latest``
     - ``jf.api.user_library.get_latest_media(user_id=..., parent_id=..., include_item_types=..., limit=...)``
   * - ``get_next`` / ``get_adjacent_episodes`` / ``get_season`` / ``get_seasons``
     - ``GET /Shows/NextUp`` and ``/Shows/{seriesId}/Episodes`` / ``/Shows/{seriesId}/Seasons``
     - ``jf.api.tv_shows.get_next_up(...)``, ``jf.api.tv_shows.get_episodes(...)``, and ``jf.api.tv_shows.get_seasons(series_id=...)``
   * - ``get_genres``
     - ``GET /Genres``
     - ``jf.api.genres.get_genres(...)``
   * - ``get_recommendation``
     - ``GET /Movies/Recommendations``
     - ``jf.api.movies.get_movie_recommendations(...)``
   * - ``get_items_by_letter`` / ``search_media_items``
     - ``GET /Users/{UserId}/Items`` with search filters
     - ``jf.api.items.get_items(user_id=..., name_starts_with=..., search_term=..., include_item_types=...)``
   * - ``get_channels``
     - ``GET /LiveTv/Channels``
     - ``jf.api.live_tv.get_channels(user_id=..., enable_images=True, enable_user_data=True)``
   * - ``get_intros`` / ``get_local_trailers``
     - ``GET /Items/{itemId}/Intros`` / ``/LocalTrailers``
     - ``jf.api.user_library.get_intros(item_id=...)`` / ``jf.api.user_library.get_local_trailers(item_id=...)``
   * - ``get_additional_parts``
     - ``GET /Videos/{itemId}/AdditionalParts``
     - ``jf.api.videos.get_additional_part(item_id=...)``
   * - ``videos`` (generic helper)
     - ``GET /Videos{...}``
     - Use the specific generated endpoint under ``jf.api.videos`` (for example ``get_video_stream`` or ``get_additional_part``)
   * - ``get_media_segments``
     - ``GET /MediaSegments/{itemId}``
     - ``jf.api.media_segments.get_item_segments(item_id=...)``
   * - ``get_transcode_settings``
     - ``GET /System/Configuration/encoding``
     - Not exposed in the generated client; query the server configuration endpoint directly if needed.
   * - ``get_ancestors``
     - ``GET /Items/{itemId}/Ancestors``
     - ``jf.api.library.get_ancestors(item_id=...)``
   * - ``get_items_theme_video`` / ``get_items_theme_song`` / ``get_themes``
     - ``GET /Items`` with theme flags or ``/Items/{itemId}/ThemeMedia``
     - ``jf.api.library.get_theme_videos(item_id=...)``, ``jf.api.library.get_theme_songs(item_id=...)``, ``jf.api.library.get_theme_media(item_id=...)``
   * - ``get_plugins``
     - ``GET /Plugins``
     - ``jf.api.plugins.get_plugins()``
   * - ``check_companion_installed``
     - ``GET /Jellyfin.Plugin.KodiSyncQueue/GetServerDateTime`` (KodiSyncQueue plugin check)
     - Not part of the generated client; issue a manual request via ``jf.client.get_httpx_client().request(...)``
   * - ``get_collection_folders`` / ``get_collections``
     - ``GET /Users/{UserId}/Items`` with ``IncludeItemTypes`` filters
     - ``jf.api.items.get_items(user_id=..., include_item_types=[CollectionType.COLLECTION_FOLDER or CollectionType.BOX_SET], recursive=...)``
   * - ``new_collection``
     - ``POST /Collections``
     - ``jf.api.collection.create_collection(name=..., ids=..., parent_id=..., is_locked=...)``
   * - ``add_collection_items`` / ``remove_collection_items``
     - ``POST/DELETE /Collections/{collectionId}/Items``
     - ``jf.api.collection.add_to_collection(collection_id=..., ids=...)`` / ``jf.api.collection.remove_from_collection(collection_id=..., ids=...)``

Playback and streaming
----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``audio_url`` / ``get_audio_stream``
     - ``GET /Audio/{itemId}/universal`` (optionally streamed)
     - ``jf.api.universal_audio.get_universal_audio_stream(item_id=..., user_id=jf.user_id, device_id=..., max_streaming_bitrate=..., audio_codec=...)`` (stream the response body to disk if you previously wrote to ``dest_file``)
   * - ``video_url``
     - ``GET /Videos/{itemId}/stream``
     - ``jf.api.videos.get_video_stream(item_id=..., media_source_id=..., static=True, device_id=...)``
   * - ``download_url``
     - ``GET /Items/{itemId}/Download``
     - ``jf.api.library.get_download(item_id=...)``
   * - ``get_play_info``
     - ``POST /Items/{itemId}/PlaybackInfo``
     - ``jf.api.media_info.get_posted_playback_info(item_id=..., user_id=..., device_profile=..., start_time_ticks=..., media_source_id=...)``
   * - ``get_live_stream`` / ``close_live_stream``
     - ``POST /LiveStreams/Open`` / ``POST /LiveStreams/Close``
     - ``jf.api.media_info.open_live_stream(body=...)`` / ``jf.api.media_info.close_live_stream(live_stream_id=...)``
   * - ``close_transcode``
     - ``DELETE /Videos/ActiveEncodings``
     - ``jf.api.hls_segment.stop_encoding_process(device_id=..., play_session_id=...)``

SyncPlay
--------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``get_sync_play``
     - ``GET /SyncPlay/List``
     - ``jf.api.sync_play.sync_play_get_groups(item_ids_filter=...)``
   * - ``join_sync_play`` / ``leave_sync_play``
     - ``POST /SyncPlay/Join`` / ``POST /SyncPlay/Leave``
     - ``jf.api.sync_play.sync_play_join_group(group_id=...)`` / ``jf.api.sync_play.sync_play_leave_group()``
   * - ``play_sync_play`` (deprecated)
     - ``POST /SyncPlay/Play``
     - No dedicated generated endpoint; use ``sync_play_set_new_queue`` + ``sync_play_unpause`` to start playback.
   * - ``pause_sync_play`` / ``unpause_sync_play``
     - ``POST /SyncPlay/Pause`` / ``POST /SyncPlay/Unpause``
     - ``jf.api.sync_play.sync_play_pause(...)`` / ``jf.api.sync_play.sync_play_unpause(...)``
   * - ``seek_sync_play``
     - ``POST /SyncPlay/Seek``
     - ``jf.api.sync_play.sync_play_seek(position_ticks=...)``
   * - ``buffering_sync_play`` / ``ready_sync_play``
     - ``POST /SyncPlay/Buffering`` / ``POST /SyncPlay/Ready``
     - ``jf.api.sync_play.sync_play_buffering(...)`` / ``jf.api.sync_play.sync_play_ready(...)``
   * - ``reset_queue_sync_play``
     - ``POST /SyncPlay/SetNewQueue``
     - ``jf.api.sync_play.sync_play_set_new_queue(playing_queue=..., playing_item_position=..., start_position_ticks=...)``
   * - ``ignore_sync_play``
     - ``POST /SyncPlay/SetIgnoreWait``
     - ``jf.api.sync_play.sync_play_set_ignore_wait(ignore_wait=...)``
   * - ``next_sync_play`` / ``prev_sync_play`` / ``set_item_sync_play``
     - ``POST /SyncPlay/NextItem`` / ``PreviousItem`` / ``SetPlaylistItem``
     - ``jf.api.sync_play.sync_play_next_item(...)`` / ``sync_play_previous_item(...)`` / ``sync_play_set_playlist_item(...)``
   * - ``ping_sync_play``
     - ``POST /SyncPlay/Ping``
     - ``jf.api.sync_play.sync_play_ping(ping=...)``
   * - ``new_sync_play`` / ``new_sync_play_v2``
     - ``POST /SyncPlay/New``
     - ``jf.api.sync_play.sync_play_create_group(group_name=...)``

Miscellaneous and plugin-specific calls
---------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``get_system_info``
     - ``GET /System/Configuration``
     - ``jf.api.system.get_system_info()``
   * - ``get_server_logs``
     - ``GET /System/Logs``
     - ``jf.api.system.get_server_logs()``
   * - ``get_log_entries``
     - ``GET /System/ActivityLog/Entries``
     - ``jf.api.activity_log.get_log_entries(...)``
   * - ``get_sync_queue`` / ``get_server_time``
     - ``Jellyfin.Plugin.KodiSyncQueue/*``
     - Not included in the generated OpenAPI client; call the plugin endpoints manually using ``jf.client.get_httpx_client().request(...)`` if needed.
   * - ``identify``
     - ``POST /Items/RemoteSearch/Apply/{itemId}``
     - ``jf.api.item_lookup.apply_search_criteria(item_id=..., body=...)``
   * - ``set_item_image`` / ``set_user_image``
     - ``POST /Items/{itemId}/Images/{imageType}`` / ``POST /UserImage``
     - Upload endpoints are not present in the generated client; issue a manual request with ``jf.client.get_httpx_client().request(...)``

Collections and playlists
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Legacy helper
     - Legacy endpoint
     - OpenAPI convenience call
   * - ``get_collection_folders``
     - ``GET /Users/{UserId}/Items`` with ``IncludeItemTypes=CollectionFolder``
     - ``jf.api.items.get_items(user_id=..., include_item_types=[CollectionType.COLLECTION_FOLDER], recursive=False)``
   * - ``get_collections``
     - ``GET /Users/{UserId}/Items`` with ``IncludeItemTypes=BoxSet``
     - ``jf.api.items.get_items(user_id=..., include_item_types=[CollectionType.BOX_SET], recursive=True, search_term=...)``
   * - ``new_collection``
     - ``POST /Collections``
     - ``jf.api.collection.create_collection(...)``
   * - ``add_collection_items`` / ``remove_collection_items``
     - ``POST/DELETE /Collections/{collectionId}/Items``
     - ``jf.api.collection.add_to_collection(...)`` / ``jf.api.collection.remove_from_collection(...)``

Notes
-----

* Methods that only wrapped low-level HTTP helpers (for example ``_get`` or
  ``send_request``) have no direct replacement because the new client exposes
  every Jellyfin endpoint explicitly via ``jf.api``.  Build manual requests with
  ``jf.client.get_httpx_client()`` only when an endpoint is missing from the
  generated surface (the plugin and image-upload cases above).
* Many legacy helpers filled ``UserId`` or ``DeviceId`` placeholders implicitly;
  the OpenAPI client requires you to pass those values explicitly.  The
  convenience wrapper provides ``jf.user_id`` and ``jf.client`` to simplify that
  migration.
