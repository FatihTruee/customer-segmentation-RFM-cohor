import datetime as dt
from data_prep import df
import pandas as pd
import os

reference_date = df["InvoiceDate"].max() + dt.timedelta(days=1)

rfm = df.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("Revenue", "sum")
).reset_index()

rfm["R_Score"] = pd.qcut(rfm["Recency"], q=5, labels=[5,4,3,2,1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), q=5, labels=[1,2,3,4,5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], q=5, labels=[1,2,3,4,5])

rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)

def assign_segment(row):
    r = int(row["R_Score"])
    f = int(row["F_Score"])
    m = int(row["M_Score"])

    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    elif r >= 3 and f >= 3 and m >= 3:
        return "Loyal Customers"
    elif r >= 4 and f >= 2 and m >= 2:
        return "Potential Loyalists"
    elif r >= 4 and f <= 1:
        return "New Customers"
    elif r <= 2 and f >= 3 and m >= 3:
        return "At Risk"
    else:
        return "Lost"

rfm["Segment"] = rfm.apply(assign_segment, axis=1)

print(rfm.groupby("Segment")["Monetary"].mean().sort_values(ascending=False))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rfm.to_csv(os.path.join(BASE_DIR, "data", "raw", "rfm_output.csv"), index=False)
print("Saved: data/raw/rfm_output.csv")