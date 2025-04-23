import re

from src.views import index


def test_index_returns_json():
    resp = index("2025-04-23 09:30:00")
    assert "result" in resp
    assert re.search(r"Сейчас \d{2}\.\d{2}\.\d{4}", resp["result"]["message"])
