from fastapi import APIRouter

from app.models.research_models import ResearchRequest
from app.services.research_service import ask_question

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)


@router.post("")
def research(request: ResearchRequest):

    return ask_question(
        request.library_name,
        request.question
    )