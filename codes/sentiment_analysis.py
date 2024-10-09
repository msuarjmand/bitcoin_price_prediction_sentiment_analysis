import pandas as pd
import io
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline


# import data from the bitcoin_titles.csv
df = pd.read_csv(io.BytesIO(uploaded['bitcoin_titles.csv']), index_col='Date', encoding='utf8')
df.head()

# CrypotBERT transformer for tokenizing and sentiment analysis
tokenizer = BertTokenizer.from_pretrained("kk08/CryptoBERT")
model = BertForSequenceClassification.from_pretrained("kk08/CryptoBERT")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Calculating the f_score
df['Score'] = ''

for i in range(len(list(df.Title))):
# for i in range(30):
    text = df.Title[i]
    result = classifier(text)

    if result[0]['label'] == 'LABEL_1':
        df['Score'][i] = result[0]['score']
    else:
        df['Score'][i] = -abs(result[0]['score'])
df.head()

# Droping the "Links" column
df2 = df.reset_index()
df2 = df2.drop(['Links'], axis=1)
df2.head()

# transform data column to datetime
df3 = df2[['Date', 'Score']]
df3['Date']= pd.to_datetime(df3['Date'])
df3.head()

# Aggregate the score per day
df4 = df3.groupby('Date')['Score'].apply(list).reset_index(name='newScore')
df4.head()


# Calculate the average score of the news score grouped by day
df4['f_Score'] = ''

for i in range(len(df4.newScore)):
  df4['f_Score'][i] = np.mean(df4.newScore[i])

df4.head()

# Download the final table as an excel file
from google.colab import files

df4.to_csv('btcNews_sentimentAnalysis.csv', encoding = 'utf-8-sig')
files.download('btcNews_sentimentAnalysis.csv')
