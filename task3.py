import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_customer_churn.csv")

print("===== SUMMARY STATISTICS =====")
print(df.describe())

# Convert TotalCharges if needed
df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

# Histogram - Monthly Charges
plt.figure(figsize=(6,4))
plt.hist(df["monthlycharges"], bins=20)
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.savefig("monthlycharges_histogram.png")
plt.show()

# Boxplot - Monthly Charges
plt.figure(figsize=(6,4))
plt.boxplot(df["monthlycharges"])
plt.title("Monthly Charges Boxplot")
plt.savefig("monthlycharges_boxplot.png")
plt.show()

# Churn Analysis
print("\n===== CHURN COUNTS =====")
print(df["churn"].value_counts())