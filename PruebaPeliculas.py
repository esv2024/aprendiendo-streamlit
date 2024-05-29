import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# Función para cargar los datos
@st.cache
def load_data():
    data = pd.read_csv("IMDB-Movie-Data.csv")  # Asegúrate de cambiar esto por la ruta correcta del archivo
    return data
 
# Cargar datos
data = load_data()
 
# Título de la aplicación
st.title('Visualización de Datos de Películas')
 
# Visualización de tendencias de recaudación y calificaciones a lo largo de los años
st.header("Tendencias de Recaudación y Calificaciones por Año")
fig, ax = plt.subplots()
sns.lineplot(data=data, x='Year', y='Revenue (Millions)', ax=ax, label='Recaudación')
sns.lineplot(data=data, x='Year', y='Rating', ax=ax, label='Calificación', color='red')
ax.set_ylabel('Recaudación / Calificación')
st.pyplot(fig)
 
# Mapa de calor para correlaciones
st.header("Correlación entre Rating, Metascore y Revenue")
corr_matrix = data[['Rating', 'Metascore', 'Revenue (Millions)']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, ax=ax)
st.pyplot(fig)
 
# Diagramas de dispersión
st.header("Relación entre la Duración de las Películas y su Éxito")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='Runtime (Minutes)', y='Revenue (Millions)', ax=ax, label='Recaudación')
sns.scatterplot(data=data, x='Runtime (Minutes)', y='Rating', ax=ax, label='Calificación', color='red')
ax.legend(title='Variable')
st.pyplot(fig)
 
# Ejecutar la aplicación
# Para ejecutar esta aplicación, guarda el código en un archivo, por ejemplo app.py, y en la terminal ejecuta: streamlit run app.py
