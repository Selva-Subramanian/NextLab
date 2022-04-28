# import the required libraries
import pandas as pd
import streamlit as st
from transformers import pipeline
from model import sentiment_pipeline

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    
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
