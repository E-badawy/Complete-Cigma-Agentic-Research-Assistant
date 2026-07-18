from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.config.settings import settings



_embeddings = None



def get_embeddings():

    global _embeddings


    if _embeddings is None:

        _embeddings = HuggingFaceEmbeddings(

            model_name=settings.EMBEDDING_MODEL,

            model_kwargs={
                "device": "cpu"
            },

            encode_kwargs={
                "normalize_embeddings": True
            }

        )


    return _embeddings





def create_vectorstore(chunks):


    db = FAISS.from_documents(

        chunks,

        get_embeddings()

    )


    return db





def save_vectorstore(db, path):

    db.save_local(path)





def load_vectorstore(path):


    return FAISS.load_local(

        path,

        get_embeddings(),

        allow_dangerous_deserialization=True

    )