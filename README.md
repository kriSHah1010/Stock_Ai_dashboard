# 📈 AI Stock Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Visualization](https://img.shields.io/badge/Visualization-Plotly-purple)
![Data](https://img.shields.io/badge/Data-Yahoo%20Finance-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

![GitHub stars](https://img.shields.io/github/stars/kriSHah1010/stock-ai-dashboard)
![GitHub forks](https://img.shields.io/github/forks/kriSHah1010/stock-ai-dashboard)
![GitHub last commit](https://img.shields.io/github/last-commit/kriSHah1010/stock-ai-dashboard)


An interactive **financial analytics dashboard** that analyzes stocks and cryptocurrencies using **technical indicators and machine learning forecasting**.

The application allows users to explore market trends, visualize indicators like **RSI and MACD**, and generate **AI-based 7-day price forecasts**.

Built with **Python, Streamlit, Plotly, and Scikit-Learn**.

---

# 🚀 Live Features

• 📊 Interactive candlestick price charts  
• 📉 Technical indicators (RSI, SMA20, MACD)  
• 📦 Trading volume analysis  
• 🤖 AI-powered **7-day price prediction**  
• ₿ Cryptocurrency support (BTC, ETH, etc.)  
• 🏢 Automatic company logos  
• ⏱ Timeframe selector (1M / 3M / 6M / 1Y / 5Y)  
• 🎨 Clean fintech-style dashboard UI  

---

# 📷 Dashboard Preview

![Dashboard Screenshot](images/dashboard.png)

*(Add a screenshot of your running app here later)*

---

# 🧠 How It Works

### 1️⃣ Data Collection
Market data is fetched using the **Yahoo Finance API (yfinance)**.

Includes:

- Open
- High
- Low
- Close
- Volume

---

### 2️⃣ Technical Indicators

The dashboard calculates several widely-used trading indicators.

#### 📈 RSI (Relative Strength Index)

Measures market momentum.

• RSI > 70 → Overbought  
• RSI < 30 → Oversold  

---

#### 📉 MACD (Moving Average Convergence Divergence)

Identifies trend momentum shifts.

• MACD crossing above signal line → bullish signal  
• MACD crossing below signal line → bearish signal  

---

#### 📊 SMA20 (20-Day Moving Average)

Smooths price data to highlight overall market trends.

---

### 3️⃣ Machine Learning Prediction

The application trains a **Random Forest Regressor** to estimate the **price 7 days into the future**.

Features used:

- SMA20
- RSI
- MACD

Output:

Predicted price vs current price to estimate market direction.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core language |
| Streamlit | Web dashboard framework |
| Plotly | Interactive charts |
| Pandas | Data processing |
| Scikit-Learn | Machine learning |
| yfinance | Financial data API |
| TA Library | Technical indicators |

---

# 📊 Example Dashboard Flow

1. Enter ticker symbol
2. Select timeframe
3. View price chart and indicators
4. Review AI forecast

---

# 🔮 Future Improvements

• Portfolio tracking system  
• Multi-stock comparison  
• AI trend classification (bullish / bearish)  
• Sentiment analysis using financial news  
• Real-time market alerts  

---

# 👨‍💻 Author

Krish Shah

Data Analyst / Data Science Enthusiast
