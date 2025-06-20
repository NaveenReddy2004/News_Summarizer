from fastapi import FastAPI
from app.news_fetcher import fetch_top_news
from app.summarizer import summarize_text
from fastapi.middleware.cors import CORSMiddleware


@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}
app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-news")
async def get_news():
    news = await fetch_top_news()
    summaries = []

    for article in news:
        content = article.get("content") or article.get("description")
        if content:
            summary = await summarize_text(content)
            summaries.append({
                "title": article["title"],
                "url": article["url"],
                "summary": summary
            })
    return {"news": summaries}
