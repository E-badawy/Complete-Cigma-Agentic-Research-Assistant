from fastapi import APIRouter

from app.models.search_models import SearchRequest
from app.services.search.search_service import search

router = APIRouter(
    prefix="/search",
    tags=["Scientific Search"]
)


@router.post("")
def search_papers(request: SearchRequest):

    papers = search(
        request.query
    )

    return {
        "source": "OpenAlex",
        "total_results": len(papers),
        "papers": papers
    }