from pathlib import Path


def get_supported_loaders():
    """
    Lazy-load document loaders only when needed.
    This avoids importing heavy LangChain modules during FastAPI startup.
    """
    from langchain_community.document_loaders import (
        PyPDFLoader,
        TextLoader,
        Docx2txtLoader,
    )

    return {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".docx": Docx2txtLoader,
    }


def load_documents(folder_path: str):
    """
    Loads every supported document inside a folder recursively.
    """

    supported_extensions = get_supported_loaders()

    documents = []

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"{folder_path} does not exist.")

    for file in folder.rglob("*"):

        suffix = file.suffix.lower()

        if suffix in supported_extensions:

            loader = supported_extensions[suffix](str(file))

            try:
                docs = loader.load()

                for doc in docs:
                    doc.metadata["source"] = str(file)
                    doc.metadata["filename"] = file.name

                documents.extend(docs)

            except Exception as e:
                print(f"Skipping {file.name}: {e}")

    return documents