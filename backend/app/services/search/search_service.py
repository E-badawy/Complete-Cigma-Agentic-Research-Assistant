
from app.utils.logger import logger

from app.services.search.openalex import search_openalex
from app.services.search.pubmed import search_pubmed


def search(query: str):

    papers = []

    try:
        papers.extend(
            search_pubmed(
                query,
                limit=10
            )
        )
    except Exception as e:
        print(f"PubMed failed: {e}")

    try:
        papers.extend(
            search_openalex(
                query,
                limit=10
            )
        )
    except Exception as e:
        print(f"OpenAlex failed: {e}")

    return papers




