from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# import the btcData
data = pd.read_csv(r'C:\Users\Project\btcData.csv', index_col='Date', encoding='utf8', parse_dates=['Date'])
data.head()

# Remove the f_score column to normalise the OHLC and TA data
data2 = data
data3 = data2.drop(columns=['newScore'])
data3.head()

# Applying MinMaxScaler to the data
caler = MinMaxScaler()

data3[['High','Low', 'Close', 'Volume', 'RSI', 'SMA', 'EMA', 'MACD', 'MACD Signal', 'LB', 'UB', 'f_Score']] = scaler.fit_transform(data3[['High','Low', 'Close', 'Volume', 'RSI', 'SMA', 'EMA', 'MACD', 'MACD Signal', 'LB', 'UB', 'f_Score']])
data3.head()

# Export the results as 'Scaled_btcData.csv'

from google.colab import files

data3.to_csv('Scaled_btcData.csv', encoding = 'utf-8-sig')
files.download('Scaled_btcData.csv')



