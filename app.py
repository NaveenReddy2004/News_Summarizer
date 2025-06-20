import streamlit as st
import requests

st.set_page_config(page_title="AI Daily News Generator", layout="wide")
st.title("📰 AI Daily News Generator")
st.write("Click the button below to get the latest summarized news using Groq LLaMA 70B.")

if st.button("Generate Today's News"):
    with st.spinner("Fetching and summarizing..."):
        response = requests.get("http://localhost:8000/get-news")  # Replace with backend URL if deployed
        news_items = response.json()["news"]
        for item in news_items:
            st.subheader(item["title"])
            st.write(item["summary"])
            st.markdown(f"[🔗 Read full article]({item['url']})")
