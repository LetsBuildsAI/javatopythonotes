from unittest.mock import MagicMock, patch

import pytest

from javatopythonotes.jsonplaceholder.client import fetch_post


def test_fetch_post_invalid_id() -> None:
    with pytest.raises(ValueError, match="post_id"):
        fetch_post(0)


@patch("javatopythonotes.jsonplaceholder.client.urlopen")
def test_fetch_post_parses_json(mock_urlopen: MagicMock) -> None:
    mock_resp = MagicMock()
    mock_resp.read.return_value = (
        b'{"userId":1,"id":1,"title":"Hello","body":"World"}'
    )
    mock_cm = MagicMock()
    mock_cm.__enter__.return_value = mock_resp
    mock_cm.__exit__.return_value = None
    mock_urlopen.return_value = mock_cm

    result = fetch_post(1)

    assert result == {
        "userId": 1,
        "id": 1,
        "title": "Hello",
        "body": "World",
    }
    mock_urlopen.assert_called_once()
    call_kw = mock_urlopen.call_args[1]
    assert call_kw.get("timeout") == 15
