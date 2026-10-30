from functools import lru_cache

from langchain_tavily import TavilySearch


@lru_cache(maxsize=1)
def get_search_tool():
    """Create and cache the Tavily search client."""

    return TavilySearch(
        max_results=5,
        topic="general",
    )


def search_web(query: str) -> dict:
    """Search the web and return relevant results."""

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    search_tool = get_search_tool()

    return search_tool.invoke({"query": query})