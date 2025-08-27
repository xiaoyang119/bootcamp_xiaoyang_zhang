import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures

def _features(df):
    """
    Create engineered features for modeling.
    Assumptions:
    - Rolling mean of spending captures short-term trends.
    - Spend-to-income ratio helps normalize across different income levels.
    """
    df['ret'] = df['aapl'].pct_change().fillna(0.0)
    df['ret'] = df['aapl'].pct_change().fillna(0.0)
    df['log_ret'] = np.log1p(df['ret'])
    return df

# df = create_features(df)
df.head()