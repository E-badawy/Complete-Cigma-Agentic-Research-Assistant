import time

from app.services.library_service import LibraryService
from app.services.llm_service import generate


def get_library_service():
    return LibraryService()


def retrieve_local_context(
    library_name: str,
    question: str,
    k: int = 8
):
    start = time.time()

    print("=" * 60)
    print("Starting local retrieval")

    library_service = get_library_service()

    t = time.time()
    db, metadata = library_service.load_library(library_name)
    print(f"Library loaded in {time.time()-t:.2f}s")

    t = time.time()
    results = db.similarity_search_with_score(
        question,
        k=k
    )
    print(f"Similarity search completed in {time.time()-t:.2f}s")

    context = ""
    sources = []
    seen = set()

    for doc, score in results:

        source = (
            doc.metadata.get("filename", "Unknown"),
            doc.metadata.get("page")
        )

        if source not in seen:
            seen.add(source)

            sources.append(
                {
                    "filename": source[0],
                    "page": source[1]
                }
            )

        context += f"""

[Page {doc.metadata.get('page')}]

{doc.page_content}

"""

    print(f"Total retrieval time: {time.time()-start:.2f}s")
    print("=" * 60)

    return {
        "context": context,
        "sources": sources
    }


def ask_question(
    library_name: str,
    question: str
):

    overall = time.time()

    print("\n")
    print("=" * 70)
    print("NEW RESEARCH REQUEST")
    print("=" * 70)

    t = time.time()

    result = retrieve_local_context(
        library_name,
        question
    )

    print(f"Context retrieval: {time.time()-t:.2f}s")

    prompt = f"""
You are an evidence-based research assistant.

Answer ONLY using the following context.

Context:

{result['context']}

Question:

{question}
"""

    t = time.time()

    print("Calling LLM...")

    answer = generate(prompt)

    print(f"LLM completed in {time.time()-t:.2f}s")

    print(f"TOTAL REQUEST TIME: {time.time()-overall:.2f}s")
    print("=" * 70)

    return {
        "question": question,
        "answer": answer,
        "sources": result["sources"]
    }