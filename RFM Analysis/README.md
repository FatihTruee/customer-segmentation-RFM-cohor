# Customer Analytics: RFM Segmentation & Cohort Analysis
> **Impact:** Identifying high-value customer segments and quantifying retention decay for a UK-based Online Retailer.

##  Overview
This project applies **RFM (Recency, Frequency, Monetary)** methodology and **Cohort Analysis** to analyze customer behavior and lifetime value. By segmenting the customer base and tracking retention over a 12-month period, I provide actionable insights to shift marketing focus from costly acquisition to high-ROI retention.

---

##  Business Value & Questions
The goal is to move beyond descriptive statistics to solve core business problems:
* **Identification:** Who are our "Champions" and how can we protect them?
* **Risk Assessment:** Which segments are at risk of churning, and what is the financial impact?
* **Retention:** How does customer loyalty evolve over time (Cohort analysis)?

---

## ️ Tech Stack & Methodology
* **Language:** Python 3.x
* **Libraries:** `Pandas`, `Numpy`, `Matplotlib`, `Seaborn`, `Datetime`
* **Dataset:** [Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) (UK-based transactions 2009-2010)

### 1. RFM Scoring
Customers are ranked on a scale of 1-5 for each metric:
* **Recency:** Days since last purchase.
* **Frequency:** Total number of transactions.
* **Monetary:** Total revenue generated.

### 2. Customer Segmentation
| Segment | Profile | Strategy |
| :--- | :--- | :--- |
| **Champions** | Recent, frequent, high spenders. | Reward with early access & VIP perks. |
| **Potential Loyalists** | Recent buyers with average frequency. | Upsell through recommendation engines. |
| **At Risk** | Formerly valuable, but haven't visited recently. | Win-back campaigns (Personalized discounts). |
| **Lost** | Lowest scores across all metrics. | Don't spend acquisition budget here. |

---

##  Key Insights & Findings

* **The "Early Adopter" Advantage:** **48%** of the December 2009 cohort became "Champions." Early customers demonstrate significantly higher long-term value than late-season acquires.
* **Retention Cliff:** Across all cohorts, there is a **65-84% drop** in activity after the first month. The "First 30 Days" is the critical window for customer survival.
* **Late-Year Fragility:** September and October 2010 cohorts show a **70% Lost rate**, suggesting that holiday-season shoppers are transactional and less likely to become loyal without intervention.

---

##  Strategic Recommendations
1. **Focus on the 30-Day Window:** Implement an automated "Welcome & Second Purchase" email sequence to tackle the 80% drop-off seen in Cohort Month 1.
2. **Re-activate 'At Risk' Champions:** The data identifies a specific group of high-monetary users who haven't purchased in 60+ days. A targeted 15% discount campaign is recommended for this group.
3. **Budget Reallocation:** Shift 20% of the acquisition budget toward loyalty programs for "Potential Loyalists" to move them into the "Champions" segment.

---

## Project Structure
    RFM Analysis/
    ├── data/
    │   └── raw/
    │       ├── online_retail_II.xlsx   # Raw transaction data
    │       └── rfm_output.csv          # Processed RFM scores
    ├── reports/
    │   ├── cohort_retention.png
    │   ├── cohort_rfm.png
    │   ├── rfm_segment_analysis.twbx
    │   └── segment_analysis.png
    └── scripts/
        ├── cohort_analysis.py          # Customer retention by cohort
        ├── cohort_rfm_analysis.py      # Cohort x RFM heatmap
        ├── data_prep.py                # Data loading and cleaning
        ├── rfm_analysis.py             # RFM scoring and segmentation
        └── visualize.py                # Segment visualizations

---

## Tools
Python, Pandas, Matplotlib, Seaborn, Tableau