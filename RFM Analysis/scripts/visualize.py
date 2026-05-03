from data_prep import df
from rfm import rfm
import matplotlib.pyplot as plt
import seaborn as sns
import os

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

segment_counts = rfm["Segment"].value_counts()
sns.barplot(
    x=segment_counts.values,
    y=segment_counts.index,
    hue=segment_counts.index,
    ax=axes[0],
    palette="Blues_r",
    legend=False
)
axes[0].set_title("Customer Count by Segment")
axes[0].set_xlabel("Number of Customers")
axes[0].set_ylabel("Segment")

segment_revenue = rfm.groupby("Segment")["Monetary"].mean().sort_values(ascending=False)
sns.barplot(
    x=segment_revenue.values,
    y=segment_revenue.index,
    hue=segment_revenue.index,
    ax=axes[1],
    palette="Greens_r",
    legend=False
)

axes[1].set_title("Average Revenue by Segment")
axes[1].set_xlabel("Average Revenue (£)")
axes[1].set_ylabel("")

plt.tight_layout()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plt.savefig(os.path.join(BASE_DIR, "reports", "segment_analysis.png"), dpi=150)
plt.show()