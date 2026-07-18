from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

from app.config.settings import settings

model = SentenceTransformer(
    settings.EMBEDDING_MODEL
    )


def rank_local(question, docs, top_k=5):
    if not docs:
        return []

    question_embedding = model.encode(question, convert_to_tensor=True)

    document_embeddings = model.encode(
        [doc.page_content for doc in docs],
        convert_to_tensor=True
    )

    similarities = cos_sim(
        question_embedding,
        document_embeddings
    )[0]

    ranked = sorted(
        zip(similarities, docs),
        key=lambda x: float(x[0]),
        reverse=True
    )

    return [doc for _, doc in ranked[:top_k]]


def rank_web(question, papers, top_k=5):
    if not papers:
        return []

    question_embedding = model.encode(question, convert_to_tensor=True)

    paper_texts = []

    for paper in papers:

        text = " ".join([

            paper.get("title", ""),

            paper.get("abstract", ""),

            paper.get("journal", ""),

            " ".join(
            paper.get("authors", [])
            ),

            str(
                paper.get("year", "")
            )

        ])

        paper_texts.append(text)

    paper_embeddings = model.encode(

        paper_texts,

        convert_to_tensor=True

    )

    similarities = cos_sim(
        question_embedding,
        paper_embeddings
    )[0]

    ranked = sorted(
        zip(similarities, papers),
        key=lambda x: float(x[0]),
        reverse=True
    )

    return [paper for _, paper in ranked[:top_k]]