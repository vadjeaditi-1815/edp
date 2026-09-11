import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_AAPL.csv")

# Features
X = df[
    [
        "Open",
        "High",
        "Low",
        "Volume"
    ]
]

# Target
y = df["Close"]

print("Features:")
print(X.head())

print("\nTarget:")
print(y.head())

print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)