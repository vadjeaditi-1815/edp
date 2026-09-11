import yfinance as yf
import os

# Companies we want to download
stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA"]

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Download data for each company
for stock in stocks:

    print("Downloading:", stock)

    df = yf.download(
        stock,
        start="2021-01-01",
        end="2026-01-01",
        auto_adjust=False
    )

    # Handle MultiIndex columns created by yfinance
    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    # Convert index into a normal Date column
    df.reset_index(inplace=True)

    # Save CSV file
    file_path = f"data/{stock}.csv"
    df.to_csv(file_path, index=False)

    print("Saved:", file_path)

print("\nAll stock data downloaded successfully!")