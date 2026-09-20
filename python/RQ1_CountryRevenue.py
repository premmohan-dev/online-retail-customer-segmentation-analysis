import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel table
df = xl("CountryRevenue", headers=False)

# Rename columns
df.columns = ["Country", "TotalRevenue"]

# Keep Top 10 countries
df = df.head(10)

# Highlight United Kingdom
colors = ["crimson"] + ["steelblue"] * (len(df) - 1)

# Create chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    df["Country"],
    df["TotalRevenue"],
    color=colors
)

# Title and labels
ax.set_title("Top 10 Countries by Revenue")
ax.set_xlabel("Revenue (£)")
ax.set_ylabel("Country")

# Highest value at top
ax.invert_yaxis()

# Add extra room for revenue labels
ax.set_xlim(0, df["TotalRevenue"].max() * 1.15)

# Add revenue labels
for bar in bars:
    width = bar.get_width()

    ax.text(
        width * 1.002,
        bar.get_y() + bar.get_height() / 2,
        f"£{width:,.0f}",
        va="center",
        ha="left"
    )

plt.tight_layout()
plt.show()
