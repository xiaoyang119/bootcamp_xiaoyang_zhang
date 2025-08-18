# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement
Small business loan approvals often rely on outdated or subjective criteria, leading to high default rates or missed opportunities. This project analyzes historical loan data (e.g., financial statements, repayment history) to build a predictive model that assesses credit risk objectively, enabling lenders to balance risk and accessibility.
## Stakeholder & User
Primary Decision-Maker: Bank Loan Officers (use model outputs to approve/reject loans).

End User: Small Business Applicants (benefit from fairer/faster decisions).

Compliance Stakeholder: Regulatory Body (ensure model meets fairness standards).
## Useful Answer & Decision
Analysis Type: Predictive (default probability) + Prescriptive (risk-based loan terms).

Deliverable:

A credit risk scoring model (Python notebook).

A fairness audit report (disparate impact analysis by demographic groups).
## Assumptions & Constraints
Data: Assumes access to anonymized loan applications (e.g., LendingClub dataset).

Legal: Model must comply with anti-discrimination laws (e.g., ECOA).
## Known Unknowns / Risks
How macroeconomic trends (e.g., inflation) affect default rates—requires external data integration.
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