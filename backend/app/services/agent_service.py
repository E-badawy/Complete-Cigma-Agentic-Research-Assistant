from app.services.memory_service import memory_service


def run_agent(
    question: str,
    library_name: str | None = None,
    search_web: bool = True,
    session_id: str = "default",
):
    """
    Main research agent.

    Heavy imports are intentionally performed inside this function
    to keep FastAPI startup fast.
    """

    # --------------------------------------------------
    # Lazy Imports
    # --------------------------------------------------
    from app.services.search.search_service import search
    from app.services.research_service import retrieve_local_context
    from app.services.llm_service import generate
    from app.services.query_optimizer import optimize_query
    from app.services.evidence_ranker import rank_web
    from app.services.citation_service import generate_references

    # --------------------------------------------------
    # INITIALIZE
    # --------------------------------------------------
    local_answer = None
    local_sources = []
    web_papers = []

    # --------------------------------------------------
    # LOCAL SEARCH
    # --------------------------------------------------
    if library_name:

        local = retrieve_local_context(
            library_name,
            question,
        )

        local_answer = local.get("context")
        local_sources = local.get("sources", [])

    # --------------------------------------------------
    # WEB SEARCH
    # --------------------------------------------------
    if search_web:

        search_query = optimize_query(question)

        web_papers = search(search_query)

        web_papers = rank_web(
            question,
            web_papers,
            top_k=3,
        )

    # --------------------------------------------------
    # BUILD CONTEXT
    # --------------------------------------------------
    context = ""

    if local_answer:

        context += f"""

LOCAL KNOWLEDGE

{local_answer}

"""

    if web_papers:

        context += "\n\nLATEST SCIENTIFIC PAPERS\n"

        for i, paper in enumerate(web_papers, start=1):

            context += f"""

Paper {i}

Title:
{paper.get("title", "Untitled")}

Authors:
{", ".join(paper.get("authors", [])) if paper.get("authors") else "Unknown"}

Journal:
{paper.get("journal", "Unknown Journal")}

Year:
{paper.get("year", "Unknown")}

Citations:
{paper.get("citations", "N/A")}

DOI:
{paper.get("doi", "N/A")}

Abstract:
{paper.get("abstract") or "No abstract available."}

"""

    # --------------------------------------------------
    # MEMORY
    # --------------------------------------------------
    conversation = memory_service.get_context(session_id)

    # --------------------------------------------------
    # PROMPT
    # --------------------------------------------------
    prompt = f"""
    You are Cigma Agentic Research Assistant.

    Use BOTH the user's uploaded research library and the latest scientific literature.

    Previous Conversation

    {conversation}

    Question

    {question}

    Available Evidence

    {context}

    Instructions

    - Use the local library whenever applicable.
    - Support claims using the latest scientific evidence.
    - Never fabricate information.
    - If evidence is insufficient, clearly state so.
    - Prefer evidence from the supplied context over general knowledge.

    Produce a professional report using this structure:

    # Executive Summary

    # Detailed Analysis

    # Key Findings

    # Limitations

    # References
    """

    # --------------------------------------------------
    # GENERATE RESPONSE
    # --------------------------------------------------
    answer = generate(prompt)

    # --------------------------------------------------
    # SAVE MEMORY
    # --------------------------------------------------
    memory_service.add_message(
        session_id,
        "User",
        question,
    )

    memory_service.add_message(
        session_id,
        "Assistant",
        answer,
    )

    # --------------------------------------------------
    # REFERENCES
    # --------------------------------------------------
    references = generate_references(web_papers[:5])

    # --------------------------------------------------
    # RESPONSE
    # --------------------------------------------------
    return {
        "question": question,
        "answer": answer,
        "local_sources": local_sources,
        "web_sources": web_papers[:5],
        "references": references,
    }