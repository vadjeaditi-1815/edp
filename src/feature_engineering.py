import pandas as pd
import os

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

    file_path = f"data/{stock}.csv"

    df = pd.read_csv(file_path)

    # Add stock name
    df["Stock"] = stock

    # Convert numeric columns
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

    # Daily return
    df["Daily_Return"] = df["Close"].pct_change()

    # Price range
    df["Price_Range"] = df["High"] - df["Low"]

    # 10-day moving average
    df["SMA_10"] = df["Close"].rolling(
        window=10
    ).mean()

    # 20-day moving average
    df["SMA_20"] = df["Close"].rolling(
        window=20
    ).mean()

    # Volatility
    df["Volatility"] = df["Daily_Return"].rolling(
        window=10
    ).std()

    # Remove missing values
    df.dropna(inplace=True)

    all_data.append(df)


# Combine all companies
final_data = pd.concat(
    all_data,
    ignore_index=True
)

# Create data folder
os.makedirs("data", exist_ok=True)

# Save prepared dataset
final_data.to_csv(
    "data/prepared_stock_data.csv",
    index=False
)

print("\nFeature engineering completed!")

print("\nDataset shape:")
print(final_data.shape)

print("\nColumns:")
print(final_data.columns.tolist())

print("\nFirst 5 rows:")
print(final_data.head())