import pandas as pd
import matplotlib.pyplot as plt

# Load prepared data
df = pd.read_csv(
    "data/prepared_stock_data.csv"
)

# Select one company
aapl = df[df["Stock"] == "AAPL"]

# Convert Date
aapl["Date"] = pd.to_datetime(aapl["Date"])

# -------------------------
# Closing Price Graph
# -------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    aapl["Date"],
    aapl["Close"]
)

plt.title("AAPL Closing Price")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# -------------------------
# Moving Average Graph
# -------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    aapl["Date"],
    aapl["Close"],
    label="Close"
)

plt.plot(
    aapl["Date"],
    aapl["SMA_10"],
    label="SMA 10"
)

plt.plot(
    aapl["Date"],
    aapl["SMA_20"],
    label="SMA 20"
)

plt.title("AAPL Price and Moving Averages")

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()