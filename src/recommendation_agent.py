from openai import OpenAI
import requests
from textblob import TextBlob
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key={api_key})

def fetch_news_headlines(ticker: str, api_key: str) -> list:
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&sortBy=publishedAt&pageSize=5&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return [article["title"] for article in articles]


def summarize_price_trend(stock_data) -> str:
    recent = stock_data.tail(20)
    change = recent["Close"].iloc[-1] - recent["Close"].iloc[0]
    trend = "upward 📈" if change > 0 else "downward 📉" if change < 0 else "flat ➖"
    return f"Over the past 20 days, the price trend has been {trend} with a change of ${change:.2f}."


def analyze_news_sentiment(headlines: list) -> str:
    scores = [TextBlob(headline).sentiment.polarity for headline in headlines]
    avg = sum(scores) / len(scores) if scores else 0
    if avg > 0.2:
        return "positive"
    elif avg < -0.2:
        return "negative"
    else:
        return "neutral"


def get_investment_recommendation(ticker: str, stock_data, news_api_key: str) -> str:

    # 1. News headlines
    headlines = fetch_news_headlines(ticker, news_api_key)
    sentiment = analyze_news_sentiment(headlines)

    # 2. Price trend
    trend_summary = summarize_price_trend(stock_data)

    # 3. GPT prompt
    prompt = f"""
You are a financial investment assistant. Analyze the following:
1. News sentiment: {sentiment}
2. Recent price trend: {trend_summary}
3. News headlines: {headlines}

Based on this information, give a recommendation: "Buy", "Hold", or "Sell" the stock '{ticker}'. Include a 2-3 sentence reasoning.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    recommendation = response.choices[0].message.content.strip()
    return recommendation
