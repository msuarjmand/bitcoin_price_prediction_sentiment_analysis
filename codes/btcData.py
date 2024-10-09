# Import libraries
import pandas as pd
import io

# Import data
from data.data import *


# Create a dataframe 
df = pd.read_csv(r'C:\Users\Project\btc_ta.csv', index_col='Date', encoding='utf8', parse_dates=['Date'])
df.head()

# Find the shape of the table
df = df.loc['2020-07-02':'2021-08-03']
df.shape

# Remove the date column to concatinate the OHLC data with sentiment analysis
df.drop(df.columns[0], axis=1, inplace=True)
df.head()

# Import the sentiment analysis file
df2 = pd.read_csv(io.BytesIO(uploaded['btcNews_sentimentAnalysis.csv']), index_col='Date', encoding='utf8', parse_dates=['Date'])
df2.head()

df2.drop(df2.columns[0], axis=1, inplace=True)
df2.head()


# Concatinate the data
data = pd.concat([df, df2], axis=1)
data.head()

# Export the final table as "btcData.csv"
from google.colab import files

data.to_csv('btcData.csv', encoding = 'utf-8-sig')
files.download('btcData.csv')

