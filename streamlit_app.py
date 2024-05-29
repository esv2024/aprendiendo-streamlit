import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


import matplotlib.pyplot as plt

# Load the CSV file to inspect its contents
data = pd.read_csv("IMDB-Movie-Data.csv")
data.head()

