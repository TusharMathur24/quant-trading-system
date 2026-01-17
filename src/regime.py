from hmmlearn import hmm
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

class RegimeModel:
    def __init__(self, n_states=3):
        self.scaler = StandardScaler()
        self.model = hmm.GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=1000, random_state=42)
        
    def fit(self, X):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled)
        
    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
        
    def save(self, path):
        # Save the entire object now to include the scaler
        joblib.dump(self, path)
        
    def load(self, path):
        # Load the entire object
        loaded_object = joblib.load(path)
        self.model = loaded_object.model
        self.scaler = loaded_object.scaler
