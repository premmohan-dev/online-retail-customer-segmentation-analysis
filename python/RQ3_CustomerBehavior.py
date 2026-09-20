import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel table
df = xl("CustomerBehavior", headers=False)

# Rename columns
df.columns = ["CustomerID", "TotalSpend", "PurchaseCount"]

# Create scatter plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(
    df["PurchaseCount"],
    df["TotalSpend"],
    color="seagreen",
    alpha=0.6
)

# Title and labels
ax.set_title("Customer Spending vs Purchase Activity")
ax.set_xlabel("Purchase Count")
ax.set_ylabel("Total Spend (£)")

plt.tight_layout()
plt.show()
