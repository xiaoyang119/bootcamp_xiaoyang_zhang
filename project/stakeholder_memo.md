# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement
This project aims to analyze historical trends and predict future movements of Apple Inc.'s (AAPL) stock price to support investment decisions. The core problem is the uncertainty in financial markets, where stakeholders need data-driven insights to assess whether AAPL is a viable investment. By leveraging time-series forecasting and macroeconomic indicators (e.g., interest rates, tech sector performance), the model will provide actionable predictions to mitigate investment risks.
## Stakeholder & User
Primary Stakeholder: Portfolio managers or individual investors deciding whether to buy/hold/sell AAPL shares.

End User: Financial analysts who interpret model outputs (e.g., predicted price ranges, risk metrics) to make recommendations.

Context: Decisions are time-sensitive, aligned with quarterly earnings reports or market shocks (e.g., supply chain disruptions).
## Useful Answer & Decision
Framing: Predictive (forecasting future prices) and Descriptive (identifying historical patterns).

Deliverable: A Jupyter Notebook with:

Time-series forecasts (e.g., ARIMA, LSTM) for AAPL stock prices.

Risk-reward metrics (e.g., Sharpe Ratio, volatility bands).

A summary slide (/docs/framing_slide.pdf) explaining key trends to non-technical stakeholders.
## Assumptions & Constraints
Data Availability: Reliable historical prices (Yahoo Finance API) and macroeconomic data (FRED).

Compliance: Avoid insider information; use only public data.

Latency: Model updates weekly; not for high-frequency trading.
## Known Unknowns / Risks
Black swan events (e.g., geopolitical crises) may disrupt predictions.

Correlation vs. causation: Macroeconomic factors may not directly drive AAPL’s price.
## Lifecycle Mapping
| Goal | Stage & Deliverable |
|------|---------------------|
| Define credit risk criteria and regulatory constraints. | **Stage 01: Problem Framing & Scoping**<br>• `README.md` with problem statement<br>• Stakeholder Memo (`/docs/stakeholder_memo.md`) |
| Clean and explore loan data (e.g., debt-to-income ratios). | **Stage 02: Data Exploration**<br>• EDA Notebook (`/notebooks/eda.ipynb`) with:<br>  - Missing data analysis<br>  - Feature correlation plots |
| Build ML models (logistic regression/XGBoost). | **Stage 03: Modeling**<br>• Model Notebook (`/notebooks/model.ipynb`) with:<br>  - SHAP explainability plots<br>  - Probability thresholds |
| Evaluate model accuracy and fairness. | **Stage 04: Evaluation**<br>• Fairness audit report (`/docs/fairness_audit.md`)<br>• Performance metrics (AUC, F1-score) |
| Present insights to loan officers. | **Stage 05: Reporting**<br>• Executive slide deck (`/docs/report.pdf`)<br>• Model API prototype (`/src/api.py`) |
## Repo Plan
- **`/data/`**:  
  - Raw datasets (e.g., `loan_applications_raw.csv`)  
  - Processed data (e.g., `cleaned_loans.parquet`)  
- **`/notebooks/`**:  
  - `eda.ipynb` (data exploration)  
  - `modeling.ipynb` (credit risk prediction)  
  - `evaluation.ipynb` (fairness metrics)  
- **`/src/`**:  
  - `preprocess.py` (data cleaning functions)  
  - `train_model.py` (ML pipeline)  
- **`/docs/`**:  
  - `stakeholder_memo.md` (problem framing)  
  - `fairness_audit.md` (bias evaluation)  
  - `final_report.pdf` (executive summary)  
- **Cadence**: Updates pushed at each lifecycle stage (see [Lifecycle Mapping](#lifecycle-mapping)).  