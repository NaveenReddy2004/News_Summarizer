# AI-Powered Daily News Generator

An end-to-end web app that fetches the latest general news and summarizes each article using the **Groq LLaMA-70B AI model**. Built with **FastAPI** (backend) and **Streamlit** (frontend).

---

## Features

-  Fetches general news headlines using GNews API
-  Summarizes articles with Groq’s LLaMA 70B (super fast!)
-  Uses Retrieval-Augmented Generation (RAG-lite style)
-  Clean web UI using Streamlit
-  Deploy-ready backend hosted on Render
-  Open-source, resume-worthy project

---

## Tech Stack

| Layer      | Tech              |
|------------|-------------------|
| AI Model   | Groq LLaMA 70B    |
| Backend    | FastAPI + Uvicorn |
| Frontend   | Streamlit         |
| API Source | GNews.io API      |
| Deployment | Render + Streamlit Cloud |

---

## How It Works

1. User clicks **“Generate Today’s News”** on Streamlit UI.
2. Frontend calls FastAPI backend hosted on Render.
3. Backend fetches latest articles from GNews API.
4. Content is summarized by Groq’s LLaMA-70B via their API.
5. Summaries are shown instantly on the web UI.

---

## 🧪 Local Setup

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ai-news-generator.git
cd ai-news-generator
