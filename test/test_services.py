import pytest

from src.services import simple_search


@pytest.fixture
def txns():
    return [
        {"description": "Coffee shop", "amount": -300},
        {"description": "Grocery store", "amount": -1500},
    ]


def test_simple_search_found(txns):
    result = simple_search("coffee", txns)
    assert result["count"] == 1
    assert result["items"][0]["description"] == "Coffee shop"


def test_simple_search_not_found(txns):
    assert simple_search("cinema", txns)["count"] == 0
