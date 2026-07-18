from fastapi import APIRouter

from app.models.agent_models import AgentRequest
from app.services.agent_service import run_agent

router = APIRouter(
    prefix="/agent",
    tags=["Research Agent"]
)


@router.post("")
def agent(request: AgentRequest):

   return run_agent(
    question=request.question,
    library_name=request.library_name,
    search_web=request.search_web
    )