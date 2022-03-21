import numpy as np
import joblib

def preprocess(Open, High, Low, AdjClose, Volume):
    test_data = np.array([[Open, High, Low, AdjClose, Volume]])
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)

    return prediction
