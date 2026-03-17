import streamlit as st
import plotly.graph_objects as go

from data_loader import get_stock_data
from indicators import add_indicators
from model import train_model, predict_next


st.set_page_config(
    page_title="AI Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #F5F7FA;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)


# Company logos
def get_logo(ticker):

    logos = {
        "AAPL": "https://logo.clearbit.com/apple.com",
        "TSLA": "https://logo.clearbit.com/tesla.com",
        "NVDA": "https://logo.clearbit.com/nvidia.com",
        "MSFT": "https://logo.clearbit.com/microsoft.com",
        "GOOG": "https://logo.clearbit.com/google.com",
        "AMZN": "https://logo.clearbit.com/amazon.com"
    }

    return logos.get(ticker.upper(), None)


# Banner
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("assets/stock_banner.png", use_container_width=True)

st.markdown("<h1 style='text-align:center;'>📈 AI Stock Analysis Dashboard</h1>", unsafe_allow_html=True)

st.markdown(
"<p style='text-align:center;'>Analyze stocks and crypto using technical indicators and machine learning forecasts.</p>",
unsafe_allow_html=True
)


# Center input
col1, col2, col3 = st.columns([1,2,1])

with col2:
    ticker = st.text_input("Enter Stock or Crypto Ticker", "AAPL")

st.markdown(
"<p style='text-align:center;'>Examples: AAPL, TSLA, NVDA, BTC-USD, ETH-USD</p>",
unsafe_allow_html=True
)

# Timeframe selector
timeframe = st.radio(
    "Select Timeframe",
    ["1M", "3M", "6M", "1Y", "5Y"],
    horizontal=True
)


# Convert timeframe
period_map = {
    "1M": "1mo",
    "3M": "3mo",
    "6M": "6mo",
    "1Y": "1y",
    "5Y": "5y"
}

period = period_map[timeframe]


if ticker:

    df = get_stock_data(ticker)

    df = add_indicators(df)

    model = train_model(df)

    predicted_price = predict_next(model, df)

    current_price = df["Close"].iloc[-1]

    logo = get_logo(ticker)

    # Header
    header_col1, header_col2 = st.columns([1,5])

    with header_col1:
        if logo:
            st.image(logo, width=90)

    with header_col2:
        st.markdown(f"### {ticker.upper()} Market Analysis")

    st.divider()

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Price", f"${current_price:.2f}")
    col2.metric("📊 RSI", f"{df['RSI'].iloc[-1]:.2f}")
    col3.metric("📉 SMA20", f"{df['SMA20'].iloc[-1]:.2f}")

    st.divider()

    # Candlestick chart
    st.subheader("📊 Price Chart")

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                increasing_line_color="#00C853",
                decreasing_line_color="#FF5252"
            )
        ]
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
"""
This candlestick chart shows the historical price movement of the asset.

Each candle represents **open, high, low and close prices for the trading period**.
"""
)

    st.divider()

    # Volume
    st.subheader("📊 Trading Volume")

    volume_fig = go.Figure()

    volume_fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Volume"],
            marker_color="#4CAF50"
        )
    )

    volume_fig.update_layout(
        template="plotly_white",
        height=300
    )

    st.plotly_chart(volume_fig, use_container_width=True)

    st.markdown(
"""
Volume represents how many shares were traded.

Higher volume often confirms **strong investor interest**.
"""
)

    st.divider()

    # RSI
    st.subheader("📈 RSI Indicator")

    rsi_fig = go.Figure()

    rsi_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            line=dict(color="#2962FF")
        )
    )

    rsi_fig.add_hline(y=70, line_dash="dash", line_color="red")
    rsi_fig.add_hline(y=30, line_dash="dash", line_color="green")

    rsi_fig.update_layout(
        template="plotly_white",
        height=300
    )

    st.plotly_chart(rsi_fig, use_container_width=True)

    st.markdown(
"""
The **Relative Strength Index (RSI)** measures price momentum.

• RSI above 70 → overbought  
• RSI below 30 → oversold
"""
)

    st.divider()

    # MACD
    st.subheader("📉 MACD Indicator")

    macd_fig = go.Figure()

    macd_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MACD"],
            name="MACD",
            line=dict(color="#FF6D00")
        )
    )

    macd_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MACD_SIGNAL"],
            name="Signal",
            line=dict(color="#2962FF")
        )
    )

    macd_fig.update_layout(
        template="plotly_white",
        height=300
    )

    st.plotly_chart(macd_fig, use_container_width=True)

    st.markdown(
"""
MACD identifies changes in **trend momentum**.

MACD crossing above the signal line → bullish momentum  
MACD crossing below the signal line → bearish momentum
"""
)

    st.divider()

    # AI prediction
    st.subheader("🤖 AI 7-Day Forecast")

    st.metric("Current Price", f"${current_price:.2f}")
    st.metric("Predicted Price (7 days)", f"${predicted_price:.2f}")

    if predicted_price > current_price:
        st.success("📈 Model expects price increase over the next week")
    else:
        st.error("📉 Model expects price decrease over the next week")