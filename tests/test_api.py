from jellyfin_apiclient_python.api import jellyfin_url, API
from jellyfin_apiclient_python.http import HTTP
from unittest.mock import Mock, patch
from unittest import TestCase

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

