import time

startup = time.time()

print("=" * 60)
print("Starting FastAPI application...")
print("=" * 60)

# -----------------------------
# Import routers with timing
# -----------------------------

t = time.time()
print("Loading library routes...")
from app.api.routes.library import router as library_router
print(f"✓ Library routes loaded in {time.time() - t:.2f}s\n")

t = time.time()
print("Loading research routes...")
from app.api.routes.research import router as research_router
print(f"✓ Research routes loaded in {time.time() - t:.2f}s\n")

t = time.time()
print("Loading search routes...")
from app.api.routes.search import router as search_router
print(f"✓ Search routes loaded in {time.time() - t:.2f}s\n")

t = time.time()
print("Loading agent routes...")
from app.api.routes.agent import router as agent_router
print(f"✓ Agent routes loaded in {time.time() - t:.2f}s\n")

t = time.time()
print("Loading export routes...")
from app.api.routes import export
print(f"✓ Export routes loaded in {time.time() - t:.2f}s\n")

t = time.time()
print("Loading health routes...")
from app.api.routes.health import router as health_router
print(f"✓ Health routes loaded in {time.time() - t:.2f}s\n")

t = time.time()
print("Loading audio routes...")
from app.api.routes.audio import router as audio_router
print(f"✓ Audio routes loaded in {time.time() - t:.2f}s\n")

# -----------------------------
# FastAPI
# -----------------------------

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

t = time.time()
print("Creating FastAPI app...")

app = FastAPI(
    title="Agentic Research Agent",
    version="1.0"
)

print(f"✓ FastAPI app created in {time.time() - t:.2f}s\n")

# -----------------------------
# Middleware
# -----------------------------

t = time.time()
print("Adding CORS middleware...")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://cigma-agentic-asistant-six.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print(f"✓ Middleware added in {time.time() - t:.2f}s\n")

# -----------------------------
# Routes
# -----------------------------

t = time.time()
print("Registering routes...")

app.include_router(library_router)
app.include_router(research_router)
app.include_router(search_router)
app.include_router(agent_router)
app.include_router(export.router)
app.include_router(health_router)
app.include_router(audio_router)

print(f"✓ Routes registered in {time.time() - t:.2f}s\n")


@app.get("/")
def home():
    return {"status": "running"}


print("=" * 60)
print(f"Application startup completed in {time.time() - startup:.2f}s")
print("=" * 60)