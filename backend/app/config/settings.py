from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # ========= LLM =========

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    # ========= Embeddings =========

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # ========= Storage =========

    LIBRARY_PATH = "data/libraries"

    OUTPUT_PATH = "data/outputs"

    DOCUMENT_PATH = "data/documents"


settings = Settings()