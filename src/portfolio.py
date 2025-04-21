import pandas as pd

class Portfolio:
    def __init__(self):
        self.holdings = pd.DataFrame(columns=['symbol', 'shares', 'avg_price'])
    
    def add_trade(self, symbol, shares, price):
        # Implement trade logic
        pass
    
    def get_summary(self):
        # Implement portfolio summary
        return "Portfolio summary"

def calculate_portfolio_value(tickers: list[str], weights: list[float], prices: dict) -> float:
    """
    weights must sum to 1.0
    prices = { "AAPL": 172.5, "MSFT": 315.2 }
    """
    total = 0
    for ticker, weight in zip(tickers, weights):
        total += prices.get(ticker, 0) * weight
    return total
