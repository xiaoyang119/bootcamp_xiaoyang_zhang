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