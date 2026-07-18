from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.research_models import ResearchRequest
from app.services.agent_service import run_agent
from app.services.export_service import (
    export_docx,
    export_pdf,
)

router = APIRouter(prefix="/export", tags=["Export"])


@router.post("/docx")
def export_as_docx(request: ResearchRequest):

    report = run_agent(
        question=request.question,
        library_name=request.library_name
    )

    file = export_docx(
        report["answer"],
        report["references"]
    )

    return StreamingResponse(
        file,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": 'attachment; filename="research_report.docx"'
        }
    )


@router.post("/pdf")
def export_as_pdf(request: ResearchRequest):

    report = run_agent(
        question=request.question,
        library_name=request.library_name
    )

    file = export_pdf(
        report["answer"],
        report["references"]
    )

    return StreamingResponse(
        file,
        media_type="application/pdf",
        headers={
            "Content-Disposition": 'attachment; filename="research_report.pdf"'
        }
    )