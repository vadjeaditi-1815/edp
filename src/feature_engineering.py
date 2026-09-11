import pandas as pd
import os

# List of stocks
stocks = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "TSLA",
    "NVDA"
]

all_data = []

for stock in stocks:

    print("Processing:", stock)

    # Load stock data
    file_path = f"data/{stock}.csv"

    df = pd.read_csv(file_path)

    # Add stock name
    df["Stock"] = stock

    # Convert columns to numeric
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # -------------------------
    # FEATURE 1: Daily Return
    # -------------------------
    df["Daily_Return"] = df["Close"].pct_change()

    # -------------------------
    # FEATURE 2: Price Range
    # -------------------------
    df["Price_Range"] = df["High"] - df["Low"]

    # -------------------------
    # FEATURE 3: 10-Day Moving Average
    # -------------------------
    df["SMA_10"] = df["Close"].rolling(
        window=10
    ).mean()

    # -------------------------
    # FEATURE 4: 20-Day Moving Average
    # -------------------------
    df["SMA_20"] = df["Close"].rolling(
        window=20
    ).mean()

    # -------------------------
    # FEATURE 5: Volatility
    # -------------------------
    df["Volatility"] = df["Daily_Return"].rolling(
        window=10
    ).std()

    # Remove missing values
    df.dropna(inplace=True)

    # Add to list
    all_data.append(df)

# Combine all companies
final_data = pd.concat(
    all_data,
    ignore_index=True
)

# Create data folder if necessary
os.makedirs("data", exist_ok=True)

# Save prepared dataset
final_data.to_csv(
    "data/prepared_stock_data.csv",
    index=False
)

print("\nFeature engineering completed!")

print("\nFinal dataset shape:")
print(final_data.shape)

print("\nFinal columns:")
print(final_data.columns)

print("\nFirst 5 rows:")
print(final_data.head())