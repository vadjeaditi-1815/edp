import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load prepared dataset
df = pd.read_csv("data/prepared_stock_data.csv")

# Select AAPL
df = df[df["Stock"] == "AAPL"].copy()

# Convert Date and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")


# Features
features = [
    "Open",
    "High",
    "Low",
    "Volume",
    "Daily_Return",
    "Price_Range",
    "SMA_10",
    "SMA_20",
    "Volatility"
]

X = df[features]
y = df["Close"]


# Time-based 80/20 split
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

test_dates = df["Date"].iloc[split_index:]


# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)


# Predictions
y_pred = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print("Linear Regression Model Results")
print("--------------------------------")
print(f"MAE  : {mae:.4f}")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R2   : {r2:.4f}")


# Save model
joblib.dump(model, "models/regression_model.pkl")

print("\nRegression model saved successfully!")


# -------------------------------
# Plot Actual vs Predicted
# -------------------------------

plt.figure(figsize=(12, 6))

plt.plot(test_dates, y_test.values, label="Actual Price")
plt.plot(test_dates, y_pred, label="Predicted Price")

plt.title("AAPL Stock Price - Actual vs Predicted")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()