from data_prep import df
from rfm_analysis import rfm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


cohort_map = df.groupby("Customer ID")["InvoiceDate"].min().dt.to_period("M").reset_index()
cohort_map.columns = ["Customer ID", "CohortMonth"]


rfm_cohort = rfm.merge(cohort_map, on="Customer ID", how="left")


cohort_segment = rfm_cohort.groupby(["CohortMonth", "Segment"])["Customer ID"].count().reset_index()
cohort_segment.columns = ["CohortMonth", "Segment", "Count"]


cohort_totals = cohort_segment.groupby("CohortMonth")["Count"].transform("sum")
cohort_segment["Percentage"] = (cohort_segment["Count"] / cohort_totals * 100).round(1)


pivot = cohort_segment.pivot(index="CohortMonth", columns="Segment", values="Percentage").fillna(0)


plt.figure(figsize=(14, 7))
sns.heatmap(
    pivot,
    annot=True,
    fmt=".1f",
    cmap="RdYlGn",
    linewidths=0.5,
    vmin=0,
    vmax=50
)
plt.title("RFM Segment Distribution by Cohort (%)", fontsize=14, fontweight="bold")
plt.xlabel("Segment")
plt.ylabel("Cohort Month")
plt.tight_layout()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plt.savefig(os.path.join(BASE_DIR, "reports", "cohort_rfm.png"), dpi=150)
plt.show()
print("Saved: reports/cohort_rfm.png")