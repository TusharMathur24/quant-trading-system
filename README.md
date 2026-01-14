# Quantitative Trading Strategy with Regime Detection and ML Enhancement

## Project Overview
This project implements an end-to-end quantitative trading system on NIFTY 50 using
spot, futures, and options data at a 5-minute frequency. The system integrates
feature engineering, Hidden Markov Model-based regime detection, rule-based trading,
machine learning-based signal filtering, and high-performance trade analysis.

## Data Sources
- NIFTY 50 Spot (5-minute OHLCV)
- NIFTY Futures (current month with rollover)
- NIFTY Options Chain (ATM ±2 strikes)

## Project Structure
- data/: raw and cleaned datasets
- notebooks/: step-by-step development notebooks
- src/: reusable Python modules
- models/: trained ML models
- plots/: visual outputs
- results/: backtest and analysis results

## Execution Flow
1. Data acquisition and cleaning
2. Feature engineering (EMA, Greeks, IV, PCR)
3. Market regime detection using HMM
4. EMA-based trading strategy with regime filter
5. ML-based trade filtering (XGBoost & LSTM)
6. Outlier and performance analysis

## Key Outcomes
- Improved risk-adjusted returns using regime filtering
- Further performance enhancement with ML signal validation
- Identification of high-performance trade patterns

## How to Run
Each notebook is sequentially numbered and should be executed in order.
