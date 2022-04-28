# import the required libraries
import pandas as pd
import streamlit as st
from transformers import pipeline

    
# load model
sentiment_pipeline = pipeline("sentiment-analysis")
# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
  # load the dataset
  df = pd.read_csv("chrome_reviews.csv")

# function to return sentiment
def return_sentiment(data):
  sentiment = sentiment_pipeline(data)
  return sentiment[0]['label']

# subset the dataset
df = df.dropna(subset=['Text'])
df['Sentiment'] = df['Text'].apply(return_sentiment)
df = df[(df['Sentiment'] == 'POSITIVE') & (df['Star'] == 1)]

# display the dataset
st.write(df)
