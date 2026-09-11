import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt


# --------------------------------
# Load test data
# --------------------------------

df = pd.read_csv("data/test_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")


# --------------------------------
# Load trained regression model
# --------------------------------

model = joblib.load("models/regression_model.pkl")


# --------------------------------
# Features
# --------------------------------

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


X_test = df[features]

actual_price = df["Close"]


# --------------------------------
# Predict prices
# --------------------------------

predicted_price = model.predict(X_test)

df["Predicted_Close"] = predicted_price


# --------------------------------
# Generate trading signal
# --------------------------------

df["Signal"] = np.where(
    df["Predicted_Close"] > df["Close"],
    "BUY",
    "HOLD"
)


# --------------------------------
# Calculate actual daily return
# --------------------------------

df["Daily_Return"] = df["Close"].pct_change()


# --------------------------------
# Strategy return
# --------------------------------

df["Strategy_Return"] = np.where(
    df["Signal"] == "BUY",
    df["Daily_Return"],
    0
)


# --------------------------------
# Cumulative returns
# --------------------------------

df["Cumulative_Market"] = (
    1 + df["Daily_Return"].fillna(0)
).cumprod()

df["Cumulative_Strategy"] = (
    1 + df["Strategy_Return"].fillna(0)
).cumprod()


# --------------------------------
# Performance
# --------------------------------

market_return = (
    df["Cumulative_Market"].iloc[-1] - 1
) * 100

strategy_return = (
    df["Cumulative_Strategy"].iloc[-1] - 1
) * 100


print("\nBACKTESTING RESULTS")
print("-----------------------------")

print(f"Market Return   : {market_return:.2f}%")
print(f"Strategy Return : {strategy_return:.2f}%")

print(
    f"\nTotal BUY signals: "
    f"{(df['Signal'] == 'BUY').sum()}"
)

print(
    f"Total HOLD signals: "
    f"{(df['Signal'] == 'HOLD').sum()}"
)


# --------------------------------
# Save backtesting results
# --------------------------------

df.to_csv(
    "data/backtest_results.csv",
    index=False
)

print("\nBacktesting results saved successfully!")


# --------------------------------
# Plot performance
# --------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Cumulative_Market"],
    label="Buy & Hold"
)

plt.plot(
    df["Date"],
    df["Cumulative_Strategy"],
    label="Regression Strategy"
)

plt.title("Backtesting: Market vs Regression Strategy")

plt.xlabel("Date")
plt.ylabel("Cumulative Growth")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()