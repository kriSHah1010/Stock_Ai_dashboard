import yfinance as yf

def get_stock_data(ticker):

    data = yf.download(
        ticker,
        period="5y",
        interval="1d"
    )

    # Flatten columns if multi-index
    if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
        data.columns = [col[0] for col in data.columns]

    return data
