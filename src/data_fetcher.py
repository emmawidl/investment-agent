import yfinance as yf
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_stock_data(symbol, period="1mo"):
    """Get OHLC data with volume"""
    return yf.download(symbol, period=period)


def get_fundamentals(symbol):
    """Get key financial metrics"""
    ticker = yf.Ticker(symbol)
    return {
        "pe_ratio": ticker.info.get("trailingPE", "N/A"),
        "eps": ticker.info.get("trailingEps", "N/A"),
        "debt_equity": ticker.info.get("debtToEquity", "N/A"),
    }


def get_news(symbol):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={api_key}"
    return requests.get(url).json()
