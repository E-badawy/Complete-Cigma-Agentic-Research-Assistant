from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    limit: int = 10


class Paper(BaseModel):
    title: str | None = None
    year: int | None = None
    journal: str | None = None
    doi: str | None = None
    url: str | None = None
    pdf: str | None = None
    citations: int | None = None
    authors: list[str] = []
    abstract: str | None = None


class SearchResponse(BaseModel):
    source: str
    total_results: int
    papers: list[Paper]