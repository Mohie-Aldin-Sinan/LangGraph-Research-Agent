from langchain_tavily import TavilySearch


def search_web(query: str) -> dict:
    """Search the web and return relevant results."""

    if not query.strip():
        raise ValueError("Search query cannot be empty.")

    search_tool = TavilySearch(
        max_results=5,
        topic="general",
    )

    return search_tool.invoke({"query": query})