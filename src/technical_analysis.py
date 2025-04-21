import talib
import pandas as pd


def calculate_indicators(data):
    """Calculate all technical indicators"""
    return {
        "sma_20": talib.SMA(data["Close"], timeperiod=20).iloc[-1],
        "rsi": talib.RSI(data["Close"], timeperiod=14).iloc[-1],
        "macd": talib.MACD(data["Close"])[0].iloc[-1],
        "macd_signal": talib.MACD(data["Close"])[1].iloc[-1],
    }


def generate_analysis(symbol, data):
    # Ensure the 'Close' column is converted to a 1-dimensional numpy.ndarray
    close_prices = data["Close"].values.squeeze()

    # Calculate indicators using talib
    sma_20 = talib.SMA(close_prices, timeperiod=20)[-1]
    rsi = talib.RSI(close_prices, timeperiod=14)[-1]
    macd, signal, _ = talib.MACD(close_prices)

    # Generate analysis text
    analysis = f"""
📊 {symbol.upper()} Analysis:
**20-day SMA**: {sma_20:.2f} ({'↑ Bullish' if sma_20 < close_prices[-1] else '↓ Bearish'})
**RSI (14)**: {rsi:.1f} {'(Overbought ⚠️)' if rsi > 70 else '(Oversold 🔍)' if rsi < 30 else ''}
**MACD**: {macd[-1] - signal[-1]:+.2f} divergence ({'Bullish ↗️' if macd[-1] > signal[-1] else 'Bearish ↘️'})
"""
    if rsi > 65 and macd[-1] > signal[-1]:
        analysis += "\n**Overall**: Strong bullish momentum, monitor resistance levels"
    elif rsi < 35 and macd[-1] < signal[-1]:
        analysis += "\n**Overall**: Strong bearish momentum, monitor support levels"

    return analysis
