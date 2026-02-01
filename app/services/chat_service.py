from app.config import client

def ask_ai(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant IA spécialisé emploi et carrière."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
