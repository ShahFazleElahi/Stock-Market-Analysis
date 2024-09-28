# stock_analysis.py
import yfinance as yf
import pandas as pd

# Step 1: Download historical stock data
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# stock_analysis.py (continued)
# Step 2: Display the first few rows of the data
print(stock_data.head())
