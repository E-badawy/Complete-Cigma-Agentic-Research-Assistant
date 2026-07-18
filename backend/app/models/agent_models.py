from pydantic import BaseModel


class AgentRequest(BaseModel):
    question: str
    library_name: str | None = None
    search_web: bool = True


class AgentResponse(BaseModel):
    answer: str
    local_sources: list = []
    web_sources: list = []