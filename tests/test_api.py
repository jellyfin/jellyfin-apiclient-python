from jellyfin_apiclient_python.api import jellyfin_url, info, API
from jellyfin_apiclient_python.http import HTTP
from unittest.mock import Mock, patch
from unittest import TestCase
import json

def test_jellyfin_url_handles_trailing_slash():
    mock_client = Mock()
    mock_client.config.data = {"auth.server": "https://example.com/"}
    handler = "Items/1234"
    url = jellyfin_url(mock_client, handler)
    assert url == "https://example.com/Items/1234"

    mock_client.config.data = {"auth.server": "https://example.com"}
    url = jellyfin_url(mock_client, handler)
    assert url == "https://example.com/Items/1234"


class TestBackup(TestCase):
    def setup_requests(self):
        patcher = patch("jellyfin_apiclient_python.http.HTTP.request")
        self.addCleanup(patcher.stop)
        self.mock_request = patcher.start()

    def setup_api(self):
        mock_client = Mock()
        self.api = API(HTTP(mock_client))

    def setUp(self):
        self.setup_requests()
        self.setup_api()

    def assert_request_matches_call_parameters(
        self, handler, params=None, json={}
    ) -> None:
        parameters = self.mock_request.call_args.args[0]

        if parameters["type"] == "GET":
            assert parameters["handler"] == handler
            assert parameters["params"] == params

        if parameters["type"] == "POST":
            assert parameters["handler"] == handler
            assert parameters["params"] == params
            assert parameters["json"] == json

    def test_create_backup_defaults_are_as_expected(self):
        handler = "Backup/Create"
        json = {
            "database": True,
            "metadata": False,
            "subtitles": False,
            "trickplay": False,
        }
        self.api.create_backup()

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(handler=handler, json=json)

    def test_create_backup_parameters_are_propagated(self):
        handler = "Backup/Create"
        json = {
            "database": True,
            "metadata": True,
            "subtitles": True,
            "trickplay": True,
        }

        self.api.create_backup(
            include_metadata=True,
            include_subtitles=True,
            include_trickplay=True,
        )

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(handler=handler, json=json)

    def test_get_backup_manifest_parameters_are_propagated(self):
        handler = "Backup/Manifest"
        path = "imaginary_path"
        params = {"path": path}

        self.api.get_backup_manifest(path=path)

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(handler=handler, params=params)

    def test_get_backups_has_no_patameters(self):
        handler = "Backup"

        self.api.get_backups()

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(handler=handler)

    def test_restore_backup_parameters_are_propagated(self):
        handler = "Backup/Restore"
        backup_name = "imaginary_name"
        json = {"ArchiveFileName": backup_name}

        self.api.restore_backup(backup_name=backup_name)

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(handler=handler, json=json)
        
class TestIdentify(TestCase):
    def setup_requests(self):
        patcher = patch('jellyfin_apiclient_python.http.HTTP.request')
        self.addCleanup(patcher.stop)
        self.mock_request = patcher.start()

    def setup_api(self):
        mock_client = Mock()
        self.api = API(HTTP(mock_client))

    def setup_data(self):
        self.defaultParams = {'replaceAllImages': True}
        self.defaultJson = {'Name': None, 'ProviderIds': None, 'ProductionYear': None}
        self.handler = 'Items/RemoteSearch/Apply'

    def setUp(self):
        self.setup_requests()
        self.setup_api()
        self.setup_data()

    def build_handler_for_item_id(self, item_id) -> str:
        return f"{self.handler}/{item_id}"

    def assert_request_matches_call_parameters(self, item_id, params, json) -> None:
        parameters = self.mock_request.call_args.args[0]
        assert(parameters['params'] == params)
        assert(parameters['json'] == json)
        assert(parameters['handler'] == self.build_handler_for_item_id(item_id))

    def test_defaults_are_as_expected(self):
        item_id = 1234

        self.api.identify(item_id=item_id)

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(item_id, self.defaultParams, self.defaultJson)

    def do_image_replacement(self, item_id, replace):
        self.api.identify(item_id=item_id, replaceAllImages=replace)

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(item_id, {'replaceAllImages': replace}, self.defaultJson)

    def test_images_are_replaced(self):
        self.do_image_replacement(1235, True)

    def test_images_are_not_replaced(self):
        self.do_image_replacement(1236, False)

    def test_parameters_are_propagated(self):
        item_id = 1237
        name = 'foo'
        ids = {'id1': 1, 'id2': 2}
        year = 1964
        json = {'Name': name, 'ProviderIds': ids, 'ProductionYear': year}

        self.api.identify(item_id=item_id, name=name, provider_ids=ids, year=year)

        self.mock_request.assert_called_once()
        self.assert_request_matches_call_parameters(item_id, self.defaultParams, json)


class TestQuickConnect(TestCase):
    # The Quick Connect endpoints, like login(), go through send_request()
    # directly rather than HTTP.request, so we mock send_request here.
    def setUp(self):
        self.api = API(HTTP(Mock()))
        # The Mock client has no real config; stub header construction since
        # these tests only care about path/method/body wiring.
        patcher = patch.object(API, "get_default_headers", return_value={})
        self.addCleanup(patcher.stop)
        patcher.start()

    @staticmethod
    def _response(status_code=200, payload=None):
        response = Mock()
        response.status_code = status_code
        response.json.return_value = payload
        response.content = b""
        return response

    def test_quick_connect_enabled_true(self):
        with patch.object(API, "send_request", return_value=self._response(200, True)) as sr:
            self.assertIs(self.api.quick_connect_enabled("https://s"), True)
            self.assertEqual(sr.call_args.args[1], "QuickConnect/Enabled")

    def test_quick_connect_enabled_failure_returns_false(self):
        with patch.object(API, "send_request", return_value=self._response(401, None)):
            self.assertIs(self.api.quick_connect_enabled("https://s"), False)

    def test_quick_connect_initiate_returns_payload(self):
        payload = {"Secret": "abc", "Code": "123456"}
        with patch.object(API, "send_request", return_value=self._response(200, payload)) as sr:
            self.assertEqual(self.api.quick_connect_initiate("https://s"), payload)
            self.assertEqual(sr.call_args.args[1], "QuickConnect/Initiate")
            self.assertEqual(sr.call_args.kwargs["method"], "post")

    def test_quick_connect_initiate_failure_returns_empty(self):
        with patch.object(API, "send_request", return_value=self._response(401, None)):
            self.assertEqual(self.api.quick_connect_initiate("https://s"), {})

    def test_quick_connect_state_encodes_secret(self):
        payload = {"Authenticated": False}
        with patch.object(API, "send_request", return_value=self._response(200, payload)) as sr:
            self.assertEqual(self.api.quick_connect_state("https://s", "a/b c"), payload)
            self.assertEqual(sr.call_args.args[1], "QuickConnect/Connect?secret=a%2Fb%20c")

    def test_login_with_quick_connect_returns_auth_result(self):
        payload = {"AccessToken": "t", "User": {"Id": "u"}, "ServerId": "s"}
        with patch.object(API, "send_request", return_value=self._response(200, payload)) as sr:
            self.assertEqual(self.api.login_with_quick_connect("https://s", "secret"), payload)
            self.assertEqual(sr.call_args.args[1], "Users/AuthenticateWithQuickConnect")
            self.assertEqual(sr.call_args.kwargs["method"], "post")
            self.assertEqual(json.loads(sr.call_args.kwargs["data"]), {"Secret": "secret"})

    def test_login_with_quick_connect_failure_returns_empty(self):
        with patch.object(API, "send_request", return_value=self._response(400, None)):
            self.assertEqual(self.api.login_with_quick_connect("https://s", "secret"), {})



class RequestCaptureMixin:
    """Captures the request dict the API mixins hand to HTTP.request."""

    def setUp(self):
        patcher = patch("jellyfin_apiclient_python.http.HTTP.request")
        self.addCleanup(patcher.stop)
        self.mock_request = patcher.start()
        self.api = API(HTTP(Mock()))

    def request(self):
        self.mock_request.assert_called_once()
        return self.mock_request.call_args.args[0]

    def params(self):
        return self.request()["params"]


class TestBrowseCalls(RequestCaptureMixin, TestCase):
    def test_get_user_items_omits_unset_arguments(self):
        self.api.get_user_items(parent_id="lib", limit=10)

        request = self.request()
        assert request["handler"] == "Users/{UserId}/Items"
        assert request["params"] == {"ParentId": "lib", "Limit": 10}

    def test_get_user_items_sends_false_values(self):
        # A falsy-but-set argument is a real instruction to the server, so it
        # must survive the "drop unset arguments" filter.
        self.api.get_user_items(recursive=False, enable_total_record_count=False)

        assert self.params() == {
            "Recursive": False,
            "EnableTotalRecordCount": False,
        }

    def test_get_user_items_joins_ids_and_merges_extra_params(self):
        self.api.get_user_items(ids=["a", "b"], params={"MinWidth": 100})

        assert self.params() == {"Ids": "a,b", "MinWidth": 100}

    def test_get_resume_items_asks_for_resumable_by_recency(self):
        self.api.get_resume_items(limit=20, media_types="Audio")

        assert self.params() == {
            "MediaTypes": "Audio",
            "Recursive": True,
            "Filters": "IsResumable",
            "SortBy": "DatePlayed",
            "SortOrder": "Descending",
            "Limit": 20,
        }

    def test_get_random_items_passes_image_filters(self):
        self.api.get_random_items(include_item_types="Movie", limit=1,
                                  image_types="Backdrop",
                                  max_official_rating="PG-13")

        params = self.params()
        assert params["SortBy"] == "Random"
        assert params["ImageTypes"] == "Backdrop"
        assert params["MaxOfficialRating"] == "PG-13"

    def test_get_items_by_person_queries_person_ids(self):
        self.api.get_items_by_person("person1", limit=50)

        params = self.params()
        assert params["PersonIds"] == "person1"
        assert params["IncludeItemTypes"] == "Movie,Series"
        assert params["Recursive"] is True

    def test_get_album_tracks_sorts_by_disc_then_track(self):
        self.api.get_album_tracks("album1", fields="Artists")

        assert self.params() == {
            "ParentId": "album1",
            "Fields": "Artists",
            "SortBy": "ParentIndexNumber,IndexNumber,SortName",
            "SortOrder": "Ascending",
        }

    def test_get_artist_albums_uses_album_artist_ids(self):
        self.api.get_artist_albums("artist1")

        params = self.params()
        assert params["AlbumArtistIds"] == "artist1"
        assert "ArtistIds" not in params
        assert params["IncludeItemTypes"] == "MusicAlbum"

    def test_get_artist_songs_uses_artist_ids(self):
        self.api.get_artist_songs("artist1", limit=500)

        params = self.params()
        assert params["ArtistIds"] == "artist1"
        assert params["IncludeItemTypes"] == "Audio"
        assert params["Limit"] == 500

    def test_get_genre_songs_scopes_to_parent_when_given(self):
        self.api.get_genre_songs("genre1", parent_id="music")

        params = self.params()
        assert params["GenreIds"] == "genre1"
        assert params["ParentId"] == "music"

    def test_get_playlists_does_not_filter_by_media_type(self):
        self.api.get_playlists(limit=300)

        assert self.params() == {
            "IncludeItemTypes": "Playlist",
            "Recursive": True,
            "SortBy": "SortName",
            "SortOrder": "Ascending",
            "Limit": 300,
        }

    def test_get_recently_added_defaults_to_the_full_field_set(self):
        self.api.get_recently_added(parent_id="lib")

        request = self.request()
        assert request["handler"] == "Users/{UserId}/Items/Latest"
        assert request["params"]["Fields"] == info()

    def test_get_recently_added_accepts_lean_fields(self):
        self.api.get_recently_added(parent_id="lib", limit=16, fields="Overview",
                                    enable_image_types="Primary",
                                    image_type_limit=1,
                                    enable_total_record_count=False)

        params = self.params()
        assert params["Fields"] == "Overview"
        assert params["EnableImageTypes"] == "Primary"
        assert params["ImageTypeLimit"] == 1
        assert params["EnableTotalRecordCount"] is False

    def test_get_items_defaults_to_the_full_field_set(self):
        self.api.get_items(["a", "b"])

        assert self.params() == {"Ids": "a,b", "Fields": info()}

    def test_get_items_accepts_lean_fields(self):
        self.api.get_items(["a"], fields="Overview")

        assert self.params() == {"Ids": "a", "Fields": "Overview"}

    def test_get_collections_stays_unpaged_by_default(self):
        from jellyfin_apiclient_python.constants import ItemType

        self.api.get_collections()

        assert self.params() == {
            "recursive": True,
            "includeItemTypes": [ItemType.BOX_SET],
        }

    def test_get_collections_accepts_paging(self):
        self.api.get_collections(limit=300, sort_by="SortName")

        params = self.params()
        assert params["Limit"] == 300
        assert params["SortBy"] == "SortName"

    def test_get_endpoint_info(self):
        self.api.get_endpoint_info()

        assert self.request()["handler"] == "System/Endpoint"

    def test_update_user_settings_posts_the_whole_document(self):
        dto = {"Id": "usersettings", "CustomPrefs": {"homesection0": "resume"}}

        self.api.update_user_settings(dto)

        request = self.request()
        assert request["type"] == "POST"
        assert request["handler"] == "DisplayPreferences/usersettings"
        assert request["params"] == {"userId": "{UserId}", "client": "emby"}
        assert request["json"] == dto


class TestLiveTvCalls(RequestCaptureMixin, TestCase):
    def test_get_live_tv_info_is_a_bare_get(self):
        # LiveTv/Info takes no query: the server resolves the caller from the
        # token, and the user id is only read from the EnabledUsers answer.
        self.api.get_live_tv_info()

        request = self.request()
        assert request["type"] == "GET"
        assert request["handler"] == "LiveTv/Info"
        assert request["params"] is None

    def test_get_channels_keeps_its_no_argument_behavior(self):
        self.api.get_channels()

        request = self.request()
        assert request["handler"] == "LiveTv/Channels"
        assert request["params"] == {
            "UserId": "{UserId}",
            "EnableImages": True,
            "EnableUserData": True,
        }

    def test_get_channels_can_be_bounded(self):
        self.api.get_channels(limit=50, start_index=100, fields="PrimaryImageAspectRatio",
                              add_current_program=False)

        params = self.params()
        assert params["Limit"] == 50
        assert params["StartIndex"] == 100
        assert params["Fields"] == "PrimaryImageAspectRatio"
        assert params["AddCurrentProgram"] is False
        # LiveTv/Channels has no enableTotalRecordCount — the controller
        # always computes the count. Sending one is silently ignored, so the
        # helper must not offer an argument that pretends otherwise.
        assert "EnableTotalRecordCount" not in params

    def test_get_programs_joins_channel_ids(self):
        self.api.get_programs(channel_ids=["c1", "c2"], min_start_date="2026-01-01T00:00:00Z")

        request = self.request()
        assert request["handler"] == "LiveTv/Programs"
        assert request["params"]["ChannelIds"] == "c1,c2"
        assert request["params"]["MinStartDate"] == "2026-01-01T00:00:00Z"

    def test_get_programs_accepts_a_prejoined_channel_string(self):
        self.api.get_programs(channel_ids="c1,c2")

        assert self.params()["ChannelIds"] == "c1,c2"

    def test_get_recommended_programs_on_now(self):
        self.api.get_recommended_programs(is_airing=True, limit=24,
                                          fields="Overview,ChannelInfo",
                                          enable_user_data=False)

        request = self.request()
        assert request["handler"] == "LiveTv/Programs/Recommended"
        assert request["params"] == {
            "UserId": "{UserId}",
            "IsAiring": True,
            "Limit": 24,
            "Fields": "Overview,ChannelInfo",
            "EnableUserData": False,
        }

    def test_close_live_stream_sends_the_id_as_a_query_parameter(self):
        # The server binds liveStreamId [FromQuery]; in the body it 400s and
        # the tuner is never released.
        self.api.close_live_stream("stream1")

        request = self.request()
        assert request["type"] == "POST"
        assert request["handler"] == "LiveStreams/Close"
        assert request["params"] == {"liveStreamId": "stream1"}
        assert request["json"] is None


class TestImageStreams(RequestCaptureMixin, TestCase):
    def test_get_chapter_image(self):
        dest = object()

        self.api.get_chapter_image(dest, "item1", 3, tag="tag1", max_width=400,
                                   quality=90)

        request = self.request()
        assert request["handler"] == "Items/item1/Images/Chapter/3"
        assert request["params"] == {"tag": "tag1", "maxWidth": 400, "quality": 90}
        assert self.mock_request.call_args.kwargs["dest_file"] is dest

    def test_get_chapter_image_omits_unset_arguments(self):
        self.api.get_chapter_image(object(), "item1", 0)

        assert self.params() == {}

    def test_get_trickplay_tile_sends_media_source_as_a_parameter(self):
        # Not appended to the handler: that would end up double-encoded and
        # bypass the parameter handling entirely.
        self.api.get_trickplay_tile(object(), "item1", 320, 2,
                                    media_source_id="src1")

        request = self.request()
        assert request["handler"] == "Videos/item1/Trickplay/320/2.jpg"
        assert request["params"] == {"MediaSourceId": "src1"}


class TestUrlTokenSpelling(TestCase):
    """A built URL carries ``ApiKey``, not ``api_key``.

    The server reads both in the same place
    (``AuthorizationContext.GetAuthorizationInfoFromDictionary``), but
    ``api_key`` is gated on ``EnableLegacyAuthorization`` -- off by default
    from Jellyfin v12 -- while ``ApiKey`` is not. So this is a spelling
    change and nothing more.

    Requests the client issues itself never depended on this: they carry
    ``Authorization: MediaBrowser Token="…"``, the non-legacy header scheme.
    Only URLs handed to something else -- a media player, a downloader --
    reach this code.
    """

    def _api(self):
        client = Mock()
        client.config.data = {"auth.server": "https://example.com",
                              "auth.token": "T0KEN",
                              "http.user_agent": "test/1.0",
                              "http.timeout": 30,
                              # audio_url substitutes {UserId}
                              "auth.user_id": "U1",
                              "app.device_id": "D1"}
        return API(HTTP(client))

    def test_a_built_url_uses_the_modern_spelling(self):
        url = self._api().download_url("item1")
        assert "ApiKey=T0KEN" in url
        assert "api_key" not in url

    def test_the_token_can_be_left_out_entirely(self):
        """For callers that authenticate the eventual request themselves --
        mpv takes --http-header-fields. A token in a URL is a token in logs,
        in ps output and in every proxy in the path."""
        url = self._api().download_url("item1", include_apikey=False)
        assert "ApiKey" not in url
        assert "api_key" not in url

    def test_every_url_builder_can_be_switched_off(self):
        api = self._api()
        built = {
            "artwork": api.artwork("i", "Primary", 100, include_apikey=False),
            "audio_url": api.audio_url("i", include_apikey=False),
            "video_url": api.video_url("i", include_apikey=False),
            "download_url": api.download_url("i", include_apikey=False),
            "image_url": api.image_url("i", include_apikey=False),
            "subtitle_url": api.subtitle_url("i", "s", 1, "srt",
                                             include_apikey=False),
            "trickplay_tile_url": api.trickplay_tile_url(
                "i", 320, 0, include_apikey=False),
        }
        for name, url in built.items():
            assert "ApiKey" not in url, name
            assert "api_key" not in url, name

    def test_and_carries_it_by_default(self):
        api = self._api()
        for url in (api.artwork("i", "Primary", 100), api.audio_url("i"),
                    api.video_url("i"), api.download_url("i"),
                    api.image_url("i"),
                    api.subtitle_url("i", "s", 1, "srt"),
                    api.trickplay_tile_url("i", 320, 0)):
            assert "ApiKey=T0KEN" in url
