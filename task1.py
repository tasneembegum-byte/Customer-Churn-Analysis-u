import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("\n===== FIRST 10 ROWS =====")
print(df.head(10))

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())