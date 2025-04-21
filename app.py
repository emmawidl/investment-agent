import streamlit as st
import yfinance as yf
import talib
import json
import os
from datetime import datetime
from src.technical_analysis import generate_analysis
from src.watchlist_manager import load_watchlist, remove_from_watchlist, save_watchlist
from src.data_fetcher import get_stock_data, get_fundamentals, get_news


# Watchlist config
WATCHLIST_FILE = "watchlist.json"


def load_watchlist():
    if not os.path.exists(WATCHLIST_FILE):
        # If the file doesn't exist, return an empty list
        return []
    try:
        with open(WATCHLIST_FILE, "r") as file:
            watchlist = json.load(file)
            # Ensure the watchlist is a list
            if not isinstance(watchlist, list):
                raise ValueError("Watchlist must be a list.")
            return watchlist
    except (json.JSONDecodeError, ValueError):
        # If the file is invalid, return an empty list
        return []


# UI Setup
st.set_page_config(layout="wide")

# Sidebar Watchlist
st.sidebar.header("💼 Watchlist Manager")
new_symbol = st.sidebar.text_input("Add symbol")
if st.sidebar.button("➕ Add"):
    save_watchlist(new_symbol)
    st.sidebar.success(f"Added {new_symbol.upper()}")

current_watchlist = load_watchlist()
if current_watchlist:
    st.sidebar.subheader("Your Stocks")
    for idx, symbol in enumerate(
        current_watchlist
    ):  # Add an index to ensure unique keys
        col1, col2 = st.sidebar.columns([3, 1])
        col1.write(f"📈 {symbol}")
        if col2.button(
            "❌", key=f"del_{symbol}_{idx}"
        ):  # Use index to ensure unique keys
            remove_from_watchlist(symbol)
            st.experimental_rerun()  # Force rerun after removing a stock

# Main Interface
st.title("📈 AI Investment Analyst")

# Single Stock Analysis
st.header("Quick Analysis")
symbol = st.text_input("Enter stock symbol (e.g. AAPL)", key="main_input")
if symbol:
    try:
        # Fetch stock data
        data = get_stock_data(symbol, period="1mo")
        st.line_chart(data["Close"])

        # Generate analysis
        analysis = generate_analysis(symbol, data)

        # Display analysis
        st.subheader(f"Analysis for {symbol.upper()}")
        st.markdown(analysis)

        # Recommendation Agent
        st.subheader("Recommendation")
        close_prices = data["Close"].values.squeeze()
        rsi = talib.RSI(close_prices, timeperiod=14)[-1]
        sma_20 = talib.SMA(close_prices, timeperiod=20)[-1]
        macd, signal, _ = talib.MACD(close_prices)

        # Recommendation logic
        if rsi < 30 and macd[-1] > signal[-1] and close_prices[-1] > sma_20:
            recommendation = (
                "📈 **Buy**: The stock is oversold and showing bullish momentum."
            )
        elif rsi > 70 and macd[-1] < signal[-1] and close_prices[-1] < sma_20:
            recommendation = (
                "📉 **Sell**: The stock is overbought and showing bearish momentum."
            )
        else:
            recommendation = (
                "🤔 **Hold**: No strong signals detected. Monitor the stock closely."
            )

        # Display recommendation
        st.markdown(recommendation)
    except Exception as e:
        st.error(f"Error analyzing {symbol}: {str(e)}")

# Watchlist Analysis
if current_watchlist:
    st.header("🔄 Watchlist Analysis")
    for symbol in current_watchlist:
        try:
            data = yf.download(symbol, period="1mo")
            st.markdown(generate_analysis(symbol, data))
            st.line_chart(data["Close"])
            st.write("---")
        except Exception as e:
            st.error(f"Couldn't fetch {symbol}: {str(e)}")

# Data Disclaimer
st.caption("ℹ️ Data provided by Yahoo Finance. Not financial advice.")
