import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_customer_churn.csv")

# Create tenure groups
df["tenure_group"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 36, df["tenure"].max()],
    labels=["0-12 Months", "13-36 Months", "37+ Months"],
    include_lowest=True
)

# -----------------------------
# Pie Chart
# -----------------------------
tenure_counts = df["tenure_group"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    tenure_counts,
    labels=tenure_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Customer Distribution by Tenure")
plt.savefig("tenure_pie_chart.png")
plt.show()

# -----------------------------
# Bar Chart
# -----------------------------
avg_monthly = df.groupby("tenure_group")["monthlycharges"].mean()

plt.figure(figsize=(7,5))
bars = plt.bar(avg_monthly.index.astype(str), avg_monthly.values)

plt.title("Average Monthly Charges by Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Average Monthly Charges")

# Add values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.savefig("monthlycharges_bar_chart.png")
plt.show()

print("\nTask 4 completed successfully!")