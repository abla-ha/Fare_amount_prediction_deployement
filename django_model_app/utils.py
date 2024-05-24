import joblib
import numpy as np

def load_model():
    # Load the model using joblib
    model = joblib.load('/Users/mac/Documents/Django_deployment/django_model/model/best_model_1.pkl')
    return model

def predict_fare(year, distance, bearing):
    model = load_model()
    features = np.array([[year, distance, bearing]])
    fare = model.predict(features)
    return fare[0]
