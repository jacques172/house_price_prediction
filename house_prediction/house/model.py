import pickle
import numpy as np

class HousePricePredictor:
    def __init__(self):
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
            
    def predict(self, features):
        # features is a dictionary with the input features for the prediction
        feature_vector = np.array([features[feature] for feature in features])
        price = self.model.predict(feature_vector.reshape(1, -1))[0]
        return price
