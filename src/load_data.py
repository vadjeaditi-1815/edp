import pandas as pd

# Load AAPL data
file_path = "data/AAPL.csv"

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())