# Import the libraries
import yfinance as yf
import pandas as pd
import talib as tb

# Define the ticker symbol and date range
btc_ticker = 'BTC-USD'
start_date = '2020-07-02'
end_date = '2021-08-03'

# Retrieve Bitcoin data from Yahoo Finance
btc_data = yf.download(btc_ticker, start=start_date, end=end_date)

# Calculate RSI
rsi = tb.RSI(btc_data['Close'])

# Calculate SMA
sma = tb.SMA(btc_data['Close'])

# Calculate MACD
macd, macd_signal, _ = tb.MACD(btc_data['Close'])

# Calculate EMA
ema = tb.EMA(btc_data['Close'], timeperiod= 30)

# Calculate Bolinger Bands
LB, _, UB = tb.BBANDS(btc_data['Close'], timeperiod= 20)

# Create a DataFrame to store the data
btc_df = pd.DataFrame({
    'Date': btc_data.index,
    'Open': btc_data['Open'],
    'High': btc_data['High'],
    'Low': btc_data['Low'],
    'Close': btc_data['Close'],
    'Volume': btc_data['Volume'],
    'RSI': rsi,
    'SMA': sma,
    'EMA': ema,
    'MACD': macd,
    'MACD Signal': macd_signal,
    'LB': LB,
    'UB': UB,
})

# Print the DataFrame
btc_df.head()

# Export the data 
from google.colab import drive

drive.mount('/drive')
btc_df.to_csv('/drive/My Drive/Datasets/btc_ta.csv')