import pandas as pd

# Load data
df = pd.read_csv("data/AAPL.csv")

print("Original shape:", df.shape)

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

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned data
df.to_csv(
    "data/cleaned_AAPL.csv",
    index=False
)

print("Cleaned shape:", df.shape)

print("\nData cleaning completed!")
print(df.head())