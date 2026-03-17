from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator
from ta.trend import MACD


def add_indicators(df):

    sma = SMAIndicator(close=df["Close"], window=20)
    df["SMA20"] = sma.sma_indicator()

    rsi = RSIIndicator(close=df["Close"], window=14)
    df["RSI"] = rsi.rsi()

    macd = MACD(close=df["Close"])

    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()

    return df