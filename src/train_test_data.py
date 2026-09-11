import pandas as pd

# Load prepared dataset
df = pd.read_csv(
    "data/prepared_stock_data.csv"
)

# Select AAPL
df = df[df["Stock"] == "AAPL"].copy()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# 80% training, 20% testing
split_index = int(len(df) * 0.8)

train_data = df.iloc[:split_index]
test_data = df.iloc[split_index:]

# Save datasets
train_data.to_csv(
    "data/train_data.csv",
    index=False
)

test_data.to_csv(
    "data/test_data.csv",
    index=False
)

print("Training data:", train_data.shape)
print("Testing data:", test_data.shape)

print("\nTraining period:")
print(train_data["Date"].min(), "to", train_data["Date"].max())

print("\nTesting period:")
print(test_data["Date"].min(), "to", test_data["Date"].max())

print("\nTrain and test datasets created successfully!")