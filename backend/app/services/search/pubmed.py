import requests
import xml.etree.ElementTree as ET

SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def search_pubmed(query: str, limit: int = 10):

    search_response = requests.get(
        SEARCH_URL,
        params={
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": limit
        },
        timeout=30
    )

    search_response.raise_for_status()

    ids = search_response.json()["esearchresult"]["idlist"]

    if not ids:
        return []

    fetch_response = requests.get(
        FETCH_URL,
        params={
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "xml"
        },
        timeout=30
    )

    fetch_response.raise_for_status()

    root = ET.fromstring(fetch_response.text)

    papers = []

    for article in root.findall(".//PubmedArticle"):

        title = article.findtext(".//ArticleTitle")

        abstract_parts = article.findall(".//AbstractText")

        abstract = " ".join(
            part.text
            for part in abstract_parts
            if part.text
        )

        year = article.findtext(".//PubDate/Year")

        journal = article.findtext(".//Journal/Title")

        doi = None

        for eid in article.findall(".//ArticleId"):
            if eid.attrib.get("IdType") == "doi":
                doi = eid.text

        authors = []

        for author in article.findall(".//Author"):

            lastname = author.findtext("LastName")

            firstname = author.findtext("ForeName")

            if lastname and firstname:
                authors.append(f"{firstname} {lastname}")

        papers.append(
            {
                "title": title,
                "abstract": abstract,
                "year": year,
                "journal": journal,
                "doi": doi,
                "authors": authors,
                "source": "PubMed"
            }
        )

    return papers