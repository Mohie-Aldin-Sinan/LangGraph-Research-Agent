import pytest

from app.tools import search_web


def test_empty_query_is_rejected():
    with pytest.raises(ValueError, match="Search query cannot be empty"):
        search_web("   ")