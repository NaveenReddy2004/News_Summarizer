import httpx
import os

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

async def fetch_top_news():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://gnews.io/api/v4/top-headlines",
            params={"token": GNEWS_API_KEY, "lang": "en", "country": "us", "max": 5}
        )
        return response.json().get("articles", [])
