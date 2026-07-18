from app.services.search.search_service import search

papers = search(
    "Tuberculosis pregnancy gut microbiome"
)

print()

for p in papers:

    print("=" * 80)

    print(p["title"])

    print(p["year"])

    print(p["doi"])

    print(p["citations"])

    print()