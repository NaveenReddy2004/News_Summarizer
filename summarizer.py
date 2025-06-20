import os
import httpx

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def summarize_text(text: str) -> str:
    prompt = f"Summarize the following news article in 3-4 bullet points:\n\n{text}"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-70b-8192",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
