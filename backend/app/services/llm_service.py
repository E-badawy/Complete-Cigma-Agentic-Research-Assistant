from groq import Groq

from app.config.settings import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate(prompt: str) -> str:

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI Research Assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1200,
    )

    return response.choices[0].message.content