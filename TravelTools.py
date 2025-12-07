from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_web_tool(query: str):
    """
    Searches the web and returns results.
    Accepts a string query. If a dictionary is passed, it will try to extract a string safely.
    """
    # Defensive check: if query is a dict, extract the string
    if isinstance(query, dict):
        # Try common keys
        query = query.get("description") or query.get("query") or str(query)
    
    # Make sure we now have a string
    if not isinstance(query, str):
        raise ValueError(f"Query must be a string, got {type(query)}: {query}")

    # Perform the search
    search_tool = DuckDuckGoSearchResults(num_results=10, verbose=True)
    return search_tool.run(query)