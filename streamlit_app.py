import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

# Load the CSV file to inspect its contents
data = pd.read_csv("IMDB-Movie-Data.csv")
# data.head()

# Sort the data by the 'Votes' column to find the movies with the least votes
sorted_data = data.sort_values(by='Votes', ascending=True)
sorted_data.head()
