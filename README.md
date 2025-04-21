# 📈 Investment Analysis AI Agent

An intelligent financial assistant that pulls real-time stock data, analyzes technical indicators, and generates a natural-language summary of current market trends using an LLM (GPT-4).

---

## 🚀 Features

- ✅ Fetches live stock price data using [yFinance](https://pypi.org/project/yfinance/)
- 📊 Technical analysis (Moving Averages, RSI, MACD, etc.)
- 🧠 AI-generated summaries and insights
- 🛠️ Modular code structure for easy expansion (e.g. news analysis, portfolio tracking)

---

## 🧱 Project Structure

investment-agent/
├── main.py # Entry point
├── stock_data.py # Pull stock data + calculate indicators
├── analysis_agent.py # Generates LLM-based summary
├── requirements.txt # Python dependencies
└── .env # Environment variables (API keys)

## 🤩 Next Steps

- 📰 Add news and sentiment analysis (Reddit, Twitter, NewsAPI)
- 📈 Plot historical trends and technical indicators
- 💼 Simulated portfolio with buy/sell tracking
- 🗣️ Voice assistant mode

## 🥉 Tech Stack

- **Data:** yfinance, Financial Modeling Prep API, News API, Reddit API
- **Analysis:** Pandas, NumPy, TA-Lib
- **AI/Agent:** LangChain, OpenAI/Claude
- **Frontend:** Streamlit
