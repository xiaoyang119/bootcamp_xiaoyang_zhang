## Lifecycle Mapping
| Goal | Stage & Deliverable |
|------|---------------------|
| Define stock trend criteria. | **Stage 01: Problem Framing & Scoping**<br>• `README.md` with problem statement<br>• Stakeholder Memo (`/docs/stakeholder_memo.md`) |
| Clean and explore stock data (e.g., stock price). | **Stage 02: Data Exploration**<br>• EDA Notebook (`/notebooks/eda.ipynb`) with:<br>  - Missing data analysis<br>  - Feature correlation plots |
| Build models (Linear regression). | **Stage 03: Modeling**<br>• Model Notebook (`/notebooks/regression.ipynb`) with:<br>  - SHAP explainability plots<br>  - Probability thresholds |
| Evaluate model accuracy and fairness. | **Stage 04: Evaluation**<br>• Fairness audit report (`/docs/summary.md`)<br>• Performance metrics (AUC, F1-score) |
| Present insights to loan officers. | **Stage 05: Reporting**<br>• Executive slide deck (`/docs/summary.md`)<br>• Model API prototype (`/notebooks/Productization.ipynb`) |
## Repo Plan
- **`/data/`**:  
  - Raw datasets 
  - Processed data  
- **`/notebooks/`**:  
  - `data_collection.ipynb`
  - `data_storage.ipynb`  
  - `EDA.ipynb` 
  - `engineering_features.ipynb`  
  - `regression.ipynb`
  - `Productization.ipynb`  
- **`/src/`**:  
  - `utils.py`
  - `cleaning.py`
  - `create_features.py`
  - `calculate_metrics.py`
  - `regression`.py`
- **`/docs/`**:  
  - `stakeholder_memo.md`    
  - `final_report.pdf`    