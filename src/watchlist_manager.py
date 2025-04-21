import json

WATCHLIST_FILE = "watchlist.json"

def load_watchlist() -> list:
    """Load the watchlist from a JSON file."""
    try:
        with open(WATCHLIST_FILE, "r") as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        watchlist = []
    return watchlist

def save_watchlist(watchlist: list) -> None:
    """Save the updated watchlist to a JSON file."""
    with open(WATCHLIST_FILE, "w") as file:
        json.dump(watchlist, file, indent=4)

def add_to_watchlist(ticker: str) -> str:
    """Add a stock ticker to the watchlist."""
    watchlist = load_watchlist()
    if ticker not in watchlist:
        watchlist.append(ticker)
        save_watchlist(watchlist)
        return f"{ticker} added to your watchlist."
    else:
        return f"{ticker} is already in your watchlist."

def remove_from_watchlist(ticker: str) -> str:
    """Remove a stock ticker from the watchlist."""
    watchlist = load_watchlist()
    if ticker in watchlist:
        watchlist.remove(ticker)
        save_watchlist(watchlist)
        return f"{ticker} removed from your watchlist."
    else:
        return f"{ticker} is not in your watchlist."

def get_watchlist() -> list:
    """Get the list of tickers in the watchlist."""
    return load_watchlist()
