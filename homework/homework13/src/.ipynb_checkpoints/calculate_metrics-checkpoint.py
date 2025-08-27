from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import joblib
import os

def predict(features, round_prediction=False):
    """
    Predict using the loaded model.
    Optional parameter: round_prediction
    """
    loaded_model = joblib.load('model/model.pkl')
    pred = loaded_model.predict([features])[0]
    if round_prediction:
        pred = round(pred, 2)
    return pred.describe()

# Test the function
print("Function test:", predict([0.1, 0.2], round_prediction=True))