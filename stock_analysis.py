# stock_analysis.py
import yfinance as yf
import pandas as pd

# Step 1: Download historical stock data
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# stock_analysis.py (continued)
# Step 2: Display the first few rows of the data
print(stock_data.head())

# stock_analysis.py (continued)
# Step 3: Calculate moving averages
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

# stock_analysis.py (continued)
# Step 4: Display summary statistics
print(stock_data.describe())

# stock_analysis.py (continued)
import matplotlib.pyplot as plt

# Step 5: Visualization of closing prices and moving averages
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='AAPL Close Price', color='blue')
plt.plot(stock_data['MA50'], label='50-Day MA', color='red')
plt.plot(stock_data['MA200'], label='200-Day MA', color='green')
plt.title('AAPL Stock Price and Moving Averages (2020-2023)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# stock_analysis.py (continued)
# Step 6: Visualization of daily trading volume
plt.figure(figsize=(14, 7))
plt.bar(stock_data.index, stock_data['Volume'], color='orange')
plt.title('AAPL Daily Trading Volume (2020-2023)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

# stock_analysis.py (continued)
# Step 7: Identify crossover points
stock_data['Signal'] = 0
stock_data['Signal'][50:] = np.where(stock_data['MA50'][50:] > stock_data['MA200'][50:], 1, 0)
stock_data['Crossover'] = stock_data['Signal'].diff()
