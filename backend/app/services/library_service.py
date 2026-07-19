import time

print("=" * 60)
print("Loading library_service.py...")
overall = time.time()

t = time.time()
import json
print(f"✓ json imported in {time.time()-t:.2f}s")

t = time.time()
import shutil
print(f"✓ shutil imported in {time.time()-t:.2f}s")

t = time.time()
import tempfile
print(f"✓ tempfile imported in {time.time()-t:.2f}s")

t = time.time()
from pathlib import Path
print(f"✓ pathlib imported in {time.time()-t:.2f}s")

t = time.time()
from datetime import datetime
print(f"✓ datetime imported in {time.time()-t:.2f}s")

t = time.time()
from fastapi import UploadFile
print(f"✓ UploadFile imported in {time.time()-t:.2f}s")

t = time.time()
from app.config.settings import settings
print(f"✓ settings imported in {time.time()-t:.2f}s")

print(f"library_service.py imports completed in {time.time()-overall:.2f}s")
print("=" * 60)


LIBRARIES_PATH = Path("data/libraries")
LIBRARIES_PATH.mkdir(parents=True, exist_ok=True)


class LibraryService:

    def create_library(self, name: str, folder_path: str):

        print("Loading RAG modules...")

        t = time.time()

        from app.rag.loader import load_documents
        from app.rag.splitter import split_documents
        from app.rag.vectorstore import (
            create_vectorstore,
            save_vectorstore,
        )

        print(f"✓ RAG modules loaded in {time.time()-t:.2f}s")
        
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

        t = time.time()

        from app.rag.vectorstore import load_vectorstore

        print(f"✓ load_vectorstore imported in {time.time()-t:.2f}s")
        
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