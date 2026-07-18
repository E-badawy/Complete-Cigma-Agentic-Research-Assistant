import json
import shutil
import tempfile
from pathlib import Path
from datetime import datetime
from fastapi import UploadFile

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vectorstore import (
    create_vectorstore,
    save_vectorstore,
    load_vectorstore
)
from app.config.settings import settings


LIBRARIES_PATH = Path("data/libraries")
LIBRARIES_PATH.mkdir(parents=True, exist_ok=True)


class LibraryService:

    def create_library(self, name: str, folder_path: str):

        library_path = LIBRARIES_PATH / name.lower().replace(" ", "_")

        if library_path.exists():
            raise Exception(f"Library '{name}' already exists.")

        library_path.mkdir(parents=True)

        print(f"Loading documents from: {folder_path}")
        documents = load_documents(folder_path)

        print(f"Loaded {len(documents)} documents")

        print("Splitting...")
        chunks = split_documents(documents)

        print(f"Created {len(chunks)} chunks")

        print("Generating embeddings...")
        db = create_vectorstore(chunks)
        save_vectorstore(db, str(library_path))

        metadata = {
            "library_name": name,
            "folder_path": folder_path,
            "documents": len(documents),
            "chunks": len(chunks),
            "embedding_model": settings.EMBEDDING_MODEL,
            "llm": settings.MODEL_NAME,
            "created_at": datetime.now().isoformat()
        }

        with open(library_path / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=4)

        return metadata

    def list_libraries(self):

        libraries = []

        for folder in LIBRARIES_PATH.iterdir():

            metadata = folder / "metadata.json"

            if metadata.exists():

                with open(metadata, "r") as f:
                    libraries.append(json.load(f))

        return libraries

    def load_library(self, name: str):

        library_path = LIBRARIES_PATH / name.lower().replace(" ", "_")

        if not library_path.exists():
            raise Exception(f"Library '{name}' not found.")

        db = load_vectorstore(str(library_path))

        metadata_file = library_path / "metadata.json"

        with open(metadata_file, "r") as f:
            metadata = json.load(f)

        return db, metadata

    def delete_library(self, name: str):

        library_path = LIBRARIES_PATH / name.lower().replace(" ", "_")

        if library_path.exists():
            shutil.rmtree(library_path)

        return {
            "message": f"{name} deleted successfully."
        }
        
    async def create_library_from_upload(
        self,
        name: str,
        files: list[UploadFile]
        ):

        library_path = LIBRARIES_PATH / name.lower().replace(" ", "_")

        if library_path.exists():
            raise Exception(f"Library '{name}' already exists.")

        with tempfile.TemporaryDirectory() as tmpdir:

            tmpdir = Path(tmpdir)

            for file in files:

                destination = tmpdir / file.filename

                with open(destination, "wb") as buffer:
                    shutil.copyfileobj(file.file, buffer)

            return self.create_library(
            name=name,
            folder_path=str(tmpdir)
            )