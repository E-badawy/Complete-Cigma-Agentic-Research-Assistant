import requests

BASE_URL = "https://api.openalex.org/works"

def decode_abstract(index):

    if not index:
        return None

    words = []

    for word, positions in index.items():
        for position in positions:
            words.append((position, word))

    words.sort()

    return " ".join(word for _, word in words)

def search_openalex(query: str, limit: int = 5):

    params = {
        "search": query,
        "per_page": limit
    }

    response = requests.get(
        BASE_URL,
        params=params,
        headers={
            "User-Agent": "Agentic Research Agent (research project)"
        },
        timeout=30
    )
    
    response.raise_for_status()

    data = response.json()

    papers = []

    for work in data.get("results", []):

        primary_location = work.get("primary_location") or {}
        source = primary_location.get("source") or {}

        authors = []

        for author in work.get("authorships", []):
            author_info = author.get("author") or {}
            authors.append(author_info.get("display_name", "Unknown"))

        paper = {

            "title": work.get("display_name"),

            "year": work.get("publication_year"),

            "doi": work.get("doi"),

            "openalex_id": work.get("id"),

            "citations": work.get("cited_by_count"),

            "type": work.get("type"),

            "language": work.get("language"),

            "abstract": decode_abstract(
            work.get("abstract_inverted_index")
            ),

            "url": primary_location.get("landing_page_url"),

            "pdf": primary_location.get("pdf_url"),

            "journal": source.get("display_name"),

            "authors": authors

        }

    papers.append(paper)
    
    return papers