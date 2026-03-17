from sklearn.ensemble import RandomForestRegressor

def train_model(df):

    df = df.dropna()

    # 7 day future price
    df["Target"] = df["Close"].shift(-7)
    df = df.dropna()
    features = df[["SMA20", "RSI", "MACD"]]
    target = df["Target"]
    model = RandomForestRegressor(n_estimators=200)
    model.fit(features, target)
    return model


def predict_next(model, df):
    latest = df[["SMA20", "RSI", "MACD"]].dropna().iloc[-1:]
    prediction = model.predict(latest)
    return prediction[0]