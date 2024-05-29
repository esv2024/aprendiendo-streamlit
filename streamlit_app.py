import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

# Load the CSV file to inspect its contents
file_path = 'aprendiento-streamlit/IMDB-Movie-Data.csv'
data = pd.read_csv(file_path)
# data.head()

# Sort the data by the 'Votes' column to find the movies with the least votes
sorted_data = data.sort_values(by='Votes', ascending=True)
sorted_data.head()
