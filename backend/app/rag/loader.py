from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)

SUPPORTED_EXTENSIONS = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
    ".docx": Docx2txtLoader,
}


def load_documents(folder_path: str):
    """
    Loads every supported document inside a folder recursively.
    """

    documents = []

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"{folder_path} does not exist.")

    for file in folder.rglob("*"):

        if file.suffix.lower() in SUPPORTED_EXTENSIONS:

            loader = SUPPORTED_EXTENSIONS[file.suffix.lower()](str(file))

            try:
                docs = loader.load()

                # Add useful metadata
                for doc in docs:
                    doc.metadata["source"] = str(file)
                    doc.metadata["filename"] = file.name

                documents.extend(docs)

            except Exception as e:
                print(f"Skipping {file.name}: {e}")

    return documents