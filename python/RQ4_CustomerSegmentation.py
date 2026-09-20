import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data from Excel table
df = xl("CustomerBehavior", headers=False)

# Rename columns
df.columns = ["CustomerID", "TotalSpend", "PurchaseCount"]

# Create K-Means model
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

# Assign clusters
df["Cluster"] = kmeans.fit_predict(
    df[["PurchaseCount", "TotalSpend"]]
)

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(
    df["PurchaseCount"],
    df["TotalSpend"],
    c=df["Cluster"],
    cmap="Dark2",
    alpha=0.6
)

# Plot cluster centers
centers = kmeans.cluster_centers_

ax.scatter(
    centers[:, 0],
    centers[:, 1],
    color="black",
    marker="X",
    s=250,
    label="Cluster Centers"
)

# Title and labels
ax.set_title("Customer Segments Using K-Means Clustering")
ax.set_xlabel("Purchase Count")
ax.set_ylabel("Total Spend (£)")

# Legend
ax.legend()

plt.tight_layout()
plt.show()
