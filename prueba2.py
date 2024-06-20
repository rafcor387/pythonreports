import pandas as pd
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

st.header('Gráficas utilizando Pandas y streamlit', divider='rainbow')
st.title("Resultados de analisis de discotecas")

df = pd.read_csv('datasetdisco.csv')

if st.checkbox('Mostrar dataframe'):
    st.write(df)


option = st.selectbox(
'Selecciona el cliente: ',
df['cliente'])
'Tu selección: ', option
df.loc[df['cliente'] == option]


#pa fecha 
# Establece la fecha por defecto
default_date = datetime(2023, 1, 1)
# Campo de texto para filtrar por fecha con fecha por defecto
date_input = st.date_input('Selecciona una fecha:', default_date)
# Campo de selección para elegir entre Forum, Pacha, Zouk Boulevard
selected_location = st.selectbox('Selecciona una ubicación:', ['Forum', 'Pacha', 'Zouk Boulevard'])

# Convierte la columna 'fechaHora' al tipo de dato de fecha y hora
df['fechaHora'] = pd.to_datetime(df['fechaHora'])
# Filtra los registros que coinciden con la fecha seleccionada y la ubicación seleccionada
filtered_data = df[(df['fechaHora'].dt.date == date_input) & (df['nombre'] == selected_location)]

# Muestra el número de registros con esa fecha y ubicación iguales
st.text(f'El número de registros con esa fecha y ubicación iguales es: {len(filtered_data)}')