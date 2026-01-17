
import sys
import os
import pandas as pd
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd()))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.regime import RegimeModel

def test_regime_model():
    print("Testing RegimeModel fix...")
    
    # Simulate data similar to the notebook
    # feats = ['avg_iv', 'iv_spread', 'ema_5']
    # We will just load the actual data if possible, or simulate it.
    
    data_path = 'data/processed/nifty_features_5min.csv'
    if os.path.exists(data_path):
        print(f"Loading data from {data_path}")
        df = pd.read_csv(data_path)
        df = df.dropna()
        valid_feats = [f for f in ['avg_iv', 'iv_spread', 'ema_5'] if f in df.columns]
        if not valid_feats:
             print("Warning: Features not found, using returns")
             valid_feats = ['returns']
             
        X = df[valid_feats].values
        print(f"Data shape: {X.shape}")
        
        print("Initializing model...")
        model = RegimeModel()
        
        print("Fitting model (this should include scaling now)...")
        try:
            model.fit(X[:int(0.7*len(X))])
            print("Fit successful.")
        except Exception as e:
            print(f"Fit failed: {e}")
            sys.exit(1)
            
        print("Predicting...")
        try:
            regimes = model.predict(X)
            print(f"Prediction successful. Regime counts: {pd.Series(regimes).value_counts().to_dict()}")
        except Exception as e:
            print(f"Prediction failed: {e}")
            sys.exit(1)

        print("Saving model...")
        os.makedirs('models', exist_ok=True)
        model.save('models/regime_hmm_test.joblib')
        print("Save successful.")
        
        print("Loading model...")
        model_loaded = RegimeModel()
        model_loaded.load('models/regime_hmm_test.joblib')
        print("Load successful.")
        
        regimes_loaded = model_loaded.predict(X)
        if np.array_equal(regimes, regimes_loaded):
             print("Verification successful: Loaded model predictions match.")
        else:
             print("Verification failed: Predictions do not match.")
             sys.exit(1)

    else:
        print(f"Data file not found at {data_path}")
        sys.exit(1)

if __name__ == "__main__":
    test_regime_model()
