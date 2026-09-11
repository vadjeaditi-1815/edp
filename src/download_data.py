import yfinance as yf
import os

# Stock symbol
stock = "AAPL"

# Create data folder
os.makedirs("data", exist_ok=True)

# Download stock data
df = yf.download(
    stock,
    start="2021-01-01",
    end="2026-01-01",
    auto_adjust=False
)

# Handle MultiIndex columns
if hasattr(df.columns, "levels"):
    df.columns = df.columns.get_level_values(0)

# Reset index
df.reset_index(inplace=True)

# Save file
df.to_csv("data/AAPL.csv", index=False)

print("AAPL stock data downloaded successfully!")
print(df.head())