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

# Calcula el porcentaje de cada nombre con respecto al total de filas
nombre_counts = filtered_data['nombre'].value_counts()
percentage = (nombre_counts / len(filtered_data)) * 100

# Crea un gráfico de pastel usando Matplotlib
fig, ax = plt.subplots()
ax.pie(nombre_counts, labels=nombre_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title(f'Distribución de nombres para {selected_location} en la fecha seleccionada')

# Muestra el gráfico de pastel
st.pyplot(fig)

# Muestra el porcentaje de cada nombre
st.write("Porcentaje de cada nombre:")
st.write(percentage)