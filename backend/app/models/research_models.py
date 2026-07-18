from pydantic import BaseModel


class ResearchRequest(BaseModel):
    library_name: str
    question: str


class Source(BaseModel):
    filename: str
    page: int | None = None


class ResearchResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]