import pandas as pd
from py_vollib.black_scholes.greeks.analytical import delta, gamma, theta, vega, rho

def add_greeks(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    r = 0.06
    
    
    if 'iv' not in df.columns:
        df['call_iv'] = 0.2
        df['put_iv'] = 0.2
    
    if 'expiry' in df.columns:
        df['time_to_expiry'] = (pd.to_datetime(df['expiry']) - pd.to_datetime(df['timestamp'])).dt.total_seconds() / (365*24*3600)
        df['time_to_expiry'] = df['time_to_expiry'].clip(lower=0.0001)
        
    if 'strike' not in df.columns:
        print("Warning: No strike column found. Skipping Greeks.")
        return df
        
    T = df['time_to_expiry']
    S = df['close']
    K = df['strike']
    
    df['call_delta'] = df.apply(lambda x: delta('c', x['close'], x['strike'], x['time_to_expiry'], r, x['call_iv']), axis=1)
    df['call_gamma'] = df.apply(lambda x: gamma('c', x['close'], x['strike'], x['time_to_expiry'], r, x['call_iv']), axis=1)
    df['call_theta'] = df.apply(lambda x: theta('c', x['close'], x['strike'], x['time_to_expiry'], r, x['call_iv']), axis=1)
    df['call_vega'] = df.apply(lambda x: vega('c', x['close'], x['strike'], x['time_to_expiry'], r, x['call_iv']), axis=1)
    
    df['put_delta'] = df.apply(lambda x: delta('p', x['close'], x['strike'], x['time_to_expiry'], r, x['put_iv']), axis=1)
    df['put_gamma'] = df.apply(lambda x: gamma('p', x['close'], x['strike'], x['time_to_expiry'], r, x['put_iv']), axis=1)
    
    return df
