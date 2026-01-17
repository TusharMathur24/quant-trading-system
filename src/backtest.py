import pandas as pd
import numpy as np

def calculate_performance_metrics(df):
    """
    Computes Sharpe, Sortino, Calmar, Win Rate, etc.
    df requires: 'strategy_return'
    """
    metrics = {}
    returns = df['strategy_return'].replace([np.inf, -np.inf], 0).dropna()
    
    if len(returns) == 0: return metrics
    
    ANN_FACTOR = 252 * 75 # Annualization: 375 mins/day / 5 min/bar = 75 bars/day. 252 days/year.
    
    cum_ret = (1 + returns).cumprod() # Cumulative Return (Total Return)
    total_return = (cum_ret.iloc[-1] - 1) * 100
    
    sharpe = np.sqrt(ANN_FACTOR) * (returns.mean() / returns.std()) if returns.std() != 0 else 0
    
    downside = returns[returns < 0]
    sortino = np.sqrt(ANN_FACTOR) * (returns.mean() / downside.std()) if len(downside) > 0 and downside.std() != 0 else 0
    
    peaks = cum_ret.cummax()
    dd = (cum_ret - peaks) / peaks
    mdd = dd.min()
    
    calmar = abs(total_return / (mdd*100)) if mdd != 0 else 0
    
    wins = (returns > 0).sum()
    total_trades = (returns != 0).sum()
    win_rate = wins / total_trades if total_trades > 0 else 0
    
    gross_win = returns[returns > 0].sum()
    gross_loss = abs(returns[returns < 0].sum())
    pf = gross_win / gross_loss if gross_loss > 0 else 0
    
    metrics = {
        'Total Return %': round(total_return, 2),
        'Sharpe Ratio': round(sharpe, 2),
        'Sortino Ratio': round(sortino, 2),
        'Calmar Ratio': round(calmar, 2),
        'Max Drawdown %': round(mdd * 100, 2),
        'Win Rate %': round(win_rate * 100, 2),
        'Profit Factor': round(pf, 2)
    }
    
    return metrics
