import feedparser
import requests
import json
from pathlib import Path

# Constants
RSS_URL = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
HUGGINGFACE_API_TOKEN = "your_huggingface_token"  # 🔐 Use your token
SUMMARY_FILE = Path("output/summaries.json")

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def fetch_rss_headlines(url, max_items=5):
    feed = feedparser.parse(url)
    return [(entry.title, entry.summary) for entry in feed.entries[:max_items]]

def summarize(text):
    response = requests.post(
        HUGGINGFACE_API_URL,
        headers=headers,
        json={"inputs": text}
    )
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    return "⚠️ Failed to summarize."

def main():
    headlines = fetch_rss_headlines(RSS_URL)
    summaries = []

    for idx, (title, summary) in enumerate(headlines, start=1):
        combined = f"{title}. {summary}"
        summarized = summarize(combined)
        summaries.append({
            "id": idx,
            "title": title,
            "summary": summarized
        })

    # Save to file
    SUMMARY_FILE.parent.mkdir(exist_ok=True)
    with open(SUMMARY_FILE, "w") as f:
        json.dump(summaries, f, indent=2)
    print("✅ Summaries saved to output/summaries.json")

if __name__ == "__main__":
    main()
