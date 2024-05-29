import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


import matplotlib.pyplot as plt

# Load the CSV file to inspect its contents
data = pd.read_csv("IMDB-Movie-Data.csv")
data.head()

# Data for plotting
plot_data = sorted_data.head()

# Create a bar plot for the movies with the least votes
plt.figure(figsize=(10, 6))
plt.barh(plot_data['Title'], plot_data['Votes'], color='skyblue')
plt.xlabel('Votes')
plt.ylabel('Movie Title')
plt.title('Movies with the Least Votes')
plt.gca().invert_yaxis()  # Invert y-axis to display the movie with the least votes on top
plt.show()

Parece que hubo un problema al intentar mostrar la visualización aquí. Sin embargo, puedo proporcionarte el código que puedes utilizar en tu entorno local, especialmente si estás trabajando con Streamlit. Aquí te dejo el código para generar una visualización de las películas con menos votos:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que 'sorted_data' es tu DataFrame ya ordenado
sorted_data = pd.DataFrame({
    'Title': ['Paint It Black', 'The Exception', 'Whisky Galore', 'Tracktown', 'The Headhunter\'s Calling'],
    'Votes': [61, 96, 102, 115, 164]
})

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(sorted_data['Title'], sorted_data['Votes'], color='skyblue')
plt.xlabel('Votes')
plt.ylabel('Movie Title')
plt.title('Movies with the Least Votes')
plt.gca().invert_yaxis()  # Invertir eje y para mostrar la película con menos votos en la parte superior

# Mostrar el gráfico en Streamlit
st.pyplot(plt)


