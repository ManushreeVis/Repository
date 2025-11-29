import json
from unittest.mock import Mock, patch

from quoteapp.app import app


def test_get_quote_success():
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"content": "Test quote", "author": "Tester"}

    with patch("quoteapp.app.requests.get", return_value=mock_resp):
        client = app.test_client()
        resp = client.get("/quote")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["quote"] == "Test quote"
        assert data["author"] == "Tester"


def test_get_quote_failure():
    mock_resp = Mock()
    mock_resp.status_code = 500

    with patch("quoteapp.app.requests.get", return_value=mock_resp):
        client = app.test_client()
        resp = client.get("/quote")
        assert resp.status_code == 502
        data = resp.get_json()
        assert "error" in data
