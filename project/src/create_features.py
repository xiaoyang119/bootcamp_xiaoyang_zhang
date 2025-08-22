import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures

def create_features(df):
    """
    Create engineered features for modeling.
    Assumptions:
    - Rolling mean of spending captures short-term trends.
    - Spend-to-income ratio helps normalize across different income levels.
    """
    df['spend_income_ratio'] = df['monthly_spend'] / df['income']
    df['rolling_spend_mean'] = df['monthly_spend'].rolling(3).mean().fillna(df['monthly_spend'])
    return df

# df = create_features(df)
df.head()