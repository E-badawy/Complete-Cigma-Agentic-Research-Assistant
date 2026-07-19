from app.services.library_service import LibraryService
from app.services.llm_service import generate

def get_library_service():
    print("Creating LibraryService...")
    return LibraryService()

def retrieve_local_context(
    library_name: str,
    question: str,
    k: int = 8
):
    library_service = get_library_service()
    db, metadata = library_service.load_library(library_name)

    results = db.similarity_search_with_score(
        question,
        k=k
    )

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

    return {

        "context": context,

        "sources": sources

    }
    

def ask_question(
    library_name: str,
    question: str
):

    result = retrieve_local_context(
        library_name,
        question
    )

    prompt = f"""
        You are an evidence-based research assistant.

        Answer ONLY using the following context.

        Context:

        {result["context"]}

        Question:

        {question}
        """

    answer = generate(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": result["sources"]
    }