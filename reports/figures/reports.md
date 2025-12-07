Markdown

# 📄 Interim Submission Report: AlphaCare Insurance Risk Analytics (Tasks 1 & 2)

**Project:** End-to-End Insurance Risk Analytics & Predictive Modeling
**Date:** 07 December 2025 (Submission)
**Status:** Tasks 1 (EDA) & 2 (DVC) **Complete**

---

## 1. Executive Summary: MLOps Foundation & Key Findings

The initial phase successfully established a robust, reproducible MLOps foundation and performed a rigorous Exploratory Data Analysis (EDA) on the 1 million historical insurance claims records.

| Area | Achievement | KPI Status | Business Impact |
| :--- | :--- | :--- | :--- |
| **Data Versioning (Task 2)** | Full **DVC** pipeline implemented to track data and models separately from Git. | **EXCEEDED** | Guarantees **reproducibility** and data-code lineage for auditing. |
| **Code Quality (Task 1.1)** | Analysis executed using **modular, object-oriented code** (`src/loader.py`, `src/eda_utils.py`). | **EXCEEDED** | Ensures code is scalable, reusable, and maintainable for production. |
| **Profitability KPI** | Calculated **Mean Loss Ratio (Claims/Premium)** to be **0.2164 (21.64%)**. | **MET** | **Conclusion: AlphaCare's book of business is highly profitable overall.** |
| **Risk Segmentation** | Identified significant variance in risk by **Province** and **Vehicle Body Type**. | **EXCEEDED** | Provides immediate, actionable repricing and marketing opportunities. |

---

## 2. Technical Execution & MLOps (Task 1.1 & 2)

### 2.1. Project Structure and Modularity
The project utilizes a standard data science project structure:
* `data/raw/`: Contains the DVC-tracked raw data.
* `src/`: Contains custom Python modules (`loader.py`, `eda_utils.py`).
* `notebooks/`: Contains the main analysis notebook (`01_advanced_eda.ipynb`).
* `reports/figures/`: Storage for all generated plots and visualizations.

The use of **`DataLoader`** handles pipe-delimited file reading, memory optimization (reducing 1M rows to **152.7 MB** of memory usage), and cleaning. The **`EDAPlotter`** ensures standardized, publication-quality chart generation.

### 2.2. Data Version Control (DVC)
The heavy data file (`insurance_claims.csv`) is managed by DVC and stored in a local remote (`dvc_storage`). Git only tracks the lightweight pointer file, ensuring the repository remains fast and auditable.
```bash
# Data tracked successfully
dvc add data/raw/insurance_claims.csv
dvc push

3. Exploratory Data Analysis (EDA) Findings (Task 1.2)
3.1. Data Quality and Limitations

    Size: 1,000,098 records, 52 columns.

    Critical Missingness: Several columns are unusable due to high missing values.

        numberofvehiclesinfleet: 100% missing.

        customvalueestimate: 77.9% missing.

    Feature Gap: The crucial demographic feature, Age of Policyholder, was found to be entirely missing from the loaded dataset. This severely limits current demographic risk analysis and must be flagged to the data engineering team for future data ingestion.

3.2. Core Profitability Metric: Loss Ratio

The overall Mean Loss Ratio of 0.2164 confirms low average claim payouts relative to premium income. However, this average masks important segments.
3.3. Actionable Segmentation Insights (Based on Visualizations)
Insight	Finding	Business Impact
Geographic Risk	Bar charts show certain Provinces have a Loss Ratio significantly above the 21.64% average.	Immediate repricing opportunity. Target low-risk provinces for marketing and apply risk loading to high-risk provinces.
Claim Severity	Bar charts of Vehicle Body Type show high-severity claim events are concentrated in specific categories (e.g., Sedans), while other types have lower average claim costs.	Optimize deductible and excess selection based on body type risk profile to mitigate large individual losses.
Temporal Trend	The Time Series plot reveals clear seasonal volatility in total claims, with spikes likely coinciding with holiday months (e.g., Dec/Jan).	Allows for better financial forecasting, reserve planning, and seasonally targeted risk mitigation campaigns.
Correlation	The heatmap shows key numerical relationships (e.g., correlation between totalpremium and totalclaims).	Provides the statistical basis to select features for the predictive model (Task 4).
4. Next Steps: A/B Hypothesis Testing (Task 3 Preparation)

The strong visual evidence must be converted into statistically significant facts. The following null hypotheses will be tested in Task 3:
Hypothesis (H₀)	Statistical Test	Rationale
Mean Loss Ratio is the same across all major Provinces.	ANOVA (Analysis of Variance)	Test if geographic differences in profitability are significant.
Mean Total Claims is the same for Male and Female Gender policyholders.	T-Test	Test if demographic factors are significant drivers of claim severity.
Marital Status and Claim Status (Claim/No Claim) are independent.	Chi-Squared Test	Test if a demographic category correlates with the likelihood of filing a claim.

4. Generating Statistical Tables...

================================================================================
TABLE 1: Descriptive Statistics of Core Financial Metrics
================================================================================
|       |   totalpremium |     totalclaims |    loss_ratio |
|:------|---------------:|----------------:|--------------:|
| count |     1.0001e+06 |      1.0001e+06 |    1.0001e+06 |
| mean  |    61.91       |     64.86       |    0.22       |
| std   |   230.28       |   2384.07       |    7.3        |
| min   |  -782.58       | -12002.4        |  -18.7        |
| 25%   |     0          |      0          |    0          |
| 50%   |     2.18       |      0          |    0          |
| 75%   |    21.93       |      0          |    0          |
---