from jellyfin_apiclient_python.api import jellyfin_url
from unittest.mock import Mock

def test_jellyfin_url_handles_trailing_slash():
    mock_client = Mock()
    mock_client.config.data = {'auth.server': 'https://example.com/'}
    handler = "Items/1234"
    url = jellyfin_url(mock_client, handler)
    assert url == "https://example.com/Items/1234"

    mock_client.config.data = {'auth.server': 'https://example.com'}
    url = jellyfin_url(mock_client, handler)
    assert url == "https://example.com/Items/1234"
