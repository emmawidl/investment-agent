import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def plot_price_with_indicators(stock_data: pd.DataFrame, ticker: str):
    # Create subplots to plot price and indicators
    fig = go.Figure()

    # Price plot (Line chart)
    fig.add_trace(go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name="Price",
        increasing_line_color='green', decreasing_line_color='red'
    ))

    # SMA plot
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['SMA'],
        mode='lines',
        name='SMA (14)',
        line=dict(color='blue', width=2)
    ))

    # MACD plot (for now showing just the MACD line)
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['MACD'],
        mode='lines',
        name='MACD',
        line=dict(color='purple', width=2)
    ))

    # Add titles and labels
    fig.update_layout(
        title=f"{ticker} Stock Price and Technical Indicators",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark",
        height=600
    )

    # Display the plot
    fig.show()

def plot_rsi(stock_data: pd.DataFrame, ticker: str):
    # Plot RSI
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['RSI'],
        mode='lines',
        name='RSI',
        line=dict(color='orange', width=2)
    ))

    fig.add_hline(y=30, line=dict(color='red', dash='dash'), name="Oversold (30)")
    fig.add_hline(y=70, line=dict(color='green', dash='dash'), name="Overbought (70)")

    # Add titles and labels
    fig.update_layout(
        title=f"{ticker} RSI Indicator",
        xaxis_title="Date",
        yaxis_title="RSI",
        template="plotly_dark",
        height=400
    )

    # Display the plot
    fig.show()
