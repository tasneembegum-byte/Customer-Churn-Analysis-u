import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Shape:", df.shape)

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Convert totalcharges to numeric
df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")