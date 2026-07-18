def format_apa(paper):

    authors = paper.get("authors", [])

    if authors:
        author_text = ", ".join(authors[:3])

        if len(authors) > 3:
            author_text += ", et al."
    else:
        author_text = "Unknown Author"


    year = paper.get("year") or "n.d."

    title = paper.get(
        "title",
        "Untitled"
    )

    journal = paper.get(
        "journal",
        ""
    )

    doi = paper.get(
        "doi",
        ""
    )

    url = paper.get(
        "url",
        ""
    )

    citation = (
        f"{author_text} "
        f"({year}). "
        f"{title}. "
    )


    if journal:
        citation += f"{journal}. "


    if doi:
        citation += f"https://doi.org/{doi}"

    elif url:
        citation += url


    return citation.strip()



def generate_references(papers):

    references = []

    seen = set()

    for paper in papers:

        citation = format_apa(paper)

        if citation not in seen:
            references.append(citation)
            seen.add(citation)

    return references