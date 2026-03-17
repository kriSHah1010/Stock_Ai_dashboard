from data_loader import get_stock_data
from indicators import add_indicators
from model import train_model, predict_next

data = get_stock_data("AAPL")

data = add_indicators(data)

model = train_model(data)

prediction = predict_next(model, data)

print("Prediction:", prediction)