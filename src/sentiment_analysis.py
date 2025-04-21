import requests
from textblob import TextBlob
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

def fetch_news(ticker: str, api_key: str) -> list:
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&language=en&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return [article['title'] for article in articles[:5]]  # top 5 headlines

def analyze_sentiment(text: str) -> float:
    return TextBlob(text).sentiment.polarity

def get_sentiment_summary(ticker: str, api_key: str) -> str:
    headlines = fetch_news(ticker, api_key)
    scores = [analyze_sentiment(h) for h in headlines]
    avg_score = sum(scores) / len(scores) if scores else 0
    mood = "Positive" if avg_score > 0.1 else "Negative" if avg_score < -0.1 else "Neutral"
    return f"{ticker} sentiment is {mood} based on news headlines."
