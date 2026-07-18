import arxiv
import time


def search_arxiv(query: str, limit: int = 5):

    papers = []

    try:

        client = arxiv.Client(
            page_size=limit,
            delay_seconds=5,
            num_retries=3
        )

        search = arxiv.Search(
            query=query,
            max_results=limit,
            sort_by=arxiv.SortCriterion.Relevance
        )


        for result in client.results(search):

            papers.append({

                "title": result.title,

                "authors": [
                    author.name
                    for author in result.authors
                ],

                "year": result.published.year,

                "abstract": result.summary,

                "url": result.entry_id,

                "pdf": result.pdf_url,

                "source": "arXiv"

            })

            time.sleep(1)


    except arxiv.HTTPError as e:

        print(
            f"arXiv API error (continuing without arXiv): {e}"
        )


    except Exception as e:

        print(
            f"Unexpected arXiv failure (continuing without arXiv): {e}"
        )


    return papers