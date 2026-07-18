from fastapi import FastAPI
print("Loading library routes...")
from app.api.routes.library import router as library_router
print("Loading research routes...")
from app.api.routes.research import router as research_router
print("Loading search routes...")
from app.api.routes.search import router as search_router
print("Loading agent routes...")
from app.api.routes.agent import router as agent_router

from app.api.routes import export
from app.api.routes.health import router as health_router
from app.api.routes.audio import router as audio_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Agentic Research Agent",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "running"
    }


app.include_router(library_router)
app.include_router(research_router)
app.include_router(search_router)
app.include_router(agent_router)
app.include_router(export.router)
app.include_router(health_router)
app.include_router(audio_router)
