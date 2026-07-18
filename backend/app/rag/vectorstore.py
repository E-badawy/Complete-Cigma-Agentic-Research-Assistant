from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.config.settings import settings

embeddings = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)


def create_vectorstore(chunks):

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    return db


def save_vectorstore(db, path):

    db.save_local(path)


def load_vectorstore(path):

    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )