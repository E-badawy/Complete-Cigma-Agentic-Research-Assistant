import re

STOP_WORDS = {
    "what", "is", "the", "a", "an", "of", "for", "to",
    "this", "that", "these", "those", "are", "was",
    "were", "does", "do", "did", "how", "why", "when",
    "where", "which", "who", "whom", "whose", "can",
    "could", "would", "should", "will", "about"
}


def optimize_query(question: str) -> str:
    question = question.lower()

    question = re.sub(r"[^\w\s]", " ", question)

    words = [
        word
        for word in question.split()
        if word not in STOP_WORDS
    ]

    return " ".join(words)