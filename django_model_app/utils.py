# fare_prediction/utils.py
import pickle
import numpy as np

def load_model():
    with open('path/to/your/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_fare(year, distance, bearing):
    model = load_model()
    features = np.array([[year, distance, bearing]])
    fare = model.predict(features)
    return fare[0]
