from data_prep import df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")
df["CohortMonth"] = df.groupby("Customer ID")["InvoiceDate"].transform("min").dt.to_period("M")


df["CohortIndex"] = (df["InvoiceMonth"] - df["CohortMonth"]).apply(lambda x: x.n)


cohort_data = df.groupby(["CohortMonth", "CohortIndex"])["Customer ID"].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index="CohortMonth", columns="CohortIndex", values="Customer ID")


cohort_retention = cohort_pivot.divide(cohort_pivot[0], axis=0) * 100


plt.figure(figsize=(16, 8))
sns.heatmap(
    cohort_retention,
    annot=True,
    fmt=".0f",
    cmap="Blues",
    vmin=0,
    vmax=50,
    linewidths=0.5
)
plt.title("Customer Retention by Cohort (%)", fontsize=14, fontweight="bold")
plt.xlabel("Months Since First Purchase")
plt.ylabel("Cohort Month")
plt.tight_layout()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plt.savefig(os.path.join(BASE_DIR, "reports", "cohort_retention.png"), dpi=150)
plt.show()
print("Saved: reports/cohort_retention.png")